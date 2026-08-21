from models.message import Message
from prompts.transcript import build_transcript
from services.llm_service import LLMService

class ConversationService:
    def __init__(self, llm_service):
        self.llm_service = llm_service

    def send_message(self, messages, user_message):
        messages.append(
            Message(role='user', content=user_message)
            )

        prompt = build_transcript(messages)
        response = self.llm_service.generate(prompt)

        messages.append(
            Message(role='assistant', content=response)
            )
            
        return response