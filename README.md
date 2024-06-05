# Proyecto Urban Grocers 

En el presente proyecto se realizo la automatización de pruebas a través de las APIS. 
En el cual se tuvo como base un checklist para la debida ejecución de cada prueba.
Estas pruebas fueron realizadas con el fin de comprobar la funcionalidad a través del testing automatizado.

## Data

- Se utiliza diversas variables las cuales se utilizan para las solicitud con el servidor al realizar las pruebas.
```sh
header
user_body
kit_body
token
```

## Configuración del Proyecto

- Dentro de la configuración del proyecto se mantienen 3 variables.

| Variable | Función                                                                                                                   |
|------|---------------------------------------------------------------------------------------------------------------------------|
| URL_SERVICE | Almacena la URL de la base del servicio                                                                                   |
| CREATE_USER_PATH | Almacena la ruta de la API                                                                                                |
| KITS_PATH | Almacena la ruta de la API para la creación del nuevo kit que se empleara para las pruebas en el servicio/aplicación web. |

## create_kit_name_kit_test

- Se emplean las pruebas o test de la aplicación web.
- Se utilizan funciones positivas y negativas.
- Se debe importar los modulos para el correcto funcionamiento de las pruebas


## sender_stand_request

- Se realizan las solicitudes hacia el servicio web utilizando `requests`
- Se debe realizar la instalación de `requests` a través del uso de la terminal con el siguiente comando: 
```sh
pip install requests
```
- Se debe importar los módulos utilizando: 
```sh
import requests
import configuration
import data
```
- En la funcion `def post_new_user` se realiza un POST al servicio web, asimismo se establece como JSON y los otros encabezados se toman del `import data`
- En la función `post_new_client_kit` se realiza un POST donde el cuerpo de la solicitud realizada es a través de un JSON donde se agregan los headers de la solicitud, el cual incluye el tipo de contenido y el token de autorización.
- Mediante estas dos funciones se realiza la creación de un nuevo usuario y la creación de un nuevo kit.
