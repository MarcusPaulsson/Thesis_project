class FitnessTracker:
    """
    A class to track fitness metrics including BMI (Body Mass Index) and calorie intake based on user's height, weight, age, and sex.
    """

    def __init__(self, height: float, weight: float, age: int, sex: str) -> None:
        """
        Initialize the class with height, weight, age, and sex.
        :param height: User's height in meters.
        :param weight: User's weight in kilograms.
        :param age: User's age in years.
        :param sex: User's sex, either 'male' or 'female'.
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex.lower()
        self.validate_inputs()

    def validate_inputs(self) -> None:
        """Validate the input parameters."""
        if self.sex not in {"male", "female"}:
            raise ValueError("Sex must be 'male' or 'female'.")

    def get_bmi(self) -> float:
        """
        Calculate the BMI based on the height and weight.
        :return: BMI as a float.
        """
        return self.weight / (self.height ** 2)

    def condition_judge(self) -> int:
        """
        Judge the user's condition based on BMI standards.
        :return: 1 if overweight, -1 if underweight, 0 if normal weight.
        """
        bmi = self.get_bmi()
        if self.sex == "male":
            if bmi < 20:
                return -1
            elif bmi > 25:
                return 1
            return 0
        else:  # self.sex == "female"
            if bmi < 19:
                return -1
            elif bmi > 24:
                return 1
            return 0

    def calculate_calorie_intake(self) -> float:
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).
        :return: Calorie intake as a float.
        """
        bmr = self.calculate_bmr()
        condition = self.condition_judge()

        if condition == 1:  # Overweight
            return bmr * 1.2
        elif condition == -1:  # Underweight
            return bmr * 1.6
        return bmr * 1.4  # Normal weight

    def calculate_bmr(self) -> float:
        """
        Calculate the Basal Metabolic Rate (BMR) based on user's height, weight, age, and sex.
        :return: BMR as a float.
        """
        if self.sex == "male":
            return 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        return 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161