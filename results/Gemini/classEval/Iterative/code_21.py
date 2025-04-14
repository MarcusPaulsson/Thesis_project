from datetime import datetime

class Classroom:
    """
    This is a class representing a classroom, capable of adding and removing courses, checking availability at a given time, and detecting conflicts when scheduling new courses.
    """

    def __init__(self, id):
        """
        Initialize the classroom management system.
        :param id: int, the id of classroom
        """
        self.id = id
        self.courses = []

    def add_course(self, course):
        """
        Add course to self.courses list if the course wasn't in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """
        if course in self.courses:
            self.courses.remove(course)

    def is_free_at(self, check_time):
        """
        change the time format as '%H:%M' and check the time is free or not in the classroom.
        :param check_time: str, the time need to be checked
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.is_free_at('10:00')
        True
        >>> classroom.is_free_at('9:00')
        False
        """
        try:
            check_time_dt = datetime.strptime(check_time, '%H:%M').time()
        except ValueError:
            return False  # Handle invalid time format

        for course in self.courses:
            try:
                start_time_dt = datetime.strptime(course['start_time'], '%H:%M').time()
                end_time_dt = datetime.strptime(course['end_time'], '%H:%M').time()
            except (ValueError, KeyError):
                continue # Skip courses with invalid time format or missing keys

            if start_time_dt <= check_time_dt < end_time_dt:
                return False
        return True

    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})
        False
        """
        try:
            new_start_time = datetime.strptime(new_course['start_time'], '%H:%M').time()
            new_end_time = datetime.strptime(new_course['end_time'], '%H:%M').time()
        except (ValueError, KeyError):
            return True  # Consider no conflict if new course has invalid time

        for course in self.courses:
            try:
                existing_start_time = datetime.strptime(course['start_time'], '%H:%M').time()
                existing_end_time = datetime.strptime(course['end_time'], '%H:%M').time()
            except (ValueError, KeyError):
                continue # Skip courses with invalid time format or missing keys

            if not (new_end_time <= existing_start_time or new_start_time >= existing_end_time):
                return False

        return True