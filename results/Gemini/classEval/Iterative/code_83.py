import sqlite3

class StudentDatabaseProcessor:
    """
    This is a class with database operation, including inserting student information, searching for student information by name, and deleting student information by name.
    """

    def __init__(self, database_name):
        """
        Initializes the StudentDatabaseProcessor object with the specified database name.
        :param database_name: str, the name of the SQLite database.
        """
        self.database_name = database_name
        self.conn = None  # Initialize connection attribute

    def _connect(self):
        """
        Establishes a database connection.
        """
        try:
            self.conn = sqlite3.connect(self.database_name)
            return self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return None

    def _close(self):
        """
        Closes the database connection.
        """
        if self.conn:
            self.conn.close()
            self.conn = None

    def create_student_table(self):
        """
        Creates a "students" table in the database if it does not exist already.
        Fields include ID of type int, name of type str, age of type int, gender of type str, and grade of type int.
        :return: None
        """
        cursor = self._connect()
        if cursor:
            try:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER,
                        gender TEXT,
                        grade INTEGER
                    )
                """)
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Database error creating table: {e}")
            finally:
                self._close()

    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: dict, a dictionary containing the student's information (name, age, gender, grade).
               Must contain keys 'name', 'age', 'gender', and 'grade'.
        :return: None
        :raises ValueError: if student_data is missing required keys.
        """
        cursor = self._connect()
        if cursor:
            try:
                if not all(key in student_data for key in ('name', 'age', 'gender', 'grade')):
                    raise ValueError("Student data is missing required keys (name, age, gender, grade).")

                cursor.execute("""
                    INSERT INTO students (name, age, gender, grade)
                    VALUES (?, ?, ?, ?)
                """, (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Database error inserting student: {e}")
            except ValueError as e:
                print(f"Invalid input: {e}")
            finally:
                self._close()

    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.  Returns an empty list if no match is found or an error occurs.
        """
        cursor = self._connect()
        if cursor:
            try:
                cursor.execute("""
                    SELECT * FROM students WHERE name = ?
                """, (name,))
                result = cursor.fetchall()
                return result
            except sqlite3.Error as e:
                print(f"Database error searching for student: {e}")
                return []
            finally:
                self._close()
        else:
            return []

    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        :return: None
        """
        cursor = self._connect()
        if cursor:
            try:
                cursor.execute("""
                    DELETE FROM students WHERE name = ?
                """, (name,))
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Database error deleting student: {e}")
            finally:
                self._close()