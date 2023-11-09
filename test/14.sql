.headers on

--Retrieve the teams that lost less than 4 games
SELECT t_teamName as Teams
FROM teams 
WHERE t_losses < 4;