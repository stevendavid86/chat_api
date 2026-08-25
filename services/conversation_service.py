from models.message import Message
from prompts.transcript import build_transcript
from repositories.conversation_repository import ConversationRepository
from services.llm_service import LLMService

class ConversationService:
    def __init__(self, llm_service, conversation_repository):
        self.llm_service = llm_service
        self.conversation_repository = conversation_repository

    def create_conversation(self):
        conversation_id = self.conversation_repository.create_conversation()

        self.conversation_repository.add_message(
            conversation_id,
            Message(role='system', content='You are a helpful programming assistant.')
        )

        return conversation_id

    def send_message(self, conversation_id, user_message):
        messages = self.conversation_repository.get_conversation(conversation_id)
        
        if messages is None:
            return None
        
        # Add the user's message to the conversation
        message = Message(role='user', content=user_message)
        self.conversation_repository.add_message(conversation_id, message)

        # Build new transcript with new user message
        prompt = build_transcript(messages)

        # Send prompt to LLM service and get response
        response = self.llm_service.generate(prompt)

        # Add llm's response to the conversation
        self.conversation_repository.add_message(
            conversation_id, 
            Message(role='assistant', content=response)
        )
            
        return response