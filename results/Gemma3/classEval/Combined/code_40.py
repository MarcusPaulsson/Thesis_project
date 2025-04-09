class FitnessTracker:
    """
    This is a class as fitness tracker that implements to calculate BMI (Body Mass Index) and calorie intake based on the user's height, weight, age, and sex.
    """

    def __init__(self, height, weight, age, sex) -> None:
        """
        Initialize the class with height, weight, age, and sex.
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex

    def get_BMI(self):
        """
        Calculate the BMI based on the height and weight.
        :return: BMI, which is the weight divided by the square of height, float.
        """
        if self.height <= 0:
            return 0  # Avoid division by zero or negative height
        return self.weight / (self.height ** 2)

    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI.
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
        else:  # Assuming female if not male
            if bmi < 19:
                return -1
            elif bmi > 24:
                return 1
            else:
                return 0

    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).
        BMR is calculated based on the user's height, weight, age, and sex.
        Calorie intake is calculated based on the BMR and the user's condition.
        :return: calorie intake, float.
        """
        if self.sex == "male":
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161

        condition = self.condition_judge()
        if condition == 1:
            return bmr * 1.2
        elif condition == -1:
            return bmr * 1.6
        else:
            return bmr * 1.4