#!/usr/bin/python3
"""
Display values in states table
"""
import sys
import MySQLdb

if __name_ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s;", (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)
