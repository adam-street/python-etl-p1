import sql
from pgsql import query
import csv
import os
import pathlib

# insert_data() function
def insert_data(file_name, num):
    with open(f'{file_name}', newline='', encoding="utf-8-sig") as csvfile:
        wrc_reader = csv.reader(csvfile, delimiter=',')
        next(wrc_reader)  # skips over the header for every table
        for row in wrc_reader:
            if row[-1] == '':
                row.pop()
                if row[0] == '':
                    continue
                else:
                    query(eval(f'sql.insert_rows{num}'), row)  # insert row into table
                    print(row)  # print the row to the console
            else:
                if row[0] == '':
                    continue
                else:
                    query(eval(f'sql.insert_rows{num}'), row)  # insert row into table
                    print(row)  # print the row to the console


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # insert data
    # query(sql.test_insert, ["My Insert!"]);
    # query(sql.create_schema) # create a new scheme called petl1

    # Create Tables in petl1 schema
    query(sql.create_tables);

    # select data
    # results = query(sql.test_select);
    # print("results: ", results)


    directory = "datasets/hollywood-theatrical-market-synopsis-1995-to-2021"
    table_number = 1

    for file_name in sorted(os.listdir(directory)):
        extension = pathlib.Path(file_name).suffix
        if extension == ".csv":
            f = os.path.join(directory, file_name)
            if os.path.isfile(f):
                insert_data(f, table_number)
            table_number += 1
        else:
            continue


'''
    # Importing and parsing CSV files (Test)
    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/AnnualTicketSales.csv', newline='', encoding="utf-8-sig") as csvfile:
        wrc_reader = csv.reader(csvfile, delimiter=',')
        next(wrc_reader)
        for row in wrc_reader:
            row.pop()  # remove trailing comma on the ones with an extra column
            query(sql.insert_rows1, row)  # insert row into table
            print(row)  # print the row to the console

    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/HighestGrossers.csv', newline='', encoding="utf-8-sig") as csvfile:
        wrc_reader = csv.reader(csvfile)
        next(wrc_reader)
        for row in wrc_reader:
            query(sql.insert_rows2, row)  # insert row into table
            print(row)  # print the row to the console

    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/PopularCreativeTypes.csv', newline='',
              encoding="utf-8-sig") as csvfile:
        wrc_reader = csv.reader(csvfile)
        next(wrc_reader)
        for row in wrc_reader:
            if (row[0] == ''):
                print("")
            else:
                query(sql.insert_rows3, row)  # insert row into table
                print(row)  # print the row to the console

    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopDistributors.csv', newline='',
              encoding="utf-8-sig") as csvfile:
        wrc_reader = csv.reader(csvfile)
        next(wrc_reader)
        for row in wrc_reader:
            query(sql.insert_rows4, row)  # insert row into table
            print(row)  # print the row to the console

    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGenres.csv', newline='',
              encoding="utf-8-sig") as csvfile:
        wrc_reader = csv.reader(csvfile)
        next(wrc_reader)
        for row in wrc_reader:
            query(sql.insert_rows5, row)  # insert row into table
            print(row)  # print the row to the console

    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingRatings.csv', newline='',
              encoding="utf-8-sig") as csvfile:
        wrc_reader = csv.reader(csvfile)
        next(wrc_reader)
        for row in wrc_reader:
            query(sql.insert_rows6, row)  # insert row into table
            print(row)  # print the row to the console

    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingSources.csv', newline='',
              encoding="utf-8-sig") as csvfile:
        wrc_reader = csv.reader(csvfile)
        next(wrc_reader)
        for row in wrc_reader:
            query(sql.insert_rows7, row)  # insert row into table
            print(row)  # print the row to the console

    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopProductionMethods.csv', newline='',
              encoding="utf-8-sig") as csvfile:
        wrc_reader = csv.reader(csvfile)
        next(wrc_reader)
        for row in wrc_reader:
            query(sql.insert_rows8, row)  # insert row into table
            print(row)  # print the row to the console

    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/WideReleasesCount.csv', newline='',
              encoding="utf-8-sig") as csvfile:
        wrc_reader = csv.reader(csvfile, delimiter=',')
        next(wrc_reader)
        for row in wrc_reader:
            row.pop()  # remove t railing comma on the ones with an extra column
            query(sql.insert_rows9, row)  # insert row into table
            print(row)  # print the row to the console

'''


# See PyCharm help at https://www.jetbrains.com/help/pycharm/