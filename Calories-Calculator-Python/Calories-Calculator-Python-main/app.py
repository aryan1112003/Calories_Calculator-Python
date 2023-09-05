from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        gender = request.form['gender']
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        activity_level = request.form['activity_level']

        rest_bmr = calculate_bmr(gender, weight, height, age)
        calories_result = total_calculation(rest_bmr, activity_level)

        return render_template('result.html', result=calories_result)
    return render_template('calculator.html')

def calculate_bmr(gender, weight, height, age):
    # Placeholder implementation - You should replace this with your BMR calculation logic.
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        # Handle other cases or provide a default value
        bmr = 0.0
    
    return bmr

def total_calculation(rest_bmr, activity_level):
    # Placeholder implementation - You should replace this with your total calorie calculation logic.
    activity_factors = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725
    }

    if activity_level in activity_factors:
        total_calories = rest_bmr * activity_factors[activity_level]
    else:
        # Handle the case where the activity level is not recognized
        total_calories = 0.0

    return total_calories

if __name__ == '__main__':
    app.run(debug=True)
