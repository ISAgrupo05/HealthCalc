Feature: Cálculo del WHR 
	Como usuario de la calculadora
	Quiero calcular el ratio cintura-cadera
	Para conocer mi estado de salud mediante la métrica elegida

Background:
	Given tengo el módulo del cálculo de WHR
	and se ha elegido la métrica en la calculadora de salud


Scenario: Cálculo de WHR con perímetro de cintura no numérico

	Given el usuario ingresa un valor de cintura no numérico
		and el usuario ingresa un valor de cadera válido
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción

Scenario: Cálculo de WHR con perímetro de cadera no numérico

	Given el usuario ingresa un valor de cadera no numérico
		And el usuario ingresa un valor de cintura válido
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción


Scenario: Cálculo de WHR con perímetro de cintura igual a cero

	Given el usuario ingresa un valor de cadera válido
	and el usuario ingresa un valor de cintura igual a cero
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción


Scenario: Cálculo de WHR con perímetro de cadera igual a cero

	Given el usuario ingresa un valor de cintura válido
		and el usuario ingresa un valor de cadera igual a cero
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción 


Scenario: Cálculo de WHR con perímetro de cintura negativo

	Given el usuario ingresa un valor de cadera válido
		and el usuario ingresa un valor de cintura negativo
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción 


Scenario: Cálculo de WHR con perímetro de cadera negativo
	
	Given el usuario ingresa un valor de cintura válido
		and el usuario ingresa un valor de cadera negativo
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción 



Scenario: Cálculo de WHR con perímetro de cintura extremadamente alto
	
	Given el usuario ingresa un valor de cadera válido
		and el usuario ingresa un valor de cintura extremadamente alto
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción


Scenario: Cálculo de WHR con perímetro de cadera extremadamente alto

	Given el usuario ingresa un valor de cintura válido
		and el usuario ingresa un valor de cadera extremadamente alto
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción


Scenario: Cálculo de WHR con perímetro de cintura biológicamente imposible

	Given el usuario ingresa un valor de cadera válido
		and el usuario ingresa un valor de cintura biológicamente imposible
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción


Scenario: Cálculo de WHR con perímetro de cadera biológicamente imposible

	Given el usuario ingresa un valor de cintura válido
		and el usuario ingresa un valor de cadera biológicamente imposible
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción


Scenario: Cálculo de WHR con ambos valores biológicamente imposibles

	Given el usuario ingresa un valor de cintura biológicamente imposible
		and el usuario ingresa un valor de cadera biológicamente imposible
	When se calcula el ratio cintura-cadera
	Then debe lanzarse una excepción


Scenario: Cálculo del WHR con valor de cintura en los límites del rango
	
	Given el usuario ingresa un valor de cadera <v>
		and el usuario ingresa un valor de cintura de <l>
	When se calcula el ratio cintura-cadera
	Then el resultado debe ser <r>

Ejemplos: 

|  <l> | <v>  | <r>  |
| 3.00 | 1.00 | 3.00 |
| 0.45 | 1.00 | 0.45 |


Scenario: Cálculo del WHR con valor de cadera en los límites del rango
	
	Given el usuario ingresa un valor de cadera <d>
		and el usuario ingresa un valor de cintura de <n>
	When se calcula el ratio cintura-cadera
	Then el resultado debe ser <i>

Ejemplos:

|  <n> | <d>  | <i>  |
| 1.00 | 3.00 | 0.33 |
| 1.00 | 0.45 | 2.22 |



Scenario: Cálculo de WHR con valores idénticos

	Given el usuario ingresa un valor de cintura de 0.50
		and el usuario ingresa un valor de cadera de 0.50
	When se calcula el ratio cintura-cadera
	Then el resultado debe ser 1


Scenario: Cálculo de WHR con valores de cintura y cadera válido

	Given el usuario ingresa un valor de cintura <w>
		and el usuario ingresa un valor de cadera <h>
	When se calcula el ratio cintura-cadera
	Then el resultado debe ser <r>

Ejemplos: 

|  <w> | <h>  | <r>  |
| 0.60 | 0.90 | 0.67 |
| 0.75 | 1.00 | 0.75 |
| 0.85 | 1.05 | 0.81 |
| 1.00 | 1.20 | 0.83 |
| 1.10 | 1.30 | 0.85 |
| 0.95 | 0.95 | 1.00 |
| 1.20 | 1.00 | 1.20 |
| 1.40 | 1.10 | 1.27 |
| 1.80 | 1.50 | 1.20 |
| 2.00 | 2.50 | 0.80 |
| 2.50 | 3.00 | 0.83 |