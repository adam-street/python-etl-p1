import sql
import csv
from pgsql import query

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    query(sql.create_schema, ["My Insert!"])
    # insert data
    # query(sql.test_insert_WRC)

    # select data
    # results = query(sql.test_select_WRC)
    # print("results: ", results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
with open("datasets/hollywood-theatrical-market-synopsis-1995-to-2021/AnnualTicketSales.csv",
          newline='', encoding='utf-8-sig') as a:
    reader = csv.reader(a, delimiter=',')
    i = 0
    for row in reader:
        row.pop()
        if i > 0:
            query(sql.test_insert_ATS, row)
        i += 1

with open("datasets/hollywood-theatrical-market-synopsis-1995-to-2021/HighestGrossers.csv",
          newline='', encoding='utf-8-sig') as a:
    reader = csv.reader(a, delimiter=',')
    i = 0
    for row in reader:
        if i > 0:
            query(sql.test_insert_HG, row)
        i += 1

with open("datasets/hollywood-theatrical-market-synopsis-1995-to-2021/PopularCreativeTypes.csv",
          newline='', encoding='utf-8-sig') as a:
    reader = csv.reader(a, delimiter=',')
    i = 0
    for row in reader:
        if i > 0 and row[0] != '':
            query(sql.test_insert_PCT, row)
        i += 1

with open("datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopDistributors.csv",
          newline='', encoding='utf-8-sig') as a:
    reader = csv.reader(a, delimiter=',')
    i = 0
    for row in reader:
        if i > 0:
            query(sql.test_insert_TD, row)
        i += 1

with open("datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGenres.csv",
          newline='', encoding='utf-8-sig') as a:
    reader = csv.reader(a, delimiter=',')
    i = 0
    for row in reader:
        if i > 0:
            query(sql.test_insert_TG, row)
        i += 1

with open("datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingRatings.csv",
          newline='', encoding='utf-8-sig') as a:
    reader = csv.reader(a, delimiter=',')
    i = 0
    for row in reader:
        if i > 0:
            query(sql.test_insert_TGR, row)
        i += 1

with open("datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingSources.csv",
          newline='', encoding='utf-8-sig') as a:
    reader = csv.reader(a, delimiter=',')
    i = 0
    for row in reader:
        if i > 0:
            query(sql.test_insert_TGS, row)
        i += 1

with open("datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopProductionMethods.csv",
          newline='', encoding='utf-8-sig') as a:
    reader = csv.reader(a, delimiter=',')
    i = 0
    for row in reader:
        if i > 0:
            query(sql.test_insert_TPM, row)
        i += 1

with open("datasets/hollywood-theatrical-market-synopsis-1995-to-2021/WideReleasesCount.csv",
          newline='', encoding='utf-8-sig') as a:
    reader = csv.reader(a, delimiter=',')
    i = 0
    for row in reader:
        row.pop()
        if i > 0:
            query(sql.test_insert_WRC, row)
        i += 1
