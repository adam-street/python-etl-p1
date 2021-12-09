
create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS petl1;
''')

annual_ticket_sales_table =('''
  CREATE TABLE  IF NOT EXISTS petl1.annual_ticket_sales (
  sales_year TEXT NOT NULL,
  tickets_sold TEXT NOT NULL,
  total_box_office TEXT NOT NULL,
  total_inflation_adjusted_box_office TEXT NOT NULL,
  average_ticket_price TEXT NOT NULL);
''')

highest_grossers_table = ('''
  CREATE TABLE IF NOT EXISTS petl1.highest_grossers (
  year TEXT NOT NULL,
  movie TEXT NOT NULL,
  genre TEXT NOT NULL,
  rating TEXT NOT NULL,
  distributor TEXT NOT NULL,
  total_for_year TEXT NOT NULL,
  total_in_2019_dollars TEXT NOT NULL,
  tickets_sold TEXT NOT NULL);
  ''')

popular_creative_types_table = ('''
   CREATE TABLE IF NOT EXISTS petl1.popular_creative_types (
   rank TEXT NOT NULL,
   creative_types TEXT NOT NULL,
   movies TEXT NOT NULL,
   total_gross TEXT NOT NULL,
   average_gross TEXT NOT NULL,
   market_share TEXT NOT NULL);
   ''')

top_distributors_table = ('''
  CREATE TABLE IF NOT EXISTS petl1.top_distributors (
  rank TEXT NOT NULL,
  distributors TEXT NOT NULL,
  movies TEXT NOT NULL,
  total_gross TEXT NOT NULL,
  average_gross TEXT NOT NULL,
  market_share TEXT NOT NULL);
  ''')

top_genres_table = ('''
  CREATE TABLE IF NOT EXISTS petl1.top_genres (
  rank TEXT NOT NULL,
  genres TEXT NOT NULL,
  movies TEXT NOT NULL,
  total_gross TEXT NOT NULL,
  average_gross TEXT NOT NULL,
  market_share TEXT NOT NULL);
  ''')

top_grossing_ratings_table = ('''
  CREATE TABLE IF NOT EXISTS petl1.top_grossing_ratings (
  rank TEXT NOT NULL,
  mpaa_ratings TEXT NOT NULL,
  movies TEXT NOT NULL,
  total_gross TEXT NOT NULL,
  average_gross TEXT NOT NULL,
  market_share TEXT NOT NULL);
  ''')

top_grossing_sources_table = ('''
  CREATE TABLE IF NOT EXISTS petl1.top_grossing_sources (
  rank TEXT NOT NULL,
  sources TEXT NOT NULL,
  movies TEXT NOT NULL,
  total_gross TEXT NOT NULL,
  average_gross TEXT NOT NULL,
  market_share TEXT NOT NULL);
  ''')

top_production_methods_table = ('''
  CREATE TABLE IF NOT EXISTS petl1.top_production_methods (
  rank TEXT NOT NULL,
  mpaa_ratings TEXT NOT NULL,
  movies TEXT NOT NULL,
  total_gross TEXT NOT NULL,
  average_gross TEXT NOT NULL,
  market_share TEXT NOT NULL);
  ''')

wide_releases_count_table = ('''
   CREATE TABLE IF NOT EXISTS petl1.wide_releases_count (
   year TEXT NOT NULL,
   warner_bros TEXT NOT NULL,
   walt_disney TEXT NOT NULL,
   twentyth_century_fox TEXT NOT NULL,
   paramount_pictures TEXT NOT NULL,
   sony_pictures TEXT NOT NULL,
   universal TEXT NOT NULL,
   total_major TEXT NOT NULL,
   six_total_other_studios TEXT NOT NULL);
''')

insert_row1 = ('''
  INSERT INTO petl1.annual_ticket_sales
  VALUES(%s, %s, %s, %s, %s);
''')

insert_row2 = ('''
  INSERT INTO petl1.highest_grossers
  VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
''')

insert_row3 = ('''
   INSERT INTO petl1.popular_creative_types
   VALUES (%s,%s,%s,%s,%s,%s);
''')

insert_row4 = ('''
  INSERT INTO petl1.top_distributors
  VALUES (%s,%s,%s,%s,%s,%s)
''')

insert_row5 = ('''
  INSERT INTO petl1.top_genres
  VALUES (%s,%s,%s,%s,%s,%s)
''')

insert_row6 = ('''
  INSERT INTO petl1.top_grossing_ratings
  VALUES (%s,%s,%s,%s,%s,%s)
''')

insert_row7 = ('''
  INSERT INTO petl1.top_grossing_sources
  VALUES (%s,%s,%s,%s,%s,%s)
''')

insert_row8 = ('''
  INSERT INTO petl1.top_production_methods
  VALUES (%s,%s,%s,%s,%s,%s)
''')

insert_row9 = ('''
   INSERT INTO petl1.wide_releases_count
   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
''')
