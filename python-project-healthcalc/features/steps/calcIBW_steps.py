from behave import use_step_matcher, given, then, when
import pytest
from healthcalc import InvalidHealthDataException
from healthcalc.health_calc_impl import HealthCalcImpl
from behave import step   

#------------clausula GIVEN (precondiciones)----------------
@given(u'tengo el módulo del cálculo de IBW')
def step_impl(context):
    context.health_calc = HealthCalcImpl()

@given(u'se ha elegido la métrica IBW en la calculadora de salud')
def step_impl(context):
    pass  # No se requiere acción específica para esta etapa en el contexto de la prueba


#-------------clausula GIVEN (escenarios)----------------

@given(u'el usuario ingresa un sexo inválido')
def step_impl(context):
    context.sexo = "X"


@given(u'el usuario ingresa una altura válida')
def step_impl(context):
    context.altura = 1.70


@given(u'el usuario ingresa un sexo válido')
def step_impl(context):
    context.sexo = "M"


@given(u'el usuario ingresa una altura anumérica')
def step_impl(context):
    context.altura = "abc"


@given(u'el usuario ingresa una altura cero')
def step_impl(context):
    context.altura = 0.00


@given(u'el usuario ingresa una altura negativa')
def step_impl(context):
    context.altura = -1.00


@given(u'el usuario ingresa una altura por debajo del rango biológico')
def step_impl(context):
    context.altura = 0.50


@given(u'el usuario ingresa una altura por encima del rango biológico')
def step_impl(context):
    context.altura = 4.00


@given(u'el usuario ingresa un sexo {sexo}')
def step_impl(context, sexo):
    context.sexo = sexo

@given(u'el usuario ingresa una altura {altura:f}')
def step_impl(context, altura):
    context.altura = altura


#-------------clausula WHEN-------------------

@when(u'se calcula el peso ideal corporal')
def step_impl(context):
    try:
        context.result = context.health_calc.lorentz(context.sexo, context.altura)
        context.exception = False
    except InvalidHealthDataException as e:
        context.exception = True


#--------------clausula THEN-----------------

@then(u'debe lanzarse una excepción en el cálculo de IBW')
def step_impl(context):  
    assert context.exception, "Se esperaba una excepción pero no se lanzó ninguna."

@then(u'el resultado del IBW debe ser {resultado: f}')
def step_impl(context, resultado):
    expected = float(resultado)
    assert abs(context.result - expected) < 0.01, f"Se esperaba un resultado de {resultado} pero se obtuvo {context.result}"