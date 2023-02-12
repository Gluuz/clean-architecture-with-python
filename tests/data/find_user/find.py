from src.data.find_user.find import FindUser
from tests.helpers.repository.user import UserRepositoryFake


def test_shout_find_user_by_id():

    user_repo = UserRepositoryFake()
    find_user = FindUser(user_repository=user_repo)

    response = find_user.by_id(user_id=123)

    assert user_repo.select_user_params["user_id"] == 123

    assert response["success"] is True
