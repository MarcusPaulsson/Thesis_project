# Prompt user for age and gender input
age = int(input("Please enter your age: "))
gender = input("Please enter your gender (M/F): ")

if gender == 'M':
    if age < 18:
        print("You must wash for at least 20 seconds before and after using the toilet or touching any surface.")
    elif age >= 65:
        print("Please dry your hands with soap before continuing with any activity")
    else:
        print("Handwashing is not required for you.")
elif gender == 'F':
    if age < 18:
        print("You must wash for at least 20 seconds before and after using the toilet or touching any surface.")
    elif age >= 65:
        print("Please dry your hands with soap before continuing with any activity")
    else:
        print("Handwashing is not required for you.")
else:
    print("Invalid input. Please enter 'M' or 'F'.")