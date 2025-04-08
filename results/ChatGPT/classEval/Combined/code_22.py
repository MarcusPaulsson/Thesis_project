class ClassRegistrationSystem:
    """
    A class representing a class registration system that allows for student registration, 
    class enrollment, retrieval of students by major, listing all majors, and finding the most popular class in a major.
    """

    def __init__(self):
        """Initialize the registration system with a list of students and a dictionary for class registrations."""
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        """
        Register a student to the system. If the student is already registered, 
        return 0; otherwise, return 1 after adding the student.

        :param student: dict, containing 'name' and 'major' keys.
        :return: int (1 for successful registration, 0 if already registered)
        """
        if any(existing_student['name'] == student['name'] for existing_student in self.students):
            return 0
        self.students.append(student)
        return 1

    def register_class(self, student_name, class_name):
        """
        Register a class for a student. If the student is not already in the system, 
        they will be initialized.

        :param student_name: str
        :param class_name: str
        :return: list of class names that the student has registered
        """
        self.students_registration_classes.setdefault(student_name, []).append(class_name)
        return self.students_registration_classes[student_name]

    def get_students_by_major(self, major):
        """
        Retrieve all students enrolled in a specified major.

        :param major: str
        :return: list of student names
        """
        return [student['name'] for student in self.students if student['major'] == major]

    def get_all_majors(self):
        """
        Get a list of all unique majors in the system.

        :return: list of majors
        """
        return list({student['major'] for student in self.students})

    def get_most_popular_class_in_major(self, major):
        """
        Determine the most popular class among students in a specified major.

        :param major: str
        :return: str of the most popular class name or None if no classes are registered
        """
        class_count = {}
        for student in self.students:
            if student['major'] == major:
                for class_name in self.students_registration_classes.get(student['name'], []):
                    class_count[class_name] = class_count.get(class_name, 0) + 1
        return max(class_count, key=class_count.get) if class_count else None