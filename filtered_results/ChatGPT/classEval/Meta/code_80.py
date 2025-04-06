class SQLQueryBuilder:
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """

    @staticmethod
    def select(table, columns='*', where=None):
        columns_str = ', '.join(columns) if isinstance(columns, list) else columns
        query = f"SELECT {columns_str} FROM {table}"
        if where:
            conditions = ' AND '.join([f"{key}='{value}'" for key, value in where.items()])
            query += f" WHERE {conditions}"
        return query

    @staticmethod
    def insert(table, data):
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{value}'" for value in data.values()])
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        return query

    @staticmethod
    def delete(table, where=None):
        query = f"DELETE FROM {table}"
        if where:
            conditions = ' AND '.join([f"{key}='{value}'" for key, value in where.items()])
            query += f" WHERE {conditions}"
        return query

    @staticmethod
    def update(table, data, where=None):
        set_clause = ', '.join([f"{key}='{value}'" for key, value in data.items()])
        query = f"UPDATE {table} SET {set_clause}"
        if where:
            conditions = ' AND '.join([f"{key}='{value}'" for key, value in where.items()])
            query += f" WHERE {conditions}"
        return query