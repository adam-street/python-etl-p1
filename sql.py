test_insert_ATS = ('''
   INSERT INTO p1_etl.annual_ticket_sales
   VALUES(%s, %s, %s, %s, %s);
''')

test_insert_HG = ('''
   INSERT INTO p1_etl.highest_grossers
   VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
''')

test_insert_PCT = ('''
   INSERT INTO p1_etl.popular_creative_types
   VALUES(%s, %s, %s, %s, %s, %s);
''')

test_insert_TD = ('''
   INSERT INTO p1_etl.top_distributors
   VALUES(%s, %s, %s, %s, %s, %s);
''')

test_insert_TG = ('''
   INSERT INTO p1_etl.top_genres
   VALUES(%s, %s, %s, %s, %s, %s);
''')

test_insert_TGR = ('''
   INSERT INTO p1_etl.top_grossing_ratings
   VALUES(%s, %s, %s, %s, %s, %s);
''')

test_insert_TGS = ('''
   INSERT INTO p1_etl.top_grossing_sources
   VALUES(%s, %s, %s, %s, %s, %s);
''')

test_insert_TPM = ('''
   INSERT INTO p1_etl.top_production_methods
   VALUES(%s, %s, %s, %s, %s, %s);
''')

test_insert_WRC = ('''
   INSERT INTO p1_etl.wide_releases_count
   VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);
''')

create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS p1_etl;

    DROP TABLE IF EXISTS p1_etl.annual_ticket_sales, p1_etl.highest_grossers, p1_etl.popular_creative_types, 
    p1_etl.top_distributors, p1_etl.top_genres, p1_etl.top_grossing_ratings, p1_etl.top_grossing_sources, 
    p1_etl.top_production_methods, p1_etl.wide_releases_count;

    CREATE TABLE IF NOT EXISTS p1_etl.annual_ticket_sales (
        year INT NOT NULL,
        tickets_sold VARCHAR(50),
        total_box_office VARCHAR(50),
        total_inflation_adjusted_box_office VARCHAR(50),
        average_ticket_price MONEY NOT NULL
        );

    CREATE TABLE IF NOT EXISTS p1_etl.highest_grossers (
        year INT NOT NULL,
        movie VARCHAR(50),
        genre VARCHAR(50),
        mpaa VARCHAR(50),
        distributor VARCHAR(50),
        total_for_year VARCHAR(50),
        total_in_2019_dollars VARCHAR(50),
        tickets_sold VARCHAR(50)
        );

    CREATE TABLE IF NOT EXISTS p1_etl.popular_creative_types (
        rank INT NOT NULL,
        creative_types VARCHAR(50),
        movies VARCHAR(50),
        total_gross VARCHAR(50),
        average_gross VARCHAR(50),
        market_share VARCHAR(50)
        );

    CREATE TABLE IF NOT EXISTS p1_etl.top_distributors (
        rank INT NOT NULL,
        distributors VARCHAR(50),
        movies VARCHAR(50),
        total_gross VARCHAR(50),
        average_gross VARCHAR(50),
        market_share VARCHAR(50)
        );

    CREATE TABLE IF NOT EXISTS p1_etl.top_genres (
        rank INT NOT NULL,
        genres VARCHAR(50),
        movies VARCHAR(50),
        total_gross VARCHAR(50),
        average_gross VARCHAR(50),
        market_share VARCHAR(50)
        );

    CREATE TABLE IF NOT EXISTS p1_etl.top_grossing_ratings (
        rank INT NOT NULL,
        mpaa_ratings VARCHAR(50),
        movies VARCHAR(50),
        total_gross VARCHAR(50),
        average_gross VARCHAR(50),
        market_share VARCHAR(50)
        );

    CREATE TABLE IF NOT EXISTS p1_etl.top_grossing_sources (
        rank INT NOT NULL,
        sources VARCHAR(50),
        movies VARCHAR(50),
        total_gross VARCHAR(50),
        average_gross VARCHAR(50),
        market_share VARCHAR(50)
        );

    CREATE TABLE IF NOT EXISTS p1_etl.top_production_methods (
        rank INT NOT NULL,
        production_methods VARCHAR(50),
        movies VARCHAR(50),
        total_gross VARCHAR(50),
        average_gross VARCHAR(50),
        market_share VARCHAR(50)
        );

    CREATE TABLE IF NOT EXISTS p1_etl.wide_releases_count (
        year INT NOT NULL,
        warner_bros INT NOT NULL,
        walt_disney INT NOT NULL,
        _20th_century_fox INT NOT NULL,
        paramount_pictures INT NOT NULL,
        sony_pictures INT NOT NULL,
        universal INT NOT NULL,
        total_major_6 INT NOT NULL,
        total_other_studios INT NOT NULL
        );
''')
