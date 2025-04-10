class AssessmentSystem:
    """
    A class representing a student assessment system that supports adding students,
    adding course scores, calculating GPAs, and other functionalities for students and courses.
    """

    def __init__(self):
        """Initialize the assessment system with an empty students dictionary."""
        self.students = {}

    def add_student(self, name: str, grade: int, major: str) -> None:
        """
        Add a new student to the system.
        
        :param name: The name of the student.
        :param grade: The grade level of the student.
        :param major: The major field of study for the student.
        """
        self.students[name] = {
            'name': name,
            'grade': grade,
            'major': major,
            'courses': {}
        }

    def add_course_score(self, name: str, course: str, score: int) -> None:
        """
        Add a score for a specific course for a student.

        :param name: The name of the student.
        :param course: The course name.
        :param score: The score received in the course.
        """
        if name in self.students:
            self.students[name]['courses'][course] = score

    def get_gpa(self, name: str) -> float:
        """
        Calculate the GPA for a student.

        :param name: The name of the student.
        :return: The average score of the student's courses, or None if no courses exist.
        """
        if name not in self.students:
            return None
        
        courses = self.students[name]['courses']
        if not courses:
            return None
        
        return sum(courses.values()) / len(courses)

    def get_all_students_with_fail_course(self) -> list:
        """
        Get a list of all students who have any scores below 60.

        :return: A list of student names who have failed any course.
        """
        return [name for name, data in self.students.items() if any(score < 60 for score in data['courses'].values())]

    def get_course_average(self, course: str) -> float:
        """
        Calculate the average score for a specific course.

        :param course: The name of the course.
        :return: The average score for the course, or None if no scores exist for the course.
        """
        total_score, count = 0, 0
        
        for student in self.students.values():
            if course in student['courses']:
                total_score += student['courses'][course]
                count += 1
        
        return total_score / count if count > 0 else None

    def get_top_student(self) -> str:
        """
        Determine the student with the highest GPA.

        :return: The name of the student with the highest GPA, or None if no students exist.
        """
        highest_gpa, top_student = -1, None
        
        for name in self.students:
            gpa = self.get_gpa(name)
            if gpa is not None and gpa > highest_gpa:
                highest_gpa = gpa
                top_student = name
        
        return top_student