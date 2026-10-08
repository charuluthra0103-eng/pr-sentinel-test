API_KEY = "sk-test-hardcoded-123"   # hardcoded secret

def get_patient(patient_id):
    print(f"Patient SSN lookup: {patient_id}")   # PHI in logs
    query = "SELECT * FROM Patients WHERE Id = " + patient_id   # SQL injection
    return query
