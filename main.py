import sql
from pgsql import query

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    results = query(sql.test_query);
    print("results: ", results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
