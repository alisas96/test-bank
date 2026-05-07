from src.main.api.models.base_model import BaseModel
from pydantic import Field
from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule


class DepositRequest(BaseModel):
	account_id: int = Field(alias='accountId')
	amount: Annotated[float, CreationRule(min_value=1000, max_value=9000)]