from repositories.conversation_repository import ConversationRepository
from services.conversation_service import ConversationService
from services.llm_service import MockLLMService, OpenAILLMService, LLMService

repository = ConversationRepository()
llm = MockLLMService()
conversation_service = ConversationService(llm, repository)

conversation_id = repository.create_conversation()


print('conversation_id:')
print(conversation_id)

response = conversation_service.send_message(
    conversation_id, 
    'What is a list in Python?'
)

print('response:')
print(response)

response = conversation_service.send_message(
    conversation_id, 
    'What is a dictionary in Python?'
)

print('response:')
print(response)

print('\nconversation:')

conversation = repository.get_conversation(conversation_id)
for message in conversation:
    print(f'{message.role}: {message.content}')