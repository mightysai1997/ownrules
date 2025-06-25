from flask import Flask, request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("example.db", check_same_thread=False)

def run_sql(query):
    return conn.execute(query).fetchall()

def build_query(name):
    return "SELECT * FROM users WHERE name = '" + name + "'"

@app.route("/test1")
def test1():
    user_input = request.args.get("name")
    query = build_query(user_input)
    return str(run_sql(query))
