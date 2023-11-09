.headers on

select p_playerName as "Players"
from players
where p_position = 'MF'
order by p_playerName;