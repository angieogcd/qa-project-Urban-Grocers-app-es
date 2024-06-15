# _Proyecto Urban Grocers_ 

En este proyecto, nos enfocamos en garantizar la calidad y fiabilidad de la funcionalidad ofrecida por la API de Urban Grocers, que es fundamental para el funcionamiento adecuado de su plataforma.

El objetivo principal de este proyecto es automatizar las pruebas de la lista de comprobación para la API de Urban Grocers, centrándonos específicamente en dos escenarios clave: la creación de un nuevo usuario y la creación de un nuevo kit. Estos escenarios cubren aspectos esenciales de la funcionalidad de la API que son críticos para la experiencia del usuario y el éxito general del sistema.

Durante el desarrollo de este proyecto, nos aseguraremos de cubrir tanto pruebas positivas como pruebas negativas.

Para la validación de las pruebas del proyecto utilizaremos una lista de comprobación para asi realizar la verificación de cada una de las pruebas.

Lista de comprobación de pruebas:

| Nº | Description                                                                                                                                         | ER                                                                                                                              |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| 01 | El número permitido de caracteres (1): kit_body = { "name": "a"}                                                                                    | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud     |
| 02 | El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}                           | Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud |
| 03 | El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }                                                           | Código de respuesta: 400                                                                                                        |
| 04 | El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } | Código de respuesta: 400                                                                                                        |
| 05 | Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }                                                                                  | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud     |
| 06 | Se permiten espacios: kit_body = { "name": " A Aaa " }                                                                                              | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud     |
| 07 | Se permiten números: kit_body = { "name": "123" }                                                                                                   | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud     |
| 08 | El parámetro no se pasa en la solicitud: kit_body = { }                                                                                             | Código de respuesta: 400                                                                                                        |
| 09 | Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }                                                                    | Código de respuesta: 400                                                                                                        |


## Tecnologías utilizadas

* Lenguaje y herramientas en el proyecto

    * Dentro de los lenguajes y herramientas utilizamos el lenguaje de Python.
    * Utilizaremos el IDE llamado Pycharm, la cual nos permitira realizar las pruebas en el lenguaje de Python.
    * Tener en cuenta en utilizar la documentación que encontramos en APIDOCS.
    * Utilizamos GitHub para almacenar el código, los files y el historial de revisiones del proyecto.
    * Utilizaremos `pytest` para ejecutar las pruebas debido a que este framework para Python permite crear pruebas de manera clara y organizada usando una sintaxis simple lo cual nos deja verificar fácilmente si tu código funciona como debería y asegurarte de que no haya errores inesperados cuando haces cambios en tu aplicación. 
    * Para la interacción con las APIs utilizaremos `requests` la cual es una libreria que nos permite enviar solicitudes HTTP de manera fácil y manejar las respuestas.
  
## Ejecución de las pruebas
* Inicio de pruebas

    * Instalar las librerias `pytest` y `requests` 
        * Desde el terminal utiliza:  
        ```sh
        pip install requests
        ```
         ```sh
        pip install pytest
        ```
      
    * Para el inicio de las pruebas es necesario que tengamos iniciado el servidor y que actualizemos el enlace en el file `configuration.py`.
        * Actualiza el enlace del servidor en :
        ```sh
        URL_SERVICE = "https://"
        ```    
        * Agrega el endpoint para la creación del nuevo usuario: 
        ```sh
        CREATE_USER_PATH = "/api/v1/users/"
        ```    
        * Agrega el endpoint para la creación del nuevo kit:
        ```sh
        KITS_PATH = "/api/v1/kits" 
        ```
    * Ejecución de las pruebas en la terminal

        * Para la ejecución de las pruebas en la terminal utilizamos:
        ```sh
        pytest create_kit_name_kit_test.py
        ```


* Preparación del proyecto

    * Se realiza las solicitudes del proyecto en el file `sender_stand_request.py`
        * Realizamos la solicitud para crear un nuevo usuario en `def get_new_user_token()` 
        * En `def post_new_client_kit(kit_name)` realizamos la solicitud para crear un nuevo kit.
  
    * Se realiza la programación para la ejecución de las pruebas en el file `create_kit_name_kit_test.py`
        * Se crea las funciones positivas y negativas utilizando `assert`
        * Se crea las funciones para cada una de las nueve pruebas
        
    * Se realiza las solicitudes POST en el file `data.py` y la extracción de los datos para cada una de las pruebas.

---
Ruth Ordoñez - Sprint 7
