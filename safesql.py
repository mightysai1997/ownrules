# safe_flask_sql_demo.py

import sqlite3
from flask import Flask, request, abort

app = Flask(__name__)
conn = sqlite3.connect("safe_demo.db", check_same_thread=False)

def is_valid_column(value):
    # Whitelist valid columns for ORDER BY, etc.
    return value in {"username", "email", "id", "name"}

def is_valid_table(value):
    # Whitelist valid table names (if dynamic)
    return value in {"users", "admins"}

@app.route('/interpolation')
def interpolation():
    username = request.args.get('username')
    result = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall()
    return str(result)

@app.route('/concat')
def concat():
    email = request.args.get('email')
    result = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchall()
    return str(result)

@app.route('/format')
def format_injection():
    user_id = request.args.get('id')
    result = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchall()
    return str(result)

@app.route('/orderby')
def orderby():
    sort_by = request.args.get('sort')
    if not is_valid_column(sort_by):
        abort(400, "Invalid sort column")
    query = f"SELECT * FROM users ORDER BY {sort_by}"  # Safe after whitelist check
    result = conn.execute(query).fetchall()
    return str(result)

@app.route('/table')
def table():
    tbl = request.args.get('table')
    if not is_valid_table(tbl):
        abort(400, "Invalid table name")
    query = f"SELECT * FROM {tbl}"  # Safe after whitelist check
    result = conn.execute(query).fetchall()
    return str(result)

@app.route('/auth')
def auth():
    user = request.args.get('user')
    passwd = request.args.get('pass')
    result = conn.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?", (user, passwd)
    ).fetchall()
    return str(result)

@app.route('/eval')
def eval_safe():
    return "Use of eval is insecure and has been disabled."

@app.route('/file')
def file_safe():
    query = "SELECT * FROM users"
    result = conn.execute(query).fetchall()
    return str(result)

@app.route('/proc')
def proc_call():
    return "Stored procedure simulation disabled for safety."

@app.route('/multi')
def multi_stmt():
    arg = request.args.get('q')
    result = conn.execute("SELECT * FROM users WHERE name = ?", (arg,)).fetchall()
    return str(result)

@app.route('/orm')
def orm_like():
    name = request.args.get('name')
    result = conn.execute("SELECT * FROM users WHERE name = ?", (name,)).fetchall()
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
