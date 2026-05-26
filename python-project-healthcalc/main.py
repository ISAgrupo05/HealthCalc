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

def main():
       
    calc = HealthCalcImpl.getInstance() #test Singleton

    print("\n--- TESTING ADAPTER PATTERN ---")

    calcHAdapter = Adapter(calc)

    hospital_bmi, classification = calcHAdapter.indiceMasaCorporal(
        HealthData(weight=75000, height=1.80, unit_system="GRAMS")
    )

    print("BMI from hospital system:", hospital_bmi)

    print("BMI Classification:", classification)

    ideal_weight = calcHAdapter.pesoCorporalIdeal(
        HealthData(sex="M", height=1.80, unit_system="GRAMS")
    )

    print("Ideal Body Weight:", ideal_weight)

    print("\n--- TESTING PROXY PATTERN: STATS ---")
    
    stats = HealthStatsImpl()

    calcHProxy = HealthCalcProxy(calcHAdapter, stats)
    
    result = calcHProxy.indiceMasaCorporal(
        HealthData(weight=78000, height=1.83, unit_system="GRAMS")
    )

    result2 = calcHProxy.indiceMasaCorporal(
        HealthData(weight=90000, height=1.75, unit_system="GRAMS")
    )

    calcHProxy.pesoCorporalIdeal(
        HealthData(sex="M", height=1.83, unit_system="GRAMS")
    )

    calcHProxy.pesoCorporalIdeal(
        HealthData(sex="F", height=1.65, unit_system="GRAMS")
    )

    print("Average height:",stats.alturaMedia())

    print("Average weight:", stats.pesoMedio())

    print("Average BMI:",stats.imcMedio())

    print("Men:",stats.numSexoH())

    print("Women:", stats.numSexoM())
    
    print("Total patients:",stats.numTotalPacientes())

    print("\n--- TESTING DECORATOR PATTERN ---")

    # EU metric + English classification
    eu_decorator = DecoratorEnglish(DecoratorEU(calcHAdapter))
    eu_bmi, eu_class = eu_decorator.indiceMasaCorporal(
        HealthData(weight=75.0, height=1.80, unit_system="KG")
    )
    eu_ibw = eu_decorator.pesoCorporalIdeal(
        HealthData(sex="M", height=1.80, unit_system="KG")
    )
    print("EU / English - BMI:", eu_bmi)
    print("EU / English - Classification:", eu_class)
    print("EU / English - Ideal Body Weight:", eu_ibw, "kg")

    # USA imperial + Español classification
    usa_decorator = DecoratorEspanol(DecoratorUSA(calcHAdapter))
    usa_bmi, usa_class = usa_decorator.indiceMasaCorporal(
        HealthData(weight=165.0, height=66.93, unit_system="LBS")
    )
    usa_ibw = usa_decorator.pesoCorporalIdeal(
        HealthData(sex='F', height=66.93, unit_system="INCHES")
    )
    print("USA / Español - BMI:", usa_bmi)
    print("USA / Español - Clasificación:", usa_class)
    print("USA / Español - Peso Corporal Ideal:", usa_ibw, "lbs")



    print("\nWelcome to your Health Calculator!")

    finish = False

    def ask_float(message):
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("Value must be a number, try again.")

    
    Rstats = HealthStatsImpl()

    RcalcHProxy = HealthCalcProxy(
        calcHAdapter,
        Rstats
    )

    while not finish:
        answer = input("Do you want to know your Body Mass Index? Y/N \n")

        while answer.upper() != "Y" and answer.upper() != "N":
            answer = input("Your answer must be 'Y' or 'N', try again: \n")

        if answer.upper() == "Y":
            valid = False
            while not valid:
                try:
                    weight = ask_float("Input your weight (kg): \n")
                    height = ask_float("Input your height (m): \n")

                    bmi, classification = RcalcHProxy.indiceMasaCorporal(
                        HealthData(weight=weight * 1000, height=height, unit_system="GRAMS")
                    )
                    valid = True
                except InvalidHealthDataException as e:
                    print(e)
                    print("Invalid health data, try again.")

            print("Your BMI is: ", bmi)
            print("According to that, your Health Status is: ", classification)

        answer2 = input("Do you want to know your Ideal Body Weight? Y/N \n")

        while answer2.upper() != "Y" and answer2.upper() != "N":
            answer2 = input("Your answer must be 'Y' or 'N', try again: \n")

        if answer2.upper() == "Y":
            valid2 = False
            while not valid2:
                try:
                    height = ask_float("Input your height (m): \n")
                    sex = input("Input your sex ('M' for male or 'F' for female): \n")

                    while sex.upper() != "M" and sex.upper() != "F":
                        sex = input("Your sex must be either 'M' (male) or 'F' (female), try again: \n")

                    ibw = RcalcHProxy.pesoCorporalIdeal(
                        HealthData(sex=sex.upper(), height=height, unit_system="GRAMS")
                    )
                    valid2 = True
                except InvalidHealthDataException:
                    print("Invalid health data, try again.")

            print("Your Ideal Body Weight is: ", ibw, " kg.")

        answer3 = input("Do you want to know your Waist-To-Hip Ratio? Y/N \n")

        while answer3.upper() != "Y" and answer3.upper() != "N":
            answer3 = input("Your answer must be 'Y' or 'N', try again: \n")

        if answer3.upper() == "Y":
            valid3 = False
            while not valid3:
                try:
                    waist = ask_float("Input your waist perimeter (m): \n")
                    hip = ask_float("Input your hip perimeter (m): \n")
                    sex = input("Input your sex ('M' for male or 'F' for female): \n")

                    while sex.upper() != "M" and sex.upper() != "F":
                        sex = input("Your sex must be either 'M' (male) or 'F' (female), try again: \n")

                    whr = calc.whr(waist, hip)
                    classification = calc.whr_classification(sex, whr)
                    valid3 = True
                except InvalidHealthDataException:
                    print("Invalid health data, try again.")

            print("Your Waist-to-Hip Ratio is: ", whr)
            print("According to that, your body morfology is: ", classification)

        answer4 = input("Are you finished using your Health Calculator? Y/N \n")

        while answer4.upper() != "Y" and answer4.upper() != "N":
            answer4 = input("Your answer must be 'Y' or 'N', try again: \n")
        
        if answer4.upper() == "Y":
            finish = True
    
    print("\n--- REAL STATS ---")

    print(
        "Average height:",
        Rstats.alturaMedia(),
        "m"
    )

    print(
        "Average weight:",
        Rstats.pesoMedio()/1000,
        "kg"
    )

    print(
        "Average BMI:",
        Rstats.imcMedio()
    )

    print(
        "Men:",
        Rstats.numSexoH()
    )

    print(
        "Women:",
        Rstats.numSexoM()
    )
    
    print(
        "Total patients:",
        Rstats.numTotalPacientes()
    )
        



if __name__ == "__main__":
    main()



        




            




