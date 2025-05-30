
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class Incident(BaseModel):
    face_id: str
    image_url: str
    video_url: str
    detected_action: str
    timestamp: datetime

@router.post("/")
def report_incident(incident: Incident):
    print(f"Incident logged: {incident}")
    return {"message": "Incident reported successfully"}
