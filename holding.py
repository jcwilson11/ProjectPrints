from flask import Flask, render_template, Response
from camera import generate_frames

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='192.168.50.18', port='5000', debug=True)


# login
from flask import Flask, render_template, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# The password should be hashed in production applications
users = {
    "": generate_password_hash("")  # replace with your desired username and password
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username], password):
        return username

@app.route('/')
@auth.login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username], password):
            return redirect(url_for('index'))  # Redirect to the main page after successful login
        else:
            return 'Invalid username or password'
    else:
        return render_template('login.html')  # Display the login page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)




