class ClassRegistrationSystem:
    """
    This is a class as a class registration system, allowing to register students, register them for classes, retrieve students by major, get a list of all majors, and determine the most popular class within a specific major.
    """

    def __init__(self):
        """
        Initialize the registration system with the attribute students and students_registration_class.
        students is a list of student dictionaries, each student dictionary has the key of name and major.
        students_registration_class is a dictionaries, key is the student name, value is a list of class names
        """
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        """
        Registers a student to the system.

        Args:
            student (dict): A dictionary containing student information (name, major).

        Returns:
            int: 1 if the student was successfully registered, 0 if the student is already registered.
        """
        if student in self.students:
            return 0
        else:
            self.students.append(student)
            return 1

    def register_class(self, student_name, class_name):
        """
        Registers a student for a class.

        Args:
            student_name (str): The name of the student.
            class_name (str): The name of the class.

        Returns:
            list: A list of class names that the student has registered for.
        """
        if student_name not in self.students_registration_classes:
            self.students_registration_classes[student_name] = [class_name]
        else:
            if class_name not in self.students_registration_classes[student_name]:
                self.students_registration_classes[student_name].append(class_name)
        return self.students_registration_classes[student_name]

    def get_students_by_major(self, major):
        """
        Retrieves a list of students in a specific major.

        Args:
            major (str): The major to search for.

        Returns:
            list: A list of student names in the specified major.
        """
        student_names = []
        for student in self.students:
            if student["major"] == major:
                student_names.append(student["name"])
        return student_names

    def get_all_major(self):
        """
        Retrieves a list of all unique majors in the system.

        Returns:
            list: A list of majors.
        """
        majors = []
        for student in self.students:
            if student["major"] not in majors:
                majors.append(student["major"])
        return majors

    def get_most_popular_class_in_major(self, major):
        """
        Retrieves the most popular class within a specific major.

        Args:
            major (str): The major to search for.

        Returns:
            str: The name of the most popular class in the major, or None if no classes are found.
        """
        class_counts = {}
        for student in self.students:
            if student["major"] == major:
                student_name = student["name"]
                if student_name in self.students_registration_classes:
                    for class_name in self.students_registration_classes[student_name]:
                        class_counts[class_name] = class_counts.get(class_name, 0) + 1

        most_popular_class = None
        max_count = 0
        for class_name, count in class_counts.items():
            if count > max_count:
                most_popular_class = class_name
                max_count = count

        return most_popular_class