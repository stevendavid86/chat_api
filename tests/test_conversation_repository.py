from database.database import initialize_database, get_connection
from models.message import Message
from repositories.conversation_repository import ConversationRepository

def test_create_conversation(repository):
    
    conversation_id = repository.create_conversation()

    assert conversation_id is not None
    assert isinstance(conversation_id, str)
    assert repository.get_conversation(conversation_id) == []

def test_add_message(repository):
    conversation_id = repository.create_conversation()
    message = Message(role="user", content="Hello, world!")

    result = repository.add_message(conversation_id, message)

    assert result is True
    assert repository.get_conversation(conversation_id) == [message]

def test_add_message_to_nonexistent_conversation(repository):    
    message = Message(role="user", content="Hello, world!")

    result = repository.add_message("nonexistent_id", message)

    assert result is False