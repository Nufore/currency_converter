# Сервис "Конвертер валют"
### Пример запроса
GET /api/rates/?from=USD&to=RYB&value=1
### Ответ
{
    "result": 62.16
}
### Разработка
Реализован на FastAPI

Сервис получения курса валют - [currency](https://www.currency.me.uk/)
___

## Инструкция по запуску приложения

Из корневой папки проекта `currency_converter` выполнить команду `docker compose up --build`
___
## Документация

После запуска приложения документация в виде swagger доступна по [ссылке](http://localhost:8000/docs)
___