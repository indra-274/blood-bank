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

