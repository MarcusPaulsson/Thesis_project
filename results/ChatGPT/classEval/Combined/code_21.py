from datetime import datetime


class Classroom:
    """
    This class represents a classroom, capable of adding and removing courses,
    checking availability at a given time, and detecting conflicts when scheduling new courses.
    """

    def __init__(self, classroom_id):
        """
        Initialize the classroom management system.
        :param classroom_id: int, the ID of the classroom
        """
        self.id = classroom_id
        self.courses = []

    def add_course(self, course):
        """
        Add a course to the classroom if it doesn't conflict with existing courses.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        """
        if self.check_course_conflict(course):
            self.courses.append(course)

    def remove_course(self, course):
        """
        Remove a course from the classroom if it exists.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        """
        if course in self.courses:
            self.courses.remove(course)

    def is_free_at(self, check_time):
        """
        Check if the classroom is free at the given time.
        :param check_time: str, the time to be checked in '%H:%M' format
        :return: True if the classroom is free at check_time, False otherwise.
        """
        check_time = self.convert_to_time(check_time)
        return all(not self.is_time_conflicting(check_time, course) for course in self.courses)

    def check_course_conflict(self, new_course):
        """
        Check if the new course time conflicts with any existing courses.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: True if no conflict exists, False otherwise.
        """
        new_start = self.convert_to_time(new_course['start_time'])
        new_end = self.convert_to_time(new_course['end_time'])

        return all(not self.is_time_conflicting(new_start, new_end, course) for course in self.courses)

    @staticmethod
    def convert_to_time(time_str):
        """
        Convert time string in '%H:%M' format to a time object.
        :param time_str: str, time in '%H:%M' format
        :return: time object
        """
        return datetime.strptime(time_str, '%H:%M').time()

    @staticmethod
    def is_time_conflicting(start_time, end_time, course):
        """
        Determine if there is a time conflict.
        :param start_time: time object, start time of the new course
        :param end_time: time object, end time of the new course
        :param course: dict, existing course information
        :return: True if there's a conflict, False otherwise.
        """
        course_start = Classroom.convert_to_time(course['start_time'])
        course_end = Classroom.convert_to_time(course['end_time'])
        return not (end_time <= course_start or start_time >= course_end)