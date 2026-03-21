from behave import use_step_matcher, given, then, when
import pytest
from healthcalc import InvalidHealthDataException
from healthcalc.health_calc_impl import HealthCalcImpl
from behave import step   

#------------clausula GIVEN (precondiciones)----------------
@given(u'tengo el módulo del cálculo de WHR')
def step_impl(context):
    context.health_calc = HealthCalcImpl()

@given(u'se ha elegido la métrica en la calculadora de salud')
def step_impl(context):
    pass  # No se requiere acción específica para esta etapa en el contexto de la prueba


#-------------clausula GIVEN (escenarios)----------------

@given(u'el usuario ingresa un valor de cintura anumérico')
def step_impl(context):
    context.cintura = "abc"


@given(u'el usuario ingresa un valor de cadera válido')
def step_impl(context):
    context.cadera = 1.00


@given(u'el usuario ingresa un valor de cadera anumérico')
def step_impl(context):
    context.cadera = "def"


@given(u'el usuario ingresa un valor de cintura válido')
def step_impl(context):
    context.cintura = 1.00


@given(u'el usuario ingresa un valor de cintura cero')
def step_impl(context):
    context.cintura = 0.00


@given(u'el usuario ingresa un valor de cadera cero')
def step_impl(context):
    context.cadera = 0.00


@given(u'el usuario ingresa un valor de cintura negativo')
def step_impl(context):
    context.cintura = -1.00


@given(u'el usuario ingresa un valor de cadera negativo')
def step_impl(context):
    context.cadera = -1.00


@given(u'el usuario ingresa un valor de cintura exorbitante')
def step_impl(context):
    context.cintura = 10.00

@given(u'el usuario ingresa un valor de cadera exorbitante')
def step_impl(context):
    context.cadera = 10.00

@given(u'el usuario ingresa un valor de cintura desbordado')
def step_impl(context):
    context.cintura = 100.00

@given(u'el usuario ingresa un valor de cadera desbordado')
def step_impl(context):
    context.cadera = 100.00

@given(u'el usuario ingresa un valor de cintura biológicamente imposible')
def step_impl(context):
    context.cintura = 0.44  # Valor por debajo del límite biológico para simular la entrada inválida

@given(u'el usuario ingresa un valor de cadera biológicamente imposible')
def step_impl(context):
    context.cadera = 0.44  # Valor por debajo del límite biológico

@given(u'el usuario ingresa un valor de cintura {cintura:f}')
def step_impl(context, cintura):
    context.cintura = cintura

@given(u'el usuario ingresa un valor de cadera {cadera:f}')
def step_impl(context, cadera):
    context.cadera = cadera


#-------------clausula WHEN-------------------

@when(u'se calcula el ratio cintura-cadera')
def step_impl(context):
    try:
        context.result = context.health_calc.whr(context.cintura, context.cadera)
        context.exception = False
    except InvalidHealthDataException as e:
        context.exception = True

#--------------clausula THEN-----------------

@then(u'debe lanzarse una excepción')
def step_impl(context):  
    assert context.exception, "Se esperaba una excepción pero no se lanzó ninguna."

@then(u'el resultado debe ser {resultado: f}')
def step_impl(context, resultado):
    expected = float(resultado)
    assert abs(context.result - expected) < 0.01, f"Se esperaba un resultado de {resultado} pero se obtuvo {context.result}"