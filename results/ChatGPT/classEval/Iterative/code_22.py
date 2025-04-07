class ClassRegistrationSystem:
    """
    This is a class as a class registration system, allowing to register students, register them for classes, retrieve students by major,
    get a list of all majors, and determine the most popular class within a specific major.
    """

    def __init__(self):
        """
        Initialize the registration system with the attribute students and students_registration_classes.
        students is a list of student dictionaries, each student dictionary has the key of name and major.
        students_registration_classes is a dictionary, key is the student name, value is a list of class names
        """
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        """
        Register a student to the system. If the student is already registered, return 0; otherwise, add the student to the list and return 1.
        :param student: dict
        :return: int
        """
        if student in self.students:
            return 0
        else:
            self.students.append(student)
            return 1

    def register_class(self, student_name, class_name):
        """
        Register a class for a student and return the updated list of classes that the student has registered for.
        :param student_name: str
        :param class_name: str
        :return: list
        """
        if student_name not in self.students_registration_classes:
            self.students_registration_classes[student_name] = []
        if class_name not in self.students_registration_classes[student_name]:
            self.students_registration_classes[student_name].append(class_name)
        return self.students_registration_classes[student_name]

    def get_students_by_major(self, major):
        """
        Get all students in the specified major.
        :param major: str
        :return: list
        """
        return [student["name"] for student in self.students if student["major"] == major]

    def get_all_major(self):
        """
        Get a list of all majors in the system.
        :return: list
        """
        return list(set(student["major"] for student in self.students))

    def get_most_popular_class_in_major(self, major):
        """
        Get the class with the highest enrollment in the specified major.
        :param major: str
        :return: str or None
        """
        class_count = {}
        for student in self.students:
            if student["major"] == major:
                student_classes = self.students_registration_classes.get(student["name"], [])
                for class_name in student_classes:
                    class_count[class_name] = class_count.get(class_name, 0) + 1
        if not class_count:
            return None
        return max(class_count, key=class_count.get)