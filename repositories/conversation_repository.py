import uuid

from database.database import get_connection
from models.message import Message

class ConversationRepository:
    
    def create_conversation(self):
        conversation_id = str(uuid.uuid4())

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("insert into conversations (id) values (?)", (conversation_id,))
        connection.commit()
        connection.close()

        return conversation_id

    def get_conversation(self, conversation_id):
        connection = get_connection()
        cursor = connection.cursor()

        #check if conversation exists, return None if it does not
        cursor.execute("select id from conversations where id = ?", (conversation_id,))
        conversation = cursor.fetchone()
        
        if conversation is None:
            connection.close()
            return None  # Conversation does not exist

        #if conversation exists, fetch all messages in conversation
        cursor.execute(
            "select role, content from messages where conversation_id = ? order by id asc",
            (conversation_id,)
        )
        
        messages = []

        #iterate over returned messages, create Message objects, and append them to the messages list
        for row in cursor.fetchall():
            messages.append(Message(role=row[0], content=row[1]))

        connection.close()
        return messages

    def add_message(self, conversation_id, message):
        connection = get_connection()
        cursor = connection.cursor()

        #fetch conversation, return false if conversation does not exist
        cursor.execute("select id from conversations where id = ?", (conversation_id,))
        if cursor.fetchone() is None:
            connection.close()
            return False  # Conversation does not exist

        #add the message to the database    
        cursor.execute(
            """
            INSERT INTO messages (conversation_id, role, content)
            VALUES (?, ?, ?)
            """, 
            (conversation_id, message.role, message.content)
        )

        connection.commit()
        connection.close()
        
        return True