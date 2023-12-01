import sqlite3
from sqlite3 import Error
from datetime import datetime

def openConnection(_dbFile):
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def display_menu():
    print("Soccer Stats Database Menu")
    print("1. Display Player Info")
    print("2. Show Team Standings")
    print("3. Retrieve Match Details")
    print("4. Update Player Information")
    print("5. Add New Match Data")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

def handle_user_choice(choice, conn):
    if choice == '1':
        display_player_info(conn)
    elif choice == '2':
        show_team(conn)
    elif choice == '3':
        retrieve_match_details(conn)
    elif choice == '4':
        update_player_info(conn)
    elif choice == '5':
        add_new_match_data(conn)
    elif choice == '6':
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please enter a valid option.")

def display_player_info(conn):
    player_name = input("Enter player's name: ")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT players.p_playerName, players.p_position, players.p_age, teams.t_teamName, players.p_born
        FROM players 
        INNER JOIN stats ON players.p_playerID = stats.s_playerID 
        INNER JOIN teams ON players.p_teamID = teams.t_teamID
        WHERE p_playerName = ?""", (player_name,))
    player_info = cursor.fetchone()

    if player_info:
        print("Player Info:")
        print(f"Name: {player_info[0]}")
        print(f"Position: {player_info[1]}")
        print(f"Age: {player_info[2]}")
        print(f"Team: {player_info[3]}")
        print(f"Born: {player_info[4]}")
    else:
        print("Player not found or no information available.")
    cursor.close()

def show_team(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT t_teamName, t_wins, t_draws, t_losses, t_goalsFor, t_goalsAgainst, t_goalsDifference, t_Points FROM teams ORDER BY t_Points DESC")
    teams = cursor.fetchall()
    if teams:
        print("Teams:")
        for idx, team in enumerate(teams, start=1):
            print(f"{idx}. {team[0]} - Wins: {team[1]}, Draws: {team[2]}, Losses: {team[3]}, Goals For: {team[4]}, Goals Against: {team[5]}, Goal Difference: {team[6]}, Points: {team[7]}")
    else:
        print("No teams found.")
    cursor.close()


def retrieve_match_details(conn):
    match_id = input("Enter match ID: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM matches WHERE m_matchID = ?", (match_id,))
    match_details = cursor.fetchone()
    if match_details:
        print("Match Details:")
        print(f"Date: {match_details[1]}")
        print(f"Stadium: {match_details[2]}")
        print(f"Home Team: {match_details[3]} - Goals: {match_details[4]}")
        print(f"Away Team: {match_details[5]} - Goals: {match_details[6]}")
    else:
        print("Match not found.")
    cursor.close()


def update_player_info(conn):
    player_name = input("Enter player's name: ")
    new_age = input("Enter new age: ")
    new_position = input("Enter new position: ")
    new_team = input("Enter new team name: ")
    
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE players 
        SET p_age = ?, p_position = ?, p_teamID = (
            SELECT t_teamID FROM teams WHERE t_teamName = ?
        )
        WHERE p_playerName = ?""", (new_age, new_position, new_team, player_name))
    
    conn.commit()
    
    if cursor.rowcount > 0:
        print("Player information updated successfully.")
    else:
        print("Player not found or unable to update.")
    
    cursor.close()


def add_new_match_data(conn):
    date = input("Enter date (YYYY-MM-DD): ")
    stadium = input("Enter stadium name: ")
    home_team = input("Enter home team name: ")
    home_goals = int(input("Enter home team goals: "))
    away_team = input("Enter away team name: ")
    away_goals = int(input("Enter away team goals: "))
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO matches (m_date, m_stadium, m_homeTeamName, m_homeTeamGoals, m_awayTeamName, m_awayTeamGoals) VALUES (?, ?, ?, ?, ?, ?)",
                   (date, stadium, home_team, home_goals, away_team, away_goals))
    conn.commit()
    print("New match data added successfully.")
    cursor.close()

def top_goal_scorers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT p_playerName, SUM(s_goals) AS total_goals FROM players INNER JOIN stats ON players.p_playerID = stats.s_playerID GROUP BY p_playerName ORDER BY total_goals DESC LIMIT 5")
    top_scorers = cursor.fetchall()
    if top_scorers:
        print("Top Goal Scorers:")
        for idx, scorer in enumerate(top_scorers, start=1):
            print(f"{idx}. {scorer[0]} - Goals: {scorer[1]}")
    else:
        print("No goal scorers found.")
    cursor.close()

