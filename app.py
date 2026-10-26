import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


def get_conn():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )


def get_items():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name FROM items ORDER BY id")
    rows = [r[0] for r in cur.fetchall()]
    conn.close()
    return rows


@app.route("/health")
def health():
    return "OK"


@app.route("/api/data")
def data():
    return jsonify(get_items())


@app.route("/api/items/count")
def count():
    return str(len(get_items()))


@app.route("/")
def index():
    items = get_items()
    return "<h1>Items</h1><ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
