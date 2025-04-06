class FitnessTracker:
    """
    A fitness tracker class that calculates BMI (Body Mass Index) and calorie intake based on the user's height, weight, age, and sex.
    """

    BMI_STANDARD = {
        "male": (20, 25),
        "female": (19, 24)
    }

    def __init__(self, height: float, weight: float, age: int, sex: str) -> None:
        """
        Initialize the class with height, weight, age, and sex.
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex.lower()
        if self.sex not in self.BMI_STANDARD:
            raise ValueError("Sex must be 'male' or 'female'.")

    def get_BMI(self) -> float:
        """
        Calculate the BMI based on height and weight.
        :return: BMI as a float.
        """
        return self.weight / (self.height ** 2)

    def condition_judge(self) -> int:
        """
        Judge the user's condition based on BMI standards.
        :return: 1 if overweight, -1 if underweight, 0 if normal.
        """
        bmi = self.get_BMI()
        lower_bound, upper_bound = self.BMI_STANDARD[self.sex]
        if bmi < lower_bound:
            return -1
        elif bmi > upper_bound:
            return 1
        return 0

    def calculate_calorie_intake(self) -> float:
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).
        :return: Calorie intake as a float.
        """
        if self.sex == "male":
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        else:
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161
        
        condition = self.condition_judge()
        if condition == 1:  # overweight
            calorie_intake = bmr * 1.2
        elif condition == -1:  # underweight
            calorie_intake = bmr * 1.6
        else:  # normal
            calorie_intake = bmr * 1.4
        
        return calorie_intake