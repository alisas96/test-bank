import pytest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.classes.api_manager import ApiManager
from sqlalchemy.orm import Session
from src.main.api.db.crud.transaction_crud import TransactionCrud as Transaction
from src.main.api.db.foundation.transaction_type import TransactionType


@pytest.mark.api
class TestDeposit:
    def test_deposit_valid_amount(
        self,
        db_session: Session,
        api_manager: ApiManager,
        create_user_request: CreateUserRequest,
        create_account_response: CreateAccountResponse,
    ):
        deposit_request = RandomModelGenerator.generate(
            DepositRequest, overrides={"account_id": create_account_response.id}
        )

        response = api_manager.user_steps.deposit_success(
            create_user_request, deposit_request
        )

        assert deposit_request.amount == response.balance

        transaction_from_db = Transaction.get_transaction_by_to_account_id(
            db_session,
            response.id,
        )

        assert transaction_from_db.transaction_type == TransactionType.DEPOSIT

    @pytest.mark.parametrize(
        "amount",
        [
            9000.01,
            999.99,
        ],
    )
    def test_deposit_invalid_amount(
        self,
        db_session: Session,
        api_manager: ApiManager,
        create_user_request: CreateUserRequest,
        create_account_response: CreateAccountResponse,
        amount: float,
    ):
        deposit_request = DepositRequest(
            account_id=create_account_response.id,
            amount=amount,
        )

        api_manager.user_steps.deposit_failure(create_user_request, deposit_request)

        transaction_from_db = Transaction.get_transaction_by_to_account_id(
            db_session, create_account_response.id
        )

        assert (
            transaction_from_db is None
        ), "Ошибка, транзакция не должна была создаться"
