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

    def _execute_query(self, query, params=None):
        """
        Executes a SQL query.  Handles connection and cursor management.
        :param query: str, the SQL query to execute.
        :param params: tuple, optional parameters for the query.
        :return: list of tuples, the result of the query (if applicable).
        """
        conn = None
        cursor = None
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            if query.lower().startswith("select"):
                result = cursor.fetchall()
            else:
                result = None
            conn.commit()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            if conn:
                conn.rollback()
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def create_student_table(self):
        """
        Creates a "students" table in the database if it does not exist already.Fields include ID of type int, name of type str, age of type int, gender of type str, and grade of type int
        :return: None
        """
        query = """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                grade INTEGER NOT NULL
            )
        """
        self._execute_query(query)

    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: dict, a dictionary containing the student's information (name, age, gender, grade).
        :return: None
        """
        query = """
            INSERT INTO students (name, age, gender, grade)
            VALUES (?, ?, ?, ?)
        """
        params = (student_data['name'], student_data['age'], student_data['gender'], student_data['grade'])
        self._execute_query(query, params)

    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        """
        query = "SELECT * FROM students WHERE name=?"
        result = self._execute_query(query, (name,))
        return result

    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        :return: None
        """
        query = "DELETE FROM students WHERE name=?"
        self._execute_query(query, (name,))