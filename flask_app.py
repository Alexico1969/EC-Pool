from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_session import Session
from database import connector, check_login, register_user, get_user_data, update_user, get_admin_info, get_match_results, update_match_results, calc_score, calc_ranking, check_existing_user, recalc_score_all
from helper import p_array, p_array_edit, today, value_date
import sqlite3


app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secret-key-123'
app.config['SESSION_TYPE'] = 'filesystem'

db = connector()
print(db)

print(today())
print(f"Today's value: {value_date(today())}")
print(f"July 1st's value: {value_date('Sat Jul 1')}")

        
@app.route('/', methods=['GET', 'POST'])
def home():

    if 'user' not in session:
            return redirect(url_for('login'))
    
    if request.method == 'POST':
        pass

    msg = "Welcome to the European Championship Soccer Pool - 2024  ⚽ <br>Please choose an option from the menu on the right of the screen 👉👉👉"
    username = session['user']
    user_data = get_user_data(username)
    score = user_data[0][5]
    return render_template('home.html', msg=msg, username=username, score=score)

@app.route('/admin', methods=['GET', 'POST'])
def admin():

    if 'user' not in session:
            return redirect(url_for('login'))
    
    username = session['user']
    if username != 'admin':
        return redirect('/')

    if request.method == 'POST':
        pass

    admin_data = get_admin_info()

    nr_of_users = admin_data['nr_of_users']

    msg = "⚽ ADMIN PAGE ⚽<br>Restricted Access"
    username = session['user']
    user_data = get_user_data(username)
    score = user_data[0][5]
    return render_template('admin.html', msg=msg, username=username, score=score, nr_of_users=nr_of_users)

@app.route('/my_predictions', methods=['GET', 'POST'])
def my_predictions():
    if 'user' not in session:
            return redirect(url_for('login'))
    msg = ""
    user_level = "user_level"
    username = session['user']
    user_data = get_user_data(username)
    #print(f"User data: {user_data}")
    score = user_data[0][5]
    predictions_raw = user_data[0][6]
    predictions = p_array(predictions_raw)

    return render_template('my_predictions.html', msg=msg, user_level=user_level, username=username, score=score, predictions = predictions)

@app.route('/edit_predictions', methods=['GET', 'POST'])
def edit_predictions():
    if 'user' not in session:
            return redirect(url_for('login'))
    msg = ""
    today_val = value_date(today())
    #today_val = value_date("Fri Jun 20") # to test if predictions can be made for today's match or matches in the past (should not be able)
    username = session['user']
    user_data = get_user_data(username)
    #print(f"User data: {user_data}")
    score = user_data[0][5]
    predictions_raw = user_data[0][6]
    predictions = p_array_edit(predictions_raw)
    

    return render_template('edit_predictions.html', msg=msg, username=username, score=score, predictions = predictions, today_val=today_val)

@app.route('/process_predictions', methods=['GET','POST'])
def process_predictions():
    if 'user' not in session:
            return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Assuming you handle the POST data here
        username = session.get('user')
        if not username:
            return jsonify({"error": "User not logged in"}), 403
        
        user_data = get_user_data(username)
        score = user_data[0][5]

        # Process the incoming data from the request
        # For example, updating the score predictions
        # Let's assume you receive and process the predictions data from the request JSON
        predictions = request.json  # This assumes the frontend sends a JSON payload
        total_str = ""
        for i in range(51):
            tmp_str = ""
            key = str(i + 1) + "H"
            tmp_str += predictions[key]
            tmp_str += "-"
            key = str(i + 1) + "A"
            tmp_str += predictions[key]
            if i != 50:
                tmp_str += ","
            total_str += tmp_str
        
        #print(f">> total_str: {total_str}")
        level = 1
        inventory = total_str
        #score = calc_score(predictions)
        update_user(username, inventory, level, score)
        user_data = get_user_data(username)
        #print(f"&&& user_data: {user_data}")
        updated_predictions = user_data[0][6]
        score = calc_score(updated_predictions)
        update_user(username, inventory, level, score)
        

        # Update the user's predictions in your database or storage here

        return jsonify({
            "message": "Your predictions have been saved. (POST)",
            "score": score,
            "username": username
        })

    elif request.method == 'GET':
        # If it's a GET request, render the HTML template as before
        username = session.get('user')
        if not username:
            return "User not logged in", 403

        user_data = get_user_data(username)
        score = user_data[0][5]
        msg = "Your predictions have been saved.(GET)"
        
        return render_template('process_predictions.html', msg=msg, score=score, username=username)

    else:
        return "Invalid method", 405
    
