import sqlite3
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DatabaseProcessor:
    """
    This is a class for processing a database, supporting to create tables, insert data into the database, search for data based on name, and delete data from the database.
    """

    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name
        self.connection = None  # Initialize connection attribute

    def _connect(self):
        """
        Establish a database connection.
        """
        try:
            self.connection = sqlite3.connect(self.database_name)
            return self.connection.cursor()
        except sqlite3.Error as e:
            logging.error(f"Database connection error: {e}")
            raise  # Re-raise the exception to be handled by the calling function

    def _close(self):
        """
        Close the database connection.
        """
        if self.connection:
            try:
                self.connection.close()
                self.connection = None
            except sqlite3.Error as e:
                logging.error(f"Database closing error: {e}")


    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        """
        try:
            cursor = self._connect()
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY,
                    {key1} TEXT,
                    {key2} INTEGER
                )
            ''')
            self.connection.commit()
            logging.info(f"Table '{table_name}' created successfully.")
        except sqlite3.Error as e:
            logging.error(f"Error creating table '{table_name}': {e}")
            raise
        finally:
            self._close()


    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        """
        try:
            cursor = self._connect()
            for row in data:
                keys = ', '.join(row.keys())
                placeholders = ', '.join(['?'] * len(row))
                sql = f'''
                    INSERT INTO {table_name} ({keys})
                    VALUES ({placeholders})
                '''
                cursor.execute(sql, tuple(row.values()))
            self.connection.commit()
            logging.info(f"Data inserted successfully into table '{table_name}'.")
        except sqlite3.Error as e:
            logging.error(f"Error inserting data into table '{table_name}': {e}")
            raise
        finally:
            self._close()


    def search_database(self, table_name, search_column, search_value):
        """
        Search the specified table in the database for rows with a matching value in the specified column.
        :param table_name: str, the name of the table to search.
        :param search_column: str, the name of the column to search in.
        :param search_value: any, the value to search for.
        :return: list, a list of tuples representing the rows with matching values, if any;
                    otherwise, returns an empty list.
        """
        try:
            cursor = self._connect()
            sql = f'''
                SELECT * FROM {table_name} WHERE {search_column} = ?
            '''
            cursor.execute(sql, (search_value,))
            result = cursor.fetchall()
            logging.info(f"Search in table '{table_name}' for column '{search_column}' with value '{search_value}' successful.")
            return result if result else []  # Return empty list instead of None
        except sqlite3.Error as e:
            logging.error(f"Error searching in table '{table_name}': {e}")
            raise
        finally:
            self._close()


    def delete_from_database(self, table_name, delete_column, delete_value):
        """
        Delete rows from the specified table in the database where the specified column matches the given value.
        :param table_name: str, the name of the table to delete rows from.
        :param delete_column: str, the column to check for the value to delete.
        :param delete_value: any, the value to match for deletion.
        """
        try:
            cursor = self._connect()
            sql = f'''
                DELETE FROM {table_name} WHERE {delete_column} = ?
            '''
            cursor.execute(sql, (delete_value,))
            self.connection.commit()
            logging.info(f"Rows deleted from table '{table_name}' where column '{delete_column}' equals '{delete_value}'.")
        except sqlite3.Error as e:
            logging.error(f"Error deleting from table '{table_name}': {e}")
            raise
        finally:
            self._close()

    def read_table_to_dataframe(self, table_name):
        """
        Reads the entire table into a Pandas DataFrame.

        Args:
            table_name (str): The name of the table to read.

        Returns:
            pandas.DataFrame: A DataFrame containing the table data, or an empty DataFrame if an error occurs.
        """
        try:
            conn = sqlite3.connect(self.database_name)
            df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
            conn.close()
            logging.info(f"Table '{table_name}' read into DataFrame successfully.")
            return df
        except sqlite3.Error as e:
            logging.error(f"Error reading table '{table_name}' into DataFrame: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of error