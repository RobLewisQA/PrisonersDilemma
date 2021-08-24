from application import app
from flask import Flask, redirect, request, url_for,render_template, Response, jsonify
import pandas as pd
import requests

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
    return render_template("freegame_2.html")
    
@app.route('/freegame3', methods=['GET','POST']) 
def freegame_3():
    return render_template("freegame_3.html")


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

