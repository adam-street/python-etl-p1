create_schema = ('''
    create schema IF NOT EXISTS Nads;
''')

test_create = ('''
    CREATE TABLE if not exists Nads.TopDistributors (
        Rank varchar NOT NULL,
        distributors varchar,
        Movies varchar,
        Total_gross varchar,
        Avergae_gross varchar,
        Market_share varchar
    )
    ''')


test_insert = ('''
  INSERT INTO Nads.TopDistributors
  VALUES(%s,%s,%s,%s,%s,%s);
''')

test_select = ('''
  SELECT *
  FROM Nads.TopDistributors
''')
