Feature: Obtener la clasificación WHR de una persona
	As usuario de la calculadora
	I want to obtener mi clasificación WHR
	So that conocer mi morfología y estado de salud

Background:
	Given tengo el módulo de clasificación de WHR
	and se ha elegido la clasificación WHR en la calculadora de salud

@ErrorHandling
Scenario: Clasificación con WHR negativo
	Given el usuario introduce un sexo válido
		and el WHR calculado es negativo
	When se obtiene la clasificación morfológica
	Then se debe lanzar una excepción en la clasificación de WHR

@ErrorHandling
Scenario: Clasificación con WHR exorbitante
	Given el usuario introduce un sexo válido
		and el WHR calculado es exorbitante
	When se obtiene la clasificación morfológica
	Then se debe lanzar una excepción en la clasificación de WHR

@ErrorHandling
Scenario: Clasificación con sexo inválido
	Given el usuario introduce un sexo inválido
		and el WHR calculado es válido
	When se obtiene la clasificación morfológica
	Then se debe lanzar una excepción en la clasificación de WHR


Scenario Outline: Clasificación con sexo y WHR normales
	Given el usuario introduce un sexo <sex>
		and el WHR calculado es <whr>
	When se obtiene la clasificación morfológica
	Then el resultado de la clasificación WHR debe ser <result>

Examples:
| sex | whr  | result  |
|  M  | 0.78 |  Pear   |
|  M  | 0.90 |  Pear   |
|  m  | 0.95 |  Apple  |
|  M  | 1.12 |  Apple  |
|  F  | 0.70 |  Pear   |
|  f  | 0.85 |  Pear   |
|  F  | 0.88 |  Apple  |
|  F  | 1.05 |  Apple  |