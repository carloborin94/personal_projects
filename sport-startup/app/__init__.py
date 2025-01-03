from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurazione del database (puoi cambiare sqlite con il database che preferisci)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crea l'istanza di SQLAlchemy
db = SQLAlchemy(app)

# Importa i moduli per registrare le route e i modelli
from app import routes, models
