from fastapi import HTTPException, status


class LLMError(HTTPException):
    def __init__(self, detail: str = "LLM service encountered an error"):
        super().__init__(status_code=status.HTTP_502_BAD_GATEWAY, detail=detail)


class LLMConnectionError(HTTPException):
    def __init__(self, detail: str = "Failed to connect to LLM provider"):
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=detail
        )


class InvalidRequestError(HTTPException):
    def __init__(self, detail: str = "Invalid request"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
