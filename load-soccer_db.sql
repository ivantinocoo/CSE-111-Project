--SQLite
DELETE FROM coaches;
DELETE FROM leagues;
DELETE FROM matches;
DELETE FROM nation;
DELETE FROM players;
DELETE FROM stats;
DELETE FROM teams;

--Run these commands in the .sqlite terminal
.mode "csv"
.separator ","
--.headers off

--Replace the file path with your path
.import 'data/2022-2023_Football_Team_Stats.csv' teams
.import 'data/nation.tbl' nation
.import 'data/league.tbl' leagues
.import 'data/2022-2023_Football_Players.csv' players
.import 'data/2022-2023_Football_Player_Stats.csv' stats