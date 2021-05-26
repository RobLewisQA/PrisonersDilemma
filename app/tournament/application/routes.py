from application import app
from flask import Flask, redirect, request, url_for,render_template, Response, jsonify
import pandas as pd
from itertools import combinations
from random import choices
import random

def calculator(player1_move,player2_move,move_hist):
    if player1_move == "c":
        if player2_move == "c":
            return [2,2]
        else:
            return [0,3]
    elif player1_move == "d":
        if player2_move == "d":
            return [1,1]
        else:
            return [3,0]
    

def C_AlwaysC(turn,player,move_hist):
    if  turn == 0:
        return "c"
    else:
        return "c"

def C_AlwaysD(turn,player,move_hist):
    if  turn == 0:
        return "c"
    else:
        return "d"
    
def D_AlwaysC(turn,player,move_hist):
    if  turn == 0:
        return "d"
    else:
        return "c"
    
def D_AlwaysD(turn,player,move_hist):
    if  turn == 0:
        return "d"
    else:
        return "d"

def C_TitForTat(turn,player,move_hist):
    if  player == 1:
        if turn == 0:
            return "c"
        else:
            return move_hist[1::2][-1]
    elif player == 2:
        if turn == 0:
            return "c"
        else:
            return move_hist[0::2][-1]

def C_UntilD(turn,player,move_hist):
    if  player == 1:
        if turn == 0:
            return "c"
        else:
            if "d" not in move_hist[1::2]:
                return "c"
            else:
                return "d"      
    elif player == 2:
        if turn == 0:
            return "c"
        else:
            if "d" not in move_hist[0::2]:
                return "c"
            else:
                return "d" 
        
def C_TitFor2Tat(turn,player,move_hist):
    if  player == 1:
        if turn <= 1:
            return "c"
        else:
            if (move_hist[1::2][-1] == "d") & (move_hist[1::2][-2] == "d"):
                return "d"
            else:
                return "c"
    elif player == 2:
        if turn <= 1:
            return "c"
        else:
            if (move_hist[0::2][-1] == "d") & (move_hist[0::2][-2] == "d"):
                return "d"
            else:
                return "c"
        
def Random_70C(turn,player,move_hist):
    if  turn == 0:
        return choices(["c","d"], weights=[0.7,0.3])[0]
    else:
        return choices(["c","d"], weights=[0.7,0.3])[0]
    
def Random_70D(turn,player,move_hist):
    if  turn == 0:
        return choices(["c","d"], weights=[0.3,0.7])[0]
    else:
        return choices(["c","d"], weights=[0.3,0.7])[0]

def D_TitFor2TatExploiter(turn,player,move_hist):
    if turn == 0:
        return "d"
    else:
        if (turn%2) == 0:
            return "d"
        else:
            return "c"

def C_OccasionalDefector(turn,player,move_hist):
    if turn <= 6:
        return "c"
    else:
        if "d" not in move_hist[-10:]:
            return "d"
        else:
            return "c"            
            
            
def D_AlwaysCExploiter(turn,player,move_hist):
    if  player == 1:
        if turn == 0:
            return "d"
        else:
            if "d" not in (move_hist[1::2]):
                return "d"
            else:
                return move_hist[0::2][-1]
    elif  player == 2:
        if turn == 0:
            return "d"
        else:
            if "d" not in (move_hist[1::2]):
                return "d"
            else:
                return move_hist[0::2][-1]
            
            
def strategies_menu():
    return C_AlwaysD,C_AlwaysC,D_AlwaysD,C_TitForTat,C_UntilD,Random_70C,Random_70D,C_TitFor2Tat,D_TitFor2TatExploiter,C_OccasionalDefector,D_AlwaysCExploiter,D_AlwaysC

