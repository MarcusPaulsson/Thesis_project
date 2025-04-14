from datetime import datetime

class Classroom:
    """
    This is a class representing a classroom, capable of adding and removing courses, checking availability at a given time, and detecting conflicts when scheduling new courses.
    """

    TIME_FORMAT = '%H:%M'

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
        Check if the classroom is free at the given time.
        :param check_time: str, the time to check (format: HH:MM)
        :return: True if the classroom is free, False otherwise.
        """
        check_time_dt = datetime.strptime(check_time, self.TIME_FORMAT).time()
        for course in self.courses:
            start_time_dt = datetime.strptime(course['start_time'], self.TIME_FORMAT).time()
            end_time_dt = datetime.strptime(course['end_time'], self.TIME_FORMAT).time()
            if start_time_dt <= check_time_dt < end_time_dt:
                return False
        return True

    def check_course_conflict(self, new_course):
        """
        Check if the new course conflicts with any existing courses.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: True if there is no conflict, False otherwise.
        """
        new_start_time = datetime.strptime(new_course['start_time'], self.TIME_FORMAT).time()
        new_end_time = datetime.strptime(new_course['end_time'], self.TIME_FORMAT).time()

        for existing_course in self.courses:
            existing_start_time = datetime.strptime(existing_course['start_time'], self.TIME_FORMAT).time()
            existing_end_time = datetime.strptime(existing_course['end_time'], self.TIME_FORMAT).time()

            if not (new_end_time <= existing_start_time or new_start_time >= existing_end_time):
                return False

        return True