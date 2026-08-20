from openai import OpenAI

class LLMService:
    def generate(self, prompt):
        raise NotImplementedError

class MockLLMService(LLMService):
    def generate(self, prompt):
        return 'Mock LLM Service response'

class OpenAILLMService(LLMService):
    def __init__(self):
        self.client = OpenAI()

    def generate(self, prompt):
        response = self.client.responses.create(
            model="gpt-5.6",
            input=prompt
        )

        return response.output_text