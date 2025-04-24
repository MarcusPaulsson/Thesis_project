class FitnessTracker:
    """
    This is a class as fitness tracker that implements to calculate BMI (Body Mass Index) and calorie intake based on the user's height, weight, age, and sex.
    """

    def __init__(self, height, weight, age, sex) -> None:
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
        self.sex = sex
        self.bmi_standards = {
            "male": [20, 25],
            "female": [19, 24]
        }

    def get_BMI(self):
        """
        Calculate the BMI based on the height and weight.

        Returns:
            float: BMI (Body Mass Index).
        """
        return self.weight / (self.height ** 2)

    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.

        Returns:
            int: 1 if the user is overweight, -1 if underweight, 0 if normal.
        """
        bmi = self.get_BMI()
        bmi_range = self.bmi_standards.get(self.sex)
        if not bmi_range:
            raise ValueError("Invalid sex. Must be 'male' or 'female'.")

        if bmi < bmi_range[0]:
            return -1
        elif bmi > bmi_range[1]:
            return 1
        else:
            return 0

    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).

        Returns:
            float: Calorie intake.
        """
        if self.sex == "male":
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        elif self.sex == "female":
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161
        else:
            raise ValueError("Invalid sex. Must be 'male' or 'female'.")

        condition = self.condition_judge()
        if condition == 1:  # Overweight
            return bmr * 1.2
        elif condition == -1:  # Underweight
            return bmr * 1.4
        else:  # Normal
            return bmr * 1.3