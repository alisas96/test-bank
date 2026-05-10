from src.main.api.foundation.http_requester import HttpRequester
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.models.base_model import BaseModel
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.foundation.endpoint import Endpoint
from typing import Optional
from src.main.api.configs.config import Config
import allure


class ValidateCrudRequester(HttpRequester):
    def __init__(
        self,
        request_spec: RequestSpecs,
        endpoint: Endpoint,
        response_spec: ResponseSpecs,
    ) -> None:
        super().__init__(request_spec, endpoint, response_spec)
        self.crud_requester = CrudRequester(
            request_spec=request_spec, endpoint=endpoint, response_spec=response_spec
        )

    def post(self, model: Optional[BaseModel] = None) -> Optional[BaseModel]:
        response = self.crud_requester.post(model)
        with allure.step(
            f"POST {Config.fetch('backendUrl')}{self.endpoint.value.url} and Validated Model"
        ):
            allure.attach(
                f"Validated Model resonse: {self.endpoint.value.response_model.__name__}"
            )

        self.response_spec(response)
        return self.endpoint.value.response_model.model_validate(response.json())

    def delete(self, user_id: int) -> Optional[BaseModel]:
        response = self.crud_requester.delete(user_id)
        self.response_spec(response)
        return self.endpoint.value.response_model.model_validate(response.json())
