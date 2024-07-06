import datetime

matches_backup = [
        ["1","Fri Jun 14","3 p.m. ET","A","Germany vs. Scotland"],
        ["2","Sat Jun 15","9 a.m. ET","A","Hungary vs. Switzerland"],
        ["3","Sat Jun 15","midday ET","B","Spain vs. Croatia"],
        ["4","Sat Jun 15","3 p.m. ET","B","Italy vs. Albania"],
        ["5","Sun Jun 16","9 a.m. ET","D","Poland vs. Netherlands"],
        ["6","Sun Jun 16","midday ET","C","Slovenia vs. Denmark"],
        ["7","Sun Jun 16","3 p.m. ET","C","Serbia vs. England"],
        ["8","Mon Jun 17","9 a.m. ET","E","Romania vs. Ukraine"],
        ["9","Mon Jun 17","midday ET","E","Belgium vs. Slovakia"],
        ["10","Mon Jun 17","3 p.m. ET","D","Austria vs. France"],
        ["11","Tue Jun 18","midday ET","F","Turkey vs. Georgia"],
        ["12","Tue Jun 18","3 p.m. ET","F","Portugal vs. Czechia"],
        ["13","Wed Jun 19","9 a.m. ET","B","Croatia vs. Albania"],
        ["14","Wed Jun 19","midday ET","A","Germany vs. Hungary"],
        ["15","Wed Jun 19","3 p.m. ET","A","Scotland vs. Switzerland"],
        ["16","Thu Jun 20","9 a.m. ET","C","Slovenia vs. Serbia"],
        ["17","Thu Jun 20","midday ET","C","Denmark vs. England"],
        ["18","Thu Jun 20","3 p.m. ET","B","Spain vs. Italy"],
        ["19","Fri Jun 21","9 a.m. ET","E","Slovakia vs. Ukraine"],
        ["20","Fri Jun 21","midday ET","D","Poland vs. Austria"],
        ["21","Fri Jun 21","3 p.m. ET","D","Netherlands vs. France"],
        ["22","Sat Jun 22","9 a.m. ET","F","Georgia vs. Czechia"],
        ["23","Sat Jun 22","midday ET","F","Turkey vs. Portugal"],
        ["24","Sat Jun 22","3 p.m. ET","E","Belgium vs. Romania"],
        ["25","Sun Jun 23","3 p.m. ET","A","Switzerland vs. Germany"],
        ["26","Sun Jun 23","3 p.m. ET","A","Scotland vs. Hungary"],
        ["27","Mon Jun 24","3 p.m. ET","B","Albania vs. Spain"],
        ["28","Mon Jun 24","3 p.m. ET","B","Croatia vs. Italy"],
        ["29","Tue Jun 25","midday ET","D","France vs. Poland"],
        ["30","Tue Jun 25","midday ET","D","Netherlands vs. Austria"],
        ["31","Tue Jun 25","3 p.m. ET","C","England vs. Slovenia"],
        ["32","Tue Jun 25","3 p.m. ET","C","Denmark vs. Serbia"],
        ["33","Wed Jun 26","midday ET","E","Ukraine vs. Belgium"],
        ["34","Wed Jun 26","midday ET","E","Slovakia vs. Romania"],
        ["35","Wed Jun 26","3 p.m. ET","F","Czechia vs. Turkey"],
        ["36","Wed Jun 26","3 p.m. ET","F","Georgia vs. Portugal"],
        ["37","Sat Jun 29","3 p.m. ET","-","Germany vs. Denmark"],
        ["38","Sat Jun 29","midday ET","-","Switzerland vs. Italy"],
        ["39","Sun Jun 30","3 p.m. ET","-","Spain vs. Georgia"],
        ["40","Sun Jun 30","midday ET","-","England vs. Slovakia"],
        ["41","Mon Jul 1","3 p.m. ET","-","Portugal vs. Slovenia"],
        ["42","Mon Jul 1","midday ET","-","France vs. Belgium"],
        ["43","Tue Jul 2","midday ET","-","Romania vs. Netherlands"],
        ["44","Tue Jul 2","3 p.m. ET","-","Austria vs. Turkiye"],
        ["45","Fri Jul 5","midday ET","-","Spain vs. Germany"],
        ["46","Fri Jul 5","3 p.m. ET","-","Portugal vs. France"],
        ["47","Sat Jul 6","3 p.m. ET","-","Netherlands vs. Turkey"],
        ["48","Sat Jul 6","midday ET","-","England vs. Switzerland"],
        ["49","Tue Jul 9","3 p.m. ET","-","Spain vs. France"],
        ["50","Wed Jul 10","3 p.m. ET","-","Win. 47 vs. Win. 48"],
        ["51","Sun Jul 14","3 p.m. ET","-","FIN: Win. 49 vs. Win. 50"]

]



