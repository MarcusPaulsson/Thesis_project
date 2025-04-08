from datetime import datetime, time

class Classroom:
    """
    Represents a classroom and its scheduling functionalities.
    """

    def __init__(self, classroom_id: int):
        """
        Initializes a Classroom object.

        Args:
            classroom_id: The unique identifier for the classroom.
        """
        self.id = classroom_id
        self.courses = []  # List of courses scheduled in the classroom

    def add_course(self, course: dict):
        """
        Adds a course to the classroom schedule.

        Args:
            course: A dictionary containing course information, including 'name', 'start_time', and 'end_time'.
        """
        if not isinstance(course, dict):
            raise TypeError("Course must be a dictionary.")
        if 'name' not in course or 'start_time' not in course or 'end_time' not in course:
            raise ValueError("Course dictionary must contain 'name', 'start_time', and 'end_time' keys.")

        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course: dict):
        """
        Removes a course from the classroom schedule.

        Args:
            course: A dictionary containing course information to be removed.
        """
        if not isinstance(course, dict):
            raise TypeError("Course must be a dictionary.")

        if course in self.courses:
            self.courses.remove(course)

    def is_free_at(self, check_time: str) -> bool:
        """
        Checks if the classroom is free at a given time.

        Args:
            check_time: A string representing the time to check in 'HH:MM' format.

        Returns:
            True if the classroom is free at the given time, False otherwise.
        """
        try:
            check_time_dt = datetime.strptime(check_time, '%H:%M').time()
        except ValueError:
            raise ValueError("Invalid time format.  Use 'HH:MM'.")

        for course in self.courses:
            start_time = course['start_time']
            end_time = course['end_time']

            try:
                start_time_dt = datetime.strptime(start_time, '%H:%M').time()
                end_time_dt = datetime.strptime(end_time, '%H:%M').time()
            except ValueError:
                raise ValueError("Invalid time format in course schedule. Use 'HH:MM'.")

            if start_time_dt <= check_time_dt < end_time_dt:
                return False  # Classroom is occupied at this time
        return True  # Classroom is free

    def check_course_conflict(self, new_course: dict) -> bool:
        """
        Checks if a new course conflicts with the existing schedule.

        Args:
            new_course: A dictionary containing information about the new course.

        Returns:
            True if the new course does not conflict with the existing schedule, False otherwise.
        """
        if not isinstance(new_course, dict):
            raise TypeError("New course must be a dictionary.")

        try:
            new_start_time = datetime.strptime(new_course['start_time'], '%H:%M').time()
            new_end_time = datetime.strptime(new_course['end_time'], '%H:%M').time()
        except ValueError:
            raise ValueError("Invalid time format in new course. Use 'HH:MM'.")

        for existing_course in self.courses:
            existing_start_time = existing_course['start_time']
            existing_end_time = existing_course['end_time']

            try:
                existing_start_time_dt = datetime.strptime(existing_start_time, '%H:%M').time()
                existing_end_time_dt = datetime.strptime(existing_end_time, '%H:%M').time()
            except ValueError:
                raise ValueError("Invalid time format in existing course. Use 'HH:MM'.")

            if not (new_end_time <= existing_start_time_dt or new_start_time >= existing_end_time_dt):
                return False  # Conflict detected

        return True  # No conflict