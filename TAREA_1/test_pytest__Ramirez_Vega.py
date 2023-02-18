#importo pytest, math y project del documento Tarea1.py, para poder hacer llamado a las funciones.
from Tarea1 import project
import pytest
import math

#defino algunas variables debido al no reconocimiento del documento referenciado
mayus_numero = ""
minus_signo = ""
primera_mitad = ""
segunda_mitad = ""
a_cuadrado = 0
a_circulo = 0

#defino los distintos tests
#primero tenemos una prueba en la cual verificamos que la frase y la operacion esten el el formato correcto y lo esperado como salida se observe
#Vemos la division de palabra y la seleccion de caracteres
test_string_divide_string = [
    pytest.param("HoLa_A_todos2531$", 1, mayus_numero == "HLA2531" and minus_signo == "oa__todos$", id="Separacion por caracteres"),
    pytest.param("HoLa_A_todos2531$", 2, primera_mitad == "HoLa_A_to" and segunda_mitad == "dos2531$", id="Division de palabra")
]

#probamos los errores, donde E0 hace referencia a un incumplimiento del fromato de la frase donde se introduce un entero
test_string_divide_string_E0 = [
    pytest.param(21, 1, 'E0', id="Operacion o frase no cumplen el requerimiento de formato"),
    pytest.param(12, 2, 'E0', id="Operacion o frase no cumplen el requerimiento de formato")
]

#E1 hace referencia a un incumplimiento del fromato de la operacion donde se introduce un string
test_string_divide_string_E1 = [
    pytest.param("HoLa_A_todos2531$", "hola", 'E1'  ,id='Operacion o frase no cumplen el requerimiento de formato'),
    pytest.param("HoLa_A_todos2531$", "hola", 'E1'  ,id='Operacion o frase no cumplen el requerimiento de formato')
]

#este test prueba vara el valor de lado y radio 3, que el valor de las areas sea el correcto
test_calculo_areas = [
    pytest.param(3, (a_cuadrado == 9, a_circulo == 6*math.pi), id='Calculo de areas')
]

#E2 hace referencia a un error en el que se introduce un string como el valor esperado como un estero
test_calculo_areas_E2 = [
    pytest.param("hola", 'E2', id='El valor introducido no es un entero')
]

#se definen las parametrizaciones, con los tests antes dispuestos
#datos de entrada frase y operacion, con la compraracion del expected, que son la media palabra y la seleccion de caracteres
@pytest.mark.parametrize("frase, operacion, expected", test_string_divide_string)
def test_string_divide(frase, operacion, expected):
    # inicia tests con un assert
    assert project.divide_string (operacion) == expected

#datos de entrada frase y operacion, con la compraracion del expected, que son la media palabra y la seleccion de caracteres, retorna el error E0 y E1
@pytest.mark.parametrize("frase, operacion, expected", test_string_divide_string_E0)
def test_string_divide_E0(frase, operacion, expected):
    # inicia tests con un assert
    assert project.divide_string(frase, operacion) == expected

#datos de entrada frase y operacion, con la compraracion del expected, que son la media palabra y la seleccion de caracteres, retorna el error E0 y E1
@pytest.mark.parametrize("frase, operacion, expected", test_string_divide_string_E1)
def test_string_divide_E1(frase, operacion, expected):
    # inicia tests con un assert
    assert project.divide_string(frase, operacion) == expected

#datos de entrada valor y la compraracion del expected, que son el area del circulo y el cuadrado
@pytest.mark.parametrize("valor, expected", test_calculo_areas)
def test_string_divide(valor, expected):
    # inicia tests con un assert
    assert project.calculo_area(valor) == expected

#datos de entrada valor y la compraracion del expected, que son el area del circulo y el cuadrado, retorna E2, por no introducirse un entero
@pytest.mark.parametrize("valor, expected", test_calculo_areas_E2)
def test_string_divide(valor, expected):
    # inicia tests con un assert
    assert project.calculo_area(valor) == expected