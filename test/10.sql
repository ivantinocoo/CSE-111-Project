.headers on

-- Find the average age of players in each team
SELECT t_teamName, ROUND(AVG(p_age), 4) as avgAge
FROM players, teams
WHERE p_teamID = t_teamID
GROUP BY t_teamName;