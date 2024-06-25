import sqlite3
from flask import session

def connector():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    # Create the tables
    conn.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT, username TEXT, password TEXT, level INTEGER, score INTEGER, inventory TEXT )')
    print("Table 'users' active")

    conn.execute('CREATE TABLE IF NOT EXISTS results (results TEXT)')
    #conn.execute('DROP TABLE results')

    # Assign the cursor and execute the SELECT statement using it
    c = conn.cursor()
    c.execute("SELECT * FROM results")
    data = c.fetchall()

    print("check-01")
    if data:
        print("TABLE results has data")
    else:
        print("TABLE results is empty. Filling with dummy data.")
        tmp_str = ""
        for i in range(51):
            tmp_str += "E-E"
            if i != 50:
                tmp_str += ","
        c.execute("INSERT INTO results (results) VALUES (?)", (tmp_str,))  # Make sure the data is inserted using the cursor
        conn.commit()
    conn.close()
    
    
def check_login(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    data = c.fetchall()
    conn.close()
    if len(data) == 0:
        return False
    return True

def check_existing_user(username):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? ", (username,))
    data = c.fetchall()
    conn.close()
    if len(data) == 0:
        return False
    return True

def create_predictions():
    out = ""
    for i in range(50):
        out += "0-0,"
    out += "0-0"
    return out

def get_user_data(username):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    data = c.fetchall()
    conn.close()
    return data

def get_match_results():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM results")
    data = c.fetchall()
    conn.close()
    return data[0]

def register_user(name, email, username, password, level, score):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    inventory = create_predictions()
    c.execute("INSERT INTO users (name, email, username, password, level, score, inventory) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, email, username, password, level, score, inventory))
    conn.commit()
    conn.close()

def update_user(username, inventory, level, score):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("UPDATE users SET level = ?, score = ?, inventory = ? WHERE username = ?", (level, score, inventory, username))
    conn.commit()
    conn.close()

'''
def delete_user(username):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    print(f"DELETING user {username}")
    c.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()
    conn.close()
'''

def delete_user(username):
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        print(f"DELETING user {username}")

        # Check if the user exists before attempting to delete
        c.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
        user_count = c.fetchone()[0]
        
        if user_count == 0:
            print(f"User {username} does not exist.")
        else:
            c.execute("DELETE FROM users WHERE username = ?", (username,))
            conn.commit()
            print(f"User {username} deleted successfully.")
        
        conn.close()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

def update_match_results(updated_results):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("UPDATE results SET results = ?", (updated_results,))
    conn.commit()
    conn.close()

'''
def store(username, score, level, inventory, objects):
    #store in Session
    session['user'] = username
    session['score'] = score
    session['level'] = level
    session['inventory'] = inventory
    session['objects'] = objects
'''

def get_admin_info():
    info = {}
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    info['nr_of_users'] = str(len(data))
    return info

def outcome_score(current_result, current_prediction):
    pred_home_score = current_prediction[0]
    pred_away_score = current_prediction[2]
    resu_home_score = current_result[0]
    resu_away_score = current_result[2]
    if pred_home_score > pred_away_score:
        pred = "home"
    elif pred_home_score < pred_away_score:
        pred = "away"
    else:
        pred = "tie"
    if resu_home_score > resu_away_score:
        resu = "home"
    elif resu_home_score < resu_away_score:
        resu = "away"
    else:
        resu = "tie"
    if pred == resu:
        return 1
    else:
        return 0

def calc_score(predictions_raw):
    score = 0
    match_results = get_match_results()[0].split(",")
    predictions = predictions_raw.split(",")
    print("=== function calc_score ==")
    print(f"predictions: {predictions}")
    print(f"match_results: {match_results}")
    for i, match in enumerate(match_results):
        if match != "E-E":
            current_result = match
            current_prediction = predictions[i]
            if current_result == current_prediction:
                score += 3
                print(f"Added 3 points: pred = {current_prediction}, result = {current_result}")
            print(f"[function calc_score] current_result: {current_result}, current_prediction: {current_prediction}")
            score_for_predicting_result = outcome_score(current_result, current_prediction)
            print(f"Points for predicting outcome: {score_for_predicting_result}")
            score += score_for_predicting_result
    print(f">> new score: {score}")
    return score

def recalc_score_all():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    level = 1
    print("  >>> feching data")
    for row in data:
        username = row[2]
        predictions = row[6]
        score = calc_score(predictions)
        update_user(username, predictions, level, score)

def calc_ranking():
    ranking = []
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    print("  >>> feching data")
    
    for row in data:
        if "admin" not in row[0]:
            tmp_list = []
            tmp_list.append(row[0])
            tmp_list.append(row[5])
            ranking.append(tmp_list)

    ranking_sorted = sorted(ranking, key=lambda x: x[1], reverse=True)

    
    return ranking_sorted