def players(winner,loser,g,df1):
    if g == 0:
        playing = 12
        player_list = []
        start_strategy = []
        for p in range(1,playing+1):
            player_list = player_list + ['player'+str(p)]
            start_strategy = start_strategy + [p-1]

        df = pd.DataFrame(index=player_list,columns=['strategy_history'],data=start_strategy)
        df.loc[loser] = [df.loc[winner]]
    else:
        df = pd.DataFrame(index=df1.index,columns=['strategy_history'],data=list(df1))
        df.loc[loser] = df1.loc[winner]
    return df


def fixtures(winner,loser,g,df1):
    fixture_list = list(combinations(players(winner,loser,g,df1).index,2))
    return fixture_list
    
def game(winner,loser,g,df1):
    gamelength = 10
    fixture_list = list(fixtures(winner,loser,g,df1))
    player_strategies = players(winner,loser,g,df1).strategy_history
    round_totals = pd.DataFrame()
    
    for n in range(len(fixtures(winner,loser,g,df1))):
        df = pd.DataFrame()
        move_hist = []
        points = []

        for turn in range(gamelength):
            player1_name = fixture_list[n][0]
            player2_name = fixture_list[n][1]

            player1_move = strategies_menu()[player_strategies.loc[player1_name]](turn,1,move_hist)
            player2_move = strategies_menu()[player_strategies.loc[player2_name]](turn,2,move_hist)

            player_scores = calculator(player1_move,player2_move,move_hist)
            move_hist = move_hist + [player1_move] + [player2_move]
            points = points + [player_scores[0]] + [player_scores[1]]

        df = pd.DataFrame([move_hist[0::2],move_hist[1::2],points[0::2],points[1::2]]).T
        df.rename(columns={0:player1_name+"_move",1:player2_name+"_move",2:player1_name,3:player2_name},inplace=True)
        #print(df)
        round_totals = pd.concat([round_totals,df.iloc[:,-2:].sum(axis=0)],axis=1)
    return round_totals.sum(axis=1)

def match(g,winner,loser,df1):
    rounds = 5
    df = pd.DataFrame()
    for r in range(rounds):
        df = pd.concat([df,game(winner,loser,g,df1)],axis=1)
    totals = pd.Series(df.sum(axis=1),name='Generation'+'_'+str(g))
    return pd.merge(players(winner,loser,g,df1),totals,how='outer',left_index=True,right_index=True)

def tournament():
    generations = 50
    df = pd.DataFrame()
    winner = 'player1'
    loser = 'player1'
    df1 = df.copy()
    for g in range(generations):
        if g == 0:
            df = pd.concat([df,match(g,winner,loser,df1)],axis=1)
            scores = df.iloc[:,-1]
            winner = choices(list(scores.loc[scores == scores.max()].index))[0]
            loser = choices(list(scores.loc[scores == scores.min()].index))[0]
        else:
            df1 = df.iloc[:,-2].copy()
            df = pd.concat([df,match(g,winner,loser,df1)],axis=1)
            scores = df.iloc[:,-1]
            winner = choices(list(scores.loc[scores == scores.max()].index))[0]
            loser = choices(list(scores.loc[scores == scores.min()].index))[0]
    return df


#############################
#############################
#############################

@app.route('/', methods=['GET','POST']) 
def home():
    return "wanna play?" + '<br><br><a href="/play">Start a tournament?</a> </br>'

@app.route('/play', methods=['GET','POST'])  # to move into strategies microservice
def play():
    strategy_list = []
    for s in strategies_menu():
        strategy_list.append(s.__name__)
    
    maps = {}
    for m in range(len(strategy_list)):
        maps.update({m:strategy_list[m]})

    df6 = match(0,'player1','player1',pd.DataFrame())
    df6_clean = pd.concat([df6.strategy_history.map(maps),df6.Generation_0],axis=1).sort_values(by='Generation_0',ascending=False)
    return df6_clean.to_html()


#@app.route('/game', methods=['GET','POST'])  # a game is a single interaction between two players
#def game():


#@app.route('/round', methods=['GET','POST'])  # a round is a fixed n-games series
#def round():

#@app.route('/match', methods=['GET','POST'])  # a match is a fixed n-rounds series
#def match():
