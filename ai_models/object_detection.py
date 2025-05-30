
import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

def detect_objects(frame):
    results = model(frame)
    for r in results:
        for box in r.boxes:
            print(f"Detected {r.names[int(box.cls)]} with confidence {box.conf:.2f}")
    return results

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret: break
        detect_objects(frame)
        cv2.imshow("Object Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
