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
        student_data = self.students.get(name)
        if not student_data or not student_data['courses']:
            return None

        courses = student_data['courses']
        total_score = sum(courses.values())
        return float(total_score) / len(courses)

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score blow 60
        :return: list of str ,student name
        """
        failed_students = []
        for name, student_data in self.students.items():
            for score in student_data['courses'].values():
                if score < 60:
                    failed_students.append(name)
                    break  # Only add the student once if they have multiple failing courses
        return failed_students

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
        total_score = 0
        student_count = 0
        for student_data in self.students.values():
            score = student_data['courses'].get(course)
            if score is not None:
                total_score += score
                student_count += 1

        if student_count > 0:
            return float(total_score) / student_count
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