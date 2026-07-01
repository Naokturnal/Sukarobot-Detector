from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.home import router as home_router
from routes.detect import router as detect_router
from routes.upload import router as upload_router

app = FastAPI(
    title="LEGO Detector",
    version="1.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(home_router)
app.include_router(detect_router)
app.include_router(upload_router)