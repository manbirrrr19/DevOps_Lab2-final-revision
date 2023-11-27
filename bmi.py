def calculate_bmi(height, weight):
    print("Height = ", height)
    print("Weight = ", weight)
    BMI = weight/(height*height)
    BMI = round(BMI, 2)
    if BMI < 18.5:
        print("Your BMI is ", BMI, ", underweight")
    elif BMI >= 18.5 and BMI <= 25:
        print("Your BMI is ", BMI, ", normal weight")
    else:
        print("Your BMI is ", BMI, ", overweight")

calculate_bmi(weight=57, height=1.73)