import pytest

from database.database import initialize_database, get_connection
from repositories.conversation_repository import ConversationRepository
from services.conversation_service import ConversationService
from services.llm_service import MockLLMService

@pytest.fixture
def repository(tmp_path):
    database_path = tmp_path / "test.db"
    initialize_database(database_path)
    return ConversationRepository(database_path)

@pytest.fixture
def conversation_service(repository):
    llm_service = MockLLMService()
    return ConversationService(llm_service, repository)