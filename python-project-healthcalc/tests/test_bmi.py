import pytest
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.BMICategory import BMICategory

class TestBMI:

    @pytest.fixture(autouse=True)  # Equivalente a @BeforeEach en JUnit
    def set_up(self):
        """Se ejecuta antes de cada test."""
        self.health_calc = HealthCalcImpl()

    # --- Tests de Cálculo de la métrica BMI ---
    def test_bmi_valido(self):
        """Cálculo de BMI con valores estándar válidos"""
        weight = 70.0
        height = 1.75
        expected_bmi = 70.0 / (1.75 ** 2)

        result = self.health_calc.bmi(weight, height)

        # pytest.approx es el equivalente a assertEquals con delta (0.01) en JUnit
        assert result == pytest.approx(expected_bmi, abs=0.01)

    def test_bmi_peso_cero(self):
        """Lanzar excepción cuando el peso es cero"""
        weight = 0
        height = 1.70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(weight, height)

    def test_bmi_altura_cero(self):
        """Lanzar excepción cuando la altura es cero"""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(70, 0)

    def test_bmi_negativos(self):
        """Lanzar excepción cuando los valores son negativos (Equivalente a assertAll)"""
        weight = -70
        height = 1.70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(weight, height)

        weight = -70
        height = -1.70
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(weight, height)

        weight = 70
        height = -1.70
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(weight, height)

    # --- Tests de Límites e Invalidación para el BMI ---

    @pytest.mark.parametrize("weight", [-10.0, 0.0, 0.99], ids=lambda x: f"Peso mínimo inválido: {x}kg")
    def test_peso_minimo_imposible(self, weight: float):
        """Lanzar excepción cuando el peso es negativo o menor que 1kg."""
        height = 1.70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(weight, height)

    @pytest.mark.parametrize("weight", [700.1, 1000.0, 5000.0], ids=lambda x: f"Peso máximo inválido: {x}kg")
    def test_peso_maximo_imposible(self, weight: float):
        """Lanzar excepción cuando el peso es extremadamente alto."""
        height = 1.70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(weight, height)

    @pytest.mark.parametrize("height", [-0.50, 0.0, 0.29], ids=lambda x: f"Altura mínima inválida: {x}m")
    def test_altura_minima_imposible(self, height: float):
        """Lanzar excepción cuando la altura es negativa o menor que 30cm."""
        weight = 70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(weight, height)

    @pytest.mark.parametrize("height", [3.01, 3.50, 5.00], ids=lambda x: f"Altura máxima inválida: {x}m")
    def test_altura_maximo_imposible(self, height: float):
        """Lanzar excepción cuando la altura es extremadamente alta."""
        weight = 70
        
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(weight, height)

    # casos específicos para cubrir cada lado del OR en los límites biológicos
    def test_bmi_peso_menor_que_uno(self):
        """Peso mayor que 0 pero menor que 1 debe fallar en el rango biológico."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(0.5, 1.70)

    def test_bmi_altura_menor_que_minima(self):
        """Altura mayor que 0 pero menor que 0.30 debe fallar en el rango biológico."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(70, 0.20)


    # --- Tests de Clasificación básica a partir del BMI ---
    
    @pytest.mark.parametrize("bmi", [10.0, 15.0, 15.99], ids=lambda x: f"BMI {x} -> Severe Thinness")
    def test_bmi_severe_thinness(self, bmi: float):
        assert (self.health_calc.bmi_classification(bmi) == BMICategory.SEVERE_THINNESS)

    @pytest.mark.parametrize("bmi", [16.0, 16.5, 16.99], ids=lambda x: f"BMI {x} -> Moderate Thinness")
    def test_bmi_moderate_thinness(self, bmi: float):
        assert (self.health_calc.bmi_classification(bmi) == BMICategory.MODERATE_THINNESS)
    
    @pytest.mark.parametrize("bmi", [17.0, 18.0, 18.49], ids=lambda x: f"BMI {x} -> Mild Thinness")
    def test_bmi_mild_thinness(self, bmi: float):
        assert (self.health_calc.bmi_classification(bmi) == BMICategory.MILD_THINNESS)

    @pytest.mark.parametrize("bmi", [18.5, 24.99], ids=lambda x: f"BMI {x} -> Normal")
    def test_bmi_normal(self, bmi: float):
        assert (self.health_calc.bmi_classification(bmi) == BMICategory.NORMAL)

    @pytest.mark.parametrize("bmi", [25.0, 29.99], ids=lambda x: f"BMI {x} -> Overweight")
    def test_bmi_overweight(self, bmi: float):
        assert (self.health_calc.bmi_classification(bmi) == BMICategory.OVERWEIGHT)
    
    @pytest.mark.parametrize("bmi", [30.0, 34.99], ids=lambda x: f"BMI {x} -> Obese Class I")
    def test_bmi_obese_class_i(self, bmi: float):
        assert (self.health_calc.bmi_classification(bmi) == BMICategory.OBESE_CLASS_I)

    @pytest.mark.parametrize("bmi", [35.0, 39.99], ids=lambda x: f"BMI {x} -> Obese Class II")
    def test_bmi_obese_class_ii(self, bmi: float):
        assert (self.health_calc.bmi_classification(bmi) == BMICategory.OBESE_CLASS_II)

    @pytest.mark.parametrize("bmi", [40.0, 100.0], ids=lambda x: f"BMI {x} -> Obese Class III")
    def test_bmi_obese_class_iii(self, bmi: float):
        assert (self.health_calc.bmi_classification(bmi) == BMICategory.OBESE_CLASS_III)

    # --- Tests de Límites e Invalidación para la clasificación BMI ---

    @pytest.mark.parametrize("bmi", [-50.0, -1.0, -0.01], ids=lambda x: f"BMI negativo: {x}")
    def test_bmi_classification_minimo_imposible(self, bmi: float):
        """Lanzar excepción cuando el BMI es negativo."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi_classification(bmi)

    @pytest.mark.parametrize("bmi", [150.1, 200.0, 500.0], ids=lambda x: f"BMI máximo extremo: {x}")
    def test_bmi_classification_maximo_imposible(self, bmi: float):
        """Lanzar excepción cuando el BMI es extremadamente alto."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi_classification(bmi)