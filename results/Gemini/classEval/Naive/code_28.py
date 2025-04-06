import sqlite3
import pandas as pd

class DatabaseProcessor:
    """
    This is a class for processing a database, supporting to create tables, insert data into the database, search for data based on name, and delete data from the database.
    """


    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name


    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        >>> db.create_table('user', 'name', 'age')
        """
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()

            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    {key1} TEXT,
                    {key2} INTEGER
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()


    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        >>> db.insert_into_database('user', [
                {'name': 'John', 'age': 25},
                {'name': 'Alice', 'age': 30}
            ])
        """
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()

            for row in data:
                columns = ', '.join(row.keys())
                placeholders = ', '.join(['?'] * len(row))
                values = tuple(row.values())

                cursor.execute(f"""
                    INSERT INTO {table_name} ({columns})
                    VALUES ({placeholders})
                """, values)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()


    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        >>> db.search_database('user', 'John')
        [(1, 'John', 25)]
        """
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()

            cursor.execute(f"""
                SELECT * FROM {table_name}
                WHERE name = ?
            """, (name,))

            rows = cursor.fetchall()
            return rows if rows else None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            if conn:
                conn.close()


    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
        """
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()

            cursor.execute(f"""
                DELETE FROM {table_name}
                WHERE name = ?
            """, (name,))

            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()

if __name__ == '__main__':
    # Example Usage
    db = DatabaseProcessor('example.db')

    # Create a table
    db.create_table('users', 'name', 'age')

    # Insert data
    data_to_insert = [
        {'name': 'John', 'age': 25},
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 28}
    ]
    db.insert_into_database('users', data_to_insert)

    # Search for data
    search_result = db.search_database('users', 'John')
    print(f"Search result for 'John': {search_result}")

    # Delete data
    db.delete_from_database('users', 'John')

    # Search again to verify deletion
    search_result = db.search_database('users', 'John')
    print(f"Search result for 'John' after deletion: {search_result}")

    # Display the remaining data
    conn = sqlite3.connect('example.db')
    df = pd.read_sql_query("SELECT * FROM users", conn)
    conn.close()

    print("\nRemaining data in the 'users' table:")
    print(df)