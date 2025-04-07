class AssessmentSystem:
    """
    This is a class for a student assessment system, which supports adding students, adding course scores, 
    calculating GPAs, and other functions for students and courses.
    """

    def __init__(self):
        """
        Initialize the students dictionary in the assessment system.
        """
        self.students = {}

    def add_student(self, name, grade, major):
        """
        Add a new student into the self.students dictionary.
        :param name: str, student name
        :param grade: int, student grade
        :param major: str, student major
        """
        if name not in self.students:
            self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        """
        Add score of a specific course for the student in self.students.
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
        :return: float or None, average grade if student exists and has courses, or None otherwise
        """
        if name in self.students:
            courses = self.students[name]['courses']
            if courses:
                return sum(courses.values()) / len(courses)
        return None

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score below 60.
        :return: list of str, student names
        """
        return [name for name, details in self.students.items() if any(score < 60 for score in details['courses'].values())]

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float or None, average score of the course if anyone has a score for this course, or None if nobody has records.
        """
        total_score = 0
        count = 0
        for details in self.students.values():
            if course in details['courses']:
                total_score += details['courses'][course]
                count += 1
        return total_score / count if count > 0 else None

    def get_top_student(self):
        """
        Calculate every student's GPA with get_gpa method, and find the student with the highest GPA.
        :return: str, name of student whose GPA is highest
        """
        top_student = None
        highest_gpa = -1
        for name in self.students:
            gpa = self.get_gpa(name)
            if gpa is not None and gpa > highest_gpa:
                highest_gpa = gpa
                top_student = name
        return top_student