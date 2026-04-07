 blood_bank_logic.py
class BloodBankSystem:
    def __init__(self):
        self.donors = []  # Replace with your existing data structure
        self.requests = []

    def add_donor(self, name, age, blood_type, contact, last_donation=None):
        """Add a new donor to the system"""
        donor = {
            'id': len(self.donors) + 1,
            'name': name,
            'age': age,
            'blood_type': blood_type.upper(),
            'contact': contact,
            'last_donation': last_donation,
            'status': 'active'
        }
        self.donors.append(donor)
        return donor

    def get_all_donors(self):
        """Return list of all donors"""
        return self.donors

