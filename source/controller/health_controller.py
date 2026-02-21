from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health")
def health_check():
    return {"status": "ok", "message": "Voice Scheduling Agent is running"}
