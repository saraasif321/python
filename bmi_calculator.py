import math

again = "y"
while again == "y":

    print("WELCOME...\nCalculate your BMI")

    user_name = input("Enter your Name: ") #.capitalize()
    user_gender = input("Enter your Gender: ") #.capitalize()
    
    # print(f"Name: {user_name}")
    # print(f"Gender: {user_gender}")

    user_age = int(input("Enter your Age: "))
    user_height = float(input("Enter your Height in centimeters: "))
    user_weight = int(input("Enter your weight in kilograms: "))

    meter = float(user_height/100)
    print(f"{user_height} centimeters is equal to {meter} meters.")

    square_of_height = float(meter*meter)
    print(square_of_height)

    bmi = user_weight / square_of_height
    rounded_bmi = round(bmi)
    print (f"Your BMI is {rounded_bmi} kilogram per meter square.")

    if rounded_bmi < 19:
        print("Your BMI is underweight.\nYou have to increase your weight to become healthy.")

    elif rounded_bmi >= 19 and rounded_bmi <= 25:
        print("Congratulations...\nYour BMI is normal.\nyou are healthy.")

    else:
        print("Your BMI is overweight.\nYou have to decrease your weight to become healthy.")    

    again=(input("If you want to continue then press y if no then press n: "))


