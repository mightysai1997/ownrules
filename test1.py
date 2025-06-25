import sqlite3
from flask import Flask, request

app = Flask(__name__)
conn = sqlite3.connect("example.db", check_same_thread=False)

@app.route("/classic_concat")
def classic_concat():
    username = request.args.get("username")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return str(conn.execute(query).fetchall())

@app.route("/format_string")
def format_string():
    user_id = request.args.get("id")
    query = "SELECT * FROM users WHERE id = {}".format(user_id)
    return str(conn.execute(query).fetchall())

@app.route("/f_string")
def f_string():
    email = request.args.get("email")
    query = f"SELECT * FROM users WHERE email = '{email}'"
    return str(conn.execute(query).fetchall())

@app.route("/percent_operator")
def percent_operator():
    name = request.args.get("name")
    query = "SELECT * FROM users WHERE name = '%s'" % name
    return str(conn.execute(query).fetchall())

@app.route("/list_join")
def list_join():
    ids = request.args.getlist("id")
    clause = " OR ".join([f"id = {i}" for i in ids])
    query = f"SELECT * FROM users WHERE {clause}"
    return str(conn.execute(query).fetchall())

@app.route("/orderby_injection")
def orderby_injection():
    sort_by = request.args.get("sort")
    query = f"SELECT * FROM users ORDER BY {sort_by}"
    return str(conn.execute(query).fetchall())

@app.route("/table_injection")
def table_injection():
    tbl = request.args.get("table")
    query = f"SELECT * FROM {tbl}"
    return str(conn.execute(query).fetchall())

@app.route("/multi_statement")
def multi_statement():
    val = request.args.get("v")
    query = f"SELECT * FROM users WHERE id = {val}; DROP TABLE users;"
    return str(conn.executescript(query))

@app.route("/raw_orm")
def raw_orm():
    # Simulated ORM query
    name = request.args.get("name")
    raw_query = f"SELECT * FROM users WHERE name = '{name}'"
    return str(conn.execute(raw_query).fetchall())

@app.route("/tainted_wrapper")
def tainted_wrapper():
    # Dangerous function that receives already-tainted query string
    def dbget(q):
        return conn.execute(q).fetchall()

    user_input = request.args.get("username")
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    return str(dbget(query))

@app.route("/secure_example")
def secure_example():
    user = request.args.get("username")
    return str(conn.execute("SELECT * FROM users WHERE username = ?", (user,)).fetchall())

if __name__ == "__main__":
    app.run(debug=True)
