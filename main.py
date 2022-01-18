from flask import Flask,jsonify,request
from day3_3 import player_request

app = Flask(_name_)

@app.route('/playerrequest',methods=["POST"])
def player():
    request_data=request.get_json()
    player1_name=request_data['player1']
    player1_symbol=request_data['symbol1']
    player2_name=request_data['player2']
    player2_symbol=request_data['symbol2']
    
    winner=player_request(player1_name,player1_symbol,player2_name,player2_symbol)
    
    

    if winner == player1_symbol:
        return f"Players_Names = {player1_name, player2_name} \n" \
               f"Players_Symbol = {player1_symbol, player2_symbol} \n" \
               f"The winner of the game 'TIC-Tac-Toa' is '{player1_name}' "
    if winner == player2_symbol:
        return f"Players_Names = {player1_name, player2_name} \n" \
               f"Players_Symbol = {player1_symbol, player2_symbol} \n" \
               f"The winner of the game 'TIC-Tac-Toa' is '{player2_name}' "


if _name_ == "_main_": 
    
   app.run(host="0.0.0.0", port=3000, debug=True