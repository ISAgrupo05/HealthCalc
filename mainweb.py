import sys
sys.path.append(r'c:\Healthcalc\HealthCalc\python-project-healthcalc')

from flask import Flask, render_template, request
from healthcalc import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    resultado = None
    return render_template('index.html', resultado=resultado)


@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    resultado = None
    classification = None

    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            health_calc = HealthCalcImpl()
            resultado = health_calc.bmi(weight, height)
            clasificacion = health_calc.bmi_classification(resultado)
            

        except InvalidHealthDataException:
            resultado= "Invalid input. Please enter numeric values for weight and height." 
        
#si o sí se envian los datos a la vista
    return render_template('index.html', resultado=resultado, classification=classification)

@app.route('/ibw', methods=['GET', 'POST'])
def ibw():
    resultado = None
    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            gender = request.form['gender']
            health_calc = HealthCalcImpl()
            resultado = health_calc.lorentz(gender, height)
        except InvalidHealthDataException:
            resultado = "Invalid input. Please enter valid values for height and gender."
    return render_template('index.html', resultado=resultado)

@app.route('/whr', methods=['GET', 'POST'])
def whr():
    resultado = None
    if request.method == 'POST':
        try:
            waist = float(request.form['waist'])
            hip = float(request.form['hip'])
            gender = request.form['gender']
            health_calc = HealthCalcImpl()  
            resultado = health_calc.whr(waist, hip)    
            classification = health_calc.whr_classification(gender, resultado)
        except InvalidHealthDataException:
            resultado = "Invalid input. Please enter valid values for waist, hip, and gender."

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)