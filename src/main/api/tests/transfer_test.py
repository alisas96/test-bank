import pytest
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.generators.model_generator import RandomModelGenerator


@pytest.mark.api
class TestTransfer:
    def test_transfer_success(
        self, api_manager, create_user_request, deposit_response, account_factory
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

    @pytest.mark.parametrize("amount", [499.99, 10000.10])
    def test_transfer_failure(
        self,
        api_manager,
        create_user_request,
        deposit_response,
        account_factory,
        amount,
    ):
        transfer_request = TransferRequest(
            from_account_id=deposit_response.id,
            to_account_id=account_factory().id,
            amount=amount,
        )
        api_manager.user_steps.transfer_failure(create_user_request, transfer_request)
