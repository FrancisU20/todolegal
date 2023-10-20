import webbrowser
import asyncio
import dotenv
import uvicorn
from fastapi import FastAPI
from currency_controller import (
    load_current_year_data,
    load_current_week_data,
    post_webhook,
)

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "¡Bienvenido a la API de cambios de divisas!",
        "usage_instructions": [
            {
                "title": "Cargar datos del último año:",
                "example_url": "http://localhost:8000/year/USDEUR",
                "description": "Para cargar los datos del último año para una moneda específica.",
            },
            {
                "title": "Cargar datos de la última semana:",
                "example_url": "http://localhost:8000/week/USDEUR",
                "description": "Para cargar los datos de la última semana para una moneda.",
            },
            {
                "title": "Obtener datos de la base de datos:",
                "example_url": "http://localhost:8000/db_data",
                "description": "Para obtener los datos de la base de datos.",
            },
        ],
    }


@app.get("/year/{currency}")
async def year(currency: str):
    await load_current_year_data(currency)
    return {
        "message": "Se ha cargado los datos del último año a la base de datos de forma exitosa para la moneda "
        + currency
        + "."
    }


@app.get("/week/{currency}")
async def week(currency: str):
    await load_current_week_data(currency)
    return {
        "message": "Se ha cargado los datos de la ultima semana a la base de datos de forma exitosa para la moneda "
        + currency
        + "."
    }


@app.get("/db_data")
async def db_data():
    response = await post_webhook()
    return response


if __name__ == "__main__":
    dotenv.load_dotenv()
    url = "http://localhost:8000"
    webbrowser.open(url)

    # Agrega un retraso de unos segundos para dar tiempo al navegador
    asyncio.sleep(5)  # Cambia el valor de 5 según tus necesidades

    uvicorn.run(app, host="localhost", port=8000)
