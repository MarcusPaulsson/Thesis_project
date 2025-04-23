class ClassRegistrationSystem:
    """
    A class registration system that allows registering students, enrolling them in classes,
    retrieving students by major, listing all majors, and determining the most popular class
    within a specific major.
    """

    def __init__(self):
        """
        Initializes the registration system with a list of students and a dictionary for class registrations.
        """
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        """
        Registers a student in the system. Returns 0 if the student is already registered, otherwise returns 1.
        
        :param student: dict with 'name' and 'major' keys
        :return: int
        """
        if any(existing_student['name'] == student['name'] for existing_student in self.students):
            return 0
        self.students.append(student)
        return 1

    def register_class(self, student_name, class_name):
        """
        Registers a class for a student. If the student is not registered, they are added to the system.
        
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
        Retrieves all students in a specified major.
        
        :param major: str
        :return: list of student names
        """
        return [student['name'] for student in self.students if student['major'] == major]

    def get_all_major(self):
        """
        Retrieves a list of all unique majors in the system.
        
        :return: list of majors
        """
        return list({student['major'] for student in self.students})

    def get_most_popular_class_in_major(self, major):
        """
        Determines the class with the highest enrollment in a specified major.
        
        :param major: str
        :return: str of the most popular class in this major, or None if no classes are registered
        """
        class_count = {}
        for student in self.students:
            if student['major'] == major:
                for class_name in self.students_registration_classes.get(student['name'], []):
                    class_count[class_name] = class_count.get(class_name, 0) + 1
        return max(class_count, key=class_count.get) if class_count else None