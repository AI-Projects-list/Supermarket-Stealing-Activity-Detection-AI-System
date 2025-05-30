
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class FaceData(BaseModel):
    face_id: str
    name: str
    image_url: str

@router.post("/")
def add_face(face: FaceData):
    print(f"Face added: {face}")
    return {"message": "Face data added successfully"}
