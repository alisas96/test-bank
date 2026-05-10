import pytest
import logging
from typing import Any, Generator
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_response import CreateUserResponse


@pytest.fixture
def created_obj() -> Generator[list[Any], None, None]:
    objects: list[Any] = []
    yield objects
    clean_user(objects)


def clean_user(objects: list[Any]) -> None:
    api_manager = ApiManager(objects)
    for u in objects:
        if isinstance(u, CreateUserResponse):
            api_manager.admin_steps.delete_user(u.id)
        else:
            logging.warning(f"Error in delete user_id: {u.id}")
