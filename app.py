from flask import Flask, jsonify, send_from_directory, request
import os
import sqlite3

app = Flask(__name__)

current_directory = os.path.dirname(os.path.abspath(__file__))

@app.route('/index.html')
def index():
    return send_from_directory(current_directory, 'index.html')

@app.route('/functions.js')
def serve_js():
    return send_from_directory(current_directory, 'functions.js')

@app.route('/style.css')
def serve_css():
    return send_from_directory(current_directory, 'style.css')

DATABASE = 'soccer_db.sqlite'

def open_connection():
    conn = sqlite3.connect(DATABASE)
    return conn

def close_connection(conn):
    conn.close()

@app.route('/api/leagues', methods=['GET'])
def get_leagues():
    conn = sqlite3.connect('soccer_db.sqlite')  # Replace with your database file name
    cursor = conn.cursor()
    cursor.execute("SELECT l_leagueID, l_leagueName FROM leagues")  # Retrieve ID and name
    leagues = cursor.fetchall()
    conn.close()
    return jsonify({'leagues': leagues})

@app.route('/api/teams-by-league', methods=['POST'])
def get_teams_by_league():
    selected_league_id = request.json['selected_league_id']  # Get the selected league ID from frontend
    conn = open_connection()
    cursor = conn.cursor()
    query = "SELECT t_teamName FROM teams WHERE league_id = ?"  # Modify this query as per your schema
    cursor.execute(query, (selected_league_id,))
    teams = cursor.fetchall()
    conn.close()
    return jsonify({'teams': teams})


@app.route('/api/search-players', methods=['POST'])
def search_players():
    search_term = request.json['search_term']
    conn = open_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM players WHERE p_playerName LIKE ?"
    cursor.execute(query, ('%' + search_term + '%',))
    players = cursor.fetchall()
    close_connection(conn)
    return jsonify({'players': players})

if __name__ == '__main__':
    app.run(debug=True)