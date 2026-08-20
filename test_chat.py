from models.message import Message
from prompts.transcript import build_transcript
from services.llm_service import OpenAILLMService

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
llm = OpenAILLMService()
response = llm.generate(prompt)

print('prompt:')
print(prompt)

print('response:')
print(response)