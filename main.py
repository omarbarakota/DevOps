from flask import Flask, render_template, request, redirect, url_for
import qrcode
import base64
from io import BytesIO  # To generate QR Code img
import secrets  # To generate random passwords
import string  # To Deal with strings (Generate Password Feature)
from datetime import datetime
import requests  # To get any API Request
import jinja2

app = Flask(__name__)

# List to store tasks (global variable for simplicity)
# tasks = ["Task1","Task2","Task3",]
tasks = []
# Route to display the form for text input and password generation and current time


@app.route('/')
def index():
    current_time = datetime.now().strftime('%Y-%B-%d \n%I:%M-%p')
    return render_template('index.html', time=current_time, tasks=tasks)


# Route to handle adding a task
@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

# Route to handle deleting a task


@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))


# Route to handle weather feature
@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    Weather_API_KEY = "1cb9661a8fbc83605a5350071cf0b230"
    if not city:
        return render_template('index.html', error='City name is required')

    # API endpoint for current weather data
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Weather_API_KEY}&units=metric'

    # Make a GET request to the API
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return render_template('weather.html', weather=weather)
    else:
        return render_template('index.html', error='City not found')


# Route to generate and display the QR code
@app.route('/generate', methods=['POST'])
def generate():
    # Get text input from the form
    text = request.form['text']

    # Generate QR code
    qr = qrcode.make(text)
    img = BytesIO()
    qr.save(img, 'PNG')
    img.seek(0)
    qr_img = base64.b64encode(img.getvalue()).decode()

    return render_template('generate.html', qr_img=qr_img, text=text)


# Route to generate a random password
@app.route('/generate_password', methods=['GET'])
def generate_password():
    password_length = 12  # Length of the generated password
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet)
                       for _ in range(password_length))

    return render_template('password.html', password=password)


if __name__ == '__main__':
    app.run(debug=True)
