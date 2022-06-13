# So you just want to try out how to work with PostgreSQL in Python and stumble 
# upon a sample like this: https://wiki.postgresql.org/wiki/Psycopg2_Tutorial 

import psycopg2

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='db' password='postgres'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("""SELECT Line from Lines""")
rows = cur.fetchall()
print ("Show me the lyrics:")
for row in rows:
    print ("   ", row[0])