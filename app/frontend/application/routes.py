from application import app
from flask import Flask, redirect, request, url_for,render_template, Response, jsonify
import pandas as pd
import requests

@app.route('/', methods=['GET','POST']) 
def home_fe():
    return "wanna play?" + '<br><br><a href="/play">Start a tournament?</a> </br>'

@app.route('/1', methods=['GET','POST']) 
def singlegame_fe():
    return 'singlegame_fe'

@app.route('/2', methods=['GET','POST']) 
def fiveturngame_fe():
    return 'fiveturngame_fe'

@app.route('/3', methods=['GET','POST']) 
def fiveturngameroundrobin_fe():
    return 'fiveturngameroundrobin_fe'

@app.route('/4', methods=['GET','POST']) 
def fiftyturngameroundrobin_fe():
    return 'fiftyturngameroundrobin_fe'

@app.route('/5', methods=['GET','POST']) 
def tournamentwitherror_fe():
    return 'tournamentwitherror_fe'

@app.route('/6', methods=['GET','POST']) 
def tournamentwithspawning_fe():
    return 'tournamentwithspawning_fe'

