from src.main.api.models.base_model import BaseModel
from pydantic import Field
from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule


class CreditRequest(BaseModel):
    account_id: int = Field(alias="accountId")
    amount: Annotated[float, CreationRule(min_value=5000, max_value=15000)]
    term_months: Annotated[int, CreationRule(min_value=1, max_value=12)] = Field(
        alias="termMonths"
    )
