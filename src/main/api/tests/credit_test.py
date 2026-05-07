import pytest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.generators.model_generator import RandomModelGenerator


class TestCredit:
	def test_credit_success(self, api_manager, create_user_credit_request, create_account_credit_response):
		credit_request = RandomModelGenerator.generate(CreditRequest)
		credit_request.account_id = create_account_credit_response.id

		response = api_manager.user_steps.credit_success(create_user_credit_request, credit_request)

		assert credit_request.amount == response.balance

	def test_credit_failure(self, api_manager, create_user_request, create_account_response):
		credit_request = RandomModelGenerator.generate(CreditRequest)
		credit_request.account_id = create_account_response.id

		api_manager.user_steps.credit_failure(create_user_request, credit_request)
