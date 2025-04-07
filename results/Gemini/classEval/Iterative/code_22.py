class ClassRegistrationSystem:
    """
    A class for managing student registration and class enrollment.
    """

    def __init__(self):
        """
        Initializes the registration system.
        - `students`: A dictionary where keys are student names and values are dictionaries containing student information (e.g., major).
        - `class_rosters`: A dictionary where keys are class names and values are sets of student names enrolled in that class.
        """
        self.students = {}  # {student_name: {major: str, ...}}
        self.class_rosters = {}  # {class_name: set(student_names)}

    def register_student(self, student_name, major):
        """
        Registers a student in the system.

        Args:
            student_name (str): The name of the student.
            major (str): The student's major.

        Returns:
            bool: True if the student was successfully registered, False if the student already exists.
        """
        if student_name in self.students:
            return False  # Student already exists
        self.students[student_name] = {"major": major}
        return True

    def register_class(self, student_name, class_name):
        """
        Registers a student for a class.

        Args:
            student_name (str): The name of the student.
            class_name (str): The name of the class.

        Returns:
            bool: True if the student was successfully registered for the class, False otherwise (e.g., student doesn't exist).
        """
        if student_name not in self.students:
            return False  # Student does not exist

        if class_name not in self.class_rosters:
            self.class_rosters[class_name] = set()

        self.class_rosters[class_name].add(student_name)
        return True

    def get_students_by_major(self, major):
        """
        Retrieves a list of student names for a given major.

        Args:
            major (str): The major to search for.

        Returns:
            list: A list of student names belonging to the specified major.
        """
        return [
            student_name
            for student_name, student_info in self.students.items()
            if student_info["major"] == major
        ]

    def get_all_majors(self):
        """
        Retrieves a list of all unique majors in the system.

        Returns:
            list: A list of unique majors.
        """
        majors = set()
        for student_info in self.students.values():
            majors.add(student_info["major"])
        return list(majors)

    def get_most_popular_class_in_major(self, major):
        """
        Finds the most popular class among students of a specific major.

        Args:
            major (str): The major to consider.

        Returns:
            str: The name of the most popular class, or None if no students in the major are registered for any classes.
        """
        class_counts = {}
        for class_name, student_set in self.class_rosters.items():
            for student_name in student_set:
                if (
                    student_name in self.students
                    and self.students[student_name]["major"] == major
                ):
                    class_counts[class_name] = class_counts.get(class_name, 0) + 1

        if not class_counts:
            return None  # No students in the major are registered for classes

        most_popular_class = max(class_counts, key=class_counts.get)
        return most_popular_class