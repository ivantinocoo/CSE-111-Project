.headers ON

select l_leagueName as League, p_playerName as Top_Scorer, s_goals as Goals
from players, stats, teams, leagues
where s_playerID = p_playerID
    and p_teamID = t_teamID
    and t_leagueID = l_leagueID
    and l_leagueName = 'La Liga'
    and s_goals = (select max(s_goals) 
                    from stats, teams, players, leagues
                    where l_leagueName = 'La Liga'
                        and s_playerID = p_playerID
                        and t_leagueID = l_leagueID
                        and p_teamId = t_teamID);