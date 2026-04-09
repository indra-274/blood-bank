from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from blood_bank_logic import BloodBankSystem

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Initialize your blood bank system
blood_bank = BloodBankSystem()

@app.route('/')
def index():
    """Home page"""
    stats = blood_bank.get_statistics()
    total_donors = len(blood_bank.get_all_donors())
    return render_template('index.html', stats=stats, total_donors=total_donors)

@app.route('/donors')
def list_donors():
    """Display all donors"""
    donors = blood_bank.get_all_donors()
    return render_template('donors.html', donors=donors)

@app.route('/add_donor', methods=['GET', 'POST'])
def add_donor():
    """Add a new donor"""
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        blood_type = request.form['blood_type']
        contact = request.form['contact']
        last_donation = request.form.get('last_donation', None)
        
        donor = blood_bank.add_donor(name, age, blood_type, contact, last_donation)
        flash(f'Donor {name} added successfully!', 'success')
        return redirect(url_for('list_donors'))
    
    return render_template('add_donor.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    """Search for donors by blood type"""
    if request.method == 'POST':
        blood_type = request.form['blood_type']
        donors = blood_bank.search_by_blood_type(blood_type)
        return render_template('search_results.html', donors=donors, search_type='Blood Type', query=blood_type)
    
    return render_template('search.html')

@app.route('/compatible/<blood_type>')
def compatible_donors(blood_type):
    """Find compatible donors for a patient"""
    donors = blood_bank.find_compatible_donors(blood_type)
    return render_template('search_results.html', donors=donors, search_type='Compatible Donors for', query=blood_type)

@app.route('/delete_donor/<int:donor_id>')
def delete_donor(donor_id):
    """Delete a donor"""
    blood_bank.delete_donor(donor_id)
    flash('Donor deleted successfully!', 'success')
    return redirect(url_for('list_donors'))

@app.route('/api/donors')
def api_donors():
    """REST API endpoint to get donors"""
    return jsonify(blood_bank.get_all_donors())

@app.route('/api/stats')
def api_stats():
    """REST API endpoint to get statistics"""
    return jsonify(blood_bank.get_statistics())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
