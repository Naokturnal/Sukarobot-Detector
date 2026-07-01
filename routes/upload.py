from fastapi import APIRouter

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.get("/")
async def upload():

    return {
        "status": "success",
        "message": "Upload API Ready"
    }