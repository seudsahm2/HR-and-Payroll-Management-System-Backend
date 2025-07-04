import pytest

from hr_and_payroll_management_system_backend.users.models import User
from hr_and_payroll_management_system_backend.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()
