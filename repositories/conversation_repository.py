from models.message import Message

import uuid

class ConversationRepository:
    def __init__(self):
        self.conversations = {}

    def create_conversation(self):
        conversation_id = str(uuid.uuid4())
        self.conversations[conversation_id] = []
        return conversation_id

    def get_conversation(self, conversation_id):
        return self.conversations.get(conversation_id)

    def add_message(self, conversation_id, message):
        conversation = self.get_conversation(conversation_id)

        if conversation is None:
            return False
        
        conversation.append(message)
        return True