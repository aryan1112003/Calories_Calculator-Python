from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        gender = request.form['gender']
        weight = float(request.form['weight'])
        height_cm = float(request.form['height'])  # Height is in cm
        age = int(request.form['age'])
        activity_level = request.form['activity_level']
        goal = request.form['goal']

        # Calculate BMR (Basal Metabolic Rate)
        if gender == "female":
            bmr = (weight * 10) + (height_cm * 6.25) - (age * 5) - 161
        else:
            bmr = (weight * 10) + (height_cm * 6.25) - (age * 5) + 5

        # Adjust BMR based on activity level and goal
        activity_factors = {
            'sedentary': 1.2,
            'lightly_active': 1.375,
            'moderately_active': 1.55,
            'very_active': 1.725
        }

        if activity_level in activity_factors:
            total_calories = bmr * activity_factors[activity_level]
            
            if goal == 'lose':
                total_calories -= 500  # Example: 500 calories deficit for weight loss
            elif goal == 'gain':
                total_calories += 500  # Example: 500 calories surplus for weight gain
        else:
            total_calories = 0.0

        # Collect nutrient intake data
        num_meals = int(request.form['num_meals'])
        nutrient_intake = {
            "protein": 0,
            "carbohydrates": 0,
            "fats": 0,
            "calories": 0
        }

        for i in range(num_meals):
            meal_protein = float(request.form[f'meal_protein_{i}'])
            meal_carbs = float(request.form[f'meal_carbs_{i}'])
            meal_fats = float(request.form[f'meal_fats_{i}'])

            nutrient_intake["protein"] += meal_protein
            nutrient_intake["carbohydrates"] += meal_carbs
            nutrient_intake["fats"] += meal_fats
            nutrient_intake["calories"] += (meal_protein + meal_carbs + meal_fats) * 4

        return render_template('result.html', result=nutrient_intake)

    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
