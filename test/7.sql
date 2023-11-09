.headers on

select t_teamName as "Team(s)" 
from teams 
where t_wins = (select max(t_wins) from teams)
order by t_teamName;