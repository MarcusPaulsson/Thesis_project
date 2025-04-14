class SQLQueryBuilder:
    """
    This class provides methods to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements.
    """

    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generates a SELECT SQL statement.

        :param table: str, the name of the table.
        :param columns: str or list of str, the columns to select.  Defaults to '*' (all columns).
        :param where: dict, the WHERE clause conditions.
        :return: str, the generated SQL query.
        """
        query = "SELECT "

        if isinstance(columns, list):
            query += ", ".join(columns)
        else:
            query += str(columns)  # Ensure columns is a string

        query += f" FROM {table}"

        if where:
            conditions = " AND ".join(f"{key}='{value}'" for key, value in where.items())
            query += f" WHERE {conditions}"

        return query

    @staticmethod
    def insert(table, data):
        """
        Generates an INSERT SQL statement.

        :param table: str, the name of the table.
        :param data: dict, the data to insert (column names and values).
        :return: str, the generated SQL query.
        """
        columns = ", ".join(data.keys())
        values = ", ".join([f"'{value}'" for value in data.values()])
        return f"INSERT INTO {table} ({columns}) VALUES ({values})"

    @staticmethod
    def delete(table, where=None):
        """
        Generates a DELETE SQL statement.

        :param table: str, the name of the table.
        :param where: dict, the WHERE clause conditions.
        :return: str, the generated SQL query.
        """
        query = f"DELETE FROM {table}"

        if where:
            conditions = " AND ".join(f"{key}='{value}'" for key, value in where.items())
            query += f" WHERE {conditions}"

        return query

    @staticmethod
    def update(table, data, where=None):
        """
        Generates an UPDATE SQL statement.

        :param table: str, the name of the table.
        :param data: dict, the data to update (column names and values).
        :param where: dict, the WHERE clause conditions.
        :return: str, the generated SQL query.
        """
        updates = ", ".join(f"{key}='{value}'" for key, value in data.items())
        query = f"UPDATE {table} SET {updates}"

        if where:
            conditions = " AND ".join(f"{key}='{value}'" for key, value in where.items())
            query += f" WHERE {conditions}"

        return query