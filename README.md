## Setup
   To run the program you must create a new file in the project's root folder called ```config.py``` with the following format.
   This is what the program reads to know what datbase to connect to and with what credentials.
   
    pgsql_config = {
        'host': '********',
        'dbname': '******',
        'user': '********',
        'password': '****'
    }
    
   - ```host``` is the hostname or url of the database, it will look like ```abcdefg.abcdefg.us-east-2.rds.amazonaws.com```
   
   - ```dbname``` is the datbase name of the host you want to connect to, you can use ```aaatest``` to test with.
   
   - ```user``` is the username
   
   - ```password``` is the password
    
## Project
   1. Create a fork of this repo with the following naming convention ```[first-name]-[last-name]-python-etl-p1```
   
   2. Update the program so that when ```main.py``` is run the csv data in the folder ```datasets/hollywood-theatrical-market-synopsis``` will be stored in the database.
   __There should be 1 database table for each csv file__
   
   ### Hints
   - __Read__ the ```main.py``` file to see how to run a query within the existing project structure.
   - New querys you write should be stored in the ```sql.py``` file. __There is an example query you can use as a template__
   - __Use the python documentation__ to learn how you can parse csv files! https://docs.python.org/3/library/csv.html
      
