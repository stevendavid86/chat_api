from models.message import Message
from repositories.conversation_repository import ConversationRepository

def test_create_conversation():
    repo = ConversationRepository()
    conversation_id = repo.create_conversation()

    assert conversation_id is not None
    assert isinstance(conversation_id, str)
    assert repo.get_conversation(conversation_id) == []

def test_add_message():
    repo = ConversationRepository()
    conversation_id = repo.create_conversation()
    message = Message(role="user", content="Hello, world!")

    result = repo.add_message(conversation_id, message)

    assert result is True
    assert repo.get_conversation(conversation_id) == [message]

def test_add_message_to_nonexistent_conversation():
    repo = ConversationRepository()
    message = Message(role="user", content="Hello, world!")

    result = repo.add_message("nonexistent_id", message)

    assert result is False