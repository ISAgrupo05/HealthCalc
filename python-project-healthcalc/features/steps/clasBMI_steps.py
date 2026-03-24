from behave import use_step_matcher, given, then, when
import pytest
from healthcalc import InvalidHealthDataException
from healthcalc.health_calc_impl import HealthCalcImpl
from behave import step

use_step_matcher("parse") 

#------------clausula GIVEN (precondiciones)--------------

@given(u'tengo el módulo de clasificación de BMI')
def step_impl(context):
    context.health_calc = HealthCalcImpl()


@given(u'se ha elegido la clasificación BMI en la calculadora de salud')
def step_impl(context):
    pass  # No se requiere acción específica para esta etapa en el contexto de la prueba


#------------clausula GIVEN (precondiciones)--------------
@given(u'el BMI calculado es negativo')
def step_impl(context):
    context.bmi = -5.0  # Ejemplo de BMI negativo


@given(u'el BMI calculado es exorbitante')
def step_impl(context):
    context.bmi = 800  # Ejemplo de BMI exorbitante (mayor a 800)


@given('el BMI calculado es {bmi:f}')
def step_impl(context, bmi):
    context.bmi = float(bmi)

#----------------------clausula WHEN ----------------------
@when(u'se obtiene la clasificación BMI')
def step_impl(context):
    try:
        context.result = context.health_calc.bmi_classification(context.bmi)
        context.exception = False  # No se lanzó una excepción

    except InvalidHealthDataException:
        context.exception = True # Se lanzó una excepción 



#----------------------clausula THEN ------------------------
@then(u'se debe lanzar una excepción')
def step_impl(context):
    assert context.exception , "Se esperaba una excepción, pero no se lanzó ninguna."

@then(u'el resultado debe ser {resultado: s}')
def step_impl(context, resultado):
    expected = context.result
    assert expected == resultado == True, f"Se esperaba '{resultado}', pero se obtuvo '{expected}'." 
