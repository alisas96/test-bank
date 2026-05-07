from src.main.api.models.base_model import BaseModel
from pydantic import Field
from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule


class TransferRequest(BaseModel):
    from_account_id: int = Field(alias="fromAccountId")
    to_account_id: int = Field(alias="toAccountId")
    amount: Annotated[float, CreationRule(min_value=500, max_value=10000)]
