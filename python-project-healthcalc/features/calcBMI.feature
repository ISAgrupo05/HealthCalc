Feature: Cálculo del BMI 
	As usuario de la calculadora
	I want calcular el índice de masa corporal
	So that conocer mi estado de salud mediante la métrica elegida

Background:
	Given tengo el módulo del cálculo de BMI
	and se ha elegido la métrica en la calculadora de salud

@ErrorHandling
Scenario: Cálculo de BMI con peso anumérico
	Given el usuario ingresa un valor de peso anumérico
		and el usuario ingresa un valor de altura válido
	When se calcula el índice de masa corporal
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de BMI con altura anumérica
	Given el usuario ingresa un valor de altura anumérico
		And el usuario ingresa un valor de peso válido
	When se calcula el índice de masa corporal
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de BMI con peso cero
	Given el usuario ingresa un valor de altura válido
	and el usuario ingresa un valor de peso cero
	When se calcula el índice de masa corporal
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de BMI con altura cero
	Given el usuario ingresa un valor de peso válido
		and el usuario ingresa un valor de altura cero
	When se calcula el índice de masa corporal
	Then debe lanzarse una excepción 

@ErrorHandling
Scenario: Cálculo de BMI con peso negativo
	Given el usuario ingresa un valor de altura válido
		and el usuario ingresa un valor de peso negativo
	When se calcula el índice de masa corporal
	Then debe lanzarse una excepción 

@ErrorHandling
Scenario: Cálculo de BMI con altura negativa
	Given el usuario ingresa un valor de peso válido
		and el usuario ingresa un valor de altura negativo
	When se calcula el índice de masa corporal
	Then debe lanzarse una excepción 

@ErrorHandling
Scenario: Cálculo de BMI con peso exorbitante
	Given el usuario ingresa un valor de altura válido
		and el usuario ingresa un valor de peso exorbitante
	When se calcula el índice de masa corporal
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de BMI con altura exorbitante
	Given el usuario ingresa un valor de peso válido
		and el usuario ingresa un valor de altura exorbitante
	When se calcula el índice de masa corporal
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de BMI con peso desbordado
	Given el usuario ingresa un valor de altura válido
		and el usuario ingresa un valor de peso desbordado
	When se calcula el índice de masa corporal
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de BMI con altura desbordada
	Given el usuario ingresa un valor de peso válido
		and el usuario ingresa un valor de altura desbordado
	When se calcula el índice de masa corporal
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de BMI con ambos valores desbordados
	Given el usuario ingresa un valor de peso desbordado
		and el usuario ingresa un valor de altura desbordado
	When se calcula el índice de masa corporal
	Then debe lanzarse una excepción


@Performance
Scenario: Cálculo de BMI con valores normales
	Given el usuario ingresa un valor de peso 45
		and el usuario ingresa un valor de altura 1.50
	When se calcula el índice de masa corporal
	Then el resultado debe ser 20.0


Scenario Outline: Cálculo de BMI con valores de peso y altura válidos

	Given el usuario ingresa un valor de peso <peso>
		and el usuario ingresa un valor de altura <altura>
	When se calcula el índice de masa corporal
	Then el resultado debe ser <resultado>

	Examples:
		|   peso    |  altura  |  resultado  |
        |   1       |  1.00    |  1.00       |
        |   700     |  1.00    |  700.00     |
        |   9       |  0.30    |  100.00     |
        |   18      |  0.30    |  200.00     |
        |   50      |  1.00    |  50.00      |
        |   36      |  1.20    |  25.00      |
		|   45      |  1.50    |  20.00      |
		|   54      |  1.50    |  24.00      |
		|   81      |  1.80    |  50.00      |
		|   36      |  1.50    |  16.00      |
		|   100     |  2.00    |  25.00      |
        |   63      |  3.00    |  7.00       |
        |   81      |  3.00    |  9.00       | 
		
		