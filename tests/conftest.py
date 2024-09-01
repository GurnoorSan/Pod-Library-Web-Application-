import pytest

from podcast import create_app
from podcast.adapters.memory_repository import MemoryRepository

from path_utils.utils import get_project_root


# Gets data from test data folder, not the main data folder in the podcast directory.
TEST_DATA_PATH = get_project_root() / "tests" / "data"


@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    repo.populate(TEST_DATA_PATH)
    return repo
