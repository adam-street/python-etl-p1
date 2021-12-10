import sql
from pgsql import query
import csv
from pgsql import query_select

def parsing_csv(i,folder):
    file_name =[]
    print(i)
    if i == 0 or i == 8:
        if i == 0:
            file_name = folder + "//AnnualTicketSales.csv"
        if i == 8:
            file_name = folder + "//WideReleasesCount.csv"

        query(eval(f'sql.test_create_{i}'))
        with open(file_name, newline='', encoding='utf-8-sig') as f:
            j = 0
            reader = csv.reader(f)
            for row in reader:
                row.pop()
                if j > 0:
                    query(eval(f'sql.test_insert_{i}'), row)
            j += 1
        f.close()

    if i == 2:
        file_name = folder+"//PopularCreativeTypes.csv"
        query(eval(f'sql.test_create_{i}'))
        with open(file_name, newline='', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            row_count = sum(1 for row in reader)

        with open(file_name, newline='', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            j = 0
            for row in reader:
                if j > 0:
                    if j < row_count - 1:
                        query(eval(f'sql.test_insert_{i}'), row)
            j += 1
    else:
        if i == 3:
            file_name = folder+"//TopDistributors.csv"
            query(eval(f'sql.test_create_{i}'))
        if i == 1:
            file_name = folder+"//HighestGrossers.csv"
            query(eval(f'sql.test_create_{i}'))
        if i == 4:
            file_name = folder+"//TopGenres.csv"
            query(eval(f'sql.test_create_{i}'))
        if i == 5:
            file_name = folder+"//TopGrossingRatings.csv"
            query(eval(f'sql.test_create_{i}'))
        if i == 6:
            file_name = folder+"//TopGrossingSources.csv"
            query(eval(f'sql.test_create_{i}'))
        if i == 7:
            file_name = folder+"//TopProductionMethods.csv"
            query(eval(f'sql.test_create_{i}'))

    with open(file_name, newline='', encoding='utf-8-sig') as f:
        j = 0
        reader = csv.reader(f)
        for row in reader:
            if j > 0:
                query(eval(f'sql.test_insert_{i}'), row)
        j += 1

if __name__ == '__main__':
    # insert data
    query(sql.create_schema)

    # parsing file
    for i in range(0,9):
        print(i)
        parsing_csv(i,".//datasets//hollywood-theatrical-market-synopsis-1995-to-2021")

    # select data
    results = query_select(sql.test_select);
    print("results: ", results)


