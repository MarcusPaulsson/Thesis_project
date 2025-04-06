import sqlite3

class StudentDatabaseProcessor:
    """
    This class performs database operations, including inserting, searching, and deleting student information.
    """

    def __init__(self, database_name):
        """
        Initializes the StudentDatabaseProcessor with the specified database name.
        :param database_name: str, the name of the SQLite database.
        """
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        self.create_student_table()

    def create_student_table(self):
        """
        Creates a "students" table in the database if it does not exist already.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                gender TEXT,
                grade INTEGER
            )
        ''')
        self.connection.commit()

    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: dict, a dictionary containing the student's information (name, age, gender, grade).
        """
        if not all(key in student_data for key in ['name', 'age', 'gender', 'grade']):
            raise ValueError("Missing student data fields.")
        
        self.cursor.execute('''
            INSERT INTO students (name, age, gender, grade) 
            VALUES (?, ?, ?, ?)''', 
            (student_data['name'], student_data['age'], student_data['gender'], student_data['grade'])
        )
        self.connection.commit()

    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        """
        self.cursor.execute('''
            SELECT * FROM students WHERE name = ?''', (name,))
        return self.cursor.fetchall()

    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        """
        self.cursor.execute('''
            DELETE FROM students WHERE name = ?''', (name,))
        self.connection.commit()

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()