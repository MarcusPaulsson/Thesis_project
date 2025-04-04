class AssessmentSystem:
    """
    This is a class as a student assessment system, which supports add student, add course score, calculate GPA, and other functions for students and courses.
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
        :return: float or None
        """
        if name in self.students:
            scores = self.students[name]['courses'].values()
            if scores:
                return sum(scores) / len(scores)
        return None

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score below 60
        :return: list of str, student names
        """
        failing_students = []
        for student in self.students.values():
            if any(score < 60 for score in student['courses'].values()):
                failing_students.append(student['name'])
        return failing_students

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float or None
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
        highest_gpa = -1
        
        for student in self.students.values():
            gpa = self.get_gpa(student['name'])
            if gpa is not None and gpa > highest_gpa:
                highest_gpa = gpa
                top_student = student['name']
        
        return top_student