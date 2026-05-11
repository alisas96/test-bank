from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_response import CreditResponse
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
import pytest
from src.main.api.db.crud.transaction_crud import TransactionCrud as Transaction
from src.main.api.db.foundation.transaction_type import TransactionType
from sqlalchemy.orm import Session


class TestCreditRepay:
    def test_credit_repay_amount_valid(
        self,
        api_manager: ApiManager,
        create_user_credit_request: CreateUserCreditRequest,
        get_credit: CreditResponse,
        db_session: Session,
    ):
        credit_repay_request = CreditRepayRequest(
            credit_id=get_credit.credit_id,
            account_id=get_credit.id,
            amount=get_credit.amount,
        )

        response = api_manager.user_steps.repay_credit_success(
            create_user_credit_request, credit_repay_request
        )

        assert credit_repay_request.amount == response.amount_deposited, "Кредит не оплачен, произошла ошибка"
        assert credit_repay_request.credit_id == response.credit_id, "Номер кредита не совпадает"

        transaction_from_db = Transaction.get_transaction_by_credit_id(
            db_session, response.credit_id
        )

        assert transaction_from_db.transaction_type == TransactionType.CREDIT_REPAYMENT, "Тип транзакции не совпадает, ошибка"

    @pytest.mark.parametrize(
        "amount",
        [
            4999.99,
            15000.01,
        ],
    )
    def test_credit_repay_amount_invalid(
        self,
        api_manager: ApiManager,
        create_user_credit_request: CreateUserCreditRequest,
        get_credit: CreditResponse,
        amount: float,
        db_session: Session,
    ):
        credit_repay_request = CreditRepayRequest(
            credit_id=get_credit.credit_id,
            account_id=get_credit.id,
            amount=amount,
        )

        api_manager.user_steps.repay_credit_failure(
            create_user_credit_request, credit_repay_request
        )

        transaction_from_db = Transaction.get_transaction_by_credit_id(
            db_session,
            get_credit.credit_id,
        )

        assert (
            transaction_from_db is None
        ), "Ошибка, транзакция не должна была создаться"
