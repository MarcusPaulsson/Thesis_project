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
        Check if the classroom is free at a given time.
        :param check_time: str, the time to check in 'HH:MM' format.
        :return: True if the classroom is free, False otherwise.
        """
        try:
            check_time_dt = datetime.strptime(check_time, '%H:%M').time()
        except ValueError:
            return False  # Invalid time format

        for course in self.courses:
            try:
                start_time_dt = datetime.strptime(course['start_time'], '%H:%M').time()
                end_time_dt = datetime.strptime(course['end_time'], '%H:%M').time()
            except (ValueError, KeyError):
                continue  # Skip courses with invalid time format or missing keys

            if start_time_dt <= check_time_dt < end_time_dt:
                return False
        return True

    def check_course_conflict(self, new_course):
        """
        Check if a new course conflicts with existing courses.
        :param new_course: dict, information of the new course, including 'start_time', 'end_time' and 'name'.
        :return: True if there is no conflict, False otherwise.
        """
        try:
            new_start_time_dt = datetime.strptime(new_course['start_time'], '%H:%M').time()
            new_end_time_dt = datetime.strptime(new_course['end_time'], '%H:%M').time()
        except (ValueError, KeyError):
            return False  # Invalid time format or missing keys

        for course in self.courses:
            try:
                start_time_dt = datetime.strptime(course['start_time'], '%H:%M').time()
                end_time_dt = datetime.strptime(course['end_time'], '%H:%M').time()
            except (ValueError, KeyError):
                continue  # Skip courses with invalid time format or missing keys

            if (new_start_time_dt < end_time_dt and new_end_time_dt > start_time_dt):
                return False
        return True