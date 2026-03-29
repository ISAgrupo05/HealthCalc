Feature: Obtener la clasificación BMI de una persona
	Como usuario de la calculadora
	Quiero obtener mi clasificación BMI
	Para conocer mi estado de salud

Background:
	Given tengo el módulo de clasificación de BMI
	and se ha elegido la clasificación BMI en la calculadora de salud

@ErrorHandling
Scenario: Clasificación con BMI negativo
	Given el BMI calculado es negativo
	When se obtiene la clasificación BMI
	Then se debe lanzar una excepción en la clasificación BMI

@ErrorHandling
Scenario: Clasificación con BMI exorbitante
	Given el BMI calculado es exorbitante
	When se obtiene la clasificación BMI
	Then se debe lanzar una excepción en la clasificación BMI

Scenario Outline: Clasificación con valores normales de BMI
	Given el BMI calculado es <bmi>
	When se obtiene la clasificación BMI
	Then el resultado de la clasificación BMI debe ser <result>

Examples:
| bmi    | result         |
|  16.00 |  Underweight   |
|  18.40 |  Underweight   |
|  20.00 |  Normal weight |
|  24.00 |  Normal weight |
|  25.00 |  Overweight    |
|  28.00 |  Overweight    |
|  30.00 |  Obesity       |
|  35    |  Obesity       |