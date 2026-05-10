from src.main.api.steps.base_steps import BaseSteps
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_response import CreditRepayResponse
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.deposit_response import DepositResponse
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.models.transfer_response import TransferResponse
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.credit_response import CreditResponse
from src.main.api.foundation.requesters.validate_crud_requester import (
    ValidateCrudRequester,
)
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.endpoint import Endpoint
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs


class UserSteps(BaseSteps):
    def create_account(
        self, create_user_request: CreateUserRequest
    ) -> CreateUserResponse:
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
    ) -> DepositResponse:
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
    ) -> None:
        CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password,
            ),
            Endpoint.DEPOSIT,
            ResponseSpecs.request_bad(),
        ).post(deposit_request)

    def transfer_success(
        self, create_user_request: CreateUserRequest, transfer_request: TransferRequest
    ) -> TransferResponse:
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
    ) -> None:
        CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password,
            ),
            Endpoint.TRANSFER,
            ResponseSpecs.request_bad(),
        ).post(transfer_request)

    def get_credit_success(
        self,
        create_user_credit_request: CreateUserCreditRequest,
        credit_request: CreditRequest,
    ) -> CreditResponse:
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_credit_request.username,
                password=create_user_credit_request.password,
            ),
            Endpoint.GET_CREDIT,
            ResponseSpecs.request_created(),
        ).post(credit_request)
        return response

    def get_credit_failure(
        self, create_user_request: CreateUserRequest, credit_request: CreditRequest
    ) -> None:
        CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password,
            ),
            Endpoint.GET_CREDIT,
            ResponseSpecs.request_forbidden(),
        ).post(credit_request)

    def repay_credit_success(
        self,
        create_user_credit_request: CreateUserCreditRequest,
        repay_credit_request: CreditRepayRequest,
    ) -> CreditRepayResponse:
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_credit_request.username,
                password=create_user_credit_request.password,
            ),
            Endpoint.REPAY_CREDIT,
            ResponseSpecs.request_ok(),
        ).post(repay_credit_request)
        return response

    def repay_credit_failure(
        self,
        create_user_credit_request: CreateUserCreditRequest,
        repay_credit_request: CreditRepayRequest,
    ) -> None:
        CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_credit_request.username,
                password=create_user_credit_request.password,
            ),
            Endpoint.REPAY_CREDIT,
            ResponseSpecs.request_unprocessable(),
        ).post(repay_credit_request)
