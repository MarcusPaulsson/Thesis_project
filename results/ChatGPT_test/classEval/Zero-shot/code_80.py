class SQLQueryBuilder:
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """

    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        return query: str, the SQL query statement.
        """
        if columns == '*':
            columns_str = '*'
        else:
            columns_str = ', '.join(columns)

        if where:
            where_str = ' AND '.join([f"{key}='{value}'" for key, value in where.items()])
            return f"SELECT {columns_str} FROM {table} WHERE {where_str}"
        else:
            return f"SELECT {columns_str} FROM {table}"

    @staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement
        :return query: str, the SQL insert statement.
        """
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{value}'" for value in data.values()])
        return f"INSERT INTO {table} ({columns}) VALUES ({values})"

    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be executed with DELETE operation in database
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return query: str, the SQL delete statement.
        """
        if where:
            where_str = ' AND '.join([f"{key}='{value}'" for key, value in where.items()])
            return f"DELETE FROM {table} WHERE {where_str}"
        else:
            return f"DELETE FROM {table}"

    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be executed with UPDATE operation in database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        """
        set_str = ', '.join([f"{key}='{value}'" for key, value in data.items()])
        if where:
            where_str = ' AND '.join([f"{key}='{value}'" for key, value in where.items()])
            return f"UPDATE {table} SET {set_str} WHERE {where_str}"
        else:
            return f"UPDATE {table} SET {set_str}"