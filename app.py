from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from services.mail_service import send_confirmation_mail

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# MongoDB Connection
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["empulse2026"]


@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route('/events')
def events():
    return render_template('pages/events.html')


@app.route('/gallery')
def gallery():
    return render_template('pages/gallery.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        event = request.form.get('event')

        # Save to MongoDB
        db.registrations.insert_one({
            "name": name,
            "email": email,
            "event": event
        })

        send_confirmation_mail(name, email, event)

        flash("Ahoy, voyager! Your expedition is registered.")

        return redirect(url_for('success'))

    return render_template('pages/register.html')


@app.route('/success')
def success():
    return render_template('pages/success.html')


if __name__ == "__main__":
    app.run(debug=True, port=5002)