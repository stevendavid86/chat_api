import pytest

from database.database import initialize_database, get_connection
from fastapi.testclient import TestClient
from repositories.conversation_repository import ConversationRepository
from services.conversation_service import ConversationService
from services.llm_service import MockLLMService

from main import app, get_conversation_service, get_repository

@pytest.fixture
def client(conversation_service, repository):
    app.dependency_overrides[get_conversation_service] = lambda: conversation_service
    app.dependency_overrides[get_repository] = lambda: repository
    
    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()
        
@pytest.fixture
def repository(tmp_path):
    database_path = tmp_path / "test.db"
    initialize_database(database_path)
    return ConversationRepository(database_path)

@pytest.fixture
def conversation_service(repository):
    llm_service = MockLLMService()
    return ConversationService(llm_service, repository)