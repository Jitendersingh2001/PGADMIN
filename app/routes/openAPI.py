from fastapi import APIRouter

router = APIRouter()

@router.get("/state")
async def states():
    return [{"username": "Rick1"}, {"username": "Morty"}]