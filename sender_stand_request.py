import requests
import configuration
import data


# Crear nuevo usuario

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,  # Cuerpo de solicitud
                         headers=data.headers)  # Encabezados


# New token
def get_new_user_token():
    rs_token = post_new_user(data.user_body.copy())
    response_js = rs_token.json()
    new_auth_token = response_js['authToken']
    return new_auth_token


# Crear nuevo kit de producto
def post_new_client_kit(kit_name):
    new_token = get_new_user_token()
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {new_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_name,
                             headers=headers)
    return response
