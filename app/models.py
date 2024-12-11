# models.py
from app import db
from datetime import datetime

class IndividualRegistration(db.Model):
    __tablename__ = 'individual_registrations'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    selected_dates = db.Column(db.PickleType, nullable=False)  # Store selected dates as a list
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<IndividualRegistration(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email})>"

class InstitutionRegistration(db.Model):
    __tablename__ = 'institution_registrations'
    
    id = db.Column(db.Integer, primary_key=True)
    institution_name = db.Column(db.String(200), nullable=False)
    institution_address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    exhibition_choices = db.Column(db.PickleType, nullable=False)  # Store exhibition choices as a list
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<InstitutionRegistration(id={self.id}, institution_name={self.institution_name}, email={self.email})>"
    

class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Feedback(id={self.id}, name={self.name}, email={self.email})>"
