.headers on

select t_teamName as Team, p_playerName as Players 
from players, teams where p_teamName = t_teamName
order by t_teamName;