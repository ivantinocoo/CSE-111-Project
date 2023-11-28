from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'soccer_db.sqlite'

# Open connection function remains the same
def open_connection():
    conn = sqlite3.connect(DATABASE)
    return conn

# Close connection function remains the same
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

if __name__ == '__main__':
    app.run(debug=True)