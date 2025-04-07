class AssessmentSystem:
    """
    This is a class as an student assessment system, which supports add student, add course score, calculate GPA, and other functions for students and courses.
    """

    def __init__(self):
        """
        Initialize the students dict in assessment system.
        """
        self.students = {}

    def add_student(self, name, grade, major):
        """
        Add a new student into self.students dict
        :param name: str, student name
        :param grade: int, student grade
        :param major: str, student major
        Raises:
            TypeError: if name is not a string, grade is not an integer, or major is not a string.
            ValueError: if grade is not a valid grade (e.g., negative or unreasonably high).
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(grade, int):
            raise TypeError("Grade must be an integer.")
        if not isinstance(major, str):
            raise TypeError("Major must be a string.")
        if grade < 0:
            raise ValueError("Grade must be a non-negative integer.")

        if name in self.students:
            raise ValueError(f"Student with name '{name}' already exists.")

        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param course: str, course name
        :param score: int, course score
        Raises:
            TypeError: if name or course is not a string, or score is not an integer.
            ValueError: if score is not a valid score (e.g., negative or greater than 100).
            KeyError: if the student does not exist.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(course, str):
            raise TypeError("Course must be a string.")
        if not isinstance(score, int):
            raise TypeError("Score must be an integer.")

        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")

        if name not in self.students:
            raise KeyError(f"Student with name '{name}' does not exist.")

        self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this students have courses grade, return average grade(float)
                    or None otherwise
        Raises:
            TypeError: if name is not a string.
            KeyError: if the student does not exist.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        if name not in self.students:
            return None

        if not self.students[name]['courses']:
            return None

        scores = list(self.students[name]['courses'].values())
        return sum(scores) / len(scores)

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score below 60
        :return: list of str ,student name
        """
        failed_students = []
        for name, student_data in self.students.items():
            for score in student_data['courses'].values():
                if score < 60:
                    failed_students.append(name)
                    break  # Only add the student once if they have multiple failing grades
        return failed_students

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        Raises:
            TypeError: if course is not a string.
        """
        if not isinstance(course, str):
            raise TypeError("Course must be a string.")

        scores = []
        for student_data in self.students.values():
            if course in student_data['courses']:
                scores.append(student_data['courses'][course])

        if scores:
            return sum(scores) / len(scores)
        return None

    def get_top_student(self):
        """
        Calculate every student's gpa with get_gpa method, and find the student with highest gpa
        :return: str, name of student whose gpa is highest
        """
        top_student = None
        highest_gpa = -1

        for name in self.students:
            gpa = self.get_gpa(name)
            if gpa is not None and gpa > highest_gpa:
                highest_gpa = gpa
                top_student = name

        return top_student