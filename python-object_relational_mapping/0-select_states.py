#!/usr/bin/python3
""" lists all states"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states')
    all_data = cursor.fetchall()
    for row in all_data:
        print(row)
