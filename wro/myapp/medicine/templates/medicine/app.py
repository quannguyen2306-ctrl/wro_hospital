from email.policy import default
import json
# from unittest import result
from flask import request
from flask import Flask, render_template
# from nbformat import write
# from numpy import result_type
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///hospital.db'
# Initialize the database
db = SQLAlchemy(app)
#Creating db models
class Prescription(db.Model):
    __tablename__ = "prescription"
    id = db.Column(db.Integer, primary_key=True)
    doctor_name = db.Column(db.String(200), nullable = False)
    patient_number = db.Column(db.String(200), nullable = False)
    medicine_list = db.Column(db.String(200), nullable = False)
    amount_list = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    # Create function to return a string when we add something
    def __repr__(self):
        medicine = json.loads(self.medicine_list)
        amount = json.loads(self.amount_list)
        med_amt = []
        for i in range(medicine):
            med_amt.append((medicine[i],amount[i]))
        return f"Doctor name: {self.doctor_name}, {med_amt}"
class Medicine(db.Model):
    __tablename__ = "medicine"
    id = db.Column(db.Integer, primary_key=True)
    medicine_name = db.Column(db.String(200), nullable = False)
    description = db.Column(db.Text(), nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

class Patient(db.Model):
    __tablename__ = "patient"
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(200), nullable = False)
    disease_description = db.Column(db.Text(), nullable = False)

def sendEv3JSON():
    pass

@app.route('/')
def index():
    return render_template('./home.html')
@app.route('/input_prescription', methods=['POST'])
def input_prescription():
    output = request.get_json()
    result = json.loads(output) 
    print(result)
    pre = Prescription(
        doctor_name = result["doctor_name"],
        patient_number = result["patient_number"],
        medicine_list = json.dumps(result["medicine"]),
        amount_list = json.dumps(result["amount"]),    
    )
    db.session.add(pre)
    db.session.commit()
    return result


if __name__ == "__main__":
    app.run(debug=True)

