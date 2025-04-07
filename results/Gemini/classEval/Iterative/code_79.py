import re


class SQLGenerator:
    """
    This class generates SQL statements for common operations on a table, such as SELECT, INSERT, UPDATE, and DELETE.
    """

    def __init__(self, table_name):
        """
        Initialize the table name.
        :param table_name: str
        """
        if not isinstance(table_name, str):
            raise TypeError("Table name must be a string.")
        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", table_name):
            raise ValueError(
                "Invalid table name. Must start with a letter or underscore and contain only alphanumeric characters and underscores."
            )
        self.table_name = table_name

    def _sanitize_field(self, field):
        """Sanitizes a field name to prevent SQL injection."""
        if not isinstance(field, str):
            raise TypeError("Field name must be a string.")
        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", field):
            raise ValueError(
                "Invalid field name. Must start with a letter or underscore and contain only alphanumeric characters and underscores."
            )
        return field

    def _sanitize_value(self, value):
        """Sanitizes a value to prevent SQL injection."""
        if isinstance(value, str):
            return "'" + value.replace("'", "''") + "'"  # Escape single quotes
        elif isinstance(value, (int, float)):
            return str(value)
        elif value is None:
            return "NULL"
        else:
            raise TypeError(f"Unsupported value type: {type(value)}")

    def select(self, fields=None, condition=None):
        """
        Generates a SELECT SQL statement based on the specified fields and conditions.
        :param fields: list, optional. Default is None. The list of fields to be queried.
        :param condition: str, optional. Default is None. The condition expression for the query.
        :return: str. The generated SQL statement.
        """
        sql = "SELECT "
        if fields:
            if not isinstance(fields, list):
                raise TypeError("Fields must be a list.")
            sanitized_fields = [self._sanitize_field(field) for field in fields]
            sql += ", ".join(sanitized_fields)
        else:
            sql += "*"
        sql += " FROM " + self.table_name
        if condition:
            if not isinstance(condition, str):
                raise TypeError("Condition must be a string.")
            sql += " WHERE " + condition
        sql += ";"
        return sql

    def insert(self, data):
        """
        Generates an INSERT SQL statement based on the given data.
        :param data: dict. The data to be inserted, in dictionary form where keys are field names and values are field values.
        :return: str. The generated SQL statement.
        """
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary.")

        if not data:
            raise ValueError("Data dictionary cannot be empty.")

        fields = [self._sanitize_field(field) for field in data.keys()]
        values = [self._sanitize_value(value) for value in data.values()]

        sql = (
            f"INSERT INTO {self.table_name} ({', '.join(fields)}) VALUES ({', '.join(values)});"
        )
        return sql

    def update(self, data, condition):
        """
        Generates an UPDATE SQL statement based on the given data and condition.
        :param data: dict. The data to be updated, in dictionary form where keys are field names and values are new field values.
        :param condition: str. The condition expression for the update.
        :return: str. The generated SQL statement.
        """
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary.")

        if not isinstance(condition, str):
            raise TypeError("Condition must be a string.")

        updates = []
        for field, value in data.items():
            sanitized_field = self._sanitize_field(field)
            sanitized_value = self._sanitize_value(value)
            updates.append(f"{sanitized_field} = {sanitized_value}")

        if not updates:
            raise ValueError("Data dictionary cannot be empty.")

        sql = f"UPDATE {self.table_name} SET {', '.join(updates)} WHERE {condition};"
        return sql

    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :param condition: str. The condition expression for the delete.
        :return: str. The generated SQL statement.
        """
        if not isinstance(condition, str):
            raise TypeError("Condition must be a string.")

        sql = f"DELETE FROM {self.table_name} WHERE {condition};"
        return sql

    def select_female_under_age(self, age):
        """
        Generates a SQL statement to select females under a specified age.
        :param age: int. The specified age.
        :return: str. The generated SQL statement.
        """
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")

        sql = f"SELECT * FROM {self.table_name} WHERE age < {age} AND gender = 'female';"
        return sql

    def select_by_age_range(self, min_age, max_age):
        """
        Generates a SQL statement to select records within a specified age range.
        :param min_age: int. The minimum age.
        :param max_age: int. The maximum age.
        :return: str. The generated SQL statement.
        """
        if not isinstance(min_age, int) or not isinstance(max_age, int):
            raise TypeError("Min_age and max_age must be integers.")

        if min_age > max_age:
            raise ValueError("Min_age cannot be greater than max_age.")

        sql = f"SELECT * FROM {self.table_name} WHERE age BETWEEN {min_age} AND {max_age};"
        return sql