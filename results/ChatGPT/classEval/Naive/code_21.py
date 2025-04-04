from datetime import datetime

class Classroom:
    """
    This is a class representing a classroom, capable of adding and removing courses,
    checking availability at a given time, and detecting conflicts when scheduling new courses.
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
        :param check_time: str, the time need to be checked in '%H:%M' format
        :return: True if the check_time does not conflict with any course time, else False.
        """
        check_time = datetime.strptime(check_time, '%H:%M').time()
        for course in self.courses:
            start_time = datetime.strptime(course['start_time'], '%H:%M').time()
            end_time = datetime.strptime(course['end_time'], '%H:%M').time()
            if start_time <= check_time < end_time:
                return False
        return True

    def check_course_conflict(self, new_course):
        """
        Check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if there is a conflict, True otherwise.
        """
        new_start = datetime.strptime(new_course['start_time'], '%H:%M').time()
        new_end = datetime.strptime(new_course['end_time'], '%H:%M').time()
        
        for course in self.courses:
            start_time = datetime.strptime(course['start_time'], '%H:%M').time()
            end_time = datetime.strptime(course['end_time'], '%H:%M').time()
            if not (new_end <= start_time or new_start >= end_time):
                return False
        return True