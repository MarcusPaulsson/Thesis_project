class AssessmentSystem:
    """
    A class representing a student assessment system that supports adding students, adding course scores, 
    calculating GPA, and various functions for managing students and courses.
    """

    def __init__(self):
        """Initialize the assessment system with an empty student dictionary."""
        self.students = {}

    def add_student(self, name: str, grade: int, major: str) -> None:
        """
        Add a new student to the assessment system.
        
        :param name: str, student name
        :param grade: int, student grade
        :param major: str, student major
        """
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name: str, course: str, score: int) -> None:
        """
        Add a score for a specific course for a student.
        
        :param name: str, student name
        :param course: str, course name
        :param score: int, course score
        """
        if name in self.students:
            self.students[name]['courses'][course] = score

    def get_gpa(self, name: str) -> float:
        """
        Calculate the GPA of a student.
        
        :param name: str, student name
        :return: float or None, average score or None if no courses exist
        """
        if name in self.students:
            courses = self.students[name]['courses']
            if courses:
                return sum(courses.values()) / len(courses)
        return None

    def get_all_students_with_fail_course(self) -> list:
        """
        Get a list of all students who have any score below 60.
        
        :return: list of str, student names
        """
        return [name for name, details in self.students.items() if any(score < 60 for score in details['courses'].values())]

    def get_course_average(self, course: str) -> float:
        """
        Calculate the average score of a specific course.
        
        :param course: str, course name
        :return: float or None, average score or None if no scores exist
        """
        total_score, count = 0, 0
        for details in self.students.values():
            if course in details['courses']:
                score = details['courses'][course]
                if score is not None:
                    total_score += score
                    count += 1
        return total_score / count if count > 0 else None

    def get_top_student(self) -> str:
        """
        Determine the student with the highest GPA.
        
        :return: str, name of the student with the highest GPA or None if no students exist
        """
        top_student, highest_gpa = None, -1
        for name in self.students:
            gpa = self.get_gpa(name)
            if gpa is not None and gpa > highest_gpa:
                highest_gpa = gpa
                top_student = name
        return top_student