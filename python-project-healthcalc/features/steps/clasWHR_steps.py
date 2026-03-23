from behave import use_step_matcher, given, then, when
import pytest
from healthcalc import InvalidHealthDataException
from healthcalc.health_calc_impl import HealthCalcImpl
from behave import step

use_step_matcher("parse") 

#------------clausula GIVEN (precondiciones)--------------

@given(u'tengo el módulo de clasificación de WHR')
def step_impl(context):
    context.health_calc = HealthCalcImpl()


@given(u'se ha elegido la clasificación WHR en la calculadora de salud')
def step_impl(context):
    pass  # No se requiere acción específica para esta etapa en el contexto de la prueba


#------------clausula GIVEN (precondiciones)--------------
@given(u'el usuario introduce un sexo válido')
def step_impl(context):
    context.sex = "M"  # Asigna un sexo válido (M o F)


@given(u'el WHR calculado es válido')
def step_impl(context):
    context.whr = 0.8  # Asigna un WHR válido


@given(u'el WHR calculado es negativo')
def step_impl(context):
    context.whr = -0.5  # Ejemplo de WHR negativo


@given(u'el WHR calculado es exorbitante')
def step_impl(context):
    context.whr = 5.1  # Ejemplo de WHR exorbitante (mayor a 5)


@given(u'el usuario introduce un sexo inválido')
def step_impl(context):
    context.sex = "X"  # Sexo inválido


# Specific values for sex
@given(u'el usuario introduce un sexo M')
def step_impl(context):
    context.sex = "M"

@given(u'el usuario introduce un sexo m')
def step_impl(context):
    context.sex = "m"

@given(u'el usuario introduce un sexo F')
def step_impl(context):
    context.sex = "F"

@given(u'el usuario introduce un sexo f')
def step_impl(context):
    context.sex = "f"


@given(u'el usuario introduce un sexo {sex: s}')
def step_impl(context, sex):
    context.sex = sex  # Asigna el valor del sexo al contexto


# Specific values for WHR
@given(u'el WHR calculado es 0.78')
def step_impl(context):
    context.whr = 0.78

@given(u'el WHR calculado es 0.90')
def step_impl(context):
    context.whr = 0.90

@given(u'el WHR calculado es 0.95')
def step_impl(context):
    context.whr = 0.95

@given(u'el WHR calculado es 1.12')
def step_impl(context):
    context.whr = 1.12

@given(u'el WHR calculado es 0.70')
def step_impl(context):
    context.whr = 0.70

@given(u'el WHR calculado es 0.85')
def step_impl(context):
    context.whr = 0.85

@given(u'el WHR calculado es 0.88')
def step_impl(context):
    context.whr = 0.88

@given(u'el WHR calculado es 1.05')
def step_impl(context):
    context.whr = 1.05


@given(u'el WHR calculado es {whr: f}')
def step_impl(context, whr):
    context.whr = float(whr)  # Convertir el valor de WHR a float y asignarlo al contexto



#----------------------clausula WHEN ----------------------
@when(u'se obtiene la clasificación morfológica')
def step_impl(context):
    try:
        context.result = context.health_calc.whr_classification(context.sex, context.whr)
        context.exception = False  # No se lanzó una excepción

    except InvalidHealthDataException:
        context.exception = True # Se lanzó una excepción 



#----------------------clausula THEN ------------------------
@then(u'se debe lanzar una excepción')
def step_impl(context):
    assert context.exception , "Se esperaba una excepción, pero no se lanzó ninguna."

@then(u'el resultado debe ser Pear')
def step_impl(context):
    expected = "Pear"
    assert context.result == expected, f"Se esperaba '{expected}', pero se obtuvo '{context.result}'."

@then(u'el resultado debe ser Apple')
def step_impl(context):
    expected = "Apple"
    assert context.result == expected, f"Se esperaba '{expected}', pero se obtuvo '{context.result}'."

@then(u'el resultado debe ser {resultado: s}')
def step_impl(context, resultado):
    expected = context.result
    assert expected == resultado == True, f"Se esperaba '{resultado}', pero se obtuvo '{expected}'." 
