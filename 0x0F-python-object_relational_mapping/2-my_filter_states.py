#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table"""

import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()
    cur.close()
    conn.close()
    for row in query_rows:
        print(row)
