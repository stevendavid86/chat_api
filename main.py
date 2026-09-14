from fastapi import FastAPI, HTTPException

from models.chat_request import ChatRequest
from repositories.conversation_repository import ConversationRepository
from services.conversation_service import ConversationService
from services.llm_service import MockLLMService, OpenAILLMService

app = FastAPI()

repository = ConversationRepository()
#llm = MockLLMService()
llm = OpenAILLMService()  # Uncomment this line to use the actual OpenAI LLM service
conversation_service = ConversationService(llm, repository)

@app.get("/")
def root():
    return {"message": "Hello, World!"}

# Create new conversation and return conversation ID
@app.post("/conversations")
def create_conversation():
    conversation_id = conversation_service.create_conversation()
    return {"conversation_id": conversation_id}

# Send message to conversation and return LLM's response
@app.post("/conversations/{conversation_id}/messages")
def send_message(conversation_id: str, chat_request: ChatRequest):
    response = conversation_service.send_message(conversation_id, chat_request.content)

    if response is None:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return {"response": response}

@app.get("/conversations/{conversation_id}")
def get_conversation(conversation_id: str):
    messages = repository.get_conversation(conversation_id)

    if messages is None:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return {"conversation_id": conversation_id, "messages": messages}