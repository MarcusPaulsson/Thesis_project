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
        self.sex = sex

    def get_BMI(self) -> float:
        """
        Calculate the BMI based on the height and weight.
        :return: BMI, which is the weight divided by the square of height.
        """
        return self.weight / (self.height ** 2)

    def condition_judge(self) -> int:
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal.
        """
        bmi = self.get_BMI()
        if self.sex == "male":
            if bmi < 20:
                return -1
            elif bmi > 25:
                return 1
            else:
                return 0
        elif self.sex == "female":
            if bmi < 19:
                return -1
            elif bmi > 24:
                return 1
            else:
                return 0
        else:
            raise ValueError("Sex must be either 'male' or 'female'.")

    def calculate_calorie_intake(self) -> float:
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).
        :return: Calorie intake based on user's condition.
        """
        bmr = (10 * self.weight) + (6.25 * self.height * 100) - (5 * self.age)
        if self.sex == "female":
            bmr -= 161
        elif self.sex == "male":
            bmr += 5
        else:
            raise ValueError("Sex must be either 'male' or 'female'.")

        condition = self.condition_judge()
        if condition == 1:  # Too fat
            return bmr * 1.2
        elif condition == -1:  # Too thin
            return bmr * 1.6
        else:  # Normal
            return bmr * 1.4