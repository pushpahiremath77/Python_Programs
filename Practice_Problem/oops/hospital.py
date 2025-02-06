# Appointment: Represents a patient's visit, containing appointment_date and reason_for_visit.
# How would you model the interaction between doctors, patients, and appointments?

class Doctor:
    def __init__(self,dr_name,specialization,availability):
        self.dr_name = dr_name
        self.specialization=specialization
        self.availability = availability

class Patient:
    def __init__(self,name,age,medical_history):
        self.name = name
        self.age = age
        self.medical_history = medical_history
        self.doctor_assigned = None

    def assign_doctor(self, doctor):
        self.doctor_assigned = doctor

class Appointment:
    def __init__(self, patient, doctor, appointment_date, reason_for_visit):
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date
        self.reason_for_visit = reason_for_visit

    def __repr__(self):
        return f"Appointment for {self.patient.name} with {self.doctor.dr_name} on {self.appointment_date} for {self.reason_for_visit}"

d1 = Doctor("Dr.Alice","cardiolist","Monday to Friday")
d2 = Doctor("Dr.Bob", "Neurologist", "Weekends")

patient1 = Patient("John", 60, "Diabetes, Stroke History")

patient1.assign_doctor(d1)

appointment1 = Appointment(patient1, d1, "2025-01-15", "Regular Checkup")
print(appointment1)










def modify_string(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'

# Test cases
print(modify_string('abc'))    # Output: 'abcing'
print(modify_string('string')) # Output: 'stringly'
