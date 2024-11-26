# License Plate Detection & Recognition System

A comprehensive system for real-time license plate detection and recognition using YOLOv10 and PaddleOCR. The system automatically stores detection data in both JSON files and SQLite database.

## Features

- 🚗 Real-time license plate detection using YOLOv10
- 📝 Text recognition using PaddleOCR
- 🕒 Automatic JSON file generation (20-second intervals)
- 💾 SQLite database storage
- 🔄 Cumulative JSON storage with deduplication
- 📊 Real-time visualization

## Project Structure

```
license-plate-system/
├── main.py              # Main application script
├── detector.py          # YOLOv10 detection implementation
├── ocr_reader.py        # PaddleOCR text recognition
├── database.py          # SQLite database handler
├── json_handler.py      # JSON file management
├── output/              # Generated JSON files directory
│   ├── interval_*.json  # Individual interval files
│   └── cumulative.json  # Cumulative detection data
└── license_plates.db    # SQLite database file
```

## Requirements

- Python 3.8+
- CUDA-compatible GPU (recommended)
- Webcam or video file for processing

## Installation

1. **Create and activate virtual environment:**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

2. **Install required packages:**

```bash
pip install paddlepaddle-gpu==2.6.0
pip install ultralytics paddleocr opencv-python
```

## Usage

### Basic Usage

```bash
# Process video file
python main.py --video path/to/video.mp4

# Use webcam
python main.py --source 0

# Custom output directory and interval
python main.py --video path/to/video.mp4 --output_dir ./custom_output --interval 30
```

### Output Formats

#### JSON Output Structure
```json
{
    "start_time": "2024-03-20T10:00:00",
    "end_time": "2024-03-20T10:00:20",
    "detections": [
        {
            "plate_number": "ABC123",
            "confidence": 0.95,
            "timestamp": "2024-03-20T10:00:05",
            "bbox": [100, 200, 300, 400]
        }
    ]
}
```

#### Database Schema
```sql
CREATE TABLE license_plates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plate_number TEXT NOT NULL,
    confidence FLOAT,
    timestamp DATETIME,
    bbox_coordinates TEXT
);
```

## Key Components

### 1. License Plate Detection (detector.py)
- Uses YOLOv10 for accurate license plate detection
- Configurable confidence threshold
- Returns bounding box coordinates

### 2. Text Recognition (ocr_reader.py)
- Implements PaddleOCR for text extraction
- Supports multiple languages
- Returns recognized text with confidence scores

### 3. Data Storage (database.py)
- SQLite database implementation
- Efficient data insertion
- Structured storage of detection results

### 4. JSON Management (json_handler.py)
- Generates interval-based JSON files
- Maintains cumulative detection history
- Implements deduplication logic

## Troubleshooting

### Common Issues

1. **CUDA/GPU Problems:**
   - Verify CUDA toolkit installation
   - Check GPU compatibility
   - Ensure correct CUDA version

2. **Installation Issues:**
   - For PaddleOCR errors: `pip install paddlepaddle-gpu`
   - For CUDA memory errors: Reduce batch size
   - For OpenCV issues: Reinstall using `pip install opencv-python`

## Performance Tips

- Use GPU acceleration when available
- Adjust detection confidence threshold as needed
- Optimize frame processing resolution
- Consider batch processing for large datasets

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Submit a pull request

## License

This project is licensed under the MIT License.


