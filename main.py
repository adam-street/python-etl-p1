import sql
from pgsql import query

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # insert data
    query(sql.test_insert, ["My Insert!"]);

    # select data
    results = query(sql.test_select);
    print("results: ", results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
