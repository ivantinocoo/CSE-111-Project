.headers on 

--List teams with more than 70 points
SELECT t_teamName as Team, t_Points as Points
FROM teams
WHERE t_Points >= 70;