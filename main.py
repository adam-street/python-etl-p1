import sql
import csv
from pgsql import query, parsing_csv, parsing_csv2, parsing_csv3, parsing_csv4, parsing_csv5, parsing_csv6, \
    parsing_csv7, parsing_csv8, parsing_csv9

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # insert data
    #    query(sql.test_insert, ["My Insert!"])

    # select data
    #    results = query(sql.test_select)
    #    print("results: ", results)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

    # result = query(sql.test)
    # print("results: ", result)

    # calls to sql.py to create schema
    query(sql.create_schema, [""])

    # calls to sql.py to create annual ticket sales table
    query(sql.create_table, [""])

    parsing_csv('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/AnnualTicketSales.csv')

    parsing_csv2('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/HighestGrossers.csv')

    parsing_csv3('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/PopularCreativeTypes.csv')

    parsing_csv4('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopDistributors.csv')

    parsing_csv5('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGenres.csv')

    parsing_csv6('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingRatings.csv')

    parsing_csv7('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingSources.csv')

    parsing_csv8('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopProductionMethods.csv')

    parsing_csv9('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/WideReleasesCount.csv')