def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def get_bmi_category(bmi):
    
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_weight_range(height):
    
    lower_limit = 18.5 * (height ** 2)
    upper_limit = 24.9 * (height ** 2)
    return lower_limit, upper_limit


def get_height_range(weight):
    
    lower_limit = (weight / 24.9) ** 0.5
    upper_limit = (weight / 18.5) ** 0.5
    return lower_limit, upper_limit


def main():
    print("BMI Calculator")
    print("--------------------")

    weight_unit = input("Enter weight unit (lbs or kgs): ")
    weight = float(input("Enter your weight in {}: ".format(weight_unit)))

    height_unit = input("Enter height unit (feet or meters): ")
    height = float(input("Enter your height in {}: ".format(height_unit)))

   
    if weight_unit.lower() == "lbs":
        weight = weight * 0.453592

    
    if height_unit.lower() == "feet":
        height = height * 0.3048

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print("\nResults")
    print("--------------------")
    print("BMI: {:.2f}".format(bmi))
    print("Category: {}".format(category))

    weight_range = get_weight_range(height)
    height_range = get_height_range(weight)

    print("\nSuggested Weight Range for Height {:.2f} meters".format(height))
    print("--------------------")
    print("Lower Limit: {:.2f} kg".format(weight_range[0]))
    print("Upper Limit: {:.2f} kg".format(weight_range[1]))

    print("\nSuggested Height Range for Weight {:.2f} kg".format(weight))
    print("--------------------")
    print("Lower Limit: {:.2f} meters".format(height_range[0]))
    print("Upper Limit: {:.2f} meters".format(height_range[1]))


if __name__ == "__main__":
    main()
