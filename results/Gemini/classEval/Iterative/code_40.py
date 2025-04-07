class FitnessTracker:
    """
    A class for tracking fitness metrics like BMI and calorie intake.
    """

    BMI_STANDARDS = {
        "male": [20, 25],
        "female": [19, 24]
    }
    ACTIVITY_MULTIPLIERS = {
        1: 1.2,  # Overweight
        -1: 1.6, # Underweight
        0: 1.4   # Normal
    }

    def __init__(self, height, weight, age, sex):
        """
        Initializes the FitnessTracker with user data.

        Args:
            height (float): Height in meters.
            weight (float): Weight in kilograms.
            age (int): Age in years.
            sex (str): Sex, either "male" or "female".

        Raises:
            ValueError: If sex is not "male" or "female".
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex.lower()

        if self.sex not in ("male", "female"):
            raise ValueError("Sex must be 'male' or 'female'.")


    def get_BMI(self):
        """
        Calculates the Body Mass Index (BMI).

        Returns:
            float: The calculated BMI.
        """
        if self.height <= 0:
            raise ValueError("Height must be a positive value.")
        return self.weight / (self.height ** 2)

    def condition_judge(self):
        """
        Determines the user's condition based on BMI.

        Returns:
            int: 1 if overweight, -1 if underweight, 0 if normal.
        """
        bmi = self.get_BMI()
        lower_limit, upper_limit = self.BMI_STANDARDS[self.sex]

        if bmi > upper_limit:
            return 1
        elif bmi < lower_limit:
            return -1
        else:
            return 0

    def calculate_calorie_intake(self):
        """
        Calculates the recommended daily calorie intake based on BMR and activity level.

        Returns:
            float: The calculated calorie intake.
        """
        bmr = self._calculate_bmr()
        condition = self.condition_judge()
        multiplier = self.ACTIVITY_MULTIPLIERS.get(condition)

        if multiplier is None:
            raise ValueError("Invalid condition value.")

        return bmr * multiplier

    def _calculate_bmr(self):
        """
        Calculates the Basal Metabolic Rate (BMR).

        Returns:
            float: The calculated BMR.
        """
        if self.sex == "male":
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        else:
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161
        return bmr