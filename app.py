from cs50 import SQL
from flask import Flask, render_template, request

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///longlist.db")

def index():
    longlist = db.execute("SELECT * FROM longlist")
    for book in longlist:
        print(book["title"])
    return "TODO"

index()