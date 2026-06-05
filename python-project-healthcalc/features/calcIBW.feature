Feature: Cálculo del IBW
	As usuario de la calculadora
	I want calcular el peso ideal corporal
	So that conocer mi estado de salud mediante la métrica elegida

Background:
	Given tengo el módulo del cálculo de IBW
	and se ha elegido la métrica IBW en la calculadora de salud

@ErrorHandling
Scenario: Cálculo de IBW con sexo inválido
	Given el usuario ingresa un sexo inválido
		and el usuario ingresa una altura válida
	When se calcula el peso ideal corporal
	Then debe lanzarse una excepción en el cálculo de IBW

@ErrorHandling
Scenario: Cálculo de IBW con altura anumérica
	Given el usuario ingresa un sexo válido
		and el usuario ingresa una altura anumérica
	When se calcula el peso ideal corporal
	Then debe lanzarse una excepción en el cálculo de IBW

@ErrorHandling
Scenario: Cálculo de IBW con altura cero
	Given el usuario ingresa un sexo válido
	and el usuario ingresa una altura cero
	When se calcula el peso ideal corporal
	Then debe lanzarse una excepción en el cálculo de IBW

@ErrorHandling
Scenario: Cálculo de IBW con altura negativa
	Given el usuario ingresa un sexo válido
		and el usuario ingresa una altura negativa
	When se calcula el peso ideal corporal
	Then debe lanzarse una excepción en el cálculo de IBW

@ErrorHandling
Scenario: Cálculo de IBW con altura por debajo del rango biológico
	Given el usuario ingresa un sexo válido
		and el usuario ingresa una altura por debajo del rango biológico
	When se calcula el peso ideal corporal
	Then debe lanzarse una excepción en el cálculo de IBW

@ErrorHandling
Scenario: Cálculo de IBW con altura por encima del rango biológico
	Given el usuario ingresa un sexo válido
		and el usuario ingresa una altura por encima del rango biológico
	When se calcula el peso ideal corporal
	Then debe lanzarse una excepción en el cálculo de IBW

@Performance
Scenario: Cálculo de IBW con valores normales
	Given el usuario ingresa un sexo F
		and el usuario ingresa una altura de 1.50
	When se calcula el peso ideal corporal
	Then el resultado del IBW debe ser 50.0

Scenario Outline: Cálculo de IBW con valores de altura y sexo válidos

	Given el usuario ingresa un sexo <sexo>
		and el usuario ingresa una altura <estatura>
	When se calcula el peso ideal corporal
	Then el resultado del IBW debe ser <resultado>

	Examples:
		|  estatura |  sexo    |  resultado  |
		| 1.00      | M        | 12.5        |
		| 1.00      | F        | 25.0        |
		| 1.50      | M        | 50.0        |
		| 1.50      | F        | 50.0        |
    	| 1.60      | M        | 57.5        |
		| 1.60      | F        | 55.0        |
    	| 1.70      | M        | 65.0        |
		| 1.70      | F        | 60.0        |
    	| 1.80      | M        | 72.5        |
		| 1.80      | F        | 65.0        |    
		| 2.00      | M        | 87.5        |
		| 2.00      | F        | 75.0        |
		| 2.50      | M        | 125.0       |
		| 2.50      | F        | 100.0       |
		| 3.00      | M        | 162.5       |
		| 3.00      | F        | 125.0       |
