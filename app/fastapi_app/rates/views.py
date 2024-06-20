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
) -> dict:
    """
    Эндпоинт по получению курса одной валюты к другой
    через функцию get_currency_data получаем текущий курс и потом умножаем на value
    если query параметры не были переданы, то выдаем данные по умолчанию из конфига

    :param request: Request для получения query_params
    :return: (dict), Возвращаем словарь с "result"
    """
    from_ = request.query_params.get("from")
    to = request.query_params.get("to")
    value = request.query_params.get("value")

    if from_ and to and value:
        result = get_currency_data(from_cur=from_, to_cur=to) * float(value)
    elif from_ and to:
        result = get_currency_data(from_cur=from_, to_cur=to) * settings.default_value
    else:
        result = get_currency_data(
            from_cur=settings.default_currency_code_from,
            to_cur=settings.default_currency_code_to
        ) * settings.default_value

    return {
        "result": result
    }
