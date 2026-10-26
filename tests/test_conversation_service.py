from models.message import Message
from repositories.conversation_repository import ConversationRepository
from services.llm_service import MockLLMService
from services.conversation_service import ConversationService

def test_create_conversation(conversation_service):
    conversation_id = conversation_service.create_conversation()
    conversation = conversation_service.conversation_repository.get_conversation(conversation_id)

    assert conversation_id is not None
    assert isinstance(conversation_id, str)
    assert conversation[0].role == 'system'
    assert conversation[0].content == 'You are a helpful programming assistant.'



def test_send_message(conversation_service):
    
    conversation_id = conversation_service.create_conversation()

    response = conversation_service.send_message(conversation_id, 'What is a linked list?')

    conversation = conversation_service.conversation_repository.get_conversation(conversation_id)

    assert response == 'Mock LLM Service response'
    assert conversation[0].role == 'system'
    assert conversation[0].content == 'You are a helpful programming assistant.'
    assert conversation[1].role == 'user'
    assert conversation[1].content == 'What is a linked list?'
    assert conversation[2].role == 'assistant'
    assert conversation[2].content == 'Mock LLM Service response'

def test_send_message_to_invalid_conversation(conversation_service):
    response = conversation_service.send_message('invalid_conversation_id', 
    'What is a linked list?')

    assert response is None