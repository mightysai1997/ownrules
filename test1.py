import sqlite3

def login(username, password):
    # Vulnerable SQL query
    query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)

    # Connect to the database
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()

    # Execute the query
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()

    # Close the connection
    connection.close()

    return result

# Example usage (vulnerable to SQL injection)
username = "admin' OR '1'='1'; --"
password = "password123"

result = login(username, password)

if result:
    print("Login successful")
else:
    print("Login failed")
