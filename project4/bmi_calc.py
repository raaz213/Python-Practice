

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("🧮 BMI Calculator\n")

    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))
        if weight <= 0 or height <= 0:
            print("❌ Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"\n📊 Your BMI is: {bmi:.2f}")
        print(f"📋 Category: {category}")

    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