def p_array(raw):
    matches = [
        ["1","Fri Jun 14","3 p.m. ET","A","Germany vs. Scotland"],
        ["2","Sat Jun 15","9 a.m. ET","A","Hungary vs. Switzerland"],
        ["3","Sat Jun 15","midday ET","B","Spain vs. Croatia"],
        ["4","Sat Jun 15","3 p.m. ET","B","Italy vs. Albania"],
        ["5","Sun Jun 16","9 a.m. ET","D","Poland vs. Netherlands"],
        ["6","Sun Jun 16","midday ET","C","Slovenia vs. Denmark"],
        ["7","Sun Jun 16","3 p.m. ET","C","Serbia vs. England"],
        ["8","Mon Jun 17","9 a.m. ET","E","Romania vs. Ukraine"],
        ["9","Mon Jun 17","midday ET","E","Belgium vs. Slovakia"],
        ["10","Mon Jun 17","3 p.m. ET","D","Austria vs. France"],
        ["11","Tue Jun 18","midday ET","F","Turkey vs. Georgia"],
        ["12","Tue Jun 18","3 p.m. ET","F","Portugal vs. Czechia"],
        ["13","Wed Jun 19","9 a.m. ET","B","Croatia vs. Albania"],
        ["14","Wed Jun 19","midday ET","A","Germany vs. Hungary"],
        ["15","Wed Jun 19","3 p.m. ET","A","Scotland vs. Switzerland"],
        ["16","Thu Jun 20","9 a.m. ET","C","Slovenia vs. Serbia"],
        ["17","Thu Jun 20","midday ET","C","Denmark vs. England"],
        ["18","Thu Jun 20","3 p.m. ET","B","Spain vs. Italy"],
        ["19","Fri Jun 21","9 a.m. ET","E","Slovakia vs. Ukraine"],
        ["20","Fri Jun 21","midday ET","D","Poland vs. Austria"],
        ["21","Fri Jun 21","3 p.m. ET","D","Netherlands vs. France"],
        ["22","Sat Jun 22","9 a.m. ET","F","Georgia vs. Czechia"],
        ["23","Sat Jun 22","midday ET","F","Turkey vs. Portugal"],
        ["24","Sat Jun 22","3 p.m. ET","E","Belgium vs. Romania"],
        ["25","Sun Jun 23","3 p.m. ET","A","Switzerland vs. Germany"],
        ["26","Sun Jun 23","3 p.m. ET","A","Scotland vs. Hungary"],
        ["27","Mon Jun 24","3 p.m. ET","B","Albania vs. Spain"],
        ["28","Mon Jun 24","3 p.m. ET","B","Croatia vs. Italy"],
        ["29","Tue Jun 25","midday ET","D","France vs. Poland"],
        ["30","Tue Jun 25","midday ET","D","Netherlands vs. Austria"],
        ["31","Tue Jun 25","3 p.m. ET","C","England vs. Slovenia"],
        ["32","Tue Jun 25","3 p.m. ET","C","Denmark vs. Serbia"],
        ["33","Wed Jun 26","midday ET","E","Ukraine vs. Belgium"],
        ["34","Wed Jun 26","midday ET","E","Slovakia vs. Romania"],
        ["35","Wed Jun 26","3 p.m. ET","F","Czechia vs. Turkey"],
        ["36","Wed Jun 26","3 p.m. ET","F","Georgia vs. Portugal"],
        ["37","Sat Jun 29","3 p.m. ET","-","Germany vs. Denmark"],
        ["38","Sat Jun 29","midday ET","-","Switzerland vs. Italy"],
        ["39","Sun Jun 30","3 p.m. ET","-","Spain vs. Georgia"],
        ["40","Sun Jun 30","midday ET","-","England vs. Slovakia"],
        ["41","Mon Jul 1","3 p.m. ET","-","Portugal vs. Slovenia"],
        ["42","Mon Jul 1","midday ET","-","France vs. Belgium"],
        ["43","Tue Jul 2","midday ET","-","Romania vs. Netherlands"],
        ["44","Tue Jul 2","3 p.m. ET","-","Austria vs. Turkiye"],
        ["45","Fri Jul 5","midday ET","-","Spain vs. Germany"],
        ["46","Fri Jul 5","3 p.m. ET","-","Portugal vs. France"],
        ["47","Sat Jul 6","3 p.m. ET","-","Netherlands vs. Turkey"],
        ["48","Sat Jul 6","midday ET","-","England vs. Switzerland"],
        ["49","Tue Jul 9","3 p.m. ET","-","Spain vs. France"],
        ["50","Wed Jul 10","3 p.m. ET","-","Netherlands vs. England"],
        ["51","Sun Jul 14","3 p.m. ET","-","FIN: Win. 49 vs. Win. 50"]

    ]
 
    # This function takes in the user's predictions as a string ("0-0, 1-1, ...."), then adds match info and returns an array like this:
    # [['1', 'Fri Jun 14', '3 p.m. ET', 'A', 'Germany vs. Scotland', '0', '0'], ['2', 'Sat Jun 15', '9 a.m. ET', 'A', 'Hungary vs. Switzerland', '0', '0'], etc.

    out_list = []
    p_matches = raw.split(",")
    m = list(matches)
    
    # merging matches with user predictions
    for i, match in enumerate(m):
        match.append(p_matches[i])
        out_list.append(match)
    for i, el in enumerate(out_list):
        tmp = el[5]
        #if i < 3:
            #print(f"#{i} : {tmp}, outlist[0] = {out_list[0]}")
        tmp2 = tmp.split("-")
        out_list[i][5] = tmp2[0]
        out_list[i].append(tmp2[1])
    return out_list

