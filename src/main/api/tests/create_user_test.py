import pytest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.generators.model_generator import RandomModelGenerator


@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize(
        "create_user_request", [RandomModelGenerator.generate(CreateUserRequest)]
    )
    def test_create_user_valid(self, api_manager, create_user_request):
        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

    @pytest.mark.parametrize(
        "username, password",
        [
            ("абв", "Pas!ssw0rd"),
            ("ab", "Pas!ssw0rd"),
            ("abv!", "Pas!ssw0rd"),
            ("Max1029", "Pas!ssw0rд"),
            ("Max1030", "Pas!sswo"),
            ("Max1031", "pas!ssw0rd"),
            ("Max1032", "PAS!SSW0RD"),
            ("Max1033", "PASSSw0RD"),
            ("Max1034", "PASSSwoRd"),
        ],
    )
    def test_create_user_invalid(self, username, password, api_manager):

        create_user_request = CreateUserRequest(
            username=username, password=password, role="ROLE_USER"
        )

        api_manager.admin_steps.create_invalid_user(create_user_request)
