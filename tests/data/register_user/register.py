from src.data.register_user.register import RegisterUser
from tests.helpers.repository.user import UserRepositoryFake


def test_should_success_register_user():
    user_repo = UserRepositoryFake()
    register_user = RegisterUser(user_repository=user_repo)

    response = register_user.register(name="fake_name", password="fake_password")

    assert user_repo.insert_user_params["name"] == "fake_name"
    assert user_repo.insert_user_params["password"] == "fake_password"

    assert response["success"] is True


def test_should_fail_register_user():
    user_repo = UserRepositoryFake()
    register_user = RegisterUser(user_repository=user_repo)

    response = register_user.register(name=123, password=1234)

    assert response["success"] is False
    assert response["data"] is None
