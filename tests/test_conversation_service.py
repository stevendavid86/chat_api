from models.message import Message
from services.llm_service import MockLLMService
from services.conversation_service import ConversationService

def test_send_message():
    messages = [
        Message(
            role='system',
            content='You are a helpful programming assistant.'
        )
    ]

    llm_service = MockLLMService()
    conversation_service = ConversationService(llm_service)

    response = conversation_service.send_message(messages, 'What is a linked list?')

    assert response == 'Mock LLM Service response'
    assert messages[0].role == 'system'
    assert messages[0].content == 'You are a helpful programming assistant.'
    assert messages[1].role == 'user'
    assert messages[1].content == 'What is a linked list?'
    assert messages[2].role == 'assistant'
    assert messages[2].content == 'Mock LLM Service response'
