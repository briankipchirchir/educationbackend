# config.py
import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.getcwd(), 'db.sqlite3')}"
