from fastapi import APIRouter

from .rates.views import router as rates_router

router = APIRouter()
router.include_router(router=rates_router, prefix="/rates")

