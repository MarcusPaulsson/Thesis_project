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
        self.BMI_std = [
            {"male": [20, 25]},
            {"female": [19, 24]}
        ]

    def get_BMI(self):
        """
        Calculate the BMI based on the height and weight.
        :return: BMI, which is the weight divide by the square of height, float.
        """
        return self.weight / (self.height ** 2)

    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        bmi = self.get_BMI()
        if self.sex == "male":
            if bmi < 20:
                return -1
            elif bmi > 25:
                return 1
            else:
                return 0
        else:  # female
            if bmi < 19:
                return -1
            elif bmi > 24:
                return 1
            else:
                return 0

    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).
        :return: calorie intake, float.
        """
        if self.sex == "male":
            BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        else:  # female
            BMR = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161

        condition = self.condition_judge()
        if condition == 1:  # too fat
            return BMR * 1.2
        elif condition == -1:  # too thin
            return BMR * 1.6
        else:  # normal
            return BMR * 1.4