from flask import Flask, render_template, Response, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from camera import generate_frames  # Import the camera script
app = Flask(__name__, static_url_path='/static')
app.secret_key = "user_test"  

# The dictionary for storing usernames and passwords
users = {
    "user_test": generate_password_hash("password_test"),  
}

# Handling login logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            next_url = session.pop('next', url_for('index'))  # Pop the URL to redirect to from the session, default to index
            return redirect(next_url)
        else:
            return 'Invalid username or password'
    else:
        return render_template('login.html')

# The previous homepage (login page)
@app.route('/login_home')
def login_home():
    return render_template('login.html')

# The new homepage
@app.route('/')
def main_home():
    return render_template('home.html')

# The index page which is protected (you have to be logged in)
@app.route('/index')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

# The prints page
@app.route('/prints')
def prints():
    '''
    if 'username' not in session:
        return redirect(url_for('login'))
    '''
    return render_template('prints.html')

# Video feed route
@app.route('/video')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='192.168.50.18', port='5000', debug=True)