def p_array_edit(raw):
    matches = [
        ["1","Fri Jun 14","3 p.m. ET","A","Germany vs. Scotland"],
        ["2","Sat Jun 15","9 a.m. ET","A","Hungary vs. Switzerland"],
        ["3","Sat Jun 15","midday ET","B","Spain vs. Croatia"],
        ["4","Sat Jun 15","3 p.m. ET","B","Italy vs. Albania"],
        ["5","Sun Jun 16","9 a.m. ET","D","Poland vs. Netherlands"],
        ["6","Sun Jun 16","midday ET","C","Slovenia vs. Denmark"],
        ["7","Sun Jun 16","3 p.m. ET","C","Serbia vs. England"],
        ["8","Mon Jun 17","9 a.m. ET","E","Romania vs. Ukraine"],
        ["9","Mon Jun 17","midday ET","E","Belgium vs. Slovakia"],
        ["10","Mon Jun 17","3 p.m. ET","D","Austria vs. France"],
        ["11","Tue Jun 18","midday ET","F","Turkey vs. Georgia"],
        ["12","Tue Jun 18","3 p.m. ET","F","Portugal vs. Czechia"],
        ["13","Wed Jun 19","9 a.m. ET","B","Croatia vs. Albania"],
        ["14","Wed Jun 19","midday ET","A","Germany vs. Hungary"],
        ["15","Wed Jun 19","3 p.m. ET","A","Scotland vs. Switzerland"],
        ["16","Thu Jun 20","9 a.m. ET","C","Slovenia vs. Serbia"],
        ["17","Thu Jun 20","midday ET","C","Denmark vs. England"],
        ["18","Thu Jun 20","3 p.m. ET","B","Spain vs. Italy"],
        ["19","Fri Jun 21","9 a.m. ET","E","Slovakia vs. Ukraine"],
        ["20","Fri Jun 21","midday ET","D","Poland vs. Austria"],
        ["21","Fri Jun 21","3 p.m. ET","D","Netherlands vs. France"],
        ["22","Sat Jun 22","9 a.m. ET","F","Georgia vs. Czechia"],
        ["23","Sat Jun 22","midday ET","F","Turkey vs. Portugal"],
        ["24","Sat Jun 22","3 p.m. ET","E","Belgium vs. Romania"],
        ["25","Sun Jun 23","3 p.m. ET","A","Switzerland vs. Germany"],
        ["26","Sun Jun 23","3 p.m. ET","A","Scotland vs. Hungary"],
        ["27","Mon Jun 24","3 p.m. ET","B","Albania vs. Spain"],
        ["28","Mon Jun 24","3 p.m. ET","B","Croatia vs. Italy"],
        ["29","Tue Jun 25","midday ET","D","France vs. Poland"],
        ["30","Tue Jun 25","midday ET","D","Netherlands vs. Austria"],
        ["31","Tue Jun 25","3 p.m. ET","C","England vs. Slovenia"],
        ["32","Tue Jun 25","3 p.m. ET","C","Denmark vs. Serbia"],
        ["33","Wed Jun 26","midday ET","E","Ukraine vs. Belgium"],
        ["34","Wed Jun 26","midday ET","E","Slovakia vs. Romania"],
        ["35","Wed Jun 26","3 p.m. ET","F","Czechia vs. Turkey"],
        ["36","Wed Jun 26","3 p.m. ET","F","Georgia vs. Portugal"],
        ["37","Sat Jun 29","3 p.m. ET","-","Germany vs. Denmark"],
        ["38","Sat Jun 29","midday ET","-","Switzerland vs. Italy"],
        ["39","Sun Jun 30","3 p.m. ET","-","Spain vs. Georgia"],
        ["40","Sun Jun 30","midday ET","-","England vs. Slovakia"],
        ["41","Mon Jul 1","3 p.m. ET","-","Portugal vs. Slovenia"],
        ["42","Mon Jul 1","midday ET","-","France vs. Belgium"],
        ["43","Tue Jul 2","midday ET","-","Romania vs. Netherlands"],
        ["44","Tue Jul 2","3 p.m. ET","-","Austria vs. Turkiye"],
        ["45","Fri Jul 5","midday ET","-","Spain vs. Germany"],
        ["46","Fri Jul 5","3 p.m. ET","-","Portugal vs. France"],
        ["47","Sat Jul 6","3 p.m. ET","-","Netherlands vs. Turkey"],
        ["48","Sat Jul 6","midday ET","-","England vs. Switzerland"],
        ["49","Tue Jul 9","3 p.m. ET","-","Spain vs. France"],
        ["50","Wed Jul 10","3 p.m. ET","-","Netherlands vs. England"],
        ["51","Sun Jul 14","3 p.m. ET","-","FIN: Win. 49 vs. Win. 50"]

    ]
 
 
    # This function takes in the user's predictions as a string ("0-0, 1-1, ...."), then adds match info and returns an array like this:
    # [['1', 'Fri Jun 14', '3 p.m. ET', 'A', 'Germany vs. Scotland', '0', '0'], ['2', 'Sat Jun 15', '9 a.m. ET', 'A', 'Hungary vs. Switzerland', '0', '0'], etc.

    out_list = []
    p_matches = raw.split(",")
    m = list(matches)
    
    # merging matches with user predictions
    for i, match in enumerate(m):
        match.append(p_matches[i])
        out_list.append(match)
    for i, el in enumerate(out_list):
        tmp = el[5]
        #if i < 3:
            #print(f"#{i} : {tmp}, outlist[0] = {out_list[0]}")
        tmp2 = tmp.split("-")
        out_list[i][5] = tmp2[0]
        out_list[i].append(tmp2[1])
        out_list[i].append(value_date(out_list[i][1]))
        #if i < 3:
            #print(f"#{i} : {tmp}, outlist[{i}] = {out_list[i]}")
    return out_list

def today():
    # Get the current date
    current_date = datetime.datetime.now()

    # Format the date as "Day Abbreviation Month Abbreviation Day Number"
    formatted_date = current_date.strftime("%a %b %d")

    # Print the formatted date
    print(f"Today's date: {formatted_date}")
    return(formatted_date)

def value_date(date):
    value = 0
    date_list = date.split(" ")
    if date_list[1] == "May":
        value += 50
    elif date_list[1] == "Jun":
        value += 100
    elif date_list[1] == "Jul":
        value += 150
    value += int(date_list[2])
    return value