@app.route('/match_results', methods=['GET', 'POST'])
def match_results():
    if 'user' not in session:
            return redirect(url_for('login'))
    msg = ""
    user_level = "user_level"
    username = session['user']
    user_data = get_user_data(username)
    #print(f"User data: {user_data}")
    score = user_data[0][5]
    match_results_raw = get_match_results()[0]
    #print(f"match_resuls_raw: {match_results_raw}")
    match_results = p_array_edit(match_results_raw)

    return render_template('match_results.html', msg=msg, user_level=user_level, username=username, score=score, match_results=match_results)
    
@app.route('/edit_match_results', methods=['GET', 'POST'])
def edit_match_results():
    if 'user' not in session:
            return redirect(url_for('login'))

    if session['user'] != 'admin':
        return redirect(url_for('home'))
    username = session['user']
    user_data = get_user_data(username)
    score = user_data[0][5]
    msg = ""
    match_results_raw = get_match_results()[0]
    #print(f"match_resuls_raw: {match_results_raw}")
    match_results = p_array_edit(match_results_raw)

    return render_template('edit_match_results.html', msg=msg, username=username, score=score, match_results=match_results)

@app.route('/process_match_results', methods=['GET','POST'])
def process_match_results():
    if 'user' not in session:
            return redirect(url_for('login'))
    if request.method == 'POST':
        # Assuming you handle the POST data here
        username = session.get('user')
        if username != "admin":
            return jsonify({"error": "Access restricted to admins only"}), 403
        
        user_data = get_user_data(username)
        score = user_data[0][5]

        # Process the incoming data from the request
        # For example, updating the score match_results
        # Let's assume you receive and process the match_results data from the request JSON
        match_results = request.json  # This assumes the frontend sends a JSON payload
        #print(f">> match_results: {match_results}")
        total_str = ""
        for i in range(51):
            tmp_str = ""
            key = str(i + 1) + "H"
            tmp_str += match_results[key]
            tmp_str += "-"
            key = str(i + 1) + "A"
            tmp_str += match_results[key]
            if i != 50:
                tmp_str += ","
            total_str += tmp_str
        
        #print(f">> total_str: {total_str}")
        level = 1
        inventory = total_str
        update_match_results(inventory)
        recalc_score_all()

        # Update the user's match_results in your database or storage here

        return jsonify({
            "message": "Your match_results have been saved. (POST)",
            "score": score,
            "username": username
        })

    elif request.method == 'GET':
        # If it's a GET request, render the HTML template as before
        username = session.get('user')
        if not username:
            return "User not logged in", 403

        user_data = get_user_data(username)
        score = user_data[0][5]
        msg = "Your match_results have been saved.(GET)"
        return render_template('process_match_results.html', msg=msg, score=score, username=username)

    else:
        return "Invalid method", 405

@app.route('/ranking', methods=['GET', 'POST'])
def ranking():
    if 'user' not in session:
            return redirect(url_for('login'))
    msg = ""
    inventory = "inventory"
    user_level = "user_level"
    username = session['user']
    user_data = get_user_data(username)
    score = user_data[0][5]
    ranking_data = calc_ranking()
    print(f"Ranking data: {ranking_data}")
    return render_template('ranking.html', msg=msg, inventory=inventory, user_level=user_level, username=username, score=score, ranking_data=ranking_data)

@app.route('/info', methods=['GET', 'POST'])
def info():
    if 'user' not in session:
            return redirect(url_for('login'))
    msg = ""
    inventory = "inventory"
    user_level = "user_level"
    username = session['user']
    user_data = get_user_data(username)
    score = user_data[0][5]
    return render_template('info.html', msg=msg, inventory=inventory, user_level=user_level, username=username, score=score)

@app.route('/pool_info', methods=['GET', 'POST'])
def pool_info():
    if 'user' not in session:
            return redirect(url_for('login'))
    msg = ""
    inventory = "inventory"
    user_level = "user_level"
    username = session['user']
    user_data = get_user_data(username)
    score = user_data[0][5]
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
        
        if check_existing_user(username):
            msg = 'Username already exists'
            return render_template('register.html', msg=msg)

        # Register the user
        register_user(name, email, username, password, 1, 0)

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

    lines = ["TABLE users: ",]

    for row in data:
        lines.append(row)

    c = conn.cursor()
    c.execute("SELECT * FROM results")
    data = c.fetchall()
    conn.close()

    lines.append(" ")
    lines.append("TABLE results:")

    for row in data:
        lines.append(row)




    return render_template('dump.html', lines=lines)



# -------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
