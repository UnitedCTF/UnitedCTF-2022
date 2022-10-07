#!/usr/bin/python3
from flask import Flask, Response, redirect, request, jsonify, render_template
from string import ascii_lowercase, digits
import sqlite3

DB_NAME = "db.sqlite"

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    q = request.args.get("q")
    if q is None or not q:
        return render_template("index.html")

    conn = sqlite3.connect(DB_NAME)
    curs = conn.cursor()
    try:
        curs.execute(
            f"SELECT * FROM quotes WHERE author LIKE '%{q}%' OR quote LIKE '%{q}%'"
        )
        quotes = curs.fetchall()
    except Exception as e:
        return str(e), 500
    finally:
        conn.close()

    return render_template("index.html", quotes=quotes)
