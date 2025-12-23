from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# =========================================================
# Table 1: Patients
# =========================================================
class Patient(db.Model):
    __tablename__ = 'patients'      # Sets the actual table name in the SQL database to 'patients'
    
    id = db.Column(db.Integer, primary_key=True)
    case_no = db.Column(db.String(20), unique=True, nullable=False)     # unique=True to avoid having duplicate case numbers.
# Full Name --- nullable=False means these fields can't be empty.
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50))   # Middle name can be empty
    last_name = db.Column(db.String(50), nullable=False)
# Demographics and contact info
    gender = db.Column(db.String(10))
    date_of_birth = db.Column(db.Date)      # Stores specific date (YYYY-MM-DD)
    age = db.Column(db.Integer)             # Stores age as a number
    contact_no = db.Column(db.String(20))
    address = db.Column(db.String(200))
# Automatically records the exact time this patient was created in the system
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
# This links the Patient to the MedicalRecord model.
# 'backref' adds a hidden .patient attribute to the MedicalRecord model.
# 'cascade="all, delete"' means if you delete the Patient, their Records are deleted too.
    records = db.relationship('MedicalRecord', backref='patient', cascade="all, delete")


# =========================================================
# Table 2: Doctors
# =========================================================
class Doctor(db.Model):
    __tablename__ = 'doctors'
    
    id = db.Column(db.Integer, primary_key=True)
    license_no = db.Column(db.String(50), unique=True)  # Unique medical license number
# Doctor details
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    specialization = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
# Stores available days as a string, e.g., "Mon-Wed"
    schedule_days = db.Column(db.String(100))
    room_number = db.Column(db.String(20))
# Soft Delete flag: If False, the doctor is hidden but not deleted from DB history
    is_active = db.Column(db.Boolean, default=True)
    date_hired = db.Column(db.Date)


# =========================================================
# Table 3: Medical_Records
# =========================================================
class MedicalRecord(db.Model):
    __tablename__ = 'medical_records'
    
    id = db.Column(db.Integer, primary_key=True)
# This links this record to a specific Patient ID.
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)   # nullable=False means a record MUST belong to a patient.  
# Stores the doctor's name directly rather than linking to ID.
    doctor_name = db.Column(db.String(100)) 
# Clinical Data
    diagnosis = db.Column(db.Text)   # Text allows unlimited length strings
    symptoms = db.Column(db.Text)
    blood_pressure = db.Column(db.String(20)) # String to handle format like with slash
    temperature = db.Column(db.String(20))
    weight_kg = db.Column(db.Float)
    height_cm = db.Column(db.Float)
    notes = db.Column(db.Text)
# Timestamp for when a visit occurred
    visit_date = db.Column(db.DateTime, default=datetime.utcnow)


# =========================================================
# Table 4: Prescriptions
# =========================================================
class Prescription(db.Model):
    __tablename__ = 'prescriptions'
    
    id = db.Column(db.Integer, primary_key=True)
# Links the medicine to a specific Medical Record
    record_id = db.Column(db.Integer, db.ForeignKey('medical_records.id'))
# Medication Details
    medicine_name = db.Column(db.String(100))
    dosage = db.Column(db.String(50))      
    frequency = db.Column(db.String(50))
    duration = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    instructions = db.Column(db.Text)
    prescribed_by = db.Column(db.String(100))
    date_issued = db.Column(db.Date)


# =========================================================
# Table 5: Appointments
# =========================================================
class Appointment(db.Model):
    __tablename__ = 'appointments'
    
    id = db.Column(db.Integer, primary_key=True)
# An appointment connects a Patient AND a Doctor
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
# Scheduling details
    appointment_date = db.Column(db.Date)
    appointment_time = db.Column(db.Time) # Stores time only (HH:MM:SS)
    purpose = db.Column(db.String(200))  
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    remarks = db.Column(db.Text)
# To access doctor details from an appointment object 
    doctor = db.relationship('Doctor', backref='appointments')