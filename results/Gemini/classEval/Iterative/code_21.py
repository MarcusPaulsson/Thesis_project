from datetime import datetime, time

class Classroom:
    """
    Represents a classroom with scheduling functionalities.
    """

    def __init__(self, classroom_id: int):
        """
        Initializes a Classroom object.

        Args:
            classroom_id: The unique identifier for the classroom.
        """
        if not isinstance(classroom_id, int):
            raise TypeError("classroom_id must be an integer.")
        if classroom_id <= 0:
            raise ValueError("classroom_id must be a positive integer.")

        self.id = classroom_id
        self.courses = []  # List of courses, each a dictionary

    def add_course(self, course: dict):
        """
        Adds a course to the classroom schedule.

        Args:
            course: A dictionary containing course information, including 'name', 'start_time', and 'end_time'.
                'start_time' and 'end_time' should be strings in 'HH:MM' format.

        Raises:
            TypeError: If course is not a dictionary or if start/end times are not strings.
            ValueError: If start/end times are not in the correct format or if the course already exists.
        """
        if not isinstance(course, dict):
            raise TypeError("course must be a dictionary.")
        if not all(key in course for key in ('name', 'start_time', 'end_time')):
            raise ValueError("course dictionary must contain 'name', 'start_time', and 'end_time' keys.")
        if not isinstance(course['start_time'], str) or not isinstance(course['end_time'], str):
            raise TypeError("start_time and end_time must be strings.")

        try:
            datetime.strptime(course['start_time'], '%H:%M').time()
            datetime.strptime(course['end_time'], '%H:%M').time()
        except ValueError:
            raise ValueError("start_time and end_time must be in 'HH:MM' format.")

        if course in self.courses:
             raise ValueError("Course already exists in the classroom schedule.")

        self.courses.append(course)

    def remove_course(self, course: dict):
        """
        Removes a course from the classroom schedule.

        Args:
            course: A dictionary representing the course to remove. Must match an existing course exactly.

        Raises:
            TypeError: If course is not a dictionary.
            ValueError: If the course does not exist in the classroom schedule.
        """
        if not isinstance(course, dict):
            raise TypeError("course must be a dictionary.")

        if course not in self.courses:
            raise ValueError("Course not found in the classroom schedule.")

        self.courses.remove(course)

    def is_free_at(self, check_time: str) -> bool:
        """
        Checks if the classroom is free at a given time.

        Args:
            check_time: A string representing the time to check in 'HH:MM' format.

        Returns:
            True if the classroom is free at the given time, False otherwise.

        Raises:
            TypeError: If check_time is not a string.
            ValueError: If check_time is not in the correct format.
        """
        if not isinstance(check_time, str):
            raise TypeError("check_time must be a string.")

        try:
            check_time_obj = datetime.strptime(check_time, '%H:%M').time()
        except ValueError:
            raise ValueError("check_time must be in 'HH:MM' format.")

        for course in self.courses:
            start_time_obj = datetime.strptime(course['start_time'], '%H:%M').time()
            end_time_obj = datetime.strptime(course['end_time'], '%H:%M').time()

            if start_time_obj <= check_time_obj < end_time_obj:
                return False  # Classroom is occupied

        return True  # Classroom is free

    def check_course_conflict(self, new_course: dict) -> bool:
        """
        Checks if a new course conflicts with any existing courses in the classroom.

        Args:
            new_course: A dictionary representing the new course to check for conflicts. Must contain 'start_time' and 'end_time'.

        Returns:
            True if the new course does not conflict with any existing courses, False otherwise.

        Raises:
            TypeError: If new_course is not a dictionary or if start/end times are not strings.
            ValueError: If start/end times are not in the correct format.
        """
        if not isinstance(new_course, dict):
            raise TypeError("new_course must be a dictionary.")
        if not all(key in new_course for key in ('start_time', 'end_time')):
            raise ValueError("new_course dictionary must contain 'start_time' and 'end_time' keys.")

        if not isinstance(new_course['start_time'], str) or not isinstance(new_course['end_time'], str):
            raise TypeError("start_time and end_time must be strings.")

        try:
            new_start_time_obj = datetime.strptime(new_course['start_time'], '%H:%M').time()
            new_end_time_obj = datetime.strptime(new_course['end_time'], '%H:%M').time()
        except ValueError:
            raise ValueError("start_time and end_time must be in 'HH:MM' format.")

        for course in self.courses:
            start_time_obj = datetime.strptime(course['start_time'], '%H:%M').time()
            end_time_obj = datetime.strptime(course['end_time'], '%H:%M').time()

            if not (new_end_time_obj <= start_time_obj or new_start_time_obj >= end_time_obj):
                return False  # Conflict detected

        return True  # No conflict