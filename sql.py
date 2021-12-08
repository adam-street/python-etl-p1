# test_select = ('''
#  SELECT *
#  FROM public.test_table;
# ''')

# test_insert = ('''
#  INSERT INTO public.test_table
#  VALUES(%s);
# ''')


# test = ('''
#    SELECT *
#    FROM public.staff
#    LIMIT 10;
# ''')


create_schema = ('''
CREATE SCHEMA IF NOT EXISTS petl1
''')

create_table = ('''
    CREATE TABLE IF NOT EXISTS petl1.annual_ticket_sales (
        YEAR TEXT NOT NULL,
        TICKETS_SOLD TEXT NOT NULL,
        TOTAL_BOX_OFFICE TEXT NOT NULL,
        TOTAL_INFLATION_ADJUSTED_BOX_OFFICE TEXT NOT NULL,
        AVERAGE_TICKET_PRICE TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.highest_grossers (
        YEAR TEXT NOT NULL,
        MOVIE TEXT NOT NULL,
        GENRE TEXT NOT NULL,
        MPAA_RATING TEXT NOT NULL,
        DISTRIBUTOR TEXT NOT NULL,
        TOTAL_FOR_YEAR TEXT NOT NULL,
        TOTAL_IN_2019_DOLLARS TEXT NOT NULL,
        TICKETS_SOLD TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.popular_creative_types (
        RANK TEXT NOT NULL,
        CREATIVE_TYPES TEXT NOT NULL,
        MOVIES TEXT NOT NULL,
        TOTAL_GROSS TEXT NOT NULL,
        AVERAGE_GROSS TEXT NOT NULL,
        MARKET_SHARE TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.top_distributors (
        RANK TEXT NOT NULL,
        DISTRIBUTERS TEXT NOT NULL,
        MOVIES TEXT NOT NULL,
        TOTAL_GROSS TEXT NOT NULL,
        AVERAGE_GROSS TEXT NOT NULL,
        MARKET_SHARE TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.top_genres (
        RANK TEXT NOT NULL,
        GENRES TEXT NOT NULL,
        MOVIES TEXT NOT NULL,
        TOT_GROSS TEXT NOT NULL,
        AVERAGE_GROSS TEXT NOT NULL,
        MARKET_SHARE TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.top_gross_ratings (
        RANK TEXT NOT NULL,
        MPAA_RATINGS TEXT NOT NULL,
        MOVIES TEXT NOT NULL,
        TOTAL_GROSS TEXT NOT NULL,
        AVERAGE_GROSS TEXT NOT NULL,
        MARKET_SHARE TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.top_grossings_sources (
        RANK TEXT NOT NULL,
        SOURCES TEXT NOT NULL,
        MOVIES TEXT NOT NULL,
        TOTAL_GROSS TEXT NOT NULL,
        AVERAGE_GROSS TEXT NOT NULL,
        MARKET_SHARE TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.top_production_methods (
        RANK TEXT NOT NULL,
        PRODUCTION_METHODS TEXT NOT NULL,
        MOVIES TEXT NOT NULL,
        TOTAL_GROSS TEXT NOT NULL,
        AVERAGE_GROSS TEXT NOT NULL,
        MARKET_SHARE TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.wide_releases_count (
        YEAR TEXT NOT NULL,
        WARNER_BROS TEXT NOT NULL,
        WALT_DISNEY TEXT NOT NULL,
        _20TH_CENTURY_FOX TEXT NOT NULL,
        PARAMOUNT_PICTURES TEXT NOT NULL,
        SONY_PICTURES TEXT NOT NULL,
        UNIVERSAL TEXT NOT NULL,
        TOTAL_MAJOR_6 TEXT NOT NULL,
        TOTAL_OTHER_STUDIOS TEXT NOT NULL
    );
''')

data_select = ('''
SELECT *
FROM petl1.annual_ticket_sales
''')

insert_data = ('''
    INSERT INTO petl1.annual_ticket_sales  
    VALUES (%s, %s, %s, %s, %s);
''')

insert_data2 = ('''
    INSERT INTO petl1.highest_grossers  
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
''')

insert_data3 = ('''
    INSERT INTO petl1.popular_creative_types  
    VALUES (%s, %s, %s, %s, %s, %s);
''')

insert_data4 = ('''
    INSERT INTO petl1.top_distributors  
    VALUES (%s, %s, %s, %s, %s, %s);
''')

insert_data5 = ('''
    INSERT INTO petl1.top_genres  
    VALUES (%s, %s, %s, %s, %s, %s);
''')

insert_data6 = ('''
    INSERT INTO petl1.top_gross_ratings  
    VALUES (%s, %s, %s, %s, %s, %s);
''')

insert_data7 = ('''
    INSERT INTO petl1.top_grossings_sources  
    VALUES (%s, %s, %s, %s, %s, %s);
''')

insert_data8 = ('''
    INSERT INTO petl1.top_production_methods  
    VALUES (%s, %s, %s, %s, %s, %s);
''')

insert_data9 = ('''
    INSERT INTO petl1.wide_releases_count  
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
''')
