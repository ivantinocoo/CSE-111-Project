.headers on 

--List all coaches from a specific nation
SELECT c_coachName as Name, t_teamName as Team
FROM coaches, teams, nation
WHERE t_teamID = c_teamID
    AND n_nationID = c_nationID
    AND n_nationName = 'Chile';