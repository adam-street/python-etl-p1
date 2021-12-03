import psycopg2
from config import pgsql_config

def query(query):
    # Connect to your postgres DB
    cursor = connect()

    # Execute a query
    cursor.execute(query)

    # return query results
    return cursor.fetchall()

def connect():
    connection = psycopg2.connect(f"""
        host='{pgsql_config['host']}'
        dbname='{pgsql_config['dbname']}'
        user='{pgsql_config['user']}'
        password='{pgsql_config['password']}'
    """)

    # Return connection cursor to perform database operations
    return connection.cursor()