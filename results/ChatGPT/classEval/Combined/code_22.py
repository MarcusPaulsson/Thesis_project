class ClassRegistrationSystem:
    """
    A class registration system that allows for registering students, enrolling them in classes,
    retrieving students by major, getting a list of all majors, and determining the most popular
    class within a specific major.
    """

    def __init__(self):
        """Initialize the registration system with students and their class registrations."""
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        """
        Register a student to the system.
        :param student: dict with 'name' and 'major' keys
        :return: 1 if the student is successfully registered, 0 if already registered.
        """
        if student in self.students:
            return 0
        self.students.append(student)
        return 1

    def register_class(self, student_name, class_name):
        """
        Register a class for a student.
        :param student_name: str
        :param class_name: str
        :return: list of class names that the student has registered.
        """
        if student_name not in self.students_registration_classes:
            self.students_registration_classes[student_name] = []
        self.students_registration_classes[student_name].append(class_name)
        return self.students_registration_classes[student_name]

    def get_students_by_major(self, major):
        """
        Get all students enrolled in a specific major.
        :param major: str
        :return: list of student names in the specified major.
        """
        return [student['name'] for student in self.students if student['major'] == major]

    def get_all_major(self):
        """
        Get a list of all majors available in the system.
        :return: list of unique majors.
        """
        return list({student['major'] for student in self.students})

    def get_most_popular_class_in_major(self, major):
        """
        Get the class with the highest enrollment in a specific major.
        :param major: str
        :return: name of the most popular class in the specified major.
        """
        class_count = {}
        for student in self.students:
            if student['major'] == major:
                for class_name in self.students_registration_classes.get(student['name'], []):
                    class_count[class_name] = class_count.get(class_name, 0) + 1
        return max(class_count, key=class_count.get, default=None)