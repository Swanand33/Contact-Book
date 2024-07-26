import sys
import os
from flask import Flask, render_template, request, redirect, url_for, flash

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from contact_book.contact_manager import ContactManager
from contact_book.file_handler import FileHandler

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the FileHandler and ContactManager
file_handler = FileHandler(os.path.join(os.path.dirname(__file__), '../data/contacts.json'))
contact_manager = ContactManager(file_handler)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        if name and phone and email:
            contact_manager.add_contact(name, phone, email)
            flash('Contact added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('All fields are required!', 'danger')
    return render_template('add_contact.html')

@app.route('/view')
def view_contacts():
    contacts = contact_manager.get_all_contacts()
    return render_template('view_contacts.html', contacts=contacts)

@app.route('/search', methods=['GET', 'POST'])
def search_contact():
    if request.method == 'POST':
        search_term = request.form['search_term']
        contacts = contact_manager.search_contact(search_term)
        return render_template('view_contacts.html', contacts=contacts)
    return render_template('search_contact.html')

if __name__ == '__main__':
    app.run(debug=True)