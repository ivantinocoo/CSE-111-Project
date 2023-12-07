import sqlite3
from sqlite3 import Error
from datetime import datetime

def openConnection(_dbFile):

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
    except Error as e:
        print(e)

    return conn

def closeConnection(_conn, _dbFile):

    try:
        _conn.close()
    except Error as e:
        print(e)

##################################################################
###############        Main Menu          ########################
##################################################################

def display_menu():
    print("\nSoccer Menu 2022-2023")
    print("1. Leagues")
    print("2. Teams")
    print("3. Players")
    print("4. Coaches")
    print("5. Matches")
    print("6. Exit")
    choice = input("\nEnter your choice (1-6): ")
    return choice

def handle_user_choice_main_menu(choice, conn):
    if choice == '1':
        display_league_info(conn)
    elif choice == '2':
        display_team_info(conn)
    elif choice == '3':
        display_player_info(conn)
    elif choice == '4':
        display_coaches_info(conn)
    elif choice == '5':
        display_match_info(conn)
    elif choice == '6':
        print("\nExiting the program. Goodbye!\n")
    else:
        print("\nInvalid choice. Please enter a valid option.")

##################################################################
###############        League Menu          ########################
##################################################################

def display_league_info(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT l_leagueName, n_nationName FROM leagues, nation WHERE l_nationID = n_nationID;")
        rows = cursor.fetchall()

        if rows:
            print("\nLeagues")
            for row in rows:
                print(f"{row[0]} ({row[1]})")
        else:
            print("\nNo leagues found.")
    except Error as e:
        print("\nError fetching leagues:", e)

##################################################################
###############        Team Menu          ########################
##################################################################

def display_team_info(conn):
    while True:
        print("\nTeam Information Menu:")
        print("1. Show all teams")
        print("2. Team Roster")
        print("3. Match Results")
        print("4. Teams Top Scorer")
        print("5. Teams Top Assists")
        print("6. Most Wins")
        print("7. Best Goal Differential")
        print("8. Go back to main menu")
        
        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT t_teamName FROM teams")
                rows = cursor.fetchall()

                if rows:
                    print("\nList of Team Names:")
                    for row in rows:
                        print(f"{row[0]}")
                else:
                    print("\nNo teams found.")
            except Error as e:
                print("\nError fetching teams:", e)

        elif choice == '2':
            team_name = input("\nEnter the name of the team: ")


            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p_playerName
                    FROM players, teams
                    WHERE t_teamName LIKE ?
                        AND t_teamID = p_teamID;""", ('%' + team_name + '%',))
                
                rows = cursor.fetchall()

                if rows:
                    print(f"\nPlayers in {team_name}:")
                    for row in rows:
                        print(row[0])
                else:
                    print("\nNo players found for the selected team.")
            except Error as e:
                print("\nError fetching team roster:", e)

        elif choice == '3':
            team_name = input("\nEnter the name of the team: ")

            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT m_homeTeamName, m_awayTeamName, m_homeTeamGoals, m_awayTeamGoals
                    FROM matches
                    WHERE m_homeTeamName = ? OR m_awayTeamName = ?
                """, (team_name, team_name))

                rows = cursor.fetchall()

                if rows:
                    print(f"\nMatch results for {team_name}:")
                    for row in rows:
                        if row[0] == team_name:
                            print(f"{row[0]} {row[2]} - {row[3]} {row[1]}")
                        else:
                            print(f"{row[1]} {row[3]} - {row[2]} {row[0]}")
                else:
                    print("\nNo match results found for the selected team.")
            except Error as e:
                print("\nError fetching match results:", e)

        
        elif choice == '4':
            team_name = input("\nEnter the name of the team: ")

            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p.p_playerName, MAX(s.s_goals) as top_goals
                    FROM players p
                    JOIN stats s ON p.p_playerID = s.s_playerID
                    JOIN teams t ON p.p_teamID = t.t_teamID
                    WHERE t.t_teamName = ?
                    GROUP BY p.p_playerName
                    ORDER BY top_goals DESC
                    LIMIT 1
                """, (team_name,))

                row = cursor.fetchone()

                if row:
                    print(f"\nTop goal scorer for {team_name}:")
                    print(f"{row[0]} - {row[1]}")
                else:
                    print(f"\nNo top goal scorer found for {team_name}.")
            except Error as e:
                print("\nError fetching top goal scorer:", e)


        elif choice == '5':
            team_name = input("\nEnter the name of the team: ")

            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p.p_playerName, MAX(s.s_assists) as top_assists
                    FROM players p
                    JOIN stats s ON p.p_playerID = s.s_playerID
                    JOIN teams t ON p.p_teamID = t.t_teamID
                    WHERE t.t_teamName = ?
                    GROUP BY p.p_playerName
                    ORDER BY top_assists DESC
                    LIMIT 1
                """, (team_name,))

                row = cursor.fetchone()

                if row:
                    print(f"\nTop assists for {team_name}:")
                    print(f"{row[0]} - {row[1]}")
                else:
                    print(f"\nNo top assists found for {team_name}.")
            except Error as e:
                print("\nError fetching top assists:", e)

        elif choice == '6':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT t_teamName, t_wins
                    FROM teams
                    WHERE t_wins = (
                        SELECT MAX(t_wins)
                        FROM teams
                    )
                """)

                rows = cursor.fetchall()

                if rows:
                    print("\nTeam with the most wins:")
                    for row in rows:
                        print(f"Team: {row[0]}, Total wins: {row[1]}")
                else:
                    print("\nNo team data found.")
            except Error as e:
                print("\nError fetching teams with most wins:", e)


        elif choice == '7':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT t_teamName, MAX(t_goalsDifference)
                    FROM teams
                """)

                row = cursor.fetchone()

                if row:
                    print(f"\nTeam with the best goal difference: {row[0]}")
                    print(f"Goal difference: {row[1]}")
                else:
                    print("\nNo team data found.")
            except Error as e:
                print("\nError fetching best goal difference:", e)

        elif choice == '8':
            print("\nGoing back to the main menu.")
            break

        else:
            print("\nInvalid choice. Please enter a valid option.")

