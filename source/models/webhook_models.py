from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional

class ToolCall(BaseModel):
    id: str
    function: Dict[str, Any]

class WebhookMessage(BaseModel):
    type: str
    toolCalls: Optional[List[ToolCall]] = None
    call: Optional[Dict[str, Any]] = None

class WebhookPayload(BaseModel):
    message: WebhookMessage
