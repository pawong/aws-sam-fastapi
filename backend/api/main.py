from fastapi import APIRouter, FastAPI
from mangum import Mangum

from backend.api.api_v1 import eight_ball, health

api = FastAPI()
router = APIRouter()


@api.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


router.include_router(health.router, prefix="/health", tags=["health"])
router.include_router(eight_ball.router, prefix="/8ball", tags=["eight_ball"])
api.include_router(router)

handler = Mangum(api, lifespan="off")
