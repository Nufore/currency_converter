from pydantic import BaseModel
from fastapi import Query


class Result(BaseModel):
    result: float | str


class CustomQueryParams:
    def __init__(
            self,
            from_: str = Query("USD", alias="from", description="Валюта конвертации FROM"),
            to: str = Query("RUB", description="Валюта конвертации TO"),
            value: int = Query(1, description="Количество VALUE")
    ):
        self.from_ = from_
        self.to = to
        self.value = value
