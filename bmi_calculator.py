user_weight = int(input("Enter your weight in kg: "))
user_height = float(input("Enter your height in meters: "))

if user_height <= 0:
    print("Height must be a positive number.")
else:
    bmi = round(user_weight / (user_height ** 2), 1)

    if bmi < 18.5:
        print(f"Your BMI is {bmi} and you are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi} and you are of normal weight.")
    elif bmi < 30:
        print(f"Your BMI is {bmi} and you are overweight.")
    elif bmi < 35:
        print(f"Your BMI is {bmi} and you are obese.")
    else:
        print(f"Your BMI is {bmi} and you are clinically obese.")
