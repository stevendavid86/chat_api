import pytest

from database.database import initialize_database, get_connection
from repositories.conversation_repository import ConversationRepository

@pytest.fixture
def repository(tmp_path):
    database_path = tmp_path / "test.db"
    initialize_database(database_path)
    return ConversationRepository(database_path)