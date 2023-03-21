def calculate_bmi(height_feet, height_inches, weight):

    if any(char.isalpha() for char in height_feet) or any(char.isalpha() for char in height_inches) or any(char.isalpha() for char in weight):
        raise ValueError("Height and weight must be valid")
    height_feet, height_inches, weight = float(
        height_feet), float(height_inches), float(weight)
    if height_feet < 0 or height_inches < 0 or weight < 0:
        raise ValueError("Height and weight must be non-negative")
    if height_feet == 0 and height_inches == 0 or weight == 0:
        raise ValueError("Height and weight must be valid")

    total_height_inches = height_feet * 12 + height_inches
    weight_kg = weight * 0.45
    height_cm = total_height_inches * 0.025

    bmi = weight_kg / (height_cm ** 2)
    bmi = round(bmi, 1)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category


if __name__ == '__main__':
    print('Enter your height in feet :')
    height_feet = input()
    print('Enter your height in inches :')
    height_inches = input()
    print('Enter your weight in pounds:')
    weight = input()

    bmi, category = calculate_bmi(height_feet, height_inches, weight)
    print("your bmi is ", bmi, "you are ", category)
