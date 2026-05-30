from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.HealthData import HealthData
from healthcalc.Adapter import Adapter
from healthcalc.Proxy import HealthCalcProxy
from healthcalc.HealthStatsImpl import HealthStatsImpl
from healthcalc.DecoratorEU import DecoratorEU
from healthcalc.DecoratorUSA import DecoratorUSA
from healthcalc.DecoratorEnglish import DecoratorEnglish
from healthcalc.DecoratorEspanol import DecoratorEspanol
from healthcalc.gender import Gender
from healthcalc.unit_system import UnitSystem


def main():
    mostrar_tests()
    calc, stats = inicializar_sistema()
    bucle_interactivo(calc, stats)
    mostrar_stats_finales(stats)


def mostrar_tests():
    calc = HealthCalcImpl.getInstance()  # test Singleton

    print("\n--- TESTING ADAPTER PATTERN ---")

    calcHAdapter = Adapter(calc)

    hospital_bmi, classification = calcHAdapter.indiceMasaCorporal(
        HealthData(weight=75000, height=1.80, unit_system=UnitSystem.GRAMS)  # 75 kg y 1.80 m
    )

    print("BMI from hospital system:", hospital_bmi)
    print("BMI Classification:", classification)

    ideal_weight = calcHAdapter.pesoCorporalIdeal(
        HealthData(gender=Gender.MALE, height=1.80, unit_system=UnitSystem.GRAMS)
    )

    print("Ideal Body Weight:", ideal_weight)

    print("\n--- TESTING PROXY PATTERN: STATS ---")

    stats = HealthStatsImpl()
    calcHProxy = HealthCalcProxy(calcHAdapter, stats)

    calcHProxy.indiceMasaCorporal(
        HealthData(weight=78000, height=1.83, unit_system=UnitSystem.GRAMS)
    )

    calcHProxy.indiceMasaCorporal(
        HealthData(weight=90000, height=1.75, unit_system=UnitSystem.GRAMS)
    )

    calcHProxy.pesoCorporalIdeal(
        HealthData(gender=Gender.MALE, height=1.83, unit_system=UnitSystem.GRAMS)
    )

    calcHProxy.pesoCorporalIdeal(
        HealthData(gender=Gender.FEMALE, height=1.65, unit_system=UnitSystem.GRAMS)
    )

    print("Average height:", stats.alturaMedia())
    print("Average weight:", stats.pesoMedio())
    print("Average BMI:", stats.imcMedio())
    print("Men:", stats.numSexoH())
    print("Women:", stats.numSexoM())
    print("Total patients:", stats.numTotalPacientes())

    print("\n--- TESTING DECORATOR PATTERN ---")

    eu_decorator = DecoratorEnglish(DecoratorEU(calcHAdapter))
    eu_bmi, eu_class = eu_decorator.indiceMasaCorporal(
        HealthData(weight=75.0, height=1.80, unit_system=UnitSystem.METRIC)
    )
    eu_ibw = eu_decorator.pesoCorporalIdeal(
        HealthData(gender=Gender.MALE, height=1.80, unit_system=UnitSystem.METRIC)
    )

    print("EU / English - BMI:", eu_bmi)
    print("EU / English - Classification:", eu_class)
    print("EU / English - Ideal Body Weight:", eu_ibw, "kg")

    usa_decorator = DecoratorEspanol(DecoratorUSA(calcHAdapter))
    usa_bmi, usa_class = usa_decorator.indiceMasaCorporal(
        HealthData(weight=165.0, height=66.93, unit_system=UnitSystem.INCHES)
    )
    usa_ibw = usa_decorator.pesoCorporalIdeal(
        HealthData(gender=Gender.FEMALE, height=66.93, unit_system=UnitSystem.INCHES)
    )

    print("USA / Español - BMI:", usa_bmi)
    print("USA / Español - Clasificación:", usa_class)
    print("USA / Español - Peso Corporal Ideal:", usa_ibw, "lbs")


def inicializar_sistema():
    calc = HealthCalcImpl.getInstance()
    calcHAdapter = Adapter(calc)
    stats = HealthStatsImpl()
    return calcHAdapter, stats


