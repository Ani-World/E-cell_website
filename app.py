from flask import Flask, render_template, request, redirect, url_for, flash
from utils.mailer import send_confirmation_mail

app = Flask(__name__)
app.secret_key = "odyssey_secret"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event = request.form['event']
        send_confirmation_mail(name, email, event)
        flash("Ahoy, voyager! Your expedition is registered.")
        return redirect(url_for('success'))
    return render_template('register.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True, port=5002)
