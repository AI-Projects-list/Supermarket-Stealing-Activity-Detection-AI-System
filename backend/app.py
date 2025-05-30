
from fastapi import FastAPI
from backend.routes import incidents, faces

app = FastAPI()

app.include_router(incidents.router, prefix="/api/incidents")
app.include_router(faces.router, prefix="/api/faces")

@app.get("/")
def read_root():
    return {"status": "Supermarket AI Backend Running"}