##################################################################
###############        Player Menu          ########################
##################################################################

def display_player_info(conn):
    while True:
        print("\nPlayer Information Menu:")
        print("1. Show all players")
        print("2. Players that play in a specific league")
        print("3. Players that have received the most red cards")
        print("4. Player with the most goals")
        print("5. Average age of players")
        print("6. Players that have played the most games")
        print("7. Players with the most assists")
        print("8. Players with the most touches")
        print("9. Players with the best goal average")
        print("10. Go back to main menu")
        
        choice = input("\nEnter your choice (1-10): ")

        if choice == '1':
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT p_playerName FROM players")
                rows = cursor.fetchall()

                if rows:
                    print("List of Player Names:")
                    for row in rows:
                        print(f"{row[0]}")
                else:
                    print("No players found.")
            except Error as e:
                print("Error fetching players:", e)
            pass

        elif choice == '2':
            league_name = input("\nEnter the name of the league: ")

            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p.p_playerName
                    FROM players p
                    JOIN teams t ON p.p_teamID = t.t_teamID
                    JOIN leagues l ON t.t_leagueID = l.l_leagueID
                    WHERE l.l_leagueName = ?
                """, (league_name,))
                
                rows = cursor.fetchall()

                if rows:
                    print(f"\nPlayers in {league_name}:")
                    for row in rows:
                        print(row[0])
                else:
                    print(f"\nNo players found for the league {league_name}.")
            except Error as e:
                print("\nError fetching players in the league:", e)

        elif choice == '3':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p.p_playerName, s.s_redCards
                    FROM players p
                    JOIN stats s ON p.p_playerID = s.s_playerID
                    ORDER BY s.s_redCards DESC
                    LIMIT 5
                """)
                
                row = cursor.fetchone()

                if row:
                    print(f"\nPlayer with the most red cards:")
                    print(f"Player Name: {row[0]}")
                    print(f"Red Cards: {row[1]}")
                else:
                    print("\nNo players found.")
            except Error as e:
                print("\nError fetching player with most red cards:", e)

        elif choice == '4':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p.p_playerName, MAX(s.s_goals)
                    FROM players p
                    JOIN stats s ON p.p_playerID = s.s_playerID
                    LIMIT 5
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nPlayer with the most goals:")
                    print(f"Player Name: {row[0]}")
                    print(f"Goals: {row[1]}")
                else:
                    print("\nNo players found.")
            except Error as e:
                print("\nError fetching youngest player with most goals:", e)

        elif choice == '5':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT AVG(p.p_age) AS average_age
                    FROM players p
                """)
                
                row = cursor.fetchone()

                if row[0] is not None:
                    print("\nAverage age of players:")
                    print(f"{row[0]:.2f}")
                else:
                    print("\nNo player data found.")
            except Error as e:
                print("\nError calculating average age of players:", e)

        elif choice == '6':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p.p_playerName, SUM(s.s_matchesPlayed) AS total_matches_played
                    FROM players p
                    JOIN stats s ON p.p_playerID = s.s_playerID
                    GROUP BY p.p_playerName
                    ORDER BY total_matches_played DESC
                    LIMIT 5
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nPlayer(s) who played the most games:")
                    print(f"Player Name: {row[0]}")
                    print(f"Total Matches Played: {row[1]}")
                else:
                    print("\nNo players found.")
            except Error as e:
                print("\nError fetching player(s) with most games played:", e)

        elif choice == '7':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p.p_playerName, SUM(s.s_assists) AS total_assists
                    FROM players p
                    JOIN stats s ON p.p_playerID = s.s_playerID
                    GROUP BY p.p_playerName
                    ORDER BY total_assists DESC
                    LIMIT 5
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nPlayer(s) with the most assists:")
                    print(f"Player Name: {row[0]}")
                    print(f"Total Assists: {row[1]}")
                else:
                    print("\nNo players found.")
            except Error as e:
                print("\nError fetching player(s) with most assists:", e)

        
        elif choice == '8':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p.p_playerName, SUM(s.s_touches) AS total_touches
                    FROM players p
                    JOIN stats s ON p.p_playerID = s.s_playerID
                    GROUP BY p.p_playerName
                    ORDER BY total_touches DESC
                    LIMIT 5
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nPlayer(s) with the most touches:")
                    print(f"Player Name: {row[0]}")
                    print(f"Total Touches: {row[1]}")
                else:
                    print("\nNo players found.")
            except Error as e:
                print("\nError fetching player(s) with most touches:", e)

        elif choice == '9':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p.p_playerName, SUM(s.s_goals) / SUM(s.s_matchesPlayed) AS goal_average
                    FROM players p
                    JOIN stats s ON p.p_playerID = s.s_playerID
                    GROUP BY p.p_playerName
                    ORDER BY goal_average DESC
                    LIMIT 5
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nPlayer(s) with the best goal average:")
                    print(f"Player Name: {row[0]}")
                    print(f"Goal Average: {row[1]:.2f}")
                else:
                    print("\nNo players found.")
            except Error as e:
                print("\nError fetching player(s) with best goal average:", e)

        elif choice == '10':
            print("\nGoing back to the main menu.")
            break

        else:
            print("\nInvalid choice. Please enter a valid option.")

##################################################################
###############        Coaches Menu          ########################
##################################################################

def display_coaches_info(conn):
    while True:
        print("\nCoach Information Menu:")
        print("1. Show all coaches")
        print("2. Coaches from a specific League")
        print("3. Coaches with the most wins")
        print("4. Oldest Coaches")
        print("5. Youngest Coaches")
        print("6. Coaches from a specific nation")
        print("7. Coaches that coach the best scorer")
        print("8. Coaches with the best goal difference")
        print("9. Coaches that coach the most players")
        print("10. Go back to main menu")
        
        choice = input("\nEnter your choice (1-10): ")

        if choice == '1':
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT c_coachName FROM coaches")
                rows = cursor.fetchall()

                if rows:
                    print("\nList of Coach Names:")
                    for row in rows:
                        print(f"{row[0]}")
                else:
                    print("\nNo coaches found.")
            except Error as e:
                print("\nError fetching coaches:", e)

        elif choice == '2':
            league_name = input("\nEnter the name of the league: ")

            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT c.c_coachName
                    FROM coaches c
                    JOIN teams t ON c.c_teamID = t.t_teamID
                    JOIN leagues l ON t.t_leagueID = l.l_leagueID
                    WHERE l.l_leagueName = ?
                """, (league_name,))
                
                rows = cursor.fetchall()

                if rows:
                    print(f"\nCoaches in {league_name}:")
                    for row in rows:
                        print(row[0])
                else:
                    print(f"\nNo coaches found for the league {league_name}.")
            except Error as e:
                print("\nError fetching coaches in the league:", e)

        elif choice == '3':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT c.c_coachName, MAX(t.t_wins) AS max_wins
                    FROM coaches c
                    JOIN teams t ON c.c_teamID = t.t_teamID
                    GROUP BY c.c_coachName
                    ORDER BY max_wins DESC
                    LIMIT 1
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nCoach(es) with the most wins:")
                    print(f"Coach Name: {row[0]}")
                    print(f"Wins: {row[1]}")
                else:
                    print("\nNo coaches found.")
            except Error as e:
                print("\nError fetching coach(es) with most wins:", e)

        elif choice == '4':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT c.c_coachName, c.c_age
                    FROM coaches c
                    ORDER BY c.c_age DESC
                    LIMIT 1
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nOldest coach:")
                    print(f"Coach Name: {row[0]}")
                    print(f"Age: {row[1]}")
                else:
                    print("\nNo coaches found.")
            except Error as e:
                print("\nError fetching oldest coach:", e)

        elif choice == '5':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT c.c_coachName, c.c_age
                    FROM coaches c
                    ORDER BY c.c_age ASC
                    LIMIT 1
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nYoungest coach:")
                    print(f"Coach Name: {row[0]}")
                    print(f"Age: {row[1]}")
                else:
                    print("\nNo coaches found.")
            except Error as e:
                print("\nError fetching youngest coach:", e)

        elif choice == '6':
            nation_name = input("\nEnter the name of the nation: ")

            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT c.c_coachName, t.t_teamName
                    FROM coaches c
                    JOIN teams t ON c.c_teamID = t.t_teamID
                    JOIN nation n ON c.c_nationID = n.n_nationID
                    WHERE n.n_nationName = ?
                """, (nation_name,))
                
                rows = cursor.fetchall()

                if rows:
                    print(f"\nCoaches from {nation_name}:")
                    for row in rows:
                        print(f"Coach Name: {row[0]}, Team: {row[1]}")
                else:
                    print(f"\nNo coaches found from the nation {nation_name}.")
            except Error as e:
                print("\nError fetching coaches from the nation:", e)

        elif choice == '7':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT c.c_coachName
                    FROM coaches c
                    JOIN teams t ON c.c_teamID = t.t_teamID
                    JOIN players p ON t.t_teamID = p.p_teamID
                    JOIN stats s ON p.p_playerID = s.s_playerID
                    WHERE s.s_goals = (
                        SELECT MAX(s_goals)
                        FROM stats
                    )
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nCoach of the top goal scorer:")
                    print(f"Coach Name: {row[0]}")
                else:
                    print("\nNo coach found for the top goal scorer.")
            except Error as e:
                print("\nError fetching coach of the top goal scorer:", e)

        elif choice == '8':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT c.c_coachName
                    FROM coaches c
                    JOIN teams t ON c.c_teamID = t.t_teamID
                    ORDER BY t.t_goalsDifference DESC
                    LIMIT 1
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nCoach of the team with the best goal difference:")
                    print(f"Coach Name: {row[0]}")
                else:
                    print("\nNo coach found for the team with the best goal difference.")
            except Error as e:
                print("\nError fetching coach of the team with the best goal difference:", e)

        elif choice == '9':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT c.c_coachName, COUNT(DISTINCT p.p_playerID) as num_players
                    FROM coaches c
                    JOIN teams t ON c.c_teamID = t.t_teamID
                    JOIN players p ON t.t_teamID = p.p_teamID
                    GROUP BY c.c_coachName
                    ORDER BY num_players DESC
                    LIMIT 1
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nCoach who coached the most players:")
                    print(f"Coach Name: {row[0]}")
                    print(f"Number of Players Coached: {row[1]}")
                else:
                    print("\nNo coach found.")
            except Error as e:
                print("\nError fetching coach who coached the most players:", e)


        elif choice == '10':
            print("\nGoing back to the main menu.")
            break

        else:
            print("\nInvalid choice. Please enter a valid option.")

##################################################################
###############        Match Menu          ########################
##################################################################

def display_match_info(conn):
    while True:
        print("\nMatch Information Menu:")
        print("1. Show all matches")
        print("2. Matches with the most goal")
        print("3. Matches on a specific Date")
        print("4. Matches coached by a specific coach")
        print("5. Match in a specific stadium")
        print("6. Team with the most matches")
        print("7. Go back to main menu")
        
        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT m_homeTeamName, m_awayTeamName FROM matches")
                rows = cursor.fetchall()

                if rows:
                    print("\nList of Matches (Home Team vs Away Team):")
                    for row in rows:
                        print(f"{row[0]} vs {row[1]}")
                else:
                    print("\nNo matches found.")
            except Error as e:
                print("\nError fetching matches:", e)

        elif choice == '2':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT m.m_homeTeamName, m.m_awayTeamName, (m.m_homeTeamGoals + m.m_awayTeamGoals) AS total_goals
                    FROM matches m
                    ORDER BY total_goals DESC
                    LIMIT 1
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nMatch(es) with the most goals:")
                    print(f"{row[0]} vs {row[1]} - Total Goals: {row[2]}")
                else:
                    print("\nNo matches found.")
            except Error as e:
                print("\nError fetching match(es) with the most goals:", e)

        elif choice == '3':
            specific_date = input("\nEnter the date (DDth MM YYYY): ")

            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT m.m_homeTeamName, m.m_awayTeamName
                    FROM matches m
                    WHERE m.m_date = ?
                """, (specific_date,))
                
                row = cursor.fetchone()

                if row:
                    print(f"\nMatches {specific_date}:")
                    print(f"{row[0]} vs {row[1]}")
                else:
                    print(f"\nNo matches found on {specific_date}.")
            except Error as e:
                print("\nError fetching matches on the specified date:", e)

        
        elif choice == '4':
            coach_name = input("\nEnter the coach's name: ")

            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT m.m_homeTeamName, m.m_awayTeamName
                    FROM matches m
                    JOIN teams t ON m.m_homeTeamName = t.t_teamName OR m.m_awayTeamName = t.t_teamName
                    JOIN coaches c ON t.t_teamID = c.c_teamID
                    WHERE c.c_coachName = ?
                """, (coach_name,))
                
                rows = cursor.fetchall()

                if rows:
                    print(f"\nMatches coached by {coach_name}:")
                    for row in rows:
                        print(f"{row[0]} vs {row[1]}")
                else:
                    print(f"\nNo matches found coached by {coach_name}.")
            except Error as e:
                print(f"\nError fetching matches coached by {coach_name}:", e)

        elif choice == '5':
            stadium_name = input("\nEnter the stadium's name: ")

            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT m.m_homeTeamName, m.m_awayTeamName
                    FROM matches m
                    WHERE m.m_stadium = ?
                """, (stadium_name,))
                
                rows = cursor.fetchall()

                if rows:
                    print(f"\nMatches played in {stadium_name}:")
                    for row in rows:
                        print(f"{row[0]} vs {row[1]}")
                else:
                    print(f"\nNo matches found in {stadium_name}.")
            except Error as e:
                print(f"\nError fetching matches in {stadium_name}:", e)

        elif choice == '6':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT t.t_teamName, COUNT(*) as matches_played
                    FROM teams t
                    JOIN matches m ON t.t_teamName = m.m_homeTeamName OR t.t_teamName = m.m_awayTeamName
                    GROUP BY t.t_teamName
                    ORDER BY matches_played DESC
                    LIMIT 1
                """)
                
                row = cursor.fetchone()

                if row:
                    print("\nTeam with the most matches:")
                    print(f"Team Name: {row[0]} - Matches Played: {row[1]}")
                else:
                    print("\nNo matches found.")
            except Error as e:
                print("\nError fetching team with the most matches:", e)


        elif choice == '7':
            print("\nGoing back to the main menu.")
            break

        else:
            print("\nInvalid choice. Please enter a valid option.")


def main():
    database = r"soccer_db.sqlite"
    conn = openConnection(database)

    while True:
        choice = display_menu()
        handle_user_choice_main_menu(choice, conn)

        if choice == '6':
            break

    closeConnection(conn, database)

if __name__ == '__main__':
    main()