from fastapi import APIRouter
from pydantic import BaseModel
from source.services.vapi_service import vapi_service
from source.core.exceptions import ExternalServiceError
from source.utils.logger import logger
from source.config.settings import settings

router = APIRouter(tags=["Voice Controller"])

class CallRequest(BaseModel):
    phone_number: str

@router.post("/call")
def make_outbound_call(request: CallRequest):
    """
    Endpoint to trigger an outbound call to the specified phone number.
    It expects an already created assistant_id on VAPI.
    """
    assistant_id = settings.vapi_config.assistant_id
    logger.info(f"Triggering outbound call to {request.phone_number} using assistant {assistant_id}")
    try:
        response = vapi_service.create_call(
            phone_number=request.phone_number,
            assistant_id=assistant_id
        )
        return {"status": "success", "call_id": response.get("id")}
    except Exception as e:
        logger.error(f"Failed to initiate call: {e}")
        raise ExternalServiceError(detail="Failed to initiate outbound call via VAPI")
