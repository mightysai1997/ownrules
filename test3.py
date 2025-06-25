# vulnerable_flask_sql_injection_demo.py

import sqlite3
from flask import Flask, request

app = Flask(__name__)
conn = sqlite3.connect("vuln_demo.db", check_same_thread=False)

# 1. String interpolation
@app.route('/interpolation')
def interpolation():
    username = request.args.get('username')
    query = f"SELECT * FROM users WHERE username = '{username}'"  # ❌ Vulnerable
    return str(conn.execute(query).fetchall())

# 2. String concatenation
@app.route('/concat')
def concat():
    email = request.args.get('email')
    query = "SELECT * FROM users WHERE email = '" + email + "'"  # ❌ Vulnerable
    return str(conn.execute(query).fetchall())

# 3. format() misuse
@app.route('/format')
def format_injection():
    user_id = request.args.get('id')
    query = "SELECT * FROM users WHERE id = '{}'".format(user_id)  # ❌ Vulnerable
    return str(conn.execute(query).fetchall())

# 4. Dynamic ORDER BY (subquery injection)
@app.route('/orderby')
def orderby():
    sort_by = request.args.get('sort')
    query = f"SELECT * FROM users ORDER BY {sort_by}"  # ❌ Can inject column or subquery
    return str(conn.execute(query).fetchall())

# 5. Dynamic table name
@app.route('/table')
def table():
    table = request.args.get('table')
    query = f"SELECT * FROM {table}"  # ❌ Table name injection
    return str(conn.execute(query).fetchall())

# 6. Multiple parameters
@app.route('/auth')
def auth():
    user = request.args.get('user')
    passwd = request.args.get('pass')
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{passwd}'"  # ❌ Vulnerable
    return str(conn.execute(query).fetchall())

# 7. Dangerous eval usage
@app.route('/eval')
def eval_injection():
    u_input = request.args.get('input')
    return eval(u_input)  # ❌ Arbitrary code execution, not SQLi but just as dangerous

# 8. Reading tainted SQL from a file
@app.route('/file')
def file_injection():
    sql = open('query.sql').read()  # e.g., contains f"SELECT * FROM {request.args.get('table')}"
    return str(conn.execute(sql).fetchall())

# 9. Simulated stored procedure call
@app.route('/proc')
def proc_call():
    proc_name = request.args.get('proc')
    query = f"CALL {proc_name}()"  # ❌ Procedure name injection (more relevant to MySQL/Postgres)
    return str(conn.execute(query).fetchall())

# 10. Chained query injection
@app.route('/multi')
def multi_stmt():
    arg = request.args.get('q')
    query = f"SELECT * FROM users WHERE name = '{arg}'; DELETE FROM users"  # ❌ Batch injection
    return str(conn.executescript(query))  # executescript allows multiple statements

# 11. ORM-like raw usage (SQLAlchemy-style simulation)
@app.route('/orm')
def orm_like():
    name = request.args.get('name')
    # Simulating SQLAlchemy raw SQL vulnerability
    return str(conn.execute(f"SELECT * FROM users WHERE name = '{name}'").fetchall())  # ❌ Unsafe

if __name__ == '__main__':
    app.run(debug=True)
