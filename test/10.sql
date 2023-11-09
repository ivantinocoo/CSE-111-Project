.headers on

--Find the average age of players in each team
SELECT p_teamName, AVG(p_age) as avgAge
FROM players
GROUP BY p_teamName;