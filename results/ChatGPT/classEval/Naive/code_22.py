class ClassRegistrationSystem:
    """
    A class representing a class registration system, allowing registration of students, 
    enrollment in classes, retrieval of students by major, listing all majors, 
    and determining the most popular class within a specific major.
    """

    def __init__(self):
        """
        Initialize the registration system with students and their class registrations.
        """
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        """
        Register a student in the system. 
        If the student is already registered, return 0; otherwise, return 1.
        
        :param student: dict containing 'name' and 'major'.
        :return: int
        """
        if any(s['name'] == student['name'] for s in self.students):
            return 0
        self.students.append(student)
        self.students_registration_classes[student['name']] = []
        return 1

    def register_class(self, student_name, class_name):
        """
        Register a class for a student and return the list of classes the student is enrolled in.
        
        :param student_name: str
        :param class_name: str
        :return: list of class names
        """
        if student_name in self.students_registration_classes:
            self.students_registration_classes[student_name].append(class_name)
            return self.students_registration_classes[student_name]
        return []

    def get_students_by_major(self, major):
        """
        Retrieve all students enrolled in a specified major.
        
        :param major: str
        :return: list of student names
        """
        return [student['name'] for student in self.students if student['major'] == major]

    def get_all_major(self):
        """
        Retrieve a list of all unique majors in the system.
        
        :return: list of majors
        """
        return list(set(student['major'] for student in self.students))

    def get_most_popular_class_in_major(self, major):
        """
        Determine the most popular class within a specific major based on enrollment.
        
        :param major: str
        :return: str of the most popular class
        """
        class_count = {}
        for student in self.students:
            if student['major'] == major:
                for class_name in self.students_registration_classes[student['name']]:
                    class_count[class_name] = class_count.get(class_name, 0) + 1
                    
        return max(class_count, key=class_count.get) if class_count else None