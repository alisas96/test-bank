import pytest
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.models.deposit_response import DepositResponse
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.classes.api_manager import ApiManager
from typing import Callable
from sqlalchemy.orm import Session
from src.main.api.db.crud.transaction_crud import TransactionCrud as Transaction
from src.main.api.db.foundation.transaction_type import TransactionType


@pytest.mark.api
class TestTransfer:
    def test_transfer_valid_amount(
        self,
        db_session: Session,
        api_manager: ApiManager,
        create_user_request: CreateUserRequest,
        deposit_response: DepositResponse,
        account_factory: Callable[[], CreateAccountResponse],
    ):
        transfer_request = TransferRequest(
            from_account_id=deposit_response.id,
            to_account_id=account_factory().id,
            amount=deposit_response.balance,
        )
        response = api_manager.user_steps.transfer_success(
            create_user_request, transfer_request
        )

        assert response.from_account_id_balance == 0

        transaction_from_db = Transaction.get_transaction_by_to_account_id(
            db_session,
            response.to_account_id,
        )

        assert transaction_from_db.transaction_type == TransactionType.TRANSFER

    @pytest.mark.parametrize("amount", [499.99, 10000.10])
    def test_transfer_invalid_amount(
        self,
        db_session: Session,
        api_manager: ApiManager,
        create_user_request: CreateUserRequest,
        deposit_response: DepositResponse,
        account_factory: Callable[[], CreateAccountResponse],
        amount: float,
    ):
        transfer_request = TransferRequest(
            from_account_id=deposit_response.id,
            to_account_id=account_factory().id,
            amount=amount,
        )
        api_manager.user_steps.transfer_failure(create_user_request, transfer_request)

        transaction_from_db = Transaction.get_transaction_by_to_account_id(
            db_session,
            transfer_request.to_account_id,
        )

        assert (
            transaction_from_db is None
        ), "Ошибка, транзакция не должна была создаться"
