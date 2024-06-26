from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_prefix: str = "/api"

    base_url: str = "https://www.currency.me.uk/convert"

    default_currency_code_from: str = "USD"

    default_currency_code_to: str = "RUB"

    default_value: float = 1.0

    html_tag: str = "input"
    html_attr: str = "id"
    html_attr_name: str = "answer"


settings = Settings()
