print("==========================================")
print("     HEALTHY DIET PLANNER CHATBOT")
print("==========================================\n")

# User Information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (Male/Female): ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))
activity = input("Activity level (low / moderate / high): ").lower()
goal = input("Your goal (weight loss / weight gain / maintain): ").lower()

print("\n Generating your personalized health report...\n")

# BMI Calculation
height_m = height / 100
bmi = weight / (height_m ** 2)

print("==========================================")
print("              HEALTH REPORT")
print("==========================================")

print(f" Name          : {name}")
print(f" Age           : {age}")
print(f" Gender        : {gender}")
print(f" Weight        : {weight} kg")
print(f" Height        : {height} cm")
print(f" Activity Level: {activity}")
print(f" Goal          : {goal}")
print(f" BMI           : {round(bmi, 2)}")

# BMI Status
if bmi < 18.5:
    print(" BMI Status    : Underweight")
elif bmi < 25:
    print(" BMI Status    : Normal Weight")
elif bmi < 30:
    print(" BMI Status    : Overweight")
else:
    print(" BMI Status    : Obese")

# Water Recommendation
water = round(weight * 0.035, 2)

print(f" Daily Water Intake Recommendation: {water} Liters")

# Calories Suggestion
if activity == "low":
    calories = 1800
elif activity == "moderate":
    calories = 2200
else:
    calories = 2600

print(f" Recommended Daily Calories: {calories} kcal")

print("\n==========================================")
print("          PERSONALIZED DIET PLAN")
print("==========================================\n")

# Diet Plan According to Goal
if goal == "weight loss":

    print(" MORNING")
    print("- Warm water with lemon")
    print("- 30 minutes walking or jogging\n")

    print(" BREAKFAST")
    print("- Oats with fruits")
    print("- Green tea")
    print("- Boiled eggs or sprouts\n")

    print(" LUNCH")
    print("- Brown rice")
    print("- Dal or grilled chicken")
    print("- Salad and vegetables\n")

    print(" EVENING SNACKS")
    print("- Nuts")
    print("- Fruit juice without sugar\n")

    print(" DINNER")
    print("- Soup")
    print("- Chapati with vegetables")
    print("- Avoid junk food at night\n")

    print(" FITNESS TIP")
    print("- Avoid soft drinks and sugary foods")
    print("- Sleep at least 7-8 hours")

elif goal == "weight gain":

    print(" MORNING")
    print("- Banana shake")
    print("- Dry fruits\n")

    print(" BREAKFAST")
    print("- Peanut butter bread")
    print("- Milk")
    print("- Omelette or paneer\n")

    print(" LUNCH")
    print("- Rice")
    print("- Chicken/Paneer")
    print("- Dal and salad\n")

    print(" EVENING SNACKS")
    print("- Protein shake")
    print("- Nuts and bananas\n")

    print(" DINNER")
    print("- Chapati")
    print("- Eggs/Paneer")
    print("- Milk before sleep\n")

    print(" FITNESS TIP")
    print("- Focus on strength training")
    print("- Eat more protein-rich foods")

elif goal == "maintain":

    print(" MORNING")
    print("- Warm water")
    print("- Light stretching or yoga\n")

    print(" BREAKFAST")
    print("- Poha/Upma")
    print("- Milk or juice\n")

    print(" LUNCH")
    print("- Home cooked balanced food")
    print("- Salad and curd\n")

    print(" EVENING SNACKS")
    print("- Fruits")
    print("- Nuts or green tea\n")

    print(" DINNER")
    print("- Light dinner")
    print("- Soup or chapati with vegetables\n")

    print(" FITNESS TIP")
    print("- Maintain regular exercise")
    print("- Avoid overeating")

else:
    print(" Invalid goal entered!")

# Extra Health Advice
print("\n==========================================")
print("             HEALTH TIPS")
print("==========================================")

print("- Drink enough water daily")
print("- Avoid excessive junk food")
print("- Exercise regularly")
print("- Include fruits and vegetables in your meals")
print("- Reduce stress and sleep properly")

print("\n==========================================")
print(f" Thank you, {name}, for using Diet Planner Chatbot!")
print(" Stay Healthy and Fit!")
print("==========================================")