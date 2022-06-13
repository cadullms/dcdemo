from flask import render_template
from flask import request
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
  try:
      conn = psycopg2.connect("dbname='postgres' user='postgres' host='db' password='postgres'")
  except:
      print("I am unable to connect to the database")
  cur = conn.cursor()
  cur.execute("""SELECT Line from Lines""")
  lines = cur.fetchall()
  return render_template('index.html',lines=lines)

if __name__ == '__main__':
  app.run()