class SQLQueryBuilder:
    """
    This class provides methods to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements.
    """

    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str or str, ['col1', 'col2'] or '*'.
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return: str, the SQL query statement.
        """
        column_string = ', '.join(columns) if isinstance(columns, list) else columns
        query = f"SELECT {column_string} FROM {table}"
        if where:
            conditions = ' AND '.join([f"{key}='{value}'" for key, value in where.items()])
            query += f" WHERE {conditions}"
        return query

    @staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement.
        :return: str, the SQL insert statement.
        """
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{value}'" for value in data.values()])
        return f"INSERT INTO {table} ({columns}) VALUES ({values})"

    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be executed with DELETE operation in database.
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return: str, the SQL delete statement.
        """
        query = f"DELETE FROM {table}"
        if where:
            conditions = ' AND '.join([f"{key}='{value}'" for key, value in where.items()])
            query += f" WHERE {conditions}"
        return query

    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be executed with UPDATE operation in database.
        :param data: dict, the key and value in SQL update statement.
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return: str, the SQL update statement.
        """
        set_clause = ', '.join([f"{key}='{value}'" for key, value in data.items()])
        query = f"UPDATE {table} SET {set_clause}"
        if where:
            conditions = ' AND '.join([f"{key}='{value}'" for key, value in where.items()])
            query += f" WHERE {conditions}"
        return query