def bucle_interactivo(calc, stats):
    print("\nWelcome to your Health Calculator!")

    finish = False
    RcalcHProxy = HealthCalcProxy(calc, stats)

    while not finish:
        patient_added = False

        if ask_yes_no("Do you want to know your Body Mass Index? Y/N \n"):
            while True:
                try:
                    weight = ask_float("Input your weight (kg): \n")
                    height = ask_float("Input your height (m): \n")

                    if patient_added:
                        bmi, classification = calc.indiceMasaCorporal(
                            HealthData(weight=weight * 1000, height=height, unit_system=UnitSystem.GRAMS)
                        )
                    else:
                        bmi, classification = RcalcHProxy.indiceMasaCorporal(
                            HealthData(weight=weight * 1000, height=height, unit_system=UnitSystem.GRAMS)
                        )
                        patient_added = True

                    break
                except InvalidHealthDataException as e:
                    print(e)
                    print("Invalid health data, try again.")

            print("Your BMI is: ", bmi)
            print("According to that, your Health Status is: ", classification)

        if ask_yes_no("Do you want to know your Ideal Body Weight? Y/N \n"):
            while True:
                try:
                    height = ask_float("Input your height (m): \n")
                    gender_input = input("Input your gender ('M' for male or 'F' for female): \n")

                    while gender_input.upper() != "M" and gender_input.upper() != "F":
                        gender_input = input("Your gender must be either 'M' (male) or 'F' (female), try again: \n")

                    if patient_added:
                        ibw = calc.pesoCorporalIdeal(
                            HealthData(gender=Gender.MALE if gender_input.upper() == "M" else Gender.FEMALE, height=height, unit_system=UnitSystem.GRAMS)
                        )
                    else:
                        ibw = RcalcHProxy.pesoCorporalIdeal(
                            HealthData(gender=Gender.MALE if gender_input.upper() == "M" else Gender.FEMALE, height=height, unit_system=UnitSystem.GRAMS)
                        )
                        patient_added = True

                    break
                except InvalidHealthDataException:
                    print("Invalid health data, try again.")

            print("Your Ideal Body Weight is: ", ibw, " kg.")

        if ask_yes_no("Do you want to know your Waist-To-Hip Ratio? Y/N \n"):
            while True:
                try:
                    waist = ask_float("Input your waist perimeter (m): \n")
                    hip = ask_float("Input your hip perimeter (m): \n")
                    gender_input = input("Input your gender ('M' for male or 'F' for female): \n")

                    while gender_input.upper() != "M" and gender_input.upper() != "F":
                        gender_input = input("Your gender must be either 'M' (male) or 'F' (female), try again: \n")

                    health_data = HealthData(
                        waist=waist,
                        hip=hip,
                        gender=(Gender.MALE if gender_input.upper() == "M" else Gender.FEMALE),
                        unit_system=UnitSystem.METRIC,
                    )

                    whr = calc.calc.whr(health_data)
                    classification = calc.calc.whr_classification(health_data, whr)
                    break
                except InvalidHealthDataException:
                    print("Invalid health data, try again.")

            print("Your Waist-to-Hip Ratio is: ", whr)
            print("According to that, your body morphology is: ", classification)

        if ask_yes_no("Are you finished using your Health Calculator? Y/N \n"):
            finish = True


def mostrar_stats_finales(stats):
    print("\n--- REAL STATS ---")
    print("Average height:", stats.alturaMedia(), "m")
    print("Average weight:", stats.pesoMedio(), "kg")
    print("Average BMI:", stats.imcMedio())
    print("Men:", stats.numSexoH())
    print("Women:", stats.numSexoM())
    print("Total patients:", stats.numTotalPacientes())


def ask_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Value must be a number, try again.")


def ask_yes_no(message):
    answer = input(message)
    while answer.upper() != "Y" and answer.upper() != "N":
        answer = input("Your answer must be 'Y' or 'N', try again: \n")
    return answer.upper() == "Y"


if __name__ == "__main__":
    main()
