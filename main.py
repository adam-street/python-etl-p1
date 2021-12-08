import sql
from pgsql import query
from pgsql import query_select
import csv


def parsing_csv():
    i = 0
    with open(".//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//PopularCreativeTypes.csv", newline='',
              encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            # row.pop()
            if i > 0:
                query(sql.test_insert, row)
            i += 1


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    # insert data
    query(sql.create_schema)

    query(sql.test_create)

    # parsing file

    parsing_csv()

    # select data
    results = query_select(sql.test_select);
    print("results: ", results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
