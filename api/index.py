from source.app import app
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Voice Scheduling Agent is running 🚀"}

handler = Mangum(app)