import pytest
from fixtures import driver  # Import the driver fixture


@pytest.fixture
def username():
    return "valid_user"


@pytest.fixture
def password():
    return "valid_password"
