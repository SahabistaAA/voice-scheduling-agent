from fastapi import APIRouter, Request, HTTPException
from source.utils.logger import logger
from source.agent.tool_handler import handle_tool_call
from source.models.webhook_models import WebhookPayload
from source.core.exceptions import InvalidPayloadError

router = APIRouter(tags=["Webhook"])

@router.post("/")
async def vapi_webhook(payload: WebhookPayload):
    """
    Endpoint for VAPI to send Server URL events.
    Handles 'tool-calls' events strongly typed with Pydantic.
    """
    try:
        message = payload.message
        if message.type == "tool-calls" and message.toolCalls:
            results = []
            
            # Since our older handle_tool_call takes dicts, we pass model diffs
            # Or we could just dict-ify it for compatibility.
            for tool_call in message.toolCalls:
                res = handle_tool_call(tool_call.model_dump())
                if "results" in res:
                    results.extend(res["results"])
                    
            return {"results": results}
        
        # We can ignore other message types for now
        return {"message": "Event ignored", "type": message.type}
        
    except Exception as e:
        logger.error(f"Error handling webhook: {str(e)}")
        raise InvalidPayloadError(detail=str(e))
