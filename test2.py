import sqlite3
import sqlite3
# Assuming ctx.getAuthenticatedUserName() returns the authenticated user's name
userName = ctx.getAuthenticatedUserName()

# Assuming ItemName.Text is user-provided input
itemName = ItemName.Text

# Constructing the SQL query (vulnerable to SQL injection)
sql_query = f"SELECT * FROM items WHERE owner = '{userName}' AND itemname = '{itemName}'"

# Establishing a connection to the database (replace with your actual database connection)
conn = sqlite3.connect("your_database.db")

# Creating a cursor
cursor = conn.cursor()

# Executing the query
cursor.execute(sql_query)

# Fetching the results
results = cursor.fetchall()

# Processing the results as needed
for row in results:
    print(row)

# Closing the cursor and connection
cursor.close()
conn.close()
