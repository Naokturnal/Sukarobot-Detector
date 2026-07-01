from fastapi import Body
from fastapi import APIRouter, UploadFile, File
import numpy as np
import cv2
import base64

from detector.detector import Detector
from detector.result_parser import parse_results

router = APIRouter(tags=["YOLO"])

detector = Detector()


@router.get("/model")
async def model_info():

    return detector.get_model_info()


@router.post("/detect/image")
async def detect_image(file: UploadFile = File(...)):

    contents = await file.read()

    image = np.frombuffer(contents, np.uint8)

    frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

    results = detector.detect(frame)

    return parse_results(results)

@router.post("/detect/frame")
async def detect_frame(data: dict = Body(...)):

    image_data = data["image"]

    image_data = image_data.split(",")[1]

    image = base64.b64decode(image_data)

    image = np.frombuffer(image, np.uint8)

    frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

    results = detector.detect(frame)

    return parse_results(results)