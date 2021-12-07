test_select = ('''
    SELECT *
    FROM public.test_table;
''')

test_insert = ('''
    INSERT INTO public.test_table
    VALUES(%s);
''')

create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS petl1;
''')

create_tables = ('''
    CREATE SCHEMA IF NOT EXISTS petl1;
   
    DROP TABLE IF EXISTS petl1.annual_ticket_sales, petl1.highest_grossers, petl1.popular_creative_types,
    petl1.top_distributors, petl1.top_genres, petl1.top_grossing_ratings, petl1.top_grossing_sources, petl1.top_production_methods, 
    petl1.wide_releases_count;
    
    CREATE TABLE IF NOT EXISTS petl1.annual_ticket_sales (
        year INT PRIMARY KEY NOT NULL,
        tickets_sold TEXT NOT NULL,
        total_box_office TEXT NOT NULL,
        total_inflation_adjusted_box_office TEXT NOT NULL, 
        average_ticket_price TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.highest_grossers (
        year INT PRIMARY KEY NOT NULL,
        movie TEXT NOT NULL,
        genre TEXT,
        mpaa_rating TEXT NOT NULL,
        distributor TEXT NOT NULL,
        total_for_year TEXT NOT NULL,
        total_in_2019_dollars TEXT NOT NULL,
        tickets_sold TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.popular_creative_types (
        rank TEXT PRIMARY KEY NOT NULL,
        creative_types TEXT NOT NULL,
        movies TEXT NOT NULL,
        total_gross TEXT NOT NULL,
        average_gross TEXT NOT NULL,
        market_share TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.top_distributors (
        rank TEXT PRIMARY KEY NOT NULL,
        distributors TEXT NOT NULL,
        movies INT NOT NULL,
        total_gross TEXT NOT NULL,
        average_gross TEXT NOT NULL,
        market_share TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.top_genres (
        rank TEXT PRIMARY KEY NOT NULL,
        genres TEXT NOT NULL,
        movies TEXT NOT NULL,
        total_gross TEXT NOT NULL,
        average_gross TEXT NOT NULL,
        market_share TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.top_grossing_ratings (
        rank TEXT PRIMARY KEY NOT NULL,
        mpaa_ratings TEXT NOT NULL,
        movies TEXT NOT NULL,
        total_gross TEXT NOT NULL,
        average_gross TEXT NOT NULL,
        market_share TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.top_grossing_sources (
        rank TEXT NOT NULL,
        sources TEXT NOT NULL,
        movies TEXT NOT NULL,
        total_gross TEXT NOT NULL,
        average_gross TEXT NOT NULL,
        market_share TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.top_production_methods (
        rank TEXT PRIMARY KEY NOT NULL,
        production_methods TEXT NOT NULL,
        movies TEXT NOT NULL,
        total_gross TEXT NOT NULL,
        average_gross TEXT NOT NULL,
        market_share TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS petl1.wide_releases_count (
        year INT PRIMARY KEY NOT NULL,
        warner_bros INT NOT NULL,
        walt_disney INT NOT NULL,
        twentieth_century_fox INT NOT NULL,
        paramount_pictures INT NOT NULL,
        sony_pictures INT NOT NULL,
        universal INT NOT NULL,
        total_major_6 INT NOT NULL,
        total_other_studios INT NOT NULL
    );
''')

more_tables = ('''
    CREATE TABLE IF NOT EXISTS petl1.annual_ticket_sales (
        year INT PRIMARY KEY NOT NULL,
        tickets_sold TEXT NOT NULL,
        total_box_office TEXT NOT NULL,
        total_inflation_adjusted_box_office TEXT NOT NULL, 
        average_ticket_price TEXT NOT NULL
    );
''')






insert_rows1 = ('''
    INSERT INTO petl1.annual_ticket_sales
    VALUES(%s, %s, %s, %s, %s)
''')

insert_rows2 = ('''
    INSERT INTO petl1.highest_grossers
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
''')

insert_rows3 = ('''
    INSERT INTO petl1.popular_creative_types
    VALUES(%s, %s, %s, %s, %s, %s);
''')

insert_rows4 = ('''
    INSERT INTO petl1.top_distributors
    VALUES(%s, %s, %s, %s, %s, %s);
''')

insert_rows5 = ('''
    INSERT INTO petl1.top_genres
    VALUES(%s, %s, %s, %s, %s, %s);
''')
 
insert_rows6 = ('''
    INSERT INTO petl1.top_grossing_ratings
    VALUES(%s, %s, %s, %s, %s, %s)
''')

insert_rows7 = ('''
    INSERT INTO petl1.top_grossing_sources
    VALUES(%s, %s, %s, %s, %s, %s)
''')

insert_rows8 = ('''
    INSERT INTO petl1.top_production_methods
    VALUES(%s, %s, %s, %s, %s, %s);
''')

insert_rows9 = ('''
    INSERT INTO petl1.wide_releases_count
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);
''')