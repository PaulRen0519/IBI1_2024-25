# creat a class
class patients:
    # define a function to contain all the information needed
    def __init__(self, patient_name, age, date_of_latest_admission, medical_history):
        self.patient_name = patient_name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history

    def print_details(self):
        print(f"Patient Name: {self.patient_name}, Age: {self.age}, Date of Latest Admission: {self.date_of_latest_admission}, Medical History: {self.medical_history}")

# example
patient1 = patients("Doe", 30, "2024-01-01", "Allergic to peanuts")
patient1.print_details()

details = input("Enter the details of the student (eg. 'Doe', 30, '2024-01-01', 'Allergic to peanuts'): ")
print(patients(details))
