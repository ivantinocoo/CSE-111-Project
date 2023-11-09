.headers on 

--Find players who have received a red card
SELECT p_playerName as Name, p_teamName as Team, s_redCards as Reds
FROM players, stats
WHERE p_playerID = s_playerID
    AND s_redCards > 0;