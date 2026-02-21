import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from source.config.settings import settings
from source.api.routes import api_router
from source.utils.logger import logger
import os

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Backend for Voice Scheduling Agent",
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include centralized routers
app.include_router(api_router, prefix="/api")

@app.on_event("startup")
def startup_event():
    logger.info(f"Starting VAPI Voice Agent System. API Config: v{settings.VERSION}")

# Serve React Front End from source/ui/dist
uiPath = os.path.join(os.path.dirname(__file__), "ui", "dist")

if os.path.exists(uiPath):
    logger.info(f"Mounting static UI from {uiPath}")
    app.mount("/assets", StaticFiles(directory=os.path.join(uiPath, "assets")), name="assets")
    
    @app.get("/{full_path:path}")
    def serve_react_app(full_path: str):
        """Serve React index.html for unknown routes to allow client-side routing, or just the root."""
        # For a basic single-page setup, we just return index.html
        return FileResponse(os.path.join(uiPath, "index.html"))
else:
    logger.warning("UI dist folder not found. API mode only.")
    @app.get("/", response_class=HTMLResponse)
    def root():
        return "<h1>API is running. (React UI not built yet)</h1>"


if __name__ == "__main__":
    uvicorn.run("source.main:app", host="0.0.0.0", port=settings.PORT, reload=True)
