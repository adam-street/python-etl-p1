# pip install
# pip install psycopg2-binary
import csv
import psycopg2
import sql
from config import pgsql_config


def query(query, values=None):
    # Connect to your postgres DB
    cursor = connect()

    # Execute a query
    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)
        # return query results
        return cursor.fetchall()


def parsing_csv(table):
    i = 0
    with open(table, newline='',
              encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            row.pop()
            if (i > 0):
                query(sql.insert_data, row)
                # print(row)
            i += 1


def parsing_csv2(table):
    i = 0
    with open(table, newline='',
              encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            if (i > 0):
                query(sql.insert_data2, row)
                # print(row)
            i += 1


def parsing_csv3(table):
    i = 0
    with open(table, newline='',
              encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            if (i > 0):
                query(sql.insert_data3, row)
                # print(row)
            i += 1


def parsing_csv4(table):
    i = 0
    with open(table, newline='',
              encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            # row.pop()
            if (i > 0):
                query(sql.insert_data4, row)
                # print(row)
            i += 1


def parsing_csv5(table):
    i = 0
    with open(table, newline='',
              encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            # row.pop()
            if (i > 0):
                query(sql.insert_data5, row)
                # print(row)
            i += 1


def parsing_csv6(table):
    i = 0
    with open(table, newline='',
              encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            # row.pop()
            if (i > 0):
                query(sql.insert_data6, row)
                # print(row)
            i += 1


def parsing_csv7(table):
    i = 0
    with open(table, newline='',
              encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            # row.pop()
            if (i > 0):
                query(sql.insert_data7, row)
                # print(row)
            i += 1


def parsing_csv8(table):
    i = 0
    with open(table, newline='',
              encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            # row.pop()
            if (i > 0):
                query(sql.insert_data8, row)
                # print(row)
            i += 1


def parsing_csv9(table):
    i = 0
    with open(table, newline='',
              encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            row.pop()
            if (i > 0):
                query(sql.insert_data9, row)
                # print(row)
            i += 1


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
