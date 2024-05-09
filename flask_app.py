from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_session import Session
from database import connector, check_login, register_user, get_user_data, Room, init_rooms, update_user, store, get
import sqlite3


app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secret-key-123'
app.config['SESSION_TYPE'] = 'filesystem'

db = connector()
print(db)

        
@app.route('/', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
            return redirect(url_for('login'))
    
    
    
    if request.method == 'POST':
        pass

    msg = "Welcome to the European Championship Soccer Pool - 2024 - Please choose an option from the menu on the right of the screen."
    inventory = "inventory"
    user_level = "user_level"
    username = session['user']
    score = 1000

    return render_template('home.html', msg=msg, inventory=inventory, user_level=user_level, username=username, score=score)


@app.route('/my_predictions', methods=['GET', 'POST'])
def my_predictions():
    msg = ""
    inventory = "inventory"
    user_level = "user_level"
    username = session['user']
    score = 1000
    return render_template('my_predictions.html', msg=msg, inventory=inventory, user_level=user_level, username=username, score=score)

@app.route('/edit_predictions', methods=['GET', 'POST'])
def edit_predictions():
    msg = ""
    inventory = "inventory"
    user_level = "user_level"
    username = session['user']
    score = 1000
    return render_template('edit_predictions.html', msg=msg, inventory=inventory, user_level=user_level, username=username, score=score)

@app.route('/ranking', methods=['GET', 'POST'])
def ranking():
    msg = ""
    inventory = "inventory"
    user_level = "user_level"
    username = session['user']
    score = 1000
    return render_template('my_predictions.html', msg=msg, inventory=inventory, user_level=user_level, username=username, score=score)

@app.route('/info', methods=['GET', 'POST'])
def info():
    msg = ""
    inventory = "inventory"
    user_level = "user_level"
    username = session['user']
    score = 1000
    return render_template('info.html', msg=msg, inventory=inventory, user_level=user_level, username=username, score=score)

@app.route('/pool_info', methods=['GET', 'POST'])
def pool_info():
    msg = ""
    inventory = "inventory"
    user_level = "user_level"
    username = session['user']
    score = 1000
    return render_template('pool_info.html', msg=msg, inventory=inventory, user_level=user_level, username=username, score=score)





@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are valid

        if check_login(username, password):
            msg = 'Username already exists'
            return render_template('register.html', msg=msg)

        # Register the user
        register_user(name, email, username, password, 1, 100, "")

        return redirect(url_for('login'))

    return render_template('register.html', msg=msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    global rooms
    msg = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are valid

        if check_login(username, password):
            session['user'] = username
            print("user logged in")
            level = get_user_data(username)[0][4]
            score = get_user_data(username)[0][5]
            inventory = []
            inventory_string = get_user_data(username)[0][6]
            if inventory_string != "":
                inventory = inventory_string.split(",")

            session['level'] = level
            session['score'] = score
            session['inventory'] = inventory

            return redirect(url_for('home'))
        else:
            msg = "Invalid login"
            print(f"Invalid login: {username}, {password}")
            

    return render_template('login.html', msg=msg)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('home'))

# dump all the data in the database to the screen
@app.route('/dump1', methods=['GET', 'POST'])
def dump1():
    if 'user' not in session:
            return redirect(url_for('login'))

    if session['user'] != 'admin':
        return redirect(url_for('home'))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()

    lines = []

    for row in data:
        lines.append(row)

    return render_template('dump.html', lines=lines)



# -------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
