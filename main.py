import sql
from pgsql import query
import csv



if __name__ == '__main__':

    # query(sql.create_schema)
    query(sql.annual_ticket_sales_table, [""])
    query(sql.highest_grossers_table, [""])
    query(sql.popular_creative_types_table, [""])
    query(sql.top_distributors_table, [""])
    query(sql.top_genres_table, [""])
    query(sql.top_grossing_ratings_table, [""])
    query(sql.top_grossing_sources_table, [""])
    query(sql.top_production_methods_table, [""])
    query(sql.wide_releases_count_table, [""])


    # select data
    # results = query(sql.test_select);
    #print("results: ", results)

    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/AnnualTicketSales.csv',
              newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            row.pop()
            if i > 0:
                query(sql.insert_row1, row)
            i += 1

    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/HighestGrossers.csv',
              newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            # row.pop()
            if i > 0:
                query(sql.insert_row2, row)
            i += 1

    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/PopularCreativeTypes.csv',
            newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            #row.pop()
            if i > 0:
                query(sql.insert_row3, row)
            i +=1

with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopDistributors.csv',
       newline='', encoding='utf-8-sig') as csvfile:
   reader = csv.reader(csvfile)
   i = 0
   for row in reader:
       #row.pop()
       if i > 0:
           query(sql.insert_row4, row)
       i +=1

with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGenres.csv',
       newline='', encoding='utf-8-sig') as csvfile:
   reader = csv.reader(csvfile)
   i = 0
   for row in reader:
       #row.pop()
       if i > 0:
           query(sql.insert_row5, row)
       i +=1

with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingRatings.csv',
       newline='', encoding='utf-8-sig') as csvfile:
   reader = csv.reader(csvfile)
   i = 0
   for row in reader:
       #row.pop()
       if i > 0:
           query(sql.insert_row6, row)
       i +=1

with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingSources.csv',
       newline='', encoding='utf-8-sig') as csvfile:
   reader = csv.reader(csvfile)
   i = 0
   for row in reader:
       #row.pop()
       if i > 0:
           query(sql.insert_row7, row)
       i +=1

with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopProductionMethods.csv',
       newline='', encoding='utf-8-sig') as csvfile:
   reader = csv.reader(csvfile)
   i = 0
   for row in reader:
       #row.pop()
       if i > 0:
           query(sql.insert_row8, row)
       i +=1

with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/WideReleasesCount.csv',
       newline='', encoding='utf-8-sig') as csvfile:
   reader = csv.reader(csvfile)
   i = 0
   for row in reader:
       row.pop()
       if i > 0:
           query(sql.insert_row9, row)
       i +=1
