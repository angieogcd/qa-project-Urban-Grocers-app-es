import sender_stand_request
import data

#Obtiene el cuerpo de la solicitud del kit de producto
def get_kit_body(kit_name, auth_token):
    #Crea copia de los headers para no editar el original
    header_copy = data.header.copy()
    #Copia el diccionario con el body de la solicitud desde el file de datos
    current_kit_body = data.kit_body.copy()
    #Cambia el valor del parámetro name
    current_kit_body["name"] = kit_name
    #Devuelve un nuevo diccionario con el valor name que se requiere
    return current_kit_body, header_copy

#Obtener el token de autenticación de un new user
def get_new_user_token():
    #Resultado de la solicitud para crear un new user
    #La variable se guarda en user_response
    response_new_user = sender_stand_request.post_new_user(data.user_body)
    #Se realiza la extracion del auth_token del new user
    user_token = response_new_user.json().get('authToken')
    return user_token

#Función de prueba positiva para crear un kit de producto
def positive_assert(kit_name, auth_token):
    #Obtiene el body de la solicitud y los headers actualizados
    kit_body, headers = get_kit_body(kit_name, auth_token)
    #Se guarda en la variable kit_response el resultado de la solicitud al crear new kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    #Comprueba que el código de estado sea 201
    assert kit_response.status_code == 201
    #Comprueba que la respuesta en el campo "name" sea igual al enviado
    assert kit_response.json()["name"] == kit_name


#Funcion de pruebas negativas

def negative_assert_code_400(kit_name, auth_token):
    #Obtiene el body de la solicitud y los headers actualizados
    kit_body, headers = get_kit_body(kit_name, auth_token)
    #El resultado es guardado en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    #Comprueba que el código de estado sea 400
    assert kit_response.status_code == 400

    #Comprueba que el atributo "code" en el body de respuesta sea 400
    assert kit_response.json()["code"] == 400
    #Comprueba el atributo "message" en el cuerpo de respuesta
    assert kit_response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                             "Los nombres solo pueden contener caracteres latinos,  " \
                                             "Los nombres deben tener al menos 1 caracter y no más de 511 caracteres"


def negative_assert_no_name(kit_name, auth_token):
    #Obtiene el body de la solicitud y los headers actualizados
    kit_body, headers = get_kit_body(kit_name, auth_token)
    #El resultado es guardado en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    #Comprueba que el código de estado sea 400
    assert kit_response.status_code == 400
    #Comprueba que el atributo code en el cuerpo de respuesta sea 400
    assert kit_response.json()["code"] == 400
    #Comprueba el atributo message en el cuerpo de respuesta
    assert kit_response.json()["message"] == "No se enviaron todos los parámetros requeridos"



#Pruebas

#Test1:El número permitido de caracteres (1)
def test_create_kit_1_letter_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("a", auth_token)


#Test2:El número permitido de caracteres (511)
def test_create_kit_511_letter_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC",
        auth_token)

#Test3: Error. El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_letter_in_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_code_400("", auth_token)

#Test4: Error. El número de caracteres es mayor que la cantidad permitida (512):
def test_create_kit_512_letter_in_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_code_400(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD",
        auth_token)

#Test5:	Se permiten caracteres especiales
def test_create_kit_has_special_symbol_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("\"№%@\",", auth_token)

#Test6: Se permiten espacios
def test_create_kit_has_space_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(" A Aaa ", auth_token)

#Test7:	Se permiten números
def test_create_kit_has_number_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("123", auth_token)

#Test8: Error.El parámetro no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_no_name({}, auth_token)

#Test9: Error. Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_has_number_in_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_code_400({"name": 1234}, auth_token)