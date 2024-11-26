import sqlite3
from datetime import datetime

class DatabaseHandler:
    def __init__(self, db_path='license_plates.db'):
        self.db_path = db_path
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS license_plates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                plate_number TEXT NOT NULL,
                confidence FLOAT,
                timestamp DATETIME,
                bbox_coordinates TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def insert_detection(self, detection_data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO license_plates (plate_number, confidence, timestamp, bbox_coordinates)
            VALUES (?, ?, ?, ?)
        ''', (
            detection_data['plate_number'],
            detection_data['confidence'],
            detection_data['timestamp'],
            str(detection_data['bbox'])
        ))
        conn.commit()
        conn.close() 