import datetime
import os
import dotenv
import requests
import json
import time
import db_connection as db

# Variables globales
dweet_url = "https://dweet.io/get/dweets/for/thecore"
start_time = time.time()


def lambda_handler(event, context):
    try:
        while True:
            # Verificar el tiempo transcurrido
            elapsed_time = time.time() - start_time

            # Comprobar si han pasado 15 minutos (900 segundos)
            if elapsed_time >= 900:
                print("Han pasado 15 minutos. Enviando datos al webhook...")
                # Enviar datos al webhook
                post_webhook()
                # parar el bucle
                break

            # Realizar una solicitud HTTP a Dweet.io
            response = requests.get(dweet_url)
            data = json.loads(response.text)

            temperature = data.get("with")[0].get("content").get("temperature")
            humidity = data.get("with")[0].get("content").get("humidity")

            save_to_db(temperature, humidity)

            # Esperar 1 minuto antes de la próxima solicitud
            time.sleep(60)

    except Exception as e:
        print({"statusCode": 500, "body": json.dumps({"error": str(e)})})


def save_to_db(temperature: float, humidity: float):
    try:
        cursor = db.connect_db()
        cursor.execute(
            "INSERT INTO dbo.weather (temperature, humidity, date) VALUES (?, ?, ?)",
            (temperature, humidity, datetime.datetime.now()),
        )
        cursor.commit()
        cursor.close()
        print("Datos guardados en la base de datos.")
    except Exception as e:
        print(f"Error al guardar en la base de datos: {str(e)}")


def get_weather_data():
    cursor = db.connect_db()
    cursor.execute("SELECT * FROM dbo.weather")
    rows = cursor.fetchall()

    # Crear una lista de diccionarios para cada fila
    data = [
        {
            "temperature": float(row[1]),
            "humidity": float(row[2]),
            "date": row[3].strftime("%Y-%m-%d").strip(),
        }
        for row in rows
    ]

    # Convertir el diccionario en formato JSON sin caracteres de escape
    json_data = json.dumps(data, ensure_ascii=False)

    return json_data


def post_webhook():
    try:
        # Obtén los datos de la función get_weather_data() o de donde sea que los obtengas
        data = get_weather_data()
        
        # URL del webhook
        webhook_url = os.environ.get("webhook")

        # Realiza una solicitud POST al webhook con los datos
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()  # Levanta una excepción si la respuesta no es exitosa

        print({"message": "Datos enviados exitosamente al webhook.", "data": data})
    except requests.RequestException as e:
        # Manejar errores de solicitud, como problemas de red
        print(f"Error en la solicitud POST: {str(e)}")
    except Exception as e:
        # Manejar otros errores inesperados
        print(f"Error inesperado: {str(e)}")


if __name__ == "__main__":
    dotenv.load_dotenv()
    lambda_handler(None, None)