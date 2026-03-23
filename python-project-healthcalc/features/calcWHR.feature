Feature: Cálculo del WHR 
	As usuario de la calculadora
	I want tengo calcular el ratio cintura-cadera
	So that conocer mi estado de salud mediante la métrica elegida

Background:
	Given tengo el módulo del cálculo de WHR
	and se ha elegido la métrica en la calculadora de salud

@ErrorHandling
Scenario: Cálculo de WHR con perímetro de cintura anumérico
	Given el usuario ingresa un valor de cintura anumérico
		and el usuario ingresa un valor de cadera válido
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de WHR con perímetro de cadera anumérico
	Given el usuario ingresa un valor de cadera anumérico
		And el usuario ingresa un valor de cintura válido
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de WHR con perímetro de cintura cero
	Given el usuario ingresa un valor de cadera válido
	and el usuario ingresa un valor de cintura cero
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de WHR con perímetro de cadera cero
	Given el usuario ingresa un valor de cintura válido
		and el usuario ingresa un valor de cadera cero
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción 

@ErrorHandling
Scenario: Cálculo de WHR con perímetro de cintura negativo
	Given el usuario ingresa un valor de cadera válido
		and el usuario ingresa un valor de cintura negativo
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción 

@ErrorHandling
Scenario: Cálculo de WHR con perímetro de cadera negativo
	Given el usuario ingresa un valor de cintura válido
		and el usuario ingresa un valor de cadera negativo
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción 

@ErrorHandling
Scenario: Cálculo de WHR con perímetro de cintura exorbitante
	Given el usuario ingresa un valor de cadera válido
		and el usuario ingresa un valor de cintura exorbitante
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de WHR con perímetro de cadera exorbitante
	Given el usuario ingresa un valor de cintura válido
		and el usuario ingresa un valor de cadera exorbitante
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de WHR con perímetro de cintura desbordado
	Given el usuario ingresa un valor de cadera válido
		and el usuario ingresa un valor de cintura desbordado
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de WHR con perímetro de cadera desbordado
	Given el usuario ingresa un valor de cintura válido
		and el usuario ingresa un valor de cadera desbordado
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción

@ErrorHandling
Scenario: Cálculo de WHR con perímetro de ambos desbordado
	Given el usuario ingresa un valor de cintura desbordado
		and el usuario ingresa un valor de cadera desbordado
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción


@Performance
Scenario: Cálculo de WHR con perímetro de ambos igual
	Given el usuario ingresa un valor de cintura 0.50
		and el usuario ingresa un valor de cadera 0.50
	When se calcula el ratio cintura-cadera
	Then el resultado debe ser 1.00


Scenario Outline: Cálculo de WHR con valores de cintura y cadera válido

	Given el usuario ingresa un valor de cintura <cintura>
		and el usuario ingresa un valor de cadera <cadera>
	When se calcula el ratio cintura-cadera
	Then el resultado debe ser <resultado>

	Examples:
		|  cintura  |  cadera  |  resultado  |
		| 0.45      | 0.50     | 0.90        |
		| 0.55      | 0.45     | 1.22        |
		| 2.50      | 3.00     | 0.83        |
		| 3.00      | 2.00     | 1.50        |
		| 0.60      | 0.90     | 0.67        |
		| 0.75      | 1.00     | 0.75        |
		| 0.85      | 1.05     | 0.81        |
		| 0.95      | 0.95     | 1.00        |
		| 1.20      | 1.00     | 1.20        |
		| 1.40      | 1.10     | 1.27        |
		| 1.80      | 1.50     | 1.20        |
		| 2.00      | 2.50     | 0.80        |
		| 2.50      | 3.00     | 0.83        |
		