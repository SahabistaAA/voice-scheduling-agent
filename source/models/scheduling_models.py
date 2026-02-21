from pydantic import BaseModel, Field
from typing import Optional

class ScheduleMeetingArgs(BaseModel):
    name: str = Field(..., description="The name of the user to schedule the meeting for")
    date: str = Field(..., description="The preferred date (YYYY-MM-DD)")
    time: str = Field(..., description="The preferred time (HH:MM)")
    title: Optional[str] = Field(None, description="The title of the meeting")

class MeetingConfirmation(BaseModel):
    status: str
    message: str
    event_id: Optional[str] = None
