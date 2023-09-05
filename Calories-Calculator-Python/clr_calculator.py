def main():
    welcome()
    gender = sex()
    weight = get_weight()
    height = get_height()
    age = get_age()
    goal = get_goal()
    rest_bmr = calculate_bmr(gender, weight, height, age)
    user_activity_lvl = get_user_activity()
    dietary_preferences = get_dietary_preferences()

    nutrient_intake = {
        "protein": 0,
        "carbohydrates": 0,
        "fats": 0,
        "calories": 0
    }

    total_calculation(rest_bmr, user_activity_lvl, goal, nutrient_intake)
    suggest_diet(goal, nutrient_intake)

def welcome():
    print("Welcome to your calories python calculator!\nFind out How many calories should you eat daily.\n")

def sex():    
    sexes = ["male", "female", "m", "f"]
    while True:
        sex = str(input("Do you identify as male or female? ")).lower()
        if sex in sexes:
            return sex
        else:
            print("Please enter either 'male' or 'female'.")

def get_weight():
    weight_kg = float(input("Enter your weight in kilograms: "))
    while weight_kg <= 0:
        weight_kg = float(input("Invalid input. Please enter your weight in kilograms: "))
    return weight_kg

def get_height():
    height_cm = float(input("Enter your height in centimeters (cm): "))
    while height_cm <= 0:
        height_cm = float(input("Invalid input. Please enter your height in centimeters (cm): "))
    return height_cm

    
    # Convert height to centimeters
    height_cm = (height_ft * 30.48) + (height_in * 2.54)
    return height_cm

def get_age():
    age_yrs = int(input("Enter your age in years: "))
    while age_yrs <= 0:
        age_yrs = int(input("Invalid Input. Please enter your age in years: "))
    return age_yrs

def get_goal():
    goals = ["maintain", "lose", "gain"]
    while True:
        goal = str(input("Do you want to maintain, lose, or gain weight? ")).lower()
        if goal in goals:
            return goal
        else:
            print("Please enter 'maintain', 'lose', or 'gain'.")

def calculate_bmr(gender, weight, height, age):
    if gender == "female":
        women = (weight * 10) + (height * 6.25) - (age * 5) - 161
        return int(women)
    else:
        men = (weight * 10) + (height * 6.25) - (age * 5) + 5
        return int(men)

def total_calculation(rest_bmr, activity_level, goal, nutrient_intake):
    activity_factors = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725
    }

    if activity_level in activity_factors:
        total_calories = rest_bmr * activity_factors[activity_level]
        
        if goal == 'lose':
            total_calories -= 500  # Example: 500 calories deficit for weight loss
        elif goal == 'gain':
            total_calories += 500  # Example: 500 calories surplus for weight gain
    else:
        total_calories = 0.0

    print(f"\nYour estimated daily calorie requirement: {total_calories} calories")

    num_meals = int(input("How many meals did you have today? "))
    for _ in range(num_meals):
        meal_protein = float(input("Protein content in this meal (grams): "))
        meal_carbs = float(input("Carbohydrates content in this meal (grams): "))
        meal_fats = float(input("Fats content in this meal (grams): "))

        nutrient_intake["protein"] += meal_protein
        nutrient_intake["carbohydrates"] += meal_carbs
        nutrient_intake["fats"] += meal_fats
        nutrient_intake["calories"] += (meal_protein + meal_carbs + meal_fats) * 4

    print("\nNutrient Intake Summary:")
    print(f"Protein: {nutrient_intake['protein']} grams")
    print(f"Carbohydrates: {nutrient_intake['carbohydrates']} grams")
    print(f"Fats: {nutrient_intake['fats']} grams")
    print(f"Total Calories Consumed: {nutrient_intake['calories']} calories")

    suggest_diet(goal, nutrient_intake)

def get_user_activity():
    activity_lvl = ["sedentary", "lightly_active", "moderately_active", "very_active"]
    while True:
        user_lvl = str(
            input("\nWhat is your activity level?\n\nSedentary is little to no exercise.\nLightly active is light "
                  "exercise/sports 1 - 3 days/week.\nModerately active is moderate exercise/sports 3 - 5 days/week."
                  "\nVery active is hard exercise every day, or 2 xs/day 6 - 7 days/week.\n\nPlease enter: "
                  "'sedentary', 'lightly_active', 'moderately_active', or 'very_active' "))

        if user_lvl in activity_lvl:
            return user_lvl
        else:
            print("Invalid input. Please enter: 'sedentary', 'lightly_active', 'moderately_active', or 'very_active'.")

def get_dietary_preferences():
    dietary_preferences = input("Are you a vegetarian or non-vegetarian? ").lower()
    while dietary_preferences not in ["vegetarian", "non-vegetarian"]:
        dietary_preferences = input("Please enter 'vegetarian' or 'non-vegetarian': ").lower()
    return dietary_preferences

def suggest_diet(goal, nutrient_intake):
    print("\nDietary Suggestions:")
    
    if goal == "lose":
        print("To support your weight loss goal, consider a balanced diet with a moderate calorie deficit. "
              "Focus on lean proteins, fruits, vegetables, and whole grains.")
    elif goal == "gain":
        print("For weight gain, you'll want to increase your calorie intake. "
              "Incorporate nutrient-rich foods such as lean proteins, healthy fats, and complex carbohydrates.")
    else:
        print("To maintain your current weight, maintain a balanced diet with a mix of macronutrients "
              "and regular exercise for overall health.")

if __name__ == '__main__':
    main()
