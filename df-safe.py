# vulnerable_multi_function_sql.py

import sqlite3
from flask import Flask, request

app = Flask(__name__)
conn = sqlite3.connect("vuln_demo.db", check_same_thread=False)

# 1. F-string injection via GET parameter
@app.route("/vuln1")
def vulnerable_get():
    user = request.args.get("user")
    query = f"SELECT * FROM users WHERE username = '{user}'"
    return str(conn.execute(query).fetchall())

# 2. Concatenation inside a helper function
def get_query(email):
    return "SELECT * FROM users WHERE email = '" + email + "'"

@app.route("/vuln2")
def vulnerable_helper():
    query = get_query(request.args.get("email"))
    return str(conn.execute(query).fetchall())

# 3. Multiple arguments to vulnerable logic
@app.route("/vuln3")
def multi_args():
    username = request.args.get("user")
    password = request.args.get("pass")
    query = f"SELECT * FROM accounts WHERE user='{username}' AND pass='{password}'"
    return str(conn.execute(query).fetchall())

# 4. Injection via loop-built WHERE clause
@app.route("/vuln4")
def bulk_check():
    ids = request.args.getlist("id")
    where_clause = " OR ".join([f"id = {i}" for i in ids])
    query = f"SELECT * FROM records WHERE {where_clause}"
    return str(conn.execute(query).fetchall())

# 5. format() abuse with column name
@app.route("/vuln5")
def template_sub():
    column = request.args.get("column")
    query = "SELECT {} FROM users".format(column)
    return str(conn.execute(query).fetchall())

if __name__ == "__main__":
    app.run(debug=True)
