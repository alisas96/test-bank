from src.main.api.requests.requester import Requester
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.deposit_response import DepositResponse
from requests import Response
from http import HTTPStatus
import requests


class DepositRequester(Requester):
    def post(self, deposit_request: DepositRequest) -> DepositResponse | Response:
        url = f"{self.base_url}/account/deposit"
        response = requests.post(
            url=url,
            json=deposit_request.model_dump(by_alias=True),
            headers=self.headers,
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return DepositResponse(**response.json())
        return response
