from fastapi import APIRouter, Request, status

from app.core.config import settings
from .get_parsed_data import get_currency_data
from .schemas import Result


router = APIRouter(tags=["Rates"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=Result,
)
async def get_currency(
    request: Request,
):
    from_ = request.query_params.get("from")
    to = request.query_params.get("to")
    value = request.query_params.get("value")

    if from_ and to and value:
        result = get_currency_data(from_cur=from_, to_cur=to, value=value)
    elif from_ and to:
        result = get_currency_data(from_cur=from_, to_cur=to, value=settings.default_value)
    else:
        result = get_currency_data(
            from_cur=settings.default_currency_code_from,
            to_cur=settings.default_currency_code_to,
            value=settings.default_value
        )

    return {
        "result": result
    }
