.headers on

--Find players with the most assists
SELECT p_playerName as Name, p_teamName as Team, p_position as Position, MAX(s_assists) as Assist
FROM players, stats
WHERE p_playerID = s_playerID
ORDER BY Assist DESC;