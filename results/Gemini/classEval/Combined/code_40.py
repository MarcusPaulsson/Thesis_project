class FitnessTracker:
    """
    A class for tracking fitness metrics like BMI and calorie intake.
    """

    def __init__(self, height: float, weight: float, age: int, sex: str) -> None:
        """
        Initializes the FitnessTracker with user data.

        Args:
            height: Height in meters.
            weight: Weight in kilograms.
            age: Age in years.
            sex: Sex ("male" or "female").
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex.lower()  # Store sex in lowercase for case-insensitive comparison

        # BMI standards for males and females
        self.bmi_standards = {
            "male": (20, 25),  # Lower and upper bounds for normal BMI
            "female": (19, 24),
        }

        if self.sex not in self.bmi_standards:
            raise ValueError("Invalid sex. Must be 'male' or 'female'.")

    def get_BMI(self) -> float:
        """
        Calculates the Body Mass Index (BMI).

        Returns:
            The BMI value.
        """
        if self.height <= 0:
            raise ValueError("Height must be a positive value.")
        return self.weight / (self.height ** 2)

    def condition_judge(self) -> int:
        """
        Judges the user's condition based on their BMI.

        Returns:
            1 if overweight, -1 if underweight, 0 if normal.
        """
        bmi = self.get_BMI()
        lower_bound, upper_bound = self.bmi_standards[self.sex]

        if bmi < lower_bound:
            return -1  # Underweight
        elif bmi > upper_bound:
            return 1  # Overweight
        else:
            return 0  # Normal

    def calculate_calorie_intake(self) -> float:
        """
        Calculates the recommended daily calorie intake based on BMR and condition.

        Returns:
            The recommended daily calorie intake.
        """
        # Calculate Basal Metabolic Rate (BMR)
        if self.sex == "male":
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        else:  # self.sex == "female"
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161

        condition = self.condition_judge()

        # Adjust calorie intake based on condition
        if condition == 1:  # Overweight
            calorie_intake = bmr * 1.2
        elif condition == -1:  # Underweight
            calorie_intake = bmr * 1.6
        else:  # Normal
            calorie_intake = bmr * 1.4

        return calorie_intake