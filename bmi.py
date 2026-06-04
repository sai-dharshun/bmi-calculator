def findBMI(height, weight):
    bmi = weight / (height ** 2)
    return round(bmi, 2)


if __name__ == "__main__":
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))

    bmi_ = findBMI(height, weight)

    print("Your BMI is: ", bmi_)