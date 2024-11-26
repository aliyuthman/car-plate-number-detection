from ultralytics import YOLO
import cv2
import numpy as np

class LicensePlateDetector:
    def __init__(self, model_path='yolov10.pt'):
        self.model = YOLO(model_path)
        self.conf_threshold = 0.5

    def detect(self, frame):
        results = self.model(frame)[0]
        detections = []

        for r in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = r
            if score > self.conf_threshold:
                detections.append([int(x1), int(y1), int(x2), int(y2)])

        return detections 