from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.routes import configure_routes

# Crea l'app Flask
app = Flask(__name__)

# Configurazione del database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'  # Cambia in futuro per un database come PostgreSQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializza SQLAlchemy
db = SQLAlchemy(app)

# Inizializza Flask-Migrate per la gestione delle migrazioni del database
migrate = Migrate(app, db)

# Importa i modelli (assicurati che il file models.py esista nella directory app/)
from app.models import Patient  # Importa i modelli definiti nel file app/models.py

# Configura le rotte (definite in routes.py)
configure_routes(app)

# Funzione principale per avviare l'app
if __name__ == "__main__":
    app.run(debug=True)  # Imposta debug=True solo in fase di sviluppo
