class FitnessTracker:
    """
    This is a class as fitness tracker that implements to calculate BMI (Body Mass Index) and calorie intake
    based on the user's height, weight, age, and sex.
    """

    def __init__(self, height, weight, age, sex) -> None:
        """
        Initialize the class with height, weight, age, and sex, and calculate the BMI standard based on sex.
        Male standard is 20-25, female is 19-24.
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex.lower()
        self.BMI_std = {
            "male": [20, 25],
            "female": [19, 24]
        }

    def get_BMI(self) -> float:
        """
        Calculate the BMI based on the height and weight.
        :return: BMI, which is the weight divided by the square of height, float.
        """
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)

    def condition_judge(self) -> int:
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        bmi = self.get_BMI()
        if self.sex == "male":
            if bmi < self.BMI_std["male"][0]:
                return -1
            elif bmi > self.BMI_std["male"][1]:
                return 1
            else:
                return 0
        elif self.sex == "female":
            if bmi < self.BMI_std["female"][0]:
                return -1
            elif bmi > self.BMI_std["female"][1]:
                return 1
            else:
                return 0
        else:
            raise ValueError("Invalid sex. Please use 'male' or 'female'.")

    def calculate_calorie_intake(self) -> float:
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate),
        BMR is calculated based on the user's height, weight, age, and sex.
        Male: BMR = 10 * weight + 6.25 * height * 100 - 5 * age + 5
        Female: BMR = 10 * weight + 6.25 * height * 100 - 5 * age - 161
        The calorie intake is adjusted based on the user's condition.
        :return: calorie intake, float.
        """
        bmr = (10 * self.weight) + (6.25 * self.height * 100) - (5 * self.age) + (5 if self.sex == "male" else -161)

        condition = self.condition_judge()
        if condition == 1:  # too fat
            calorie_intake = bmr * 1.2
        elif condition == -1:  # too thin
            calorie_intake = bmr * 1.6
        else:  # normal
            calorie_intake = bmr * 1.4

        return round(calorie_intake, 2)