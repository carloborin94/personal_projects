from flask import render_template, request, jsonify
from .models import Patient, db

def configure_routes(app):
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/patient-data", methods=["GET", "POST"])
    def patient_data():
        if request.method == "POST":
            # Riceve i dati del paziente e li salva nel database
            data = request.form
            new_patient = Patient(
                name=data.get('name'),
                age=data.get('age'),
                medical_history=data.get('history')
            )
            db.session.add(new_patient)
            db.session.commit()
            return jsonify({"message": "Dati paziente salvati con successo!"})
        else:
            # Ritorna un form per inserire i dati del paziente
            return render_template("patient_form.html")
