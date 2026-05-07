from src.main.api.steps.base_steps import BaseSteps
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.foundation.requesters.validate_crud_requester import (
    ValidateCrudRequester,
)
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.endpoint import Endpoint
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password,
            ),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created(),
        ).post()
        return response

    def deposit_success(
        self, create_user_request: CreateUserRequest, deposit_request: DepositRequest
    ):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password,
            ),
            Endpoint.DEPOSIT,
            ResponseSpecs.request_ok(),
        ).post(deposit_request)
        return response

    def deposit_failure(
        self, create_user_request: CreateUserRequest, deposit_request: DepositRequest
    ):
        response = CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password,
            ),
            Endpoint.DEPOSIT,
            ResponseSpecs.request_bad(),
        ).post(deposit_request)
        return response

    def transfer_success(
        self, create_user_request: CreateUserRequest, transfer_request: TransferRequest
    ):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password,
            ),
            Endpoint.TRANSFER,
            ResponseSpecs.request_ok(),
        ).post(transfer_request)
        return response

    def transfer_failure(
        self, create_user_request: CreateUserRequest, transfer_request: TransferRequest
    ):
        response = CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password,
            ),
            Endpoint.TRANSFER,
            ResponseSpecs.request_bad(),
        ).post(transfer_request)
        return response

    def credit_success(
        self,
        create_user_credit_request: CreateUserCreditRequest,
        credit_request: CreditRequest,
    ):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_credit_request.username,
                password=create_user_credit_request.password,
            ),
            Endpoint.CREDIT,
            ResponseSpecs.request_created(),
        ).post(credit_request)
        return response

    def credit_failure(
        self, create_user_request: CreateUserRequest, credit_request: CreditRequest
    ):
        response = CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password,
            ),
            Endpoint.CREDIT,
            ResponseSpecs.request_forbidden(),
        ).post(credit_request)
        return response
