import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    # Vulnerable code - directly incorporating user input into the SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Executing the SQL query
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    if result:
        return "Login successful"
    else:
        return "Login failed"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
