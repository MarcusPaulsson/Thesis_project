import sqlite3

class StudentDatabaseProcessor:
    """
    This class handles database operations including inserting, searching, and deleting student information.
    """

    def __init__(self, database_name):
        """
        Initializes the StudentDatabaseProcessor object with the specified database name.
        :param database_name: str, the name of the SQLite database.
        """
        self.database_name = database_name
        self.create_student_table()

    def create_student_table(self):
        """
        Creates a "students" table in the database if it does not exist already.
        Fields include ID of type int, name of type str, age of type int, gender of type str, and grade of type int.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    age INTEGER NOT NULL CHECK(age > 0),
                    gender TEXT NOT NULL CHECK(gender IN ('Male', 'Female', 'Other')),
                    grade INTEGER NOT NULL CHECK(grade >= 0 AND grade <= 100)
                )
            ''')
            conn.commit()

    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: dict, a dictionary containing the student's information (name, age, gender, grade).
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (name, age, gender, grade)
                VALUES (?, ?, ?, ?)
            ''', (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
            conn.commit()

    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students WHERE name=?', (name,))
            return cursor.fetchall()

    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM students WHERE name=?', (name,))
            conn.commit()