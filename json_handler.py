import json
from datetime import datetime
import os

class JSONHandler:
    def __init__(self, output_dir='output'):
        self.output_dir = output_dir
        self.cumulative_file = os.path.join(output_dir, 'cumulative.json')
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize cumulative file if it doesn't exist
        if not os.path.exists(self.cumulative_file):
            with open(self.cumulative_file, 'w') as f:
                json.dump({"intervals": []}, f)

    def save_interval(self, detections, start_time):
        interval_data = {
            "start_time": datetime.fromtimestamp(start_time).isoformat(),
            "end_time": datetime.now().isoformat(),
            "detections": detections
        }

        # Save interval file
        interval_file = os.path.join(
            self.output_dir, 
            f"interval_{int(start_time)}.json"
        )
        with open(interval_file, 'w') as f:
            json.dump(interval_data, f, indent=4)

        # Update cumulative file
        self._update_cumulative(interval_data)

    def _update_cumulative(self, interval_data):
        try:
            with open(self.cumulative_file, 'r') as f:
                cumulative_data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            cumulative_data = {"intervals": []}

        # Add new interval while checking for duplicates
        existing_plates = set()
        for interval in cumulative_data["intervals"]:
            for detection in interval["detections"]:
                existing_plates.add(detection["plate_number"])

        # Filter out duplicates from new interval
        interval_data["detections"] = [
            d for d in interval_data["detections"]
            if d["plate_number"] not in existing_plates
        ]

        cumulative_data["intervals"].append(interval_data)

        with open(self.cumulative_file, 'w') as f:
            json.dump(cumulative_data, f, indent=4) 