# pgsql.py

import psycopg2
from config import pgsql_config

def query(query, values=None):
    # Connect to your postgres DB
    cursor = connect()

    # Execute a query
    if (values):
        cursor.execute(query, values)
    else:
        cursor.execute(query)
        # return query results
        # return cursor.fetchall()

def connect():
    connection = psycopg2.connect(f"""
        host='{pgsql_config['host']}'
        dbname='{pgsql_config['dbname']}'
        user='{pgsql_config['user']}'
        password='{pgsql_config['password']}'
    """)

    # Configure connection
    connection.autocommit = True

    # Return connection cursor to perform database operations
    return connection.cursor()