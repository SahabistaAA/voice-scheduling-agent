from source.config.settings import settings

def get_assistant_configuration() -> dict:
    """
    Returns the programmatic configuration for the VAPI Voice Scheduling Assistant.
    This can be used to dynamically create or update the assistant on VAPI.
    """
    return {
        "name": "Scheduling Assistant",
        "firstMessage": "Hello! I am your scheduling assistant. What is your name, and when would you like to schedule a meeting?",
        "model": {
            "provider": "openai",
            "model": "gpt-4"
        },
        "voice": {
            "provider": "11labs",
            "voiceId": "burt" # arbitrary default
        },
        "systemPrompt": (
            "You are a polite, professional virtual scheduling assistant.\n"
            "Your goal is to book a meeting with the user.\n\n"
            "Follow these steps:\n"
            "1. Greet the user and ask for their name.\n"
            "2. Once they provide their name, ask for their preferred date and time for the meeting.\n"
            "3. Optionally, ask if they have a specific title or topic for the meeting.\n"
            "4. Confirm all the details (Name, Date, Time, Title) with the user before proceeding.\n"
            "5. Once confirmed, use the `createCalendarEvent` tool to schedule the meeting.\n"
            "6. Let them know the meeting has been scheduled and end the conversation politely.\n"
        ),
        "tools": [
            {
                "type": "createCalendarEvent",
                "function": {
                    "name": "createCalendarEvent",
                    "description": "Schedules a calendar event for the user.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "description": "User's name"},
                            "date": {"type": "string", "description": "Date (YYYY-MM-DD)"},
                            "time": {"type": "string", "description": "Time (HH:MM)"},
                            "title": {"type": "string", "description": "Title of the meeting"}
                        },
                        "required": ["name", "date", "time"]
                    }
                }
            }
        ]
    }
