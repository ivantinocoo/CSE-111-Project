.headers on 

--Find the team with the highest total number of goals
SELECT t_teamName as Team, SUM(t_goalsFor) as TOTALGoals
FROM teams
GROUP BY t_teamName
ORDER BY totalGoals DESC
LIMIT 1;