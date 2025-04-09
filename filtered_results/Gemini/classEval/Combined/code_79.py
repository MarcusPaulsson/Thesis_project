class SQLGenerator:
    """
    This class generates SQL statements for common operations on a table, such as SELECT, INSERT, UPDATE, and DELETE.
    """

    def __init__(self, table_name):
        """
        Initialize the table name.

        Args:
            table_name (str): The name of the table.
        """
        if not isinstance(table_name, str):
            raise TypeError("table_name must be a string.")
        if not table_name:
            raise ValueError("table_name cannot be empty.")

        self.table_name = table_name

    def select(self, fields=None, condition=None):
        """
        Generates a SELECT SQL statement based on the specified fields and conditions.

        Args:
            fields (list, optional): The list of fields to be queried. Defaults to None (selects all fields).
            condition (str, optional): The condition expression for the query. Defaults to None (no condition).

        Returns:
            str: The generated SQL statement.

        Raises:
            TypeError: If fields is not None and not a list.
            TypeError: If condition is not None and not a string.

        Examples:
            >>> sql = SQLGenerator('table1')
            >>> sql.select(['field1', 'field2'], 'field3 = value1')
            'SELECT field1, field2 FROM table1 WHERE field3 = value1;'
        """
        if fields is not None and not isinstance(fields, list):
            raise TypeError("fields must be a list or None.")
        if condition is not None and not isinstance(condition, str):
            raise TypeError("condition must be a string or None.")

        field_string = "*"
        if fields:
            if not all(isinstance(field, str) for field in fields):
                raise ValueError("All fields must be strings.")
            field_string = ", ".join(fields)
        
        sql = f"SELECT {field_string} FROM {self.table_name}"

        if condition:
            sql += f" WHERE {condition}"

        sql += ";"
        return sql

    def insert(self, data):
        """
        Generates an INSERT SQL statement based on the given data.

        Args:
            data (dict): The data to be inserted, where keys are field names and values are field values.

        Returns:
            str: The generated SQL statement.

        Raises:
            TypeError: If data is not a dictionary.
            ValueError: If data is empty.

        Examples:
            >>> sql = SQLGenerator('table1')
            >>> sql.insert({'key1': 'value1', 'key2': 'value2'})
            "INSERT INTO table1 (key1, key2) VALUES ('value1', 'value2');"
        """
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary.")
        if not data:
            raise ValueError("data cannot be empty.")

        fields = ", ".join(data.keys())
        values = ", ".join([f"'{str(v)}'" for v in data.values()])  # Quote values
        sql = f"INSERT INTO {self.table_name} ({fields}) VALUES ({values});"
        return sql

    def update(self, data, condition):
        """
        Generates an UPDATE SQL statement based on the given data and condition.

        Args:
            data (dict): The data to be updated, where keys are field names and values are new field values.
            condition (str): The condition expression for the update.

        Returns:
            str: The generated SQL statement.

        Raises:
            TypeError: If data is not a dictionary.
            ValueError: If data is empty.
            TypeError: If condition is not a string.
            ValueError: If condition is empty.

        Examples:
            >>> sql = SQLGenerator('table1')
            >>> sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
            "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
        """
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary.")
        if not data:
            raise ValueError("data cannot be empty.")
        if not isinstance(condition, str):
            raise TypeError("condition must be a string.")
        if not condition:
            raise ValueError("condition cannot be empty.")

        updates = ", ".join([f"{k} = '{v}'" for k, v in data.items()])  # Quote values
        sql = f"UPDATE {self.table_name} SET {updates} WHERE {condition};"
        return sql

    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.

        Args:
            condition (str): The condition expression for the delete.

        Returns:
            str: The generated SQL statement.

        Raises:
            TypeError: If condition is not a string.
            ValueError: If condition is empty.

        Examples:
            >>> sql = SQLGenerator('table1')
            >>> sql.delete("field1 = value1")
            'DELETE FROM table1 WHERE field1 = value1;'
        """
        if not isinstance(condition, str):
            raise TypeError("condition must be a string.")
        if not condition:
            raise ValueError("condition cannot be empty.")

        sql = f"DELETE FROM {self.table_name} WHERE {condition};"
        return sql

    def select_female_under_age(self, age):
        """
        Generates a SQL statement to select females under a specified age.

        Args:
            age (int): The specified age.

        Returns:
            str: The generated SQL statement.

        Raises:
            TypeError: If age is not an integer.
            ValueError: If age is not a positive integer.

        Examples:
            >>> sql = SQLGenerator('table1')
            >>> sql.select_female_under_age(30)
            "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';"
        """
        if not isinstance(age, int):
            raise TypeError("age must be an integer.")
        if age <= 0:
            raise ValueError("age must be a positive integer.")

        sql = f"SELECT * FROM {self.table_name} WHERE age < {age} AND gender = 'female';"
        return sql

    def select_by_age_range(self, min_age, max_age):
        """
        Generates a SQL statement to select records within a specified age range.

        Args:
            min_age (int): The minimum age.
            max_age (int): The maximum age.

        Returns:
            str: The generated SQL statement.

        Raises:
            TypeError: If min_age is not an integer.
            TypeError: If max_age is not an integer.
            ValueError: If min_age is not a positive integer.
            ValueError: If max_age is not a positive integer.
            ValueError: If min_age is greater than max_age.

        Examples:
            >>> sql = SQLGenerator('table1')
            >>> sql.select_by_age_range(20, 30)
            'SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;'
        """
        if not isinstance(min_age, int):
            raise TypeError("min_age must be an integer.")
        if not isinstance(max_age, int):
            raise TypeError("max_age must be an integer.")
        if min_age <= 0:
            raise ValueError("min_age must be a positive integer.")
        if max_age <= 0:
            raise ValueError("max_age must be a positive integer.")
        if min_age > max_age:
            raise ValueError("min_age cannot be greater than max_age.")

        sql = f"SELECT * FROM {self.table_name} WHERE age BETWEEN {min_age} AND {max_age};"
        return sql