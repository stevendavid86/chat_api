from models.message import Message
from prompts.transcript import build_transcript

def test_build_transcript_with_user_message():
    messages = [
        Message(
            role = 'user',
            content = 'Hello'
        )
    ]

    transcript = build_transcript(messages)

    expected = """user:
Hello

assistant:
"""

    assert transcript == expected

def test_build_full_conversation():
    messages = [
        Message(
            role = 'system',
            content = 'You are a helpful programming assistant.'
        ),
        Message(
            role = 'user',
            content = 'What is Python?'
        ),
        Message(
            role = 'assistant',
            content = 'Python is a programming language.'
        ),
        Message(
            role = 'user',
            content = 'Is it object-oriented?'
        )
    ]

    transcript = build_transcript(messages)

    expected = """system:
You are a helpful programming assistant.

user:
What is Python?

assistant:
Python is a programming language.

user:
Is it object-oriented?

assistant:
"""

    assert transcript == expected