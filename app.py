from cs50 import SQL
from flask import Flask, render_template, request

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///longlist.db")

@app.route("/")
def index():
    longlist = db.execute("SELECT * FROM longlist LIMIT 50")
    return render_template("index.html", longlist=longlist)