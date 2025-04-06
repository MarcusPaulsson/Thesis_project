class AssessmentSystem:
    """
    This is a class representing a student assessment system, which supports adding students, 
    adding course scores, calculating GPA, and other functions for students and courses.
    """

    def __init__(self):
        """
        Initialize the students dictionary in the assessment system.
        """
        self.students = {}

    def add_student(self, name, grade, major):
        """
        Add a new student to the self.students dictionary.
        
        :param name: str, student name
        :param grade: int, student grade
        :param major: str, student major
        """
        if name in self.students:
            raise ValueError(f"Student '{name}' already exists.")
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        """
        Add the score of a specific course for a student in self.students.
        
        :param name: str, student name
        :param course: str, course name
        :param score: int, course score
        """
        if name not in self.students:
            raise ValueError(f"Student '{name}' does not exist.")
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100.")
        self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        """
        Get the average grade of one student.
        
        :param name: str, student name
        :return: float or None, average grade if student has courses, otherwise None
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
        return [name for name, data in self.students.items() if any(score < 60 for score in data['courses'].values())]

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        
        :param course: str, course name
        :return: float or None, average score of this course if anyone has a score, otherwise None
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
        Calculate every student's GPA with the get_gpa method, and find the student with the highest GPA.
        
        :return: str, name of the student whose GPA is highest
        """
        top_student = None
        highest_gpa = -1
        for student in self.students:
            gpa = self.get_gpa(student)
            if gpa is not None and gpa > highest_gpa:
                highest_gpa = gpa
                top_student = student
        return top_student