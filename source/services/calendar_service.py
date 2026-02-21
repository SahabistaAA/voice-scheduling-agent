# Mock Calendar Service
import logging

logger = logging.getLogger(__name__)

class CalendarService:
    def __init__(self, credentials_path: str = None):
        self.credentials_path = credentials_path
        logger.info("Calendar service initialized (Mock Mode).")

    def create_event(self, summary: str, date: str, time: str, attendee_name: str) -> bool:
        """
        Mocks creating a Google Calendar event.
        Returns True if successful.
        """
        logger.info(f"MOCK: Creating event '{summary}' for {attendee_name} on {date} at {time}.")
        # In a real implementation, you would use google-api-python-client here
        return True

calendar_service = CalendarService()