def player_with_most_assists(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT p_playerName, MAX(s_assists) AS max_assists FROM players INNER JOIN stats ON players.p_playerID = stats.s_playerID")
    top_assist_player = cursor.fetchone()
    if top_assist_player:
        print(f"Player with Most Assists: {top_assist_player[0]} - Assists: {top_assist_player[1]}")
    else:
        print("No player found with assists.")
    cursor.close()

def average_goals_per_match(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(m_homeTeamGoals + m_awayTeamGoals) AS avg_goals_per_match FROM matches")
    avg_goals = cursor.fetchone()
    if avg_goals[0]:
        print(f"Average Goals Per Match: {avg_goals[0]:.2f}")
    else:
        print("No match data found.")
    cursor.close()

def best_goal_difference_teams(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT t_teamName, t_goalsDifference FROM teams ORDER BY t_goalsDifference DESC LIMIT 3")
    best_goal_diff_teams = cursor.fetchall()
    if best_goal_diff_teams:
        print("Teams with Best Goal Difference:")
        for idx, team in enumerate(best_goal_diff_teams, start=1):
            print(f"{idx}. {team[0]} - Goal Difference: {team[1]}")
    else:
        print("No teams found.")
    cursor.close()

def display_complex_queries_menu():
    print("More Complex Queries Menu")
    print("1. Top Goal Scorers")
    print("2. Player with Most Assists")
    print("3. Average Goals Per Match")
    print("4. Teams with Best Goal Difference")
    print("5. Back to Main Menu")
    choice = input("Enter your choice (1-5): ")
    return choice

def handle_complex_queries_choice(choice, conn):
    if choice == '1':
        top_goal_scorers(conn)
    elif choice == '2':
        player_with_most_assists(conn)
    elif choice == '3':
        average_goals_per_match(conn)
    elif choice == '4':
        best_goal_difference_teams(conn)
    else:
        print("Invalid choice. Please enter a valid option.")

def search_matches_by_date(conn):
    target_date = input("Enter a date (YYYY-MM-DD): ")
    
    try:
        target_date_obj = datetime.strptime(target_date, "%Y-%m-%d")

        target_date_db_format = target_date_obj.strftime("%dth %B %Y")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM matches WHERE m_date = ?", (target_date_db_format,))
        matched_matches = cursor.fetchall()
        if matched_matches:
            print("Matches on the specified date:")
            for match in matched_matches:
                print(f"Match ID: {match[0]}, Date: {match[1]}, Home Team: {match[3]}, Away Team: {match[5]}")
        else:
            print("No matches found on the specified date.")
        cursor.close()

    except ValueError:
        print("Invalid date format. Please enter dates in YYYY-MM-DD format.")


def display_coaches_and_teams(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT c_coachName, teams.t_teamName FROM coaches INNER JOIN teams ON coaches.c_teamID = teams.t_teamID")
    coach_teams = cursor.fetchall()
    if coach_teams:
        print("Coaches and Their Teams:")
        for coach in coach_teams:
            print(f"Coach: {coach[0]} - Team: {coach[1]}")
    else:
        print("No coach information found.")
    cursor.close()

def team_players_list(conn):
    team_name = input("Enter team name: ")
    cursor = conn.cursor()
    cursor.execute("SELECT p_playerName FROM players INNER JOIN teams ON players.p_teamID = teams.t_teamID WHERE teams.t_teamName LIKE ?", ('%' + team_name + '%',))
    team_players = cursor.fetchall()
    if team_players:
        print(f"Players in teams containing '{team_name}':")
        for player in team_players:
            print(player[0])
    else:
        print(f"No players found for teams containing '{team_name}'.")
    cursor.close()

def highest_scoring_match(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT m_matchID, m_homeTeamGoals + m_awayTeamGoals AS total_goals FROM matches ORDER BY total_goals DESC LIMIT 1")
    highest_scoring_match = cursor.fetchone()
    if highest_scoring_match:
        print(f"Highest Scoring Match (ID: {highest_scoring_match[0]}): Total Goals - {highest_scoring_match[1]}")
    else:
        print("No matches found.")
    cursor.close()

def display_additional_menu():
    print("Additional Features Menu")
    print("1. Search Matches by Date Range")
    print("2. Display Coaches and Their Teams")
    print("3. Team Players List")
    print("4. Highest Scoring Match")
    print("5. Back to Main Menu")
    choice = input("Enter your choice (1-5): ")
    return choice

def handle_additional_choice(choice, conn):
    if choice == '1':
        search_matches_by_date(conn)
    elif choice == '2':
        display_coaches_and_teams(conn)
    elif choice == '3':
        team_players_list(conn)
    elif choice == '4':
        highest_scoring_match(conn)
    elif choice == '5':
        print("Returning to the main menu.")
    else:
        print("Invalid choice. Please enter a valid option.")


def main():
    database = r"soccer_db.sqlite"
    conn = openConnection(database)

    while True:
        print("\n1. Perform Basic Operations")
        print("2. Perform More Complex Queries")
        print("3. Additional Features")
        print("4. Exit")
        menu_choice = input("Enter your choice (1-4): ")

        if menu_choice == '1':
            while True:
                choice = display_menu()
                if choice == '6':
                    break
                handle_user_choice(choice, conn)
        elif menu_choice == '2':
            while True:
                choice = display_complex_queries_menu()
                if choice == '5':
                    break
                handle_complex_queries_choice(choice, conn)
        elif menu_choice == '3':
            while True:
                choice = display_additional_menu()
                if choice == '5':
                    break
                handle_additional_choice(choice, conn)
        elif menu_choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    closeConnection(conn, database)

if __name__ == '__main__':
    main()