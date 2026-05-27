import pytest
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.gender import Gender
from healthcalc.HealthData import HealthData

class TestLorenz:

    @pytest.fixture(autouse=True)  # Equivalente a @BeforeEach en JUnit
    def set_up(self):
        """Se ejecuta antes de cada test."""
        self.health_calc = HealthCalcImpl()

    # --- Tests de Cálculo de la métrica IBW ---
    def test_lorentz_valido_hombre(self):
        """Cálculo de IBW con valores estándar válidos para hombres"""
        
        height = 1.75
        expected_lorentz = (height*100-100) - ((height*100 -150)/4)

        result = self.health_calc.lorentz(HealthData(gender=Gender.MALE, height=height))

        # pytest.approx es el equivalente a assertEquals con delta (0.01) en JUnit
        assert result == pytest.approx(expected_lorentz, abs=0.01)
    
    def test_lorentz_valido_mujer(self):
        """Cálculo de IBW con valores estándar válidos para mujeres"""
        
        height = 1.75
        expected_lorentz = (height*100-100) - ((height*100 -150)/2)

        result = self.health_calc.lorentz(HealthData(gender=Gender.FEMALE, height=height))

        # pytest.approx es el equivalente a assertEquals con delta (0.01) en JUnit
        assert result == pytest.approx(expected_lorentz, abs=0.01)

    def test_lorentz_altura_cero(self):
        """Lanzar excepción cuando la altura es cero"""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.lorentz(HealthData(gender=Gender.MALE, height=0))

    def test_lorentz_negativos(self):
        """Lanzar excepción cuando los valores son negativos (Equivalente a assertAll)"""
        height = -1.70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.lorentz(HealthData(gender=Gender.FEMALE, height=height))

    # --- Tests de Límites e Invalidación para el IBW ---
    @pytest.mark.parametrize("height", [-0.50, 0.0, 0.99], ids=lambda x: f"Altura mínima inválida: {x}m")
    def test_altura_minima_imposible(self, height: float):
        """Lanzar excepción cuando la altura es negativa o menor que 30cm."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.lorentz(HealthData(gender=Gender.FEMALE, height=height))

    @pytest.mark.parametrize("height", [3.01, 3.50, 5.00], ids=lambda x: f"Altura máxima inválida: {x}m")
    def test_altura_maximo_imposible(self, height: float):
        """Lanzar excepción cuando la altura es extremadamente alta."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.lorentz(HealthData(gender=Gender.MALE, height=height))
    
