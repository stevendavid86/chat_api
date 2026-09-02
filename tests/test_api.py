from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_create_conversation():
    response = client.post("/conversations")
    assert response.status_code == 200
    assert "conversation_id" in response.json()
    assert response.json()["conversation_id"] is not None

def test_send_message():
    #create new conversation
    new_conversation = client.post("/conversations")
    conversation_id = new_conversation.json()["conversation_id"]

    # Send message to the conversation
    message_content = {"content": "Hello, how are you?"}
    message_response = client.post(
        f"/conversations/{conversation_id}/messages", json=message_content
    )

    assert message_response.status_code == 200
    assert "response" in message_response.json()
    assert message_response.json()["response"] is not None

def test_conversation_history():
    # Create new conversation
    new_conversation = client.post("/conversations")
    conversation_id = new_conversation.json()["conversation_id"]

    # Send a message to the conversation
    message_content = {"content": "Hello, how are you?"}
    message_response = client.post(
        f"/conversations/{conversation_id}/messages", json=message_content
    )

    # Get conversation history
    conversation_history = client.get(f"/conversations/{conversation_id}")

    assert conversation_history.status_code == 200
    assert "conversation_id" in conversation_history.json()
    assert conversation_history.json()["conversation_id"] == conversation_id
    assert "messages" in conversation_history.json()
    # 1 system message,1 user message, and 1 LLM response
    assert len(conversation_history.json()["messages"]) == 3

def test_multiple_messages():
    # Create new conversation
    new_conversation = client.post("/conversations")
    conversation_id = new_conversation.json()["conversation_id"]

    # Send multiple messages to the conversation
    messages = [
        {"content": "Hello, how are you?"},
        {"content": "What is the weather like today?"},
        {"content": "Tell me a joke."}
    ]

    for message in messages:
        message_response = client.post(
            f"/conversations/{conversation_id}/messages", json=message
        )
        assert message_response.status_code == 200
        assert "response" in message_response.json()
        assert message_response.json()["response"] is not None

    # Get conversation history
    conversation_history = client.get(f"/conversations/{conversation_id}")

    assert conversation_history.status_code == 200
    assert "conversation_id" in conversation_history.json()
    assert conversation_history.json()["conversation_id"] == conversation_id
    assert "messages" in conversation_history.json()
    # 1 system message,3 user messages, and 3 LLM responses
    assert len(conversation_history.json()["messages"]) == 7 

def test_send_message_to_missing_conversation():
    response = client.post("/conversations/invalid/messages", json={"content": "Hello"})

    assert response.status_code == 404
    assert response.json() == {"detail": "Conversation not found"}

def test_get_missing_conversation():
    response = client.get("/conversations/invalid")

    assert response.status_code == 404
    assert response.json() == {"detail": "Conversation not found"}

def test_send_empty_message():
    # Create new conversation
    new_conversation = client.post("/conversations")
    conversation_id = new_conversation.json()["conversation_id"]

    # Send empty message to the conversation
    message_content = {}
    message_response = client.post(
        f"/conversations/{conversation_id}/messages", json=message_content
    )

    assert message_response.status_code == 422