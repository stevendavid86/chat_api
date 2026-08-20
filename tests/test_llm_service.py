from services.llm_service import MockLLMService

def test_mock_llm_service():
    llm = MockLLMService()

    response = llm.generate('user:\nHello\n\nassistant:\n')

    assert response == 'Mock LLM Service response'