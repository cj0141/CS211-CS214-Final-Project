from app import create_app
from models import db, Patient, Doctor, MedicalRecord, Prescription, Appointment
from datetime import datetime, time

app = create_app()

with app.app_context():
    print("-----------------------------------")
    print("Refreshing Database (Dropping & Recreating)...")
    db.drop_all()
    db.create_all()

    # ==========================================
    # 1. TABLE: PATIENTS
    # ==========================================
    print("Seeding Patients...")
    patients_list = [
        {"case_no": "P-01", "last": "Hassan", "first": "Jenna", "mid": "Castro", "gen": "Female", "age": 26, "contact": "09293932931", "addr": "San Juan, Iriga City", "dob": "1998-03-13"},
        {"case_no": "P-02", "last": "Navarro", "first": "James", "mid": "Fernandez", "gen": "Male", "age": 25, "contact": "09292342923", "addr": "San Nicolas, Iriga City", "dob": "1999-05-20"},
        {"case_no": "P-03", "last": "Cuevas", "first": "Justin", "mid": "Aquino", "gen": "Male", "age": 29, "contact": "09292234122", "addr": "San Roque, Iriga City", "dob": "1995-11-02"},
        {"case_no": "P-04", "last": "Castro", "first": "Chris", "mid": "Moreno", "gen": "Male", "age": 26, "contact": "09023923020", "addr": "San Francisco, Iriga City", "dob": "1998-01-15"},
        {"case_no": "P-05", "last": "Santos", "first": "Maria", "mid": "Lopez", "gen": "Female", "age": 32, "contact": "09175551234", "addr": "San Miguel, Iriga City", "dob": "1992-08-10"},
        {"case_no": "P-06", "last": "Reyes", "first": "Mark", "mid": "Tan", "gen": "Male", "age": 45, "contact": "09182229876", "addr": "Santa Cruz, Iriga City", "dob": "1979-12-05"},
        {"case_no": "P-07", "last": "Dizon", "first": "Sarah", "mid": "Gomez", "gen": "Female", "age": 21, "contact": "09193334567", "addr": "Santo Domingo, Iriga City", "dob": "2003-02-14"},
        {"case_no": "P-08", "last": "Mendoza", "first": "Ryan", "mid": "Perez", "gen": "Male", "age": 38, "contact": "09204445678", "addr": "San Agustin, Iriga City", "dob": "1986-06-30"},
        {"case_no": "P-09", "last": "Lim", "first": "Kimberly", "mid": "Go", "gen": "Female", "age": 27, "contact": "09215556789", "addr": "San Jose, Iriga City", "dob": "1997-09-22"},
        {"case_no": "P-10", "last": "Torres", "first": "Michael", "mid": "Ruiz", "gen": "Male", "age": 50, "contact": "09226667890", "addr": "San Pedro, Iriga City", "dob": "1974-04-18"}
    ]

    for p in patients_list:
        new_p = Patient(
            case_no = p["case_no"], 
            last_name = p["last"], 
            first_name = p["first"], 
            middle_name = p["mid"],
            gender = p["gen"], 
            age = p["age"], 
            contact_no = p["contact"], 
            address = p["addr"],
            date_of_birth = datetime.strptime(p["dob"], "%Y-%m-%d").date()
        )
        db.session.add(new_p)
    db.session.commit()

    # ==========================================
    # 2. TABLE: DOCTORS
    # ==========================================
    print("Seeding Doctors...")
    doctors_list = [
        {"lic": "D-1001", "f": "Alice", "l": "Guzman", "spec": "Pediatrics", "rm": "101", "sched": "Mon-Wed-Fri"},
        {"lic": "D-1002", "f": "Ben", "l": "Rosario", "spec": "Cardiology", "rm": "102", "sched": "Tue-Thu-Sat"},
        {"lic": "D-1003", "f": "David", "l": "Sy", "spec": "General Medicine", "rm": "104", "sched": "Daily"},
        {"lic": "D-1004", "f": "Carla", "l": "Pineda", "spec": "Dermatology", "rm": "103", "sched": "Mon-Thu"},
        {"lic": "D-1005", "f": "Elena", "l": "Cruz", "spec": "OB-GYN", "rm": "201", "sched": "Wed-Sat"},
        {"lic": "D-1006", "f": "Francis", "l": "Tiu", "spec": "Orthopedics", "rm": "202", "sched": "Mon-Fri"},
        {"lic": "D-1007", "f": "Grace", "l": "Lee", "spec": "Ophthalmology", "rm": "203", "sched": "Tue-Fri"},
        {"lic": "D-1008", "f": "Hector", "l": "Vega", "spec": "Neurology", "rm": "204", "sched": "Thu-Sat"},
        {"lic": "D-1009", "f": "Irene", "l": "Yap", "spec": "Psychiatry", "rm": "301", "sched": "Mon-Wed"},
        {"lic": "D-1010", "f": "Jack", "l": "Nieves", "spec": "Surgery", "rm": "302", "sched": "On-Call"}
    ]

    for d in doctors_list:
        new_d = Doctor(
            license_no = d["lic"], 
            first_name = d["f"], 
            last_name = d["l"], 
            specialization = d["spec"],
            room_number = d["rm"], 
            schedule_days = d["sched"], 
            phone = "09170000000", 
            email = f"{d['f']}@clinic.com",
            date_hired = datetime.strptime("2020-01-01", "%Y-%m-%d").date()
        )
        db.session.add(new_d)
    db.session.commit()

    # ==========================================
    # 3. TABLE: MEDICAL RECORDS
    # ==========================================
    print("Seeding Medical Records...")
    # Creating 1 record per patient (IDs 1-10)
    records_list = [
        {"pid": 1, "doc": "Alice Guzman", "diag": "Acute Bronchitis", "symp": "Cough, Fever", "bp": "120/80", "wt": 55, "ht": 160},
        {"pid": 2, "doc": "Ben Rosario", "diag": "Hypertension", "symp": "Dizziness", "bp": "150/90", "wt": 70, "ht": 175},
        {"pid": 3, "doc": "David Sy", "diag": "Viral Flu", "symp": "Fever, Chills", "bp": "110/70", "wt": 65, "ht": 168},
        {"pid": 4, "doc": "Carla Pineda", "diag": "Eczema", "symp": "Itchy Skin", "bp": "120/80", "wt": 60, "ht": 165},
        {"pid": 5, "doc": "Elena Cruz", "diag": "Pregnancy Checkup", "symp": "Nausea", "bp": "110/70", "wt": 58, "ht": 155},
        {"pid": 6, "doc": "Francis Tiu", "diag": "Ankle Sprain", "symp": "Swelling, Pain", "bp": "130/80", "wt": 75, "ht": 170},
        {"pid": 7, "doc": "Grace Lee", "diag": "Conjunctivitis", "symp": "Red Eyes", "bp": "120/80", "wt": 50, "ht": 158},
        {"pid": 8, "doc": "Hector Vega", "diag": "Migraine", "symp": "Headache", "bp": "125/85", "wt": 68, "ht": 172},
        {"pid": 9, "doc": "Irene Yap", "diag": "Anxiety Disorder", "symp": "Palpitations", "bp": "120/80", "wt": 52, "ht": 160},
        {"pid": 10, "doc": "Jack Nieves", "diag": "Appendicitis", "symp": "Abdominal Pain", "bp": "140/90", "wt": 80, "ht": 178}
    ]

    for r in records_list:
        new_r = MedicalRecord(
            patient_id = r["pid"], 
            doctor_name = r["doc"], 
            diagnosis = r["diag"], 
            symptoms = r["symp"],
            blood_pressure = r["bp"], 
            weight_kg = r["wt"], 
            height_cm = r["ht"],
            notes = f"Patient advised to rest.", 
            visit_date = datetime.utcnow()
        )
        db.session.add(new_r)
    db.session.commit()

    # ==========================================
    # 4. TABLE: PRESCRIPTIONS
    # ==========================================
    print("Seeding Prescriptions...")
    presc_list = [
        {"rid": 1, "med": "Azithromycin", "dos": "500mg", "freq": "Once daily", "dur": "3 days", "qty": 3},
        {"rid": 2, "med": "Amlodipine", "dos": "10mg", "freq": "Once daily", "dur": "30 days", "qty": 30},
        {"rid": 3, "med": "Paracetamol", "dos": "500mg", "freq": "Every 4 hours", "dur": "5 days", "qty": 15},
        {"rid": 4, "med": "Cetirizine", "dos": "10mg", "freq": "Once daily", "dur": "7 days", "qty": 7},
        {"rid": 5, "med": "Folic Acid", "dos": "5mg", "freq": "Once daily", "dur": "30 days", "qty": 30},
        {"rid": 6, "med": "Ibuprofen", "dos": "400mg", "freq": "Every 6 hours", "dur": "7 days", "qty": 21},
        {"rid": 7, "med": "Tobramycin Drops", "dos": "2 drops", "freq": "4x a day", "dur": "7 days", "qty": 1},
        {"rid": 8, "med": "Sumatriptan", "dos": "50mg", "freq": "As needed", "dur": "N/A", "qty": 10},
        {"rid": 9, "med": "Alprazolam", "dos": "250mcg", "freq": "As needed", "dur": "15 days", "qty": 15},
        {"rid": 10, "med": "Cefalexin", "dos": "500mg", "freq": "3x a day", "dur": "7 days", "qty": 21}
    ]

    for pr in presc_list:
        new_pr = Prescription(
            record_id = pr["rid"], 
            medicine_name = pr["med"], 
            dosage = pr["dos"], 
            frequency = pr["freq"],
            duration = pr["dur"], 
            quantity = pr["qty"], 
            instructions = "Take after meals.",
            prescribed_by = "Attending Physician", 
            date_issued = datetime.utcnow().date()
        )
        db.session.add(new_pr)
    
    # ==========================================
    # 5. TABLE: APPOINTMENTS
    # ==========================================
    print("Seeding Appointments...")
    apps_list = [
        {"pid": 1, "did": 1, "purp": "Follow-up", "stat": "Scheduled"},
        {"pid": 2, "did": 2, "purp": "BP Check", "stat": "Scheduled"},
        {"pid": 3, "did": 3, "purp": "Consultation", "stat": "Completed"},
        {"pid": 4, "did": 4, "purp": "Regular Checkup", "stat": "Scheduled"},
        {"pid": 5, "did": 5, "purp": "Prenatal", "stat": "Scheduled"},
        {"pid": 6, "did": 6, "purp": "Cast Removal", "stat": "Pending"},
        {"pid": 7, "did": 7, "purp": "Eye Exam", "stat": "Completed"},
        {"pid": 8, "did": 8, "purp": "Consultation", "stat": "Cancelled"},
        {"pid": 9, "did": 9, "purp": "Therapy", "stat": "Scheduled"},
        {"pid": 10, "did": 10, "purp": "Surgery Prep", "stat": "Scheduled"}
    ]

    for a in apps_list:
        new_app = Appointment(
            patient_id = a["pid"], 
            doctor_id = a["did"], 
            appointment_date = datetime.utcnow().date(),
            appointment_time = time(9, 0), 
            purpose = a["purp"], 
            status = a["stat"],
            remarks = "Please come on time."
        )
        db.session.add(new_app)
    db.session.commit()
    
    print("Success! All 5 tables populated with 10 rows each.")