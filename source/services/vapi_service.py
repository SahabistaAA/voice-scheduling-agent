import requests
from source.config.settings import settings
from source.utils.logger import logger

VAPI_BASE_URL = "https://api.vapi.ai"

class VapiService:
    def __init__(self):
        self.api_key = settings.vapi_config.api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def fetch_assistant(self, assistant_id: str):
        """Fetch assistant details from VAPI."""
        url = f"{VAPI_BASE_URL}/assistant/{assistant_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_call(self, phone_number: str, assistant_id: str):
        """Initiate an outbound call to a user."""
        url = f"{VAPI_BASE_URL}/call/phone"
        payload = {
            "phoneNumberId": settings.vapi_config.phone_number_id,
            "customer": {
                "number": phone_number
            },
            "assistantId": assistant_id
        }
        response = requests.post(url, headers=self.headers, json=payload)
        if not response.ok:
            logger.error(f"VAPI Error: {response.text}")
            response.raise_for_status()
        return response.json()

vapi_service = VapiService()
