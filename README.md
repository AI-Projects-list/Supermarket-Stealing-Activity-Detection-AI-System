
# 🛒 Supermarket Stealing Activity Detection AI System

This project is an AI-powered system to detect and log suspicious or stealing activity in supermarkets using object detection, action recognition, and face recognition. It stores video/photo evidence and face data in a database and provides a monitoring dashboard via a web interface.

## 📌 Features

- Real-time object and person detection using YOLOv8
- Face recognition using `face_recognition` library
- Suspicious behavior detection via action recognition (placeholder for future models)
- Stores incident data (video, photo, face ID, action) in a database
- Web dashboard for monitoring incidents
- Deployed on GCP using Cloud Run, Cloud SQL, and Firebase Hosting

---

## 🧠 AI Modules

| Module             | Technology              | Description |
|--------------------|--------------------------|-------------|
| Object Detection   | YOLOv8 + OpenCV          | Detects people and objects (bags, hands, goods) |
| Face Recognition   | `face_recognition` lib   | Recognizes known/unknown individuals |
| Action Recognition | (Planned: SlowFast/TSN)  | Detects suspicious activity (e.g. hiding items) |

---

## 📁 Project Structure

```
supermarket-stealing-ai/
├── ai_models/
│   ├── object_detection.py      # YOLOv8-based object detection
│   ├── face_recognition.py      # Face recognition and match
├── backend/
│   ├── app.py                   # FastAPI app entrypoint
│   ├── db.py                    # (future) DB config
│   └── routes/
│       ├── incidents.py         # Incident data API
│       └── faces.py             # Face data API
├── frontend/                    # React dashboard (to be implemented)
├── gcp/
│   ├── Dockerfile               # Container for backend
│   └── deployment.yaml          # Cloud Run deployment
├── scripts/
│   ├── upload_to_gcs.py         # Upload media to GCS
│   └── record_video.py          # Capture and save videos
├── README.md                    # Project documentation
```

---

## ☁️ GCP Deployment Plan

| Component     | Service             | Description |
|---------------|----------------------|-------------|
| Backend API   | Cloud Run            | Hosts FastAPI app |
| Frontend      | Firebase Hosting     | Public dashboard |
| Database      | Cloud SQL (Postgres) | Incident and face logs |
| File Storage  | Cloud Storage (GCS)  | Videos and images |
| Monitoring    | Cloud Logging        | Track events and errors |

---

## ⚙️ Installation & Running Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Object Detection

```bash
python ai_models/object_detection.py
```

### 3. Run Face Recognition

```bash
python ai_models/face_recognition.py
```

### 4. Start Backend API (Local)

```bash
uvicorn backend.app:app --reload --port 8000
```

---

## 🚀 Deploy to GCP

### 1. Build and Push Docker

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/stealing-api
```

### 2. Deploy to Cloud Run

```bash
gcloud run deploy stealing-api --image gcr.io/YOUR_PROJECT_ID/stealing-api --platform managed
```

### 3. Firebase Hosting for Frontend

```bash
cd frontend
npm run build
firebase deploy
```

---

## 📷 Incident Data Example

```json
{
  "face_id": "face123",
  "image_url": "https://storage.googleapis.com/.../img.jpg",
  "video_url": "https://storage.googleapis.com/.../vid.mp4",
  "detected_action": "hiding item in clothes",
  "timestamp": "2025-05-30T12:34:56Z"
}
```

---

## 🧪 Future Improvements

- Train action recognition model (e.g. SlowFast, PoseNet)
- Live stream integration with RTSP
- Alert system via email/SMS
- Face embedding database with cosine similarity
- Frontend dashboard with user authentication
