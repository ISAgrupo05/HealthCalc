Feature: Obtener la clasificación WHR de una persona
	Como usuario de la calculadora
	Quiero obtener mi clasificación WHR
	Para conocer mi morfología y estado de salud

Background:
	Given tengo el módulo de clasificación de WHR
	and se ha elegido la métrica en la calculadora de salud

Scenario: Clasificación con WHR negativo
	Given el usuario introduce un sexo válido
		and el WHR calculado es negativo
	When se obtiene la clasificación morfológica
	Then se debe lanzar una excepción

Scenario: Clasificación con WHR alto
	Given el usuario introduce un sexo válido
		and el WHR calculado es extremadamente alto
	When se obtiene la clasificación morfológica
	Then se debe lanzar una excepción

Scenario: Clasificación con sexo inválido
	Given el usuario introduce un sexo inválido
		and el WHR calculado es normal
	When se obtiene la clasificación morfológica
	Then se debe lanzar una excepción

Scenario: Clasificación con sexo y WHR normales
	Given el usuario introduce un sexo <s>
		and el WHR calculado es <whr>
	When se obtiene la clasificación morfológica
	Then el resultado debe ser <r>

Ejemplos:
| <s> | <whr> |   <r>   |
|  M  |  0.78 |  Pear   |
|  M  |  0.90 |  Pear   |
|  m  |  0.95 | Apple |
|  M  |  1.12 | Apple |
|  F  |  0.70 |  Pear   |
|  f  |  0.85 |  Pear   |
|  F  |  0.88 | Apple |
|  F  | 1.05  | Apple |