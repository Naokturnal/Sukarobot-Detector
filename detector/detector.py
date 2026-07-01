from ultralytics import YOLO
from config import MODEL_PATH
import cv2


class Detector:

    def __init__(self):

        self.model = YOLO(str(MODEL_PATH))

    def get_model_info(self):

        return {

            "model": str(MODEL_PATH.name),

            "classes": self.model.names

        }

    def detect(self, image):

        results = self.model(image)

        return results