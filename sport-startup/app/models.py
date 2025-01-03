from app import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    medical_history = db.Column(db.Text, nullable=True)

    def __init__(self, name, age, medical_history):
        self.name = name
        self.age = age
        self.medical_history = medical_history
