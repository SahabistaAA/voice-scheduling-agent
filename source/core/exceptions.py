from fastapi import HTTPException
from fastapi import status

class AgentConfigError(HTTPException):
    def __init__(self, detail: str = "Assistant Configuration Error"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)

class ExternalServiceError(HTTPException):
    def __init__(self, detail: str = "Failed to communicate with external service"):
        super().__init__(status_code=status.HTTP_502_BAD_GATEWAY, detail=detail)

class InvalidPayloadError(HTTPException):
    def __init__(self, detail: str = "Invalid payload received"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
