from fastapi import APIRouter

from v1.endpoints import endpoint

router = APIRouter()

router.include_router(endpoint.router)
