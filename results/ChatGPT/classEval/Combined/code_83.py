import sqlite3
from contextlib import closing

class StudentDatabaseProcessor:
    """
    This class handles database operations for student information, 
    including inserting, searching, and deleting student records.
    """

    def __init__(self, database_name):
        """
        Initializes the StudentDatabaseProcessor with the specified database name.
        :param database_name: str, the name of the SQLite database.
        """
        self.database_name = database_name
        self.create_student_table()

    def create_student_table(self):
        """
        Creates a "students" table in the database if it does not exist already.
        :return: None
        """
        with sqlite3.connect(self.database_name) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        gender TEXT NOT NULL,
                        grade INTEGER NOT NULL
                    )
                ''')
                conn.commit()

    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: dict, a dictionary containing the student's information (name, age, gender, grade).
        :return: None
        """
        with sqlite3.connect(self.database_name) as conn:
            with closing(conn.cursor()) as cursor:
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
            with closing(conn.cursor()) as cursor:
                cursor.execute('SELECT * FROM students WHERE name=?', (name,))
                return cursor.fetchall()

    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        :return: None
        """
        with sqlite3.connect(self.database_name) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('DELETE FROM students WHERE name=?', (name,))
                conn.commit()