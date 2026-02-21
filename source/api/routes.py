from fastapi import APIRouter
from source.controller.health_controller import router as health_router
from source.controller.webhook_controller import router as webhook_router
from source.controller.voice_controller import router as voice_router

api_router = APIRouter()

api_router.include_router(health_router, prefix="/health")
api_router.include_router(webhook_router, prefix="/webhook")
api_router.include_router(voice_router, prefix="/voice")
