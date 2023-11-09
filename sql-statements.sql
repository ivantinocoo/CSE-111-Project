select l_leagueName as Leagues
from leagues;

select n_nationName as Nations
from nation;

select t_teamName as Teams
from teams;

select c_coachName as Coaches
from coaches;

select p_playerName as Players
from players;

select t_teamName as Team, p_playerName as Players 
from players, teams where p_teamName = t_teamName
order by t_teamName;

select t_teamName as "Team(s)" 
from teams 
where t_wins = (select max(t_wins) from teams)
order by t_teamName;

select p_playerName as "Players"
from players
where p_position = MF
order by p_playerName;

