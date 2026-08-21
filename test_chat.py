from models.message import Message
from services.conversation_service import ConversationService
from services.llm_service import MockLLMService, OpenAILLMService, LLMService

messages = [
    Message(
        role = 'system',
        content = 'You are a helpful programming assistant.'
    )
]

llm = MockLLMService()
conversation_service = ConversationService(llm)

response = conversation_service.send_message(
    messages, 
    'What is a linked list?')

print('response:')
print(response)

response = conversation_service.send_message(
    messages,
    'How is it different from an array?'
    )

print('response:')
print(response)

print('\nmessages:')
for message in messages:
    print(f'{message.role}: {message.content}')