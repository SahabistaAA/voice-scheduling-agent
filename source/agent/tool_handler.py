from typing import Dict, Any
from source.models.scheduling_models import ScheduleMeetingArgs
from source.utils.logger import logger
from source.services.calendar_service import calendar_service

def handle_tool_call(tool_call: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle incoming tool calls from VAPI.
    """
    function_name = tool_call.get("function", {}).get("name")
    arguments = tool_call.get("function", {}).get("arguments", {})
    tool_call_id = tool_call.get("id")

    if function_name == "createCalendarEvent":
        logger.info(f"Agent requested to schedule meeting with args: {arguments}")
        
        try:
            # Validate via Pydantic Model from the newly moved scheduling_models.py
            args_model = ScheduleMeetingArgs(**arguments)
            
            # Use calendar mock service replacing the old print with a service call
            calendar_service.create_event(
                summary=args_model.title or f"Meeting with {args_model.name}",
                date=args_model.date,
                time=args_model.time,
                attendee_name=args_model.name
            )
            
            result = f"Successfully scheduled '{args_model.title}' for {args_model.name} on {args_model.date} at {args_model.time}."
            return {
                "results": [
                    {
                        "toolCallId": tool_call_id,
                        "result": result
                    }
                ]
            }
        except Exception as e:
            logger.error(f"Error processing tool call: {e}")
            return {
                "results": [
                    {
                        "toolCallId": tool_call_id,
                        "error": str(e)
                    }
                ]
            }
            
    # Unknown tool
    logger.warning(f"Unknown tool called: {function_name}")
    return {
        "results": [
            {
                "toolCallId": tool_call_id,
                "error": "Unknown tool called"
            }
        ]
    }
