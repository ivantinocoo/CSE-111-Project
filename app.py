from flask import Flask, jsonify, send_from_directory
import os
import sqlite3

app = Flask(__name__)

current_directory = os.path.dirname(os.path.abspath(__file__))
html_directory = os.path.join(current_directory, 'HTML')

@app.route('/HomePage.html')
def Home():
    return send_from_directory(html_directory, 'HomePage.html')

@app.route('/Leagues.html')
def Leagues():
    return send_from_directory(current_directory, 'html/Leagues.html')

@app.route('/Teams.html')
def Teams():
    return send_from_directory(current_directory, 'html/Teams.html')

@app.route('/Players.html')
def Players():
    return send_from_directory(current_directory, 'html/Players.html')

@app.route('/Coaches.html')
def Coaches():
    return send_from_directory(current_directory, 'html/Coaches.html')

@app.route('/Matches.html')
def Matches():
    return send_from_directory(current_directory, 'html/Matches.html')

@app.route('/Stats.html')
def Stats():
    return send_from_directory(current_directory, 'html/Stats.html')

@app.route('/style.css')
def style():
    return send_from_directory(current_directory, 'style.css')

@app.route('/Soccer.jpeg')
def image():
    return send_from_directory(current_directory, 'Soccer.jpeg')

DATABASE = 'soccer_db.sqlite'

def open_connection():
    conn = sqlite3.connect(DATABASE)
    return conn

def close_connection(conn):
    conn.close()

@app.route('/api/leagues', methods=['GET'])
def get_leagues():
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leagues")
    leagues = cursor.fetchall()
    close_connection(conn)
    return jsonify({'leagues': leagues})

@app.route('/api/teams', methods=['GET'])
def get_teams():
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()
    close_connection(conn)
    return jsonify({'teams': teams})

@app.route('/api/players', methods=['GET'])
def get_players():
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players")
    players = cursor.fetchall()
    close_connection(conn)
    return jsonify({'players': players})

@app.route('/api/coaches', methods=['GET'])
def get_coaches():
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM coaches")
    coaches = cursor.fetchall()
    close_connection(conn)
    return jsonify({'coaches': coaches})

@app.route('/api/matches', methods=['GET'])
def get_matches():
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM matches")
    matches = cursor.fetchall()
    close_connection(conn)
    return jsonify({'matches': matches})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stats")
    stats = cursor.fetchall()
    close_connection(conn)
    return jsonify({'stats': stats})

if __name__ == '__main__':
    app.run(debug=True)