from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UID = db.Column(db.String(50), unique=True, nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    Score = db.Column(db.Integer, nullable=False)
    Country = db.Column(db.String(2), nullable=False)
    TimeStamp = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return f"User('{self.UID}', '{self.Name}', '{self.Score}', '{self.Country}', '{self.TimeStamp}')"
