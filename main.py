import cv2
import time
from datetime import datetime
from detector import LicensePlateDetector
from ocr_reader import OCRReader
from database import DatabaseHandler
from json_handler import JSONHandler

class LicensePlateSystem:
    def __init__(self):
        self.detector = LicensePlateDetector()
        self.ocr = OCRReader()
        self.db = DatabaseHandler()
        self.json_handler = JSONHandler()
        self.interval = 20  # seconds

    def process_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        start_time = time.time()
        interval_detections = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Detect license plates
            detections = self.detector.detect(frame)
            
            for bbox in detections:
                # Extract license plate region
                plate_img = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]
                
                # Perform OCR
                plate_text, confidence = self.ocr.read_text(plate_img)
                
                if plate_text:
                    detection_data = {
                        "plate_number": plate_text,
                        "confidence": confidence,
                        "timestamp": datetime.now().isoformat(),
                        "bbox": bbox
                    }
                    interval_detections.append(detection_data)
                    
                    # Save to database
                    self.db.insert_detection(detection_data)

            # Check if interval has passed
            if time.time() - start_time >= self.interval:
                self.json_handler.save_interval(interval_detections, start_time)
                interval_detections = []
                start_time = time.time()

            # Display frame
            cv2.imshow('License Plate Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    system = LicensePlateSystem()
    system.process_video("path_to_your_video.mp4") 