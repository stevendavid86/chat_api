class LLMService:
    def generate(self, prompt):
        raise NotImplementedError

class MockLLMService(LLMService):
    def generate(self, prompt):
        return 'Mock LLM Service response'