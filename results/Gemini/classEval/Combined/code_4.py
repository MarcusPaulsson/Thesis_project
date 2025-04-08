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
        """
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param course: str, course name
        :param score: int, course score
        """
        if name in self.students:
            self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this students have courses grade, return average grade(float)
                    or None otherwise
        """
        student = self.students.get(name)
        if not student or not student['courses']:
            return None

        scores = list(student['courses'].values())
        return sum(scores) / len(scores)

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score below 60
        :return: list of str, student name
        """
        failing_students = []
        for name, student_data in self.students.items():
            for score in student_data['courses'].values():
                if score < 60:
                    failing_students.append(name)
                    break  # Only add a student once, even if they fail multiple courses
        return failing_students

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
        scores = []
        for student_data in self.students.values():
            score = student_data['courses'].get(course)
            if score is not None:
                scores.append(score)

        if not scores:
            return None

        return sum(scores) / len(scores)

    def get_top_student(self):
        """
        Calculate every student's gpa with get_gpa method, and find the student with highest gpa
        :return: str, name of student whose gpa is highest
        """
        top_student = None
        highest_gpa = float('-inf')  # Initialize with negative infinity

        for name in self.students:
            gpa = self.get_gpa(name)
            if gpa is not None and gpa > highest_gpa:
                top_student = name
                highest_gpa = gpa

        return top_student