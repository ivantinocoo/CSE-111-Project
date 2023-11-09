.headers on 

--Find matches where the home team scored more than 3 goals
SELECT m_date as Date, m_stadium as Stadium, m_homeTeamName as HomeTeam, m_homeTeamGoals as Goals
FROM matches 
WHERE m_homeTeamGoals > 3;