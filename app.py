from models import *
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

DB_FILE = "clubreview.sqlite3"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_FILE}"
db = SQLAlchemy(app)


@app.route('/')
def main():
    return "Welcome to Penn Club Review!"


@app.route('/api')
def api():
    return jsonify({"message": "Welcome to the Penn Club Review API!."})


@app.route('/data')
def data():
    return jsonify({"data": "code, name, description, tags"})


if __name__ == '__main__':
    app.run()
