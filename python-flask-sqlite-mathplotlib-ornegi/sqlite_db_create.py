import sqlite3 as lite
import sys
con = lite.connect('system_usage.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS system_usage")
    cur.execute("CREATE TABLE system_usage(timestamp DATETIME, cpu NUMERIC, mem NUMERIC)")
