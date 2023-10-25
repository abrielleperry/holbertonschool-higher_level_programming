#!/usr/bin/python3
"""takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument"""


import MySQLdb
from sys import argv


def state_name_searched():
    """takes 4 args: username, password, database and state_name_searched"""
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id",
        (argv[4],)
    )
    all_data = cursor.fetchall()
    for row in all_data:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    state_name_searched()
