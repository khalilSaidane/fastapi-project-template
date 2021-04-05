import pytest
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from starlette.config import environ
from starlette.testclient import TestClient

# This line would raise an error if we use it after 'settings' has been imported.
environ['TESTING'] = 'TRUE'

from {{cookiecutter.project_slug}} import settings
from {{cookiecutter.project_slug}}.db.database import Base
from {{cookiecutter.project_slug}}.main import app


@pytest.fixture(autouse=True, scope="session")
def setup_test_database():
    """
    Create a clean test database every time the tests are run.
    """
    url = str(settings.DATABASE_URL)
    engine = create_engine(url, connect_args={"check_same_thread": False})
    if not database_exists(url):
        create_database(url)  # Create the test database if it doesn't exists.
    Base.metadata.create_all(bind=engine)  # Create the tables.
    yield  # Run the tests.
    Base.metadata.drop_all(bind=engine)  # Drop the test database.


@pytest.fixture()
def client():
    """
    Make a 'client' fixture available to test cases.
    """
    # Our fixture is created within a context manager. This ensures that
    # application startup and shutdown run for every test case.
    #
    # Because we've configured the DatabaseMiddleware with `rollback_on_shutdown`
    # we'll get a complete rollback to the initial state after each test case runs.
    with TestClient(app) as test_client:
        yield test_client
