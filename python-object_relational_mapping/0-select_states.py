#!/usr/bin/Python
"""prints states from database"""

import MySQLdb
import sys

if __name__ == "__main__":
  db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3])

  cursor = db.cursor()

  cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
  all_data = cursor.fetchall()
  for row in all_data:
    print(row)
  cursor.close()
  db.close()