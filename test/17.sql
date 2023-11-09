.headers on 

--Retrieve all matches on a specific day
SELECT m_date as Date, m_stadium as Stadium, m_homeTeamName as HomeTeam, m_homeTeamGoals as HomeGoals, m_awayTeamName as AwayTeam, m_awayTeamGoals as AwayGoals
FROM matches
WHERE m_date = '5th March 2023';