class FitnessTracker:
    """
    A class to track fitness metrics, including BMI (Body Mass Index) and calorie intake,
    based on user attributes: height, weight, age, and sex.
    """

    def __init__(self, height: float, weight: float, age: int, sex: str) -> None:
        """
        Initialize the FitnessTracker with height, weight, age, and sex.
        
        :param height: User's height in meters.
        :param weight: User's weight in kilograms.
        :param age: User's age in years.
        :param sex: User's sex ('male' or 'female').
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex.lower()

    def get_BMI(self) -> float:
        """
        Calculate and return the BMI based on height and weight.
        
        :return: BMI as a float.
        """
        return self.weight / (self.height ** 2)

    def condition_judge(self) -> int:
        """
        Determine the user's condition based on BMI standards.
        
        :return: 1 if overweight, -1 if underweight, 0 if normal weight.
        """
        bmi = self.get_BMI()
        if self.sex == "male":
            return 1 if bmi > 25 else -1 if bmi < 20 else 0
        elif self.sex == "female":
            return 1 if bmi > 24 else -1 if bmi < 19 else 0
        return 0  # Default case for invalid sex input

    def calculate_calorie_intake(self) -> float:
        """
        Calculate daily calorie intake based on BMR and user's condition.
        
        :return: Recommended calorie intake as a float.
        """
        bmr = (10 * self.weight) + (6.25 * self.height * 100) - (5 * self.age) + (5 if self.sex == "male" else -161)
        condition = self.condition_judge()
        
        if condition == 1:  # Overweight
            return bmr * 1.2
        elif condition == -1:  # Underweight
            return bmr * 1.6
        else:  # Normal weight
            return bmr * 1.4