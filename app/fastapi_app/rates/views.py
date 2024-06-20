from fastapi import APIRouter, status, Depends, Response

from .get_parsed_data import get_currency_data
from .schemas import Result, CustomQueryParams

router = APIRouter(tags=["Rates"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=Result,
)
async def get_currency(
        response: Response,
        params: CustomQueryParams = Depends(),
) -> dict:
    """
    Эндпоинт по получению курса одной валюты к другой
    """

    cur_rate = get_currency_data(
        from_cur=params.from_,
        to_cur=params.to,
    )

    if isinstance(cur_rate, str):
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "result": cur_rate
        }

    result = cur_rate * float(params.value)

    return {
        "result": result
    }
