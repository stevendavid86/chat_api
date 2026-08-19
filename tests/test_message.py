import pytest
from pydantic import ValidationError

from models.message import Message

def test_create_valid_user_message():
    message = Message(
        role = 'user',
        content = 'Hello'
    )

    assert message.role == 'user'
    assert message.content == 'Hello'

def test_create_valid_assistant_message():
    message = Message(
        role = 'assistant',
        content = 'Hello'
    )

    assert message.role == 'assistant'
    assert message.content == 'Hello'

def test_create_valid_system_message():
    message = Message(
        role = 'system',
        content = 'Hello'
    )

    assert message.role == 'system'
    assert message.content == 'Hello'

def test_invalid_role_message():
    with pytest.raises(ValidationError):
        message = Message(
            role = 'bananna',
            content = 'Hello'
        )


def test_missing_content():
    with pytest.raises(ValidationError):
        message = Message(
            role = 'user'
        )

def test_missing_role():
    with pytest.raises(ValidationError):
        message = Message(
            content = 'Hello'
        )