import pytest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.generators.model_generator import RandomModelGenerator


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request


@pytest.fixture
def create_account_response(api_manager, create_user_request):
    response = api_manager.user_steps.create_account(create_user_request)
    return response


@pytest.fixture
def account_factory(api_manager, create_user_request):
    def _create():
        return api_manager.user_steps.create_account(create_user_request)

    return _create

@pytest.fixture
def deposit_response(api_manager, create_account_response, create_user_request):
    deposit_req = RandomModelGenerator.generate(DepositRequest)
    deposit_req.account_id = create_account_response.id
    response = api_manager.user_steps.deposit_success(create_user_request, deposit_req)
    return response

@pytest.fixture
def create_user_credit_request(api_manager):
    user_credit_request = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user(user_credit_request)
    return user_credit_request

@pytest.fixture
def create_account_credit_response(api_manager, create_user_credit_request):
    response = api_manager.user_steps.create_account(create_user_credit_request)
    return response
