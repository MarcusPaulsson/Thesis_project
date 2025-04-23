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
        if not table_name:
            raise ValueError("Table name cannot be empty.")
        self.table_name = table_name

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
            sql += ", ".join(fields)
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

        fields = ", ".join(data.keys())
        values = ", ".join(["'" + str(v) + "'" for v in data.values()])
        sql = "INSERT INTO " + self.table_name + " (" + fields + ") VALUES (" + values + ");"
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
        if not data:
            raise ValueError("Data dictionary cannot be empty.")
        if not isinstance(condition, str):
            raise TypeError("Condition must be a string.")
        if not condition:
            raise ValueError("Condition cannot be empty.")

        set_clause = ", ".join([f"{k} = '{v}'" for k, v in data.items()])
        sql = "UPDATE " + self.table_name + " SET " + set_clause + " WHERE " + condition + ";"
        return sql

    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :param condition: str. The condition expression for the delete.
        :return: str. The generated SQL statement.
        """
        if not isinstance(condition, str):
            raise TypeError("Condition must be a string.")
        if not condition:
            raise ValueError("Condition cannot be empty.")

        sql = "DELETE FROM " + self.table_name + " WHERE " + condition + ";"
        return sql

    def select_female_under_age(self, age):
        """
        Generates a SQL statement to select females under a specified age.
        :param age: int. The specified age.
        :return: str. The generated SQL statement.
        """
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")
        if age < 0:
            raise ValueError("Age cannot be negative.")

        sql = "SELECT * FROM " + self.table_name + " WHERE age < " + str(age) + " AND gender = 'female';"
        return sql

    def select_by_age_range(self, min_age, max_age):
        """
        Generates a SQL statement to select records within a specified age range.
        :param min_age: int. The minimum age.
        :param max_age: int. The maximum age.
        :return: str. The generated SQL statement.
        """
        if not isinstance(min_age, int) or not isinstance(max_age, int):
            raise TypeError("Ages must be integers.")
        if min_age < 0 or max_age < 0:
            raise ValueError("Ages cannot be negative.")
        if min_age > max_age:
            raise ValueError("Minimum age cannot be greater than maximum age.")

        sql = "SELECT * FROM " + self.table_name + " WHERE age BETWEEN " + str(min_age) + " AND " + str(max_age) + ";"
        return sql