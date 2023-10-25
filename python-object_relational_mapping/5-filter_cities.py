#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""


import MySQLdb
from sys import argv


def show_state_name():
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s \
        ORDER BY id ASC;", (argv[4],)
    )
    all_data = cursor.fetchall()

    num_cities = len(all_data)
    if num_cities == 0:
        print()
        return

    for i in range(0, num_cities - 1):
        print(all_data[i][1], end=", ")
    print(all_data[num_cities - 1][1])

    cursor.close()
    db.close()


if __name__ == '__main__':
    show_state_name()
