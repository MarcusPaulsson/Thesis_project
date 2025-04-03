class FitnessTracker:
    """
    This is a class as fitness tracker that implements to calculate BMI (Body Mass Index) and calorie intake based on the user's height, weight, age, and sex.
    """

    def __init__(self, height, weight, age, sex) -> None:
        """
        Initialize the class with height, weight, age, and sex, and calculate the BMI standard based on sex, and male is 20-25, female is 19-24.
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        self.BMI_std = {
            "male": [20, 25],
            "female": [19, 24]
        }

    def get_BMI(self):
        """
        Calculate the BMI based on the height and weight.
        :return: BMI, which is the weight divided by the square of height, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.get_BMI()
        21.604938271604937
        """
        return self.weight / (self.height ** 2)

    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        0
        """
        bmi = self.get_BMI()
        if self.sex in self.BMI_std:
            lower_bound, upper_bound = self.BMI_std[self.sex]
            if bmi < lower_bound:
                return -1  # Too thin
            elif bmi > upper_bound:
                return 1   # Too fat
            else:
                return 0   # Normal
        return None  # Invalid sex

    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).
        BMR is calculated based on the user's height, weight, age, and sex.
        :return: calorie intake, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.calculate_calorie_intake()
        2580.0
        """
        if self.sex == "male":
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        elif self.sex == "female":
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161
        else:
            return None  # Invalid sex

        condition = self.condition_judge()
        if condition == 1:  # Too fat
            return bmr * 1.2
        elif condition == -1:  # Too thin
            return bmr * 1.6
        else:  # Normal
            return bmr * 1.4