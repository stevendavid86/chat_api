from models.message import Message
from prompts.transcript import build_transcript

messages = [
    Message(
        role = 'system',
        content = 'You are a helpful programming assistant'
    ),
    Message(
        role = 'user',
        content = 'What is a Python dictionary?'
    ),
    Message(
        role = 'assistant',
        content = 'A Python dictionary stores key-value pairs.'
    ),
    Message(
        role = 'user',
        content = 'Can the keys be integers?'
    )
]

transcript = build_transcript(messages)
print(transcript)