from src.main.api.classes.api_manager import ApiManager
from typing import Any
import pytest


@pytest.fixture
def api_manager(created_obj: list[Any]) -> ApiManager:
    return ApiManager(created_obj)
