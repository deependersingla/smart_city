import sqlite3 as lite
import sys
import api_request

con = lite.connect('smart_city.db')

with con:
    
    cur = con.cursor()    
    cur.execute("CREATE TABLE Routes(Id INT, StopName TEXT, ScheduledTime TEXT, StopId TEXT, TripId TEXT, ActualTime TEXT)")