from application import app
from flask import Flask, redirect, request, url_for,render_template, Response, jsonify
import pandas as pd
import requests
import json

@app.route('/', methods=['GET','POST']) 
def home():
    return render_template("homepage.html")#"wanna play?" + '<br><br><a href="/1">Start a tournament?</a> </br>'

## Tutorial section ##

@app.route('/tutorial1', methods=['GET','POST']) 
def tutorial_1():
    return render_template("tutorial_1.html")

@app.route('/tutorial2', methods=['GET','POST']) 
def tutorial_2():
    return render_template("tutorial_2.html")

@app.route('/tutorial3', methods=['GET','POST']) 
def tutorial_3():
    return render_template("tutorial_3.html")

## Tutorial end ##

@app.route('/freegame1', methods=['GET','POST']) 
def freegame_1():
    return render_template("freegame_1.html")

@app.route('/freegame2', methods=['GET','POST']) 
def freegame_2():
    if request.method == 'POST':
        cc_points = request.form['cc_points']
        dd_points = request.form['dd_points']
        dc_points = request.form['dc_points']
        cd_points = request.form['cd_points']

        rounds_no = request.form['rounds']
        matches_no = request.form['matches']
        noise = request.form['noise']

        selected_strategies = []
        for n in range(1,11):
            strategy_no = 'strategy'+str(n)
            try:
                selected_strategies.append(request.form[strategy_no])
            except:
                ""
        playing_strategies = str(selected_strategies).replace(", ","-")

        # data = {"cc_points":cc_points, "dd_points":dd_points,"cd_points":cd_points,"dc_points":dc_points,
        # "rounds":rounds_no,"matches":matches_no}
        # requests.post('http://frontend:5001/freegame3', json = data)

        return render_template("freegame_2.html", cc_points = cc_points, dd_points = dd_points, cd_points = cd_points, dc_points = dc_points,
        rounds_no = rounds_no, matches_no = matches_no, noise = noise, playing_strategies = playing_strategies)    

    if response.method == 'GET':
        return 'Hmm, this is not a gettable page. Try again'##render_template("freegame_2.html")
    
@app.route('/dataholding', methods=['GET','POST']) 
def dataholding():
    if request.method == 'POST':
        strategies_request_string = request.form['playing_strategies']
        strategies_list = strategies_request_string.replace("[","").replace("]","").replace(" ","").replace("'","").split('-')
        data = {"cc_points":request.form['cc_points'], "dd_points":request.form['dd_points'],"cd_points":request.form['cd_points'],
        "dc_points":request.form['dc_points'], "rounds":request.form['rounds_no'],"matches":request.form['matches_no'],"strategies":strategies_list}
        json_data = json.dumps(data)
        f = open("game_rules.json", "w")
        f.write(json_data)
        f.close()
        return redirect('freegame3')
    if request.method == 'GET':
        f = open('game_rules.json',)
        data = json.load(f)
        f.close()
        return data

        
@app.route('/freegame3', methods=['GET','POST']) 
def freegame_3():
    if request.method == 'GET':
        content = requests.get('http://tournament:5000/play').json()
        return pd.DataFrame.from_dict(content,orient='index').to_html()    




# def singlegame_fe():
#     return 'singlegame_fe'

# @app.route('/2', methods=['GET','POST']) 
# def fiveturngame_fe():
#     return 'fiveturngame_fe'

# @app.route('/3', methods=['GET','POST']) 
# def fiveturngameroundrobin_fe():
#     return 'fiveturngameroundrobin_fe'

# @app.route('/4', methods=['GET','POST']) 
# def fiftyturngameroundrobin_fe():
#     return 'fiftyturngameroundrobin_fe'

# @app.route('/5', methods=['GET','POST']) 
# def tournamentwitherror_fe():
#     return 'tournamentwitherror_fe'

# @app.route('/6', methods=['GET','POST']) 
# def tournamentwithspawning_fe():
#     return 'tournamentwithspawning_fe'

