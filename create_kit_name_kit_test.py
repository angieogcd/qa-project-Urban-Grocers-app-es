import sender_stand_request
import data


# Prueba positiva
def positive_assert(kit_body):
    n_kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert n_kit_response.status_code == 201


# Prueba negativa
def negative_assert_code_400(kit_body):
    n_kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert n_kit_response.status_code == 400
    assert n_kit_response.json()["code"] == 400
    assert n_kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"


# Test1 : El número permitido de caracteres (1)
def test_create_kit_1_letter_in_name_get_success_response():
    kit_test1 = data.one_letter_name
    positive_assert(kit_test1)


# Test2:El número permitido de caracteres (511)
def test_create_kit_511_letter_in_name_get_success_response():
    kit_test2 = data.inside_511_letters
    positive_assert(kit_test2)


# Test3: Error. El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_letter_in_name_get_error_response():
    kit_test3 = data.zero_letter_name
    negative_assert_code_400(kit_test3)


# Test4: Error. El número de caracteres es mayor que la cantidad permitida (512):
def test_create_kit_512_letter_in_name_get_error_response():
    kit_test4 = data.outside_limit_512_letters
    negative_assert_code_400(kit_test4)


# Test5:	Se permiten caracteres especiales
def test_create_kit_has_special_symbol_in_name_get_success_response():
    kit_test5 = data.special_symbol
    positive_assert(kit_test5)


# Test6: Se permiten espacios
def test_create_kit_has_space_in_name_get_success_response():
    kit_test6 = data.space_in_name
    positive_assert(kit_test6)


# Test7:	Se permiten números
def test_create_kit_has_number_in_name_get_success_response():
    kit_test7 = data.number_in_name
    positive_assert(kit_test7)


# Test8: Error.El parámetro no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    kit_test8 = data.no_name
    negative_assert_code_400(kit_test8)


# Test9: Error. Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_has_number_in_name_get_error_response():
    kit_test9 = data.kit_has_number
    negative_assert_code_400(kit_test9)
