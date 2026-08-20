from models.message import Message
from propmps.transcript import build_transcript
from services.llm_service import MockLLMService

messages = [
    Message(
        role = 'system',
        content = 'You are a helpful programming assistant.'
    ),
    Message(
        role = 'user',
        content = 'What is a linked list?'
    )
]

prompt = build_transcript(messages)
llm = MockLLMService()
response = llm.generate(prompt)

print('prompt:')
print(prompt)

print('response:')
print('response')