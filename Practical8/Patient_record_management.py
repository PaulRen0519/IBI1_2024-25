class patients:
    # define a function to contain all the information needed
    def __init__(self, patient_name, age, date_of_latest_admission, medical_history):
        self.patient_name = patient_name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history

    def print_details(self):
        print(f"Patient Name: {self.patient_name}, Age: {self.age}, Date of Latest Admission: {self.date_of_latest_admission}, Medical History: {self.medical_history}")

# Example
patient1 = patients("Doe", 30, "2024-01-01", "Allergic to peanuts")
patient1.print_details()

# For input personal details
try:
    # Prompt the user to enter details in a comma-separated format
    user_input = input("Enter the details of the patient (e.g., Doe, 30, 2024-01-01, Allergic to peanuts): ")
    # Split the input string by commas and strip whitespace
    details = [x.strip() for x in user_input.split(",")]
    
    # Ensure exactly 4 values are provided
    if len(details) != 4:
        raise ValueError("Please provide exactly 4 values: patient_name, age, date_of_latest_admission, medical_history")
    
    # Extract and convert the values
    patient_name = details[0]
    age = int(details[1])  # Convert age to integer
    date_of_latest_admission = details[2]
    medical_history = details[3]
    
    # Create a new patient object
    details = patients(patient_name, age, date_of_latest_admission, medical_history)
    details.print_details()

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
