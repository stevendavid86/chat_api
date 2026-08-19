from models.message import Message

def build_transcript(messages):
    transcript = ""

    for message in messages:
        role = message.role.upper()
        content = message.content

        transcript += f'{role}:\n'
        transcript += f'{content}\n\n'

    transcript += 'Assistant:\n'

    return transcript