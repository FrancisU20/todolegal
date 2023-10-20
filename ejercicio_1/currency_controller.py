from http.client import HTTPException
import json
import os
import re
import httpx
import yfinance as yf
from datetime import datetime, timedelta
import db_connection as db
import currency_model as cm
from pyodbc import IntegrityError


async def load_data_to_database(currency: str, fecha: str = None):
    try:
        fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Fecha inválida. Debe tener el formato YYYY-MM-DD",
        )

    data = yf.download(currency + "=X", start=fecha_obj)

    currency_obj = cm.Currency(currency, fecha_obj, data["Close"][0])

    cursor = db.connect_db()
    try:
        cursor.execute(
            "INSERT INTO dbo.exchange (currency, date, value) VALUES (?, ?, ?)",
            (currency_obj.currency, currency_obj.date, currency_obj.value),
        )
        cursor.commit()
    except IntegrityError:
        cursor.rollback()


async def load_current_year_data(currency: str):
    today = datetime.now()
    start_date = datetime(today.year, 1, 1)

    success_count = 0
    error_count = 0

    for i in range((today - start_date).days + 1):
        fecha = start_date + timedelta(days=i)
        try:
            result = await load_data_to_database(currency, fecha.strftime("%Y-%m-%d"))
            if result == "success":
                success_count += 1
            else:
                error_count += 1
        except Exception as e:
            error_message = str(e.args[0]) if e.args else str(e)
            print(f"Atención: {error_message}")
            error_count += 1

    response = {
        "message": f"Carga de datos del año actual para {currency}",
        "success_count": success_count,
        "error_count": error_count,
    }
    return response


async def load_current_week_data(currency: str):
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())

    success_count = 0
    error_count = 0

    for i in range(7):
        fecha = start_of_week + timedelta(days=i)
        if fecha <= today:
            try:
                result = await load_data_to_database(
                    currency, fecha.strftime("%Y-%m-%d")
                )
                if result == "success":
                    success_count += 1
                else:
                    error_count += 1
            except Exception as e:
                error_message = str(e.args[1]) if e.args else str(e)
                clean_error_message = re.sub(r"[\(\[\{].*?[\)\]\}]", "", error_message)
                print(f"Atención: {clean_error_message}")
                error_count += 1

    response = {
        "message": f"Carga de datos de la semana actual para {currency}",
        "success_count": success_count,
        "error_count": error_count,
    }
    return response


async def get_currency_data():
    cursor = db.connect_db()
    cursor.execute("SELECT * FROM dbo.exchange")
    rows = cursor.fetchall()

    # Crear una lista de diccionarios para cada fila
    data = [
        {
            "currency": row[0].strip(),
            "date": row[1].strftime("%Y-%m-%d").strip(),
            "value": float(row[2]),
        }
        for row in rows
    ]

    # Convertir el diccionario en formato JSON sin caracteres de escape
    json_data = json.dumps(data, ensure_ascii=False)

    return json_data

async def post_webhook():
    try:
        # Obtén los datos de la función get_currency_data() o de donde sea que los obtengas
        data = await get_currency_data()

        # URL del webhook
        webhook_url = os.environ.get("webhook")

        # Realiza una solicitud POST al webhook con los datos
        async with httpx.AsyncClient() as client:
            response = await client.post(webhook_url, json=data)
            response.raise_for_status()  # Levanta una excepción si la respuesta no es exitosa

        return {"message": "Datos enviados exitosamente al webhook.", "data": data}
    except httpx.RequestError as e:
        # Manejar errores de solicitud, como problemas de red
        return f"Error en la solicitud POST: {str(e)}"
    except httpx.HTTPStatusError as e:
        # Manejar errores relacionados con el estado HTTP de la respuesta
        return f"Error HTTP al realizar la solicitud POST: {e}"
    except Exception as e:
        # Manejar otros errores inesperados
        return f"Error inesperado: {str(e)}"
