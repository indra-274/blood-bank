# blood_bank_logic.py
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
    
    def search_by_blood_type(self, blood_type):
        """Search donors by blood type"""
        return [d for d in self.donors if d['blood_type'] == blood_type.upper()]
    
    def find_compatible_donors(self, patient_blood_type):
        """Find compatible donors based on blood type compatibility"""
        compatibility = {
            'O-': ['O-'],
            'O+': ['O+', 'O-'],
            'A-': ['A-', 'O-'],
            'A+': ['A+', 'A-', 'O+', 'O-'],
            'B-': ['B-', 'O-'],
            'B+': ['B+', 'B-', 'O+', 'O-'],
            'AB-': ['AB-', 'A-', 'B-', 'O-'],
            'AB+': ['AB+', 'AB-', 'A+', 'A-', 'B+', 'B-', 'O+', 'O-']
        }
        compatible_types = compatibility.get(patient_blood_type, [])
        return [d for d in self.donors if d['blood_type'] in compatible_types]
    
    def delete_donor(self, donor_id):
        """Remove a donor from the system"""
        self.donors = [d for d in self.donors if d['id'] != donor_id]
        return True
    
    def get_statistics(self):
        """Get blood bank statistics"""
        stats = {}
        for donor in self.donors:
            blood_type = donor['blood_type']
            stats[blood_type] = stats.get(blood_type, 0) + 1
        return stats
    
    # Add any other methods from your original Tkinter code here
    # Copy the business logic, not the GUI code
