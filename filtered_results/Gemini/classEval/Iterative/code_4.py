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
        if name in self.students:
            courses = self.students[name]['courses']
            if courses:
                total_score = sum(courses.values())
                return float(total_score) / len(courses)
        return None

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score blow 60
        :return: list of str ,student name
        """
        fail_students = []
        for name, student_info in self.students.items():
            for score in student_info['courses'].values():
                if score < 60:
                    fail_students.append(name)
                    break
        return fail_students

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
        course_scores = []
        for student_info in self.students.values():
            if course in student_info['courses']:
                score = student_info['courses'][course]
                course_scores.append(score)

        if course_scores:
            valid_scores = [score for score in course_scores if score is not None]
            if valid_scores:
                return float(sum(valid_scores)) / len(valid_scores)
        return None

    def get_top_student(self):
        """
        Calculate every student's gpa with get_gpa method, and find the student with highest gpa
        :return: str, name of student whose gpa is highest
        """
        top_student = None
        highest_gpa = None
        for name in self.students:
            gpa = self.get_gpa(name)
            if gpa is not None:
                if top_student is None or gpa > highest_gpa:
                    top_student = name
                    highest_gpa = gpa
        return top_student