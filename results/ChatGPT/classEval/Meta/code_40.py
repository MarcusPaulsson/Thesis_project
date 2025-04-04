class FitnessTracker:
    """
    This is a class as fitness tracker that implements to calculate BMI (Body Mass Index) and calorie intake based on the user's height, weight, age, and sex.
    """

    def __init__(self, height, weight, age, sex) -> None:
        """
        Initialize the class with height, weight, age, and sex, and calculate the BMI standard based on sex.
        """
        self.height = height  # in meters
        self.weight = weight  # in kilograms
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
        """
        return self.weight / (self.height ** 2)

    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        bmi = self.get_BMI()
        if self.sex not in self.BMI_std:
            raise ValueError("Sex must be 'male' or 'female'")
        
        std = self.BMI_std[self.sex]
        if bmi < std[0]:  # below the lower limit
            return -1  # too thin
        elif bmi > std[1]:  # above the upper limit
            return 1  # too fat
        else:
            return 0  # normal

    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).
        :return: calorie intake, float.
        """
        if self.sex == "male":
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age + 5
        elif self.sex == "female":
            bmr = 10 * self.weight + 6.25 * self.height * 100 - 5 * self.age - 161
        else:
            raise ValueError("Sex must be 'male' or 'female'")

        condition = self.condition_judge()
        if condition == 1:  # too fat
            calorie_intake = bmr * 1.2
        elif condition == -1:  # too thin
            calorie_intake = bmr * 1.6
        else:  # normal
            calorie_intake = bmr * 1.4
        
        return calorie_intake