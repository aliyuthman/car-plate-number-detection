from paddleocr import PaddleOCR

class OCRReader:
    def __init__(self):
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')

    def read_text(self, img):
        result = self.ocr.ocr(img, cls=True)
        if result and result[0]:
            text = result[0][1][0]  # Get the recognized text
            confidence = float(result[0][1][1])  # Get the confidence score
            return text, confidence
        return None, 0.0 