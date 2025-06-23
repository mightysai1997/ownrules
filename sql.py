from flask import request
import sqlite3

def search_user():
    name = request.args.get("name")  # Tainted source
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = '%s'" % name)  # Sink

# SQL Injection via f-string
def sqli_fstring(name):
    cursor.execute(f"SELECT * FROM accounts WHERE name = '{name}'")

# SQL Injection via .format()
def sqli_format(name):
    cursor.execute("SELECT * FROM accounts WHERE name = '{}'".format(name))

# SQL Injection via old-style % formatting
def sqli_percent(name):
    cursor.execute("SELECT * FROM accounts WHERE name = '%s'" % name)

# Django ORM raw query with concatenation
def django_raw_sqli(name):
    return Group.objects.raw("SELECT * FROM groups WHERE name = '" + name + "'")
