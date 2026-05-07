import pytest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.generators.model_generator import RandomModelGenerator


@pytest.mark.api
class TestDeposit:
    def test_deposit_success(
        self, api_manager, create_user_request, create_account_response
    ):
        deposit_request = RandomModelGenerator.generate(DepositRequest)
        deposit_request.account_id = create_account_response.id

        response = api_manager.user_steps.deposit_success(
            create_user_request, deposit_request
        )

        assert deposit_request.amount == response.balance

    @pytest.mark.parametrize(
        "amount",
        [
            9000.01,
            999.99,
        ],
    )
    def test_deposit_failure(
        self, api_manager, create_user_request, create_account_request, amount
    ):
        deposit_request = DepositRequest(
            account_id=create_account_request.id,
            amount=amount,
        )

        api_manager.user_steps.deposit_failure(create_user_request, deposit_request)
