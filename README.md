# Test Todo Legal
## Ejercicio 1
- Se creó una base de datos en aws con el motor sql server
- Se creó una api rest utilizando fastapi la cual realiza acciones consulta a la base de datos y poblado de la misma mediante consultas a la api de yahoo finance
- Se creó un webhook y se parametrizó en una variable de entorno junto con las variable de conexión a dbb
- Se creó una función post que ayuda a enviar información al webhook
## Ejercicio 2
- Se creó una base de datos en aws con el motor sql server
- Se creó una funcion lambda que realiza un bucle durante 1 min recuperando del api rest de dweet los valores de temepratura y humedad
- Se creó una funcion que agrega los datos a la base de datos
- Se creó una función que realiza una petición post al webhook y envia los datos de la base de datos
## Ejercicio 3
- Se creó la pantalla principal guiandose de acuerdo al modelo de adobe xd

### Consireciones generales
- Para jecutar los proyectos intalar las librerías de los imports
- Editar los archivos .env la variable webhook para probar con el webhook deseado

### Importante se creó un trigger en la base de datos exchange la cual lo pueden visualziar con SMSS para ello utilizar las credenciales de conexión del archivo .env de ejercicio 1
