from datetime import datetime

class Classroom:
    """
    A class representing a classroom, capable of adding and removing courses,
    checking availability at a given time, and detecting conflicts when scheduling new courses.
    """

    def __init__(self, classroom_id):
        """
        Initialize the classroom management system.
        :param classroom_id: int, the id of the classroom
        """
        self.classroom_id = classroom_id
        self.courses = []

    def add_course(self, course):
        """
        Add a course to the classroom if it doesn't conflict with existing courses.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        """
        if not self.has_course(course) and self.is_schedule_available(course):
            self.courses.append(course)

    def remove_course(self, course):
        """
        Remove a course from the classroom.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        """
        if self.has_course(course):
            self.courses.remove(course)

    def is_free_at(self, check_time):
        """
        Check if the classroom is free at the given time.
        :param check_time: str, the time to check in 'HH:MM' format
        :return: True if the check_time does not conflict with any course time, False otherwise.
        """
        check_time = self._parse_time(check_time)
        return all(not self._is_time_conflicted(check_time, course) for course in self.courses)

    def is_schedule_available(self, new_course):
        """
        Check if a new course can be added without conflicting with existing courses.
        :param new_course: dict, information of the new course, including 'start_time', 'end_time' and 'name'
        :return: True if no conflict exists, False otherwise.
        """
        new_start = self._parse_time(new_course['start_time'])
        new_end = self._parse_time(new_course['end_time'])
        return all(self._is_non_conflicting(new_start, new_end, course) for course in self.courses)

    def has_course(self, course):
        """
        Check if a course exists in the classroom.
        :param course: dict, information of the course
        :return: True if the course exists, False otherwise.
        """
        return course in self.courses

    def _parse_time(self, time_str):
        """Convert time string to a datetime object."""
        return datetime.strptime(time_str, '%H:%M')

    def _is_time_conflicted(self, check_time, course):
        """Check if the check_time conflicts with the given course."""
        start_time = self._parse_time(course['start_time'])
        end_time = self._parse_time(course['end_time'])
        return start_time < check_time < end_time

    def _is_non_conflicting(self, new_start, new_end, course):
        """Check if the new course's time does not conflict with the existing course."""
        existing_start = self._parse_time(course['start_time'])
        existing_end = self._parse_time(course['end_time'])
        return new_end <= existing_start or new_start >= existing_end