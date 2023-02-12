from src.data.find_user.find import FindUser
from tests.helpers.repository.user import UserRepositoryFake


def test_should_find_user_by_id():

    user_repo = UserRepositoryFake()
    find_user = FindUser(user_repository=user_repo)

    response = find_user.by_id(user_id=123)

    assert user_repo.select_user_params["user_id"] == 123

    assert response["success"] is True


def test_should_fail_when_id_is_invalid():

    user_repo = UserRepositoryFake()
    find_user = FindUser(user_repository=user_repo)

    response = find_user.by_id(user_id="shoud_fail")

    assert user_repo.select_user_params == {}

    assert response["success"] is False
    assert response["data"] is None


def test_should_find_user_by_name():

    user_repo = UserRepositoryFake()
    find_user = FindUser(user_repository=user_repo)

    response = find_user.by_name(name="fake_name")

    assert user_repo.select_user_params["name"] == "fake_name"

    assert response["success"] is True
    assert response["data"]


def test_should_fail_when_user_name_is_invalid():

    user_repo = UserRepositoryFake()
    find_user = FindUser(user_repository=user_repo)

    response = find_user.by_name(name=1234)

    assert user_repo.select_user_params == {}

    assert response["success"] is False
    assert response["data"] is None
