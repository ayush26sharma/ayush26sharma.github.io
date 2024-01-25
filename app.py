# from app import app, db
from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/')
def homepage():
    return render_template('index.html')

def create_tables():
    with app.app_context():
        db.create_all()


@app.before_first_request
def before_first_request():
    create_tables()


app.before_first_request(create_tables)

if __name__ == '__main__':
    app.run(debug=True)
