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
        """
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        """
        if course in self.courses:
            self.courses.remove(course)

    def is_free_at(self, check_time):
        """
        change the time format as '%H:%M' and check the time is free or not in the classroom.
        :param check_time: str, the time need to be checked
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        """
        try:
            check_time_dt = datetime.strptime(check_time, '%H:%M').time()
        except ValueError:
            return True  # Or raise an exception, depending on desired behavior

        for course in self.courses:
            try:
                start_time_dt = datetime.strptime(course['start_time'], '%H:%M').time()
                end_time_dt = datetime.strptime(course['end_time'], '%H:%M').time()
            except (ValueError, KeyError):
                continue  # Skip this course if time format is invalid

            if start_time_dt <= check_time_dt < end_time_dt:
                return False
        return True

    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        """
        try:
            new_start_time_dt = datetime.strptime(new_course['start_time'], '%H:%M').time()
            new_end_time_dt = datetime.strptime(new_course['end_time'], '%H:%M').time()
        except (ValueError, KeyError):
            return True  # Or handle the error as appropriate

        for course in self.courses:
            try:
                start_time_dt = datetime.strptime(course['start_time'], '%H:%M').time()
                end_time_dt = datetime.strptime(course['end_time'], '%H:%M').time()
            except (ValueError, KeyError):
                continue  # Skip this course if time format is invalid

            if not (new_end_time_dt <= start_time_dt or new_start_time_dt >= end_time_dt):
                return False
        return True