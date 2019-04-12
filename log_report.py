# Report 1 - what are the most popular three articles of all time?
# Report 2 - who are the most popular article authors of all time?
# Report 3 - on which days did more than 1% of requests lead to errors?

import psycopg2 as psy

db = psy.connect("dbname=news")
db_cursor = db.cursor()
db_cursor.execute()
data = db_cursor.fetchall()
db.close()
print data
