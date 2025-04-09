class SQLQueryBuilder:
    """
    This class provides methods to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements.
    """

    @staticmethod
    def _build_where_clause(where):
        """
        Helper function to build the WHERE clause of an SQL query.

        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return: str, the WHERE clause.  Returns an empty string if `where` is None or empty.
        """
        if not where:
            return ""

        conditions = [f"{key}='{value}'" for key, value in where.items()]
        return " WHERE " + " AND ".join(conditions)

    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.

        :param table: str, the query table in database.
        :param columns: str or list of str, the columns to select.  Defaults to '*' (all columns).
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return: str, the SQL query statement.
        """
        col_str = ", ".join(columns) if isinstance(columns, list) else str(columns)
        where_clause = SQLQueryBuilder._build_where_clause(where)

        return f"SELECT {col_str} FROM {table}{where_clause}"

    @staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.

        :param table: str, the table to be inserted in database.
        :param data: dict, the key-value pairs to insert.
        :return: str, the SQL insert statement.
        """
        columns = ", ".join(data.keys())
        values = ", ".join([f"'{value}'" for value in data.values()])
        return f"INSERT INTO {table} ({columns}) VALUES ({values})"

    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.

        :param table: str, the table that will be executed with the DELETE operation.
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return: str, the SQL delete statement.
        """
        where_clause = SQLQueryBuilder._build_where_clause(where)
        return f"DELETE FROM {table}{where_clause}"

    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.

        :param table: str, the table that will be executed with the UPDATE operation.
        :param data: dict, the key-value pairs to update.
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return: str, the SQL update statement.
        """
        updates = ", ".join([f"{key}='{value}'" for key, value in data.items()])
        where_clause = SQLQueryBuilder._build_where_clause(where)
        return f"UPDATE {table} SET {updates}{where_clause}"