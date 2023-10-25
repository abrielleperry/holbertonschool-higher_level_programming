#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""


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
    cursor.execute(
      "SELECT cities.id, cities.name, states.name FROM cities \
      JOIN states ON cities.state_id = states.id \
      ORDER BY cities.id ASC"
      )
    cities = cursor.fetchall()
    for city in cities:
        print(city)
