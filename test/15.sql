.headers on 

--Find players who have received a red card
SELECT p_playerName as Name, t_teamName as Team
FROM players, stats, teams
WHERE t_teamID = p_teamID
    AND p_playerID = s_playerID
    AND s_redCards > 0;