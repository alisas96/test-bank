import pytest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.credit_response import CreditResponse
from src.main.api.models.deposit_response import DepositResponse
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.classes.api_manager import ApiManager
from typing import Callable


@pytest.fixture
def create_user_request(api_manager: ApiManager) -> CreateUserRequest:
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request


@pytest.fixture
def create_account_response(
    api_manager: ApiManager, create_user_request: CreateUserRequest
) -> CreateAccountResponse:
    response = api_manager.user_steps.create_account(create_user_request)
    return response


@pytest.fixture
def account_factory(
    api_manager: ApiManager, create_user_request: CreateUserRequest
) -> Callable[[], CreateAccountResponse]:
    def _create():
        return api_manager.user_steps.create_account(create_user_request)

    return _create


@pytest.fixture
def deposit_response(
    api_manager: ApiManager,
    create_account_response: CreateAccountResponse,
    create_user_request: CreateUserRequest,
) -> DepositResponse:
    deposit_req = RandomModelGenerator.generate(DepositRequest)
    deposit_req.account_id = create_account_response.id
    response = api_manager.user_steps.deposit_success(create_user_request, deposit_req)
    return response


@pytest.fixture
def create_user_credit_request(api_manager: ApiManager) -> CreateUserCreditRequest:
    user_credit_request = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user(user_credit_request)
    return user_credit_request


@pytest.fixture
def create_account_credit_response(
    api_manager: ApiManager, create_user_credit_request: CreateUserCreditRequest
) -> CreateAccountResponse:
    response = api_manager.user_steps.create_account(create_user_credit_request)
    return response


@pytest.fixture
def get_credit(
    api_manager: ApiManager,
    create_account_credit_response: CreateAccountResponse,
    create_user_credit_request: CreateUserCreditRequest,
) -> CreditResponse:
    credit_request = RandomModelGenerator.generate(
        CreditRequest, overrides={"account_id": create_account_credit_response.id}
    )
    response = api_manager.user_steps.get_credit_success(
        create_user_credit_request, credit_request
    )
    return response
