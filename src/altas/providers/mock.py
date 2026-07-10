class MockProvider:

    def invoke(self, message: str) -> str:
        return f"Echo: {message}"