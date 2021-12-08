# Python ETL Project
# 12.07.21
# Taylor Bell

import sql
from pgsql import query
import csv
import os
import pathlib

# insert_data() function
def insert_data(file_name, num):
    with open(f'{file_name}', newline='', encoding="utf-8-sig") as csvfile:  # open given file
        wrc_reader = csv.reader(csvfile, delimiter=',')  # red file
        next(wrc_reader)  # skips over the header for every table
        for row in wrc_reader:  # iterate through all rows in each table
            if row[-1] == '':  # check to see if the end column is blank, if so, remove it with pop()
                row.pop()
                if row[0] == '':  # check to see if the row starts with a blank, if so, skip it
                    continue
                else:
                    query(eval(f'sql.insert_rows{num}'), row)  # insert row into table
                    print(row)  # print the row to the console
            else:
                if row[0] == '':  # check to see if the row starts with a blank, if so, skip it
                    continue
                else:
                    query(eval(f'sql.insert_rows{num}'), row)  # insert row into table
                    print(row)  # print the row to the console


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Drop and Create petl1 Schema and its Tables
    query(sql.create_tables);

    # Define the file directory
    directory = "datasets/hollywood-theatrical-market-synopsis-1995-to-2021"
    table_number = 1  # create a number to keep track of files / tables

    # iterate through all files in the directory
    for file_name in sorted(os.listdir(directory)):  # pull all files from directory, and sort
        extension = pathlib.Path(file_name).suffix
        if extension == ".csv":  # check if the file is a .csv file
            f = os.path.join(directory, file_name)  # join directory path and file name
            if os.path.isfile(f):  # check to make sure the file is a valid file
                insert_data(f, table_number)  # calls insert_data function
            table_number += 1  # increment table_number
        else:
            continue