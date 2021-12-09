create_schema = ('''
    create schema IF NOT EXISTS petl1;
''')

test_create1 = ('''
    CREATE TABLE if not exists petl1.AnnualTicketSales (
        _Year_ varchar NOT NULL,
        Tickets_Sold varchar,
        Total_Box_Office varchar,
        Total_Inflated_Adjusted_Box_Office varchar,
        Avergae_Ticket_Price varchar
    )
    ''')

test_create2 = ('''
    CREATE TABLE if not exists petl1.HighestGrossers (
        Year varchar NOT NULL,
        Movie varchar,
        Genre varchar,
        MPAA_Rating varchar,
        Distributor varchar,
        Total_For_Year varchar,
        Total_in_2019_dollars varchar,
        Tickets_Sold varchar
    )
    ''')

test_create3 = ('''
    CREATE TABLE if not exists petl1.PopularCreativeTypes (
        Rank varchar NOT NULL,
        Creative_types varchar,
        Movies varchar,
        Total_gross varchar,
        Avergae_gross varchar,
        Market_share varchar
    )
    ''')

test_create4 = ('''
    CREATE TABLE if not exists petl1.TopDistributors (
        Rank varchar NOT NULL,
        distributors varchar,
        Movies varchar,
        Total_gross varchar,
        Avergae_gross varchar,
        Market_share varchar
    )
    ''')

test_create5 = ('''
    CREATE TABLE if not exists petl1.TopGenres (
        Rank varchar NOT NULL,
        Genres varchar,
        Movies varchar,
        Total_gross varchar,
        Avergae_gross varchar,
        Market_share varchar
    )
    ''')

test_create6 = ('''
    CREATE TABLE if not exists petl1.TopGrossingRatings (
        Rank varchar NOT NULL,
        MPAA_Ratings varchar,
        Movies varchar,
        Total_gross varchar,
        Avergae_gross varchar,
        Market_share varchar
    )
    ''')

test_create7 = ('''
    CREATE TABLE if not exists petl1.TopGrossingSources (
        Rank varchar NOT NULL,
        Sources varchar,
        Movies varchar,
        Total_gross varchar,
        Avergae_gross varchar,
        Market_share varchar
    )
    ''')

test_create8 = ('''
    CREATE TABLE if not exists petl1.TopProductionMethods (
        Rank varchar NOT NULL,
        Production_Methods varchar,
        Movies varchar,
        Total_gross varchar,
        Average_gross varchar,
        Market_share varchar
    )
    ''')

test_create9 = ('''
    CREATE TABLE if not exists petl1.WideReleasesCount (
        _Year_ int NOT NULL,
        Warner_Bros int,
        Walt_Disney int,
        _20th_Century_Fox int,
        Paramount_Pictures int,
        Sony_Pictures int,
        Universal int,
        Total_Major_6 int,
        Total_Other_Studios int
        
    )
    ''')

test_insert1 = ('''
  INSERT INTO petl1.AnnualTicketSales
  VALUES(%s,%s,%s,%s,%s);
''')

test_insert2 = ('''
  INSERT INTO petl1.HighestGrossers
  VALUES(%s,%s,%s,%s,%s,%s,%s,%s);
''')

test_insert3 = ('''
  INSERT INTO petl1.PopularCreativeTypes
  VALUES(%s,%s,%s,%s,%s,%s);
''')

test_insert4 = ('''
  INSERT INTO petl1.TopDistributors
  VALUES(%s,%s,%s,%s,%s,%s);
''')

test_insert5 = ('''
  INSERT INTO petl1.TopGenres
  VALUES(%s,%s,%s,%s,%s,%s);
''')

test_insert6 = ('''
  INSERT INTO petl1.TopGrossingRatings
  VALUES(%s,%s,%s,%s,%s,%s);
''')

test_insert7 = ('''
  INSERT INTO petl1.TopGrossingSources
  VALUES(%s,%s,%s,%s,%s,%s);
''')

test_insert8 = ('''
  INSERT INTO petl1.TopProductionMethods
  VALUES(%s,%s,%s,%s,%s,%s);
''')

test_insert9 = ('''
  INSERT INTO petl1.WideReleasesCount
  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);
''')
test_select = ('''
  SELECT *
  FROM petl1.WideReleasesCount
''')
