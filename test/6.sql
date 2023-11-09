.headers on

select t_teamName as Team, p_playerName as Players 
from players, teams where p_teamID = t_teamID
order by t_teamName;