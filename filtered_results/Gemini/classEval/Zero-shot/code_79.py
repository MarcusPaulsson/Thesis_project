class SQLGenerator:
    """
    This class generates SQL statements for common operations on a table, such as SELECT, INSERT, UPDATE, and DELETE.
    """

    def __init__(self, table_name):
        """
        Initialize the table name.
        :param table_name: str
        """
        self.table_name = table_name

    def select(self, fields=None, condition=None):
        """
        Generates a SELECT SQL statement based on the specified fields and conditions.
        :param fields: list, optional. Default is None. The list of fields to be queried.
        :param condition: str, optional. Default is None. The condition expression for the query.
        :return: str. The generated SQL statement.
        >>> sql = SQLGenerator('table1')
        >>> sql.select(['field1', 'field2'], 'filed3 = value1')
        'SELECT field1, field2 FROM table1 WHERE filed3 = value1;'
        """
        sql = "SELECT "
        if fields:
            sql += ", ".join(fields)
        else:
            sql += "*"
        sql += " FROM " + self.table_name
        if condition:
            sql += " WHERE " + condition
        sql += ";"
        return sql

    def insert(self, data):
        """
        Generates an INSERT SQL statement based on the given data.
        :param data: dict. The data to be inserted, in dictionary form where keys are field names and values are field values.
        :return: str. The generated SQL statement.
        >>> sql.insert({'key1': 'value1', 'key2': 'value2'})
        "INSERT INTO table1 (key1, key2) VALUES ('value1', 'value2');"
        """
        fields = ", ".join(data.keys())
        values = ", ".join("'" + str(v) + "'" for v in data.values())
        sql = "INSERT INTO " + self.table_name + " (" + fields + ") VALUES (" + values + ");"
        return sql


    def update(self, data, condition):
        """
        Generates an UPDATE SQL statement based on the given data and condition.
        :param data: dict. The data to be updated, in dictionary form where keys are field names and values are new field values.
        :param condition: str. The condition expression for the update.
        :return: str. The generated SQL statement.
        >>> sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
        "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
        """
        set_clause = ", ".join([f"{k} = '{v}'" for k, v in data.items()])
        sql = "UPDATE " + self.table_name + " SET " + set_clause + " WHERE " + condition + ";"
        return sql

    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :param condition: str. The condition expression for the delete.
        :return: str. The generated SQL statement.
        >>> sql.delete("field1 = value1")
        'DELETE FROM table1 WHERE field1 = value1;'
        """
        sql = "DELETE FROM " + self.table_name + " WHERE " + condition + ";"
        return sql

    def select_female_under_age(self, age):
        """
        Generates a SQL statement to select females under a specified age.
        :param age: int. The specified age.
        :return: str. The generated SQL statement.
        >>> sql.select_female_under_age(30)
        "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';"
        """
        sql = "SELECT * FROM " + self.table_name + " WHERE age < " + str(age) + " AND gender = 'female';"
        return sql

    def select_by_age_range(self, min_age, max_age):
        """
        Generates a SQL statement to select records within a specified age range.
        :param min_age: int. The minimum age.
        :param max_age: int. The maximum age.
        :return: str. The generated SQL statement.
        >>> sql.select_by_age_range(20, 30)
        'SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;'
        """
        sql = "SELECT * FROM " + self.table_name + " WHERE age BETWEEN " + str(min_age) + " AND " + str(max_age) + ";"
        return sql