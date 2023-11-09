.headers on 

--List all coaches from a specific nation
SELECT c_coachName as Name, c_teamName as Team
FROM coaches
WHERE c_nationName = 'Chile';