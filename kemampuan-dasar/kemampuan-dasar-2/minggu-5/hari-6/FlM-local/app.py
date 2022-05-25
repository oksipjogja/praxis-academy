from flask import Flask, render_template

app = Flask(__name__)

# Route
from user import routes

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
  return render_template('dashboard.html')
