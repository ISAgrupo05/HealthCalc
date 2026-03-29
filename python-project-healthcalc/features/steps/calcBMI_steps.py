from behave import use_step_matcher, given, then, when
import pytest
from healthcalc import InvalidHealthDataException
from healthcalc.health_calc_impl import HealthCalcImpl
from behave import step   

#------------clausula GIVEN (precondiciones)----------------
@given(u'tengo el módulo del cálculo de BMI')
def step_impl(context):
    context.health_calc = HealthCalcImpl()

@given(u'se ha elegido la métrica BMI en la calculadora de salud')
def step_impl(context):
    pass  # No se requiere acción específica para esta etapa en el contexto de la prueba


#-------------clausula GIVEN (escenarios)----------------

@given(u'el usuario ingresa un valor de peso anumérico')
def step_impl(context):
    context.peso = "abc"


@given(u'el usuario ingresa un valor de altura válido')
def step_impl(context):
    context.altura = 1.00


@given(u'el usuario ingresa un valor de altura anumérico')
def step_impl(context):
    context.altura = "abc"


@given(u'el usuario ingresa un valor de peso válido')
def step_impl(context):
    context.peso = 1.00


@given(u'el usuario ingresa un valor de peso cero')
def step_impl(context):
    context.peso = 0.00


@given(u'el usuario ingresa un valor de altura cero')
def step_impl(context):
    context.altura = 0.00


@given(u'el usuario ingresa un valor de peso negativo')
def step_impl(context):
    context.peso = -1.00


@given(u'el usuario ingresa un valor de altura negativo')
def step_impl(context):
    context.altura = -1.00


@given(u'el usuario ingresa un valor de peso exorbitante')
def step_impl(context):
    context.peso = 1000.00

@given(u'el usuario ingresa un valor de altura exorbitante')
def step_impl(context):
    context.altura = 10.00

@given(u'el usuario ingresa un valor de peso desbordado por encima')
def step_impl(context):
    context.peso = float('inf')

@given(u'el usuario ingresa un valor de altura desbordado por encima')
def step_impl(context):
    context.altura = float('inf')

@given(u'el usuario ingresa un valor de peso desbordado por debajo')
def step_impl(context):
    context.peso = 0.50  # Valor por debajo del límite biológico para simular la entrada inválida

@given(u'el usuario ingresa un valor de altura desbordado por debajo')
def step_impl(context):
    context.altura = 0.1  # Valor por debajo del límite biológico

@given(u'el usuario ingresa un valor de peso {peso}')
def step_impl(context, peso):
    context.peso = float(peso)

@given(u'el usuario ingresa un valor de altura {altura}')
def step_impl(context, altura):
    context.altura = float(altura)


#-------------clausula WHEN-------------------

@when(u'se calcula el índice de masa corporal')
def step_impl(context):
    try:
        context.result = context.health_calc.bmi(context.peso, context.altura)
        context.exception = False
    except Exception as e:
        context.exception = True

#--------------clausula THEN-----------------

@then(u'debe lanzarse una excepción en el cálculo de BMI')
def step_impl(context):  
    assert context.exception, "Se esperaba una excepción en el cálculo de BMI pero no se lanzó ninguna."

@then(u'el resultado del BMI debe ser {resultado}')
def step_impl(context, resultado):
    expected = float(resultado)
    assert abs(context.result - expected) < 0.01, f"Se esperaba un resultado de BMI de {resultado} pero se obtuvo {context.result}"