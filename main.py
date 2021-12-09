import sql
from pgsql import query
import csv
from pgsql import query_select

def parsing_csv1(file_name):
    query(sql.test_create1)
    with open(file_name, newline='', encoding='utf-8-sig') as f:
        j = 0
        reader = csv.reader(f)
        for row in reader:
            row.pop()
            if j > 0:
                query(sql.test_insert1, row)
            j += 1


def parsing_csv2(file_name):
    query(sql.test_create2)
    with open(file_name, newline='', encoding='utf-8-sig') as f:
        j = 0
        reader = csv.reader(f)
        for row in reader:
            if j > 0:
                query(sql.test_insert2, row)
            j += 1


def parsing_csv3(file_name):
    query(sql.test_create3)
    with open(file_name, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        row_count = sum(1 for row in reader)

    with open(file_name, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        j = 0
        for row in reader:
            if j > 0:
                if j < row_count - 1:
                    query(sql.test_insert3, row)
            j += 1


def parsing_csv4(file_name):
    query(sql.test_create4)
    with open(file_name, newline='', encoding='utf-8-sig') as f:
        j = 0
        reader = csv.reader(f)
        for row in reader:
            if j > 0:
                query(sql.test_insert4, row)
            j += 1


def parsing_csv5(file_name):
    query(sql.test_create5)
    with open(file_name, newline='', encoding='utf-8-sig') as f:
        j = 0
        reader = csv.reader(f)
        for row in reader:
            if j > 0:
                query(sql.test_insert5, row)
            j += 1


def parsing_csv6(file_name):
    query(sql.test_create6)
    with open(file_name, newline='', encoding='utf-8-sig') as f:
        j = 0
        reader = csv.reader(f)
        for row in reader:
            if j > 0:
                query(sql.test_insert6, row)
            j += 1


def parsing_csv7(file_name):
    query(sql.test_create7)
    with open(file_name, newline='', encoding='utf-8-sig') as f:
        j = 0
        reader = csv.reader(f)
        for row in reader:
            if j > 0:
                query(sql.test_insert7, row)
            j += 1

def parsing_csv8(file_name):
    query(sql.test_create8)
    with open(file_name, newline='', encoding='utf-8-sig') as f:
        j = 0
        reader = csv.reader(f)
        for row in reader:
            if j > 0:
                query(sql.test_insert8, row)
            j += 1


def parsing_csv9(file_name):
    query(sql.test_create9)
    with open(file_name, newline='', encoding='utf-8-sig') as f:
        j = 0
        reader = csv.reader(f)
        for row in reader:
            row.pop()
            if j > 0:
                query(sql.test_insert9, row)
            j += 1


if __name__ == '__main__':
    # insert data
    query(sql.create_schema)

    # parsing file
    parsing_csv1(".//datasets/hollywood-theatrical-market-synopsis-1995-to-2021/AnnualTicketSales.csv")
    parsing_csv2(".//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//HighestGrossers.csv")
    parsing_csv3(".//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//PopularCreativeTypes.csv")
    parsing_csv4(".//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//TopDistributors.csv")
    parsing_csv5(".//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//TopGenres.csv")
    parsing_csv6(".//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//TopGrossingRatings.csv")
    parsing_csv7(".//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//TopGrossingSources.csv")
    parsing_csv8(".//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//TopProductionMethods.csv")
    parsing_csv9(".//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//WideReleasesCount.csv")

    # select data
    results = query_select(sql.test_select);
    print("results: ", results)


