import sqlite3
from flask import Flask, request

app = Flask(__name__)
conn = sqlite3.connect("example.db", check_same_thread=False)

# Function that executes whatever SQL it's given — no checks (sink)
def db_execute(q):
    return conn.execute(q).fetchall()

# Function that builds the query using unsafe user input (source + concat)
@app.route("/search")
def search():
    name = request.args.get("name")  # tainted input
    query = "SELECT * FROM users WHERE name = '" + name + "'"  # unsafe
    return str(db_execute(query))  # passed to sink function
