import requests
import configuration
import data

#Crear nuevo usuario

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body, #Cuerpo de solicitud
                         headers=data.header) #Encabezados

#Crear nuevo kit de producto
def post_new_client_kit(bodykit, token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=bodykit,
                         headers={"Content-Type": "application/json",
                                  "Authorization": "Bearer " + str(token)}
                         )
