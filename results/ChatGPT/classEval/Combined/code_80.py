class SQLQueryBuilder:
    """
    This class provides methods to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements.
    """

    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.

        :param table: str, the query table in the database.
        :param columns: list of str, ['col1', 'col2'] or '*' for all columns.
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return: str, the SQL query statement.
        """
        columns_str = ', '.join(columns) if isinstance(columns, list) else columns
        query = f"SELECT {columns_str} FROM {table}"

        if where:
            where_clauses = [f"{key}='{value}'" for key, value in where.items()]
            query += " WHERE " + " AND ".join(where_clauses)

        return query

    @staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.

        :param table: str, the table to insert into.
        :param data: dict, the key and value for the SQL insert statement.
        :return: str, the SQL insert statement.
        """
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{value}'" for value in data.values())
        return f"INSERT INTO {table} ({columns}) VALUES ({values})"

    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.

        :param table: str, the table for the DELETE operation.
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return: str, the SQL delete statement.
        """
        query = f"DELETE FROM {table}"

        if where:
            where_clauses = [f"{key}='{value}'" for key, value in where.items()]
            query += " WHERE " + " AND ".join(where_clauses)

        return query

    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.

        :param table: str, the table for the UPDATE operation.
        :param data: dict, the key and value for the SQL update statement.
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return: str, the SQL update statement.
        """
        set_clauses = ', '.join(f"{key}='{value}'" for key, value in data.items())
        query = f"UPDATE {table} SET {set_clauses}"

        if where:
            where_clauses = [f"{key}='{value}'" for key, value in where.items()]
            query += " WHERE " + " AND ".join(where_clauses)

        return query