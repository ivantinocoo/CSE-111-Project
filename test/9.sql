.headers on

select p_playerName as "Player(s)", s_goals as Goals
from players, stats
where s_goals = (select max(s_goals) from stats);