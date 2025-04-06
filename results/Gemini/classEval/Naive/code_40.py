class FitnessTracker:
    """
    This is a class as fitness tracker that implements to calculate BMI (Body Mass Index) and calorie intake based on the user's height, weight, age, and sex.
    """

    def __init__(self, height, weight, age, sex):
        """
        Initialize the class with height, weight, age, and sex.

        Args:
            height (float): Height in meters.
            weight (float): Weight in kilograms.
            age (int): Age in years.
            sex (str): Sex ("male" or "female").
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex.lower()  # Convert sex to lowercase for case-insensitive comparison

    def get_BMI(self):
        """
        Calculate the BMI (Body Mass Index).

        Returns:
            float: BMI value.
        """
        return self.weight / (self.height ** 2)

    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI.

        Returns:
            int: 1 if the user is overweight, -1 if underweight, 0 if normal.
        """
        bmi = self.get_BMI()
        if self.sex == "male":
            if bmi < 20:
                return -1  # Underweight
            elif bmi > 25:
                return 1  # Overweight
            else:
                return 0  # Normal
        elif self.sex == "female":
            if bmi < 19:
                return -1  # Underweight
            elif bmi > 24:
                return 1  # Overweight
            else:
                return 0  # Normal
        else:
            raise ValueError("Invalid sex. Must be 'male' or 'female'.")

    def calculate_calorie_intake(self):
        """
        Calculate the recommended daily calorie intake based on BMR and activity level.

        Returns:
            float: Recommended daily calorie intake.
        """
        if self.sex == "male":
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        elif self.sex == "female":
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161
        else:
            raise ValueError("Invalid sex. Must be 'male' or 'female'.")

        condition = self.condition_judge()
        if condition == 1:  # Overweight
            calorie_intake = bmr * 1.2
        elif condition == -1:  # Underweight
            calorie_intake = bmr * 1.6
        else:  # Normal
            calorie_intake = bmr * 1.4

        return calorie_intake


if __name__ == '__main__':
    # Example usage and testing
    fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
    bmi = fitnessTracker.get_BMI()
    print(f"BMI: {bmi}")
    condition = fitnessTracker.condition_judge()
    print(f"Condition: {condition} (-1: Underweight, 0: Normal, 1: Overweight)")
    calorie_intake = fitnessTracker.calculate_calorie_intake()
    print(f"Recommended calorie intake: {calorie_intake}")

    fitnessTracker_female = FitnessTracker(1.6, 55, 25, "female")
    bmi_female = fitnessTracker_female.get_BMI()
    print(f"Female BMI: {bmi_female}")
    condition_female = fitnessTracker_female.condition_judge()
    print(f"Female Condition: {condition_female} (-1: Underweight, 0: Normal, 1: Overweight)")
    calorie_intake_female = fitnessTracker_female.calculate_calorie_intake()
    print(f"Female Recommended calorie intake: {calorie_intake_female}")

    fitnessTracker_overweight = FitnessTracker(1.75, 90, 30, "male")
    bmi_overweight = fitnessTracker_overweight.get_BMI()
    print(f"Overweight BMI: {bmi_overweight}")
    condition_overweight = fitnessTracker_overweight.condition_judge()
    print(f"Overweight Condition: {condition_overweight} (-1: Underweight, 0: Normal, 1: Overweight)")
    calorie_intake_overweight = fitnessTracker_overweight.calculate_calorie_intake()
    print(f"Overweight Recommended calorie intake: {calorie_intake_overweight}")