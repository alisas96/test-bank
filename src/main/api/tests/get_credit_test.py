from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.credit_crud import CreditCrud as Credit
from sqlalchemy.orm import Session


class TestCredit:
    def test_get_credit_with_role_credit_secret(
        self,
        api_manager: ApiManager,
        create_user_credit_request: CreateUserCreditRequest,
        create_account_credit_response: CreateAccountResponse,
        db_session: Session,
    ):
        credit_request = RandomModelGenerator.generate(
            CreditRequest, overrides={"account_id": create_account_credit_response.id}
        )

        response = api_manager.user_steps.get_credit_success(
            create_user_credit_request, credit_request
        )

        assert credit_request.amount == response.balance

        credit_from_db = Credit.get_credit_by_id(db_session, response.credit_id)

        assert credit_from_db.id == response.credit_id, "Выданного кредита нет в бд"

    def test_get_credit_with_role_user(
        self,
        api_manager: ApiManager,
        create_user_request: CreateUserRequest,
        create_account_response: CreateAccountResponse,
        db_session: Session,
    ):
        credit_request = RandomModelGenerator.generate(
            CreditRequest, overrides={"account_id": create_account_response.id}
        )

        response = api_manager.user_steps.get_credit_failure(
            create_user_request, credit_request
        )

        credit_from_db = Credit.get_credit_by_account_id(
            db_session, create_account_response.id
        )

        assert credit_from_db is None, "Ошибка, кредит выдан"
