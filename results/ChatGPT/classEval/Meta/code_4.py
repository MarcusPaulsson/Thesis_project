class AssessmentSystem:
    """
    This is a class as a student assessment system, which supports adding a student, adding course scores, calculating GPA, and other functions for students and courses.
    """

    def __init__(self):
        """
        Initialize the students dict in the assessment system.
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
        Add score of a specific course for a student in self.students
        :param name: str, student name
        :param course: str, course name
        :param score: int, course score
        """
        if name in self.students:
            self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        """
        Get the average grade of one student.
        :param name: str, student name
        :return: if name is in students and this student has course grades, return average grade(float)
                or None otherwise
        """
        if name not in self.students or not self.students[name]['courses']:
            return None
        total_score = sum(self.students[name]['courses'].values())
        return total_score / len(self.students[name]['courses'])

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score below 60
        :return: list of str, student names
        """
        return [name for name, data in self.students.items() if any(score < 60 for score in data['courses'].values())]

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone has score of this course, or None if nobody has records.
        """
        total_score = 0
        count = 0
        for student in self.students.values():
            if course in student['courses']:
                total_score += student['courses'][course]
                count += 1
        return total_score / count if count > 0 else None

    def get_top_student(self):
        """
        Calculate every student's GPA with get_gpa method, and find the student with highest GPA
        :return: str, name of student whose GPA is highest
        """
        top_student = None
        top_gpa = -1
        for name in self.students:
            gpa = self.get_gpa(name)
            if gpa is not None and gpa > top_gpa:
                top_gpa = gpa
                top_student = name
        return top_student