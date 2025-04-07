class SQLQueryBuilder:
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """

    @staticmethod
    def _build_where_clause(where):
        """Helper function to build the WHERE clause."""
        if not where:
            return ""
        conditions = []
        for key, value in where.items():
            conditions.append(f"{key}='{value}'")
        return " WHERE " + " AND ".join(conditions)

    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        return query: str, the SQL query statement.
        """
        query = "SELECT "
        if isinstance(columns, list):
            query += ", ".join(columns)
        else:
            query += str(columns)  # Ensure columns is converted to string
        query += " FROM " + table
        query += SQLQueryBuilder._build_where_clause(where)
        return query

    @staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement
        :return query: str, the SQL insert statement.
        """
        columns = ", ".join(data.keys())
        values = ", ".join([f"'{str(value)}'" for value in data.values()])  # Ensure values are converted to string
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        return query

    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with DELETE operation in database
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return query: str, the SQL delete statement.
        """
        query = f"DELETE FROM {table}"
        query += SQLQueryBuilder._build_where_clause(where)
        return query

    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with UPDATE operation in database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        """
        query = f"UPDATE {table} SET "
        updates = []
        for key, value in data.items():
            updates.append(f"{key}='{value}'")
        query += ", ".join(updates)
        query += SQLQueryBuilder._build_where_clause(where)
        return query