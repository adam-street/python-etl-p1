## Setup
   Create a new file in the project's root folder called ```config.py``` with the following format.
    
    pgsql_config = {
        'host': '********',
        'dbname': '******',
        'user': '********',
        'password': '****'
    }
    
## Project
   1. Create a fork of this repo with the following naming convention ```[first-name]-[last-name]-python-etl-p1```
   
   2. Update the program so that when ```main.py``` is run the csv data in the folder ```datasets/hollywood-theatrical-market-synopsis``` will be stored in the database.
   __There should be 1 database table for each csv file__
   
   ### Hints
   - __Read__ the ```main.py``` file to see how to run a query withing the existing project structure.
   - New querys you write should be stored in the sql.py file. __There is an example query you can use as a template__
   - Use the python documentation to learn how you can parse csv files! https://docs.python.org/3/library/csv.html
      
