import pytest

@pytest.fixture(scope="session")
def path():
    return "https://swapi.dev/"