class ClassRegistrationSystem:
    """
    A class registration system that allows registering students, enrolling them in classes, retrieving students by major,
    getting a list of all majors, and determining the most popular class within a specific major.
    """

    def __init__(self):
        """
        Initializes the registration system with lists and dictionaries to track students and their registered classes.
        """
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        """
        Registers a student in the system. If the student is already registered, returns 0, else returns 1.
        
        :param student: dict with keys 'name' and 'major'
        :return: 1 if registered successfully, 0 if the student is already registered
        """
        if any(existing_student['name'] == student['name'] for existing_student in self.students):
            return 0
        self.students.append(student)
        self.students_registration_classes[student['name']] = []
        return 1

    def register_class(self, student_name, class_name):
        """
        Registers a class for a student.
        
        :param student_name: str
        :param class_name: str
        :return: list of class names that the student has registered
        """
        if student_name not in self.students_registration_classes:
            self.students_registration_classes[student_name] = []
        self.students_registration_classes[student_name].append(class_name)
        return self.students_registration_classes[student_name]

    def get_students_by_major(self, major):
        """
        Retrieves all students in a specific major.
        
        :param major: str
        :return: list of student names
        """
        return [student['name'] for student in self.students if student['major'] == major]

    def get_all_majors(self):
        """
        Retrieves all unique majors in the system.
        
        :return: list of majors
        """
        return list(set(student['major'] for student in self.students))

    def get_most_popular_class_in_major(self, major):
        """
        Determines the class with the highest enrollment in a specific major.
        
        :param major: str
        :return: name of the most popular class or None if no classes are registered
        """
        class_enrollment = {}
        for student in self.students:
            if student['major'] == major:
                for class_name in self.students_registration_classes[student['name']]:
                    class_enrollment[class_name] = class_enrollment.get(class_name, 0) + 1
        return max(class_enrollment, key=class_enrollment.get) if class_enrollment else None