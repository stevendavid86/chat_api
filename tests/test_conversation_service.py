from models.message import Message
from repositories.conversation_repository import ConversationRepository
from services.llm_service import MockLLMService
from services.conversation_service import ConversationService

def test_send_message():
    
    llm_service = MockLLMService()
    repository = ConversationRepository()
    conversation_service = ConversationService(llm_service, repository)

    message_id = conversation_service.create_conversation()

    response = conversation_service.send_message(message_id, 'What is a linked list?')

    converstaion = repository.get_conversation(message_id)

    assert response == 'Mock LLM Service response'
    assert converstaion[0].role == 'system'
    assert converstaion[0].content == 'You are a helpful programming assistant.'
    assert converstaion[1].role == 'user'
    assert converstaion[1].content == 'What is a linked list?'
    assert converstaion[2].role == 'assistant'
    assert converstaion[2].content == 'Mock LLM Service response'
