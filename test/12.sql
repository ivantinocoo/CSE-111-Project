.headers on

--Retrieve teams with the highest goal difference
SELECT t_teamName, t_goalsDifference
FROM teams
ORDER BY t_goalsDifference DESC
LIMIT 5;