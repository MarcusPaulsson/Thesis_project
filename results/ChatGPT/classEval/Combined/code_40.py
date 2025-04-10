class FitnessTracker:
    """
    A class to track fitness metrics such as BMI (Body Mass Index) and calorie intake 
    based on the user's height, weight, age, and sex.
    """

    def __init__(self, height: float, weight: float, age: int, sex: str) -> None:
        """
        Initialize the FitnessTracker with user's height, weight, age, and sex.
        
        :param height: Height in meters (float)
        :param weight: Weight in kilograms (float)
        :param age: Age in years (int)
        :param sex: Sex of the user ('male' or 'female') (str)
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex.lower()
        self.validate_inputs()

    def validate_inputs(self):
        """ Validates the input parameters for correctness. """
        if self.sex not in ["male", "female"]:
            raise ValueError("Invalid sex. Please use 'male' or 'female'.")
        if self.height <= 0 or self.weight <= 0 or self.age <= 0:
            raise ValueError("Height, weight, and age must be positive values.")

    def get_BMI(self) -> float:
        """
        Calculate the BMI based on height and weight.
        
        :return: BMI as a float.
        """
        return self.weight / (self.height ** 2)

    def condition_judge(self) -> int:
        """
        Determine the user's weight condition based on BMI.
        
        :return: 1 if overweight, -1 if underweight, 0 if normal weight.
        """
        bmi = self.get_BMI()
        if self.sex == "male":
            if bmi < 20:
                return -1  # Underweight
            elif bmi > 25:
                return 1   # Overweight
            else:
                return 0   # Normal weight
        else:  # Female
            if bmi < 19:
                return -1  # Underweight
            elif bmi > 24:
                return 1   # Overweight
            else:
                return 0   # Normal weight

    def calculate_calorie_intake(self) -> float:
        """
        Calculate the recommended calorie intake based on BMR and weight condition.
        
        :return: Recommended calorie intake as a float.
        """
        bmr = (10 * self.weight) + (6.25 * (self.height * 100)) - (5 * self.age)
        bmr += 5 if self.sex == "male" else -161
        
        condition = self.condition_judge()
        if condition == 1:  # Overweight
            return bmr * 1.2
        elif condition == -1:  # Underweight
            return bmr * 1.6
        else:  # Normal weight
            return bmr * 1.4