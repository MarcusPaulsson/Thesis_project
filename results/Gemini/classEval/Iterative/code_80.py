import re
from typing import Dict, List, Union


class SQLQueryBuilder:
    """
    This class provides methods to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements.
    It includes basic sanitization to prevent SQL injection.
    """

    @staticmethod
    def _sanitize_value(value: Union[str, int, float]) -> str:
        """
        Sanitizes a value to prevent SQL injection.
        """
        if isinstance(value, (int, float)):
            return str(value)  # Numbers are generally safe
        if isinstance(value, str):
            # Escape single quotes by replacing them with two single quotes
            escaped_value = value.replace("'", "''")
            return f"'{escaped_value}'"
        return "NULL"  # Handle other types as NULL or raise an exception

    @staticmethod
    def select(table: str, columns: Union[str, List[str]] = '*', where: Dict[str, Union[str, int, float]] = None) -> str:
        """
        Generates a SELECT SQL statement.

        Args:
            table: The name of the table.
            columns: A string or a list of strings representing the columns to select.
                     Defaults to '*' (all columns).
            where: A dictionary representing the WHERE clause conditions.
                   Keys are column names, and values are the conditions.

        Returns:
            A string representing the SELECT SQL statement.

        Raises:
            ValueError: If the table or column names contain invalid characters.

        Example:
            >>> SQLQueryBuilder.select('users', columns=['id', 'name'], where={'age': 30, 'city': 'New York'})
            "SELECT id, name FROM users WHERE age=30 AND city='New York'"
        """
        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", table):
            raise ValueError("Invalid table name.")

        if isinstance(columns, list):
            for col in columns:
                if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", col):
                    raise ValueError("Invalid column name.")
            columns_str = ', '.join(columns)
        elif columns == '*':
            columns_str = '*'
        else:
            if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", columns):
                raise ValueError("Invalid column name.")
            columns_str = columns

        query = f"SELECT {columns_str} FROM {table}"

        if where:
            where_clauses = []
            for key, value in where.items():
                if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", key):
                    raise ValueError("Invalid column name in WHERE clause.")
                sanitized_value = SQLQueryBuilder._sanitize_value(value)
                where_clauses.append(f"{key}={sanitized_value}")
            query += " WHERE " + " AND ".join(where_clauses)

        return query

    @staticmethod
    def insert(table: str, data: Dict[str, Union[str, int, float]]) -> str:
        """
        Generates an INSERT SQL statement.

        Args:
            table: The name of the table.
            data: A dictionary representing the data to insert.
                  Keys are column names, and values are the data to insert.

        Returns:
            A string representing the INSERT SQL statement.

        Raises:
            ValueError: If the table or column names contain invalid characters.

        Example:
            >>> SQLQueryBuilder.insert('users', {'name': 'Alice', 'age': 25})
            "INSERT INTO users (name, age) VALUES ('Alice', 25)"
        """
        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", table):
            raise ValueError("Invalid table name.")

        columns = []
        values = []
        for key, value in data.items():
            if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", key):
                raise ValueError("Invalid column name in INSERT statement.")
            columns.append(key)
            sanitized_value = SQLQueryBuilder._sanitize_value(value)
            values.append(sanitized_value)

        columns_str = ', '.join(columns)
        values_str = ', '.join(values)

        query = f"INSERT INTO {table} ({columns_str}) VALUES ({values_str})"
        return query

    @staticmethod
    def delete(table: str, where: Dict[str, Union[str, int, float]] = None) -> str:
        """
        Generates a DELETE SQL statement.

        Args:
            table: The name of the table.
            where: A dictionary representing the WHERE clause conditions.
                   Keys are column names, and values are the conditions.

        Returns:
            A string representing the DELETE SQL statement.

        Raises:
            ValueError: If the table or column names contain invalid characters.

        Example:
            >>> SQLQueryBuilder.delete('users', where={'id': 123})
            "DELETE FROM users WHERE id=123"
        """
        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", table):
            raise ValueError("Invalid table name.")

        query = f"DELETE FROM {table}"

        if where:
            where_clauses = []
            for key, value in where.items():
                if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", key):
                    raise ValueError("Invalid column name in WHERE clause.")
                sanitized_value = SQLQueryBuilder._sanitize_value(value)
                where_clauses.append(f"{key}={sanitized_value}")
            query += " WHERE " + " AND ".join(where_clauses)

        return query

    @staticmethod
    def update(table: str, data: Dict[str, Union[str, int, float]], where: Dict[str, Union[str, int, float]] = None) -> str:
        """
        Generates an UPDATE SQL statement.

        Args:
            table: The name of the table.
            data: A dictionary representing the data to update.
                  Keys are column names, and values are the new values.
            where: A dictionary representing the WHERE clause conditions.
                   Keys are column names, and values are the conditions.

        Returns:
            A string representing the UPDATE SQL statement.

        Raises:
            ValueError: If the table or column names contain invalid characters.

        Example:
            >>> SQLQueryBuilder.update('users', data={'name': 'Bob'}, where={'id': 123})
            "UPDATE users SET name='Bob' WHERE id=123"
        """
        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", table):
            raise ValueError("Invalid table name.")

        set_clauses = []
        for key, value in data.items():
            if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", key):
                raise ValueError("Invalid column name in SET clause.")
            sanitized_value = SQLQueryBuilder._sanitize_value(value)
            set_clauses.append(f"{key}={sanitized_value}")
        set_str = ', '.join(set_clauses)

        query = f"UPDATE {table} SET {set_str}"

        if where:
            where_clauses = []
            for key, value in where.items():
                if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", key):
                    raise ValueError("Invalid column name in WHERE clause.")
                sanitized_value = SQLQueryBuilder._sanitize_value(value)
                where_clauses.append(f"{key}={sanitized_value}")
            query += " WHERE " + " AND ".join(where_clauses)

        return query