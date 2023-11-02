CREATE TABLE leagues (
    l_leagueID              int not null,
    l_leagueName            char(15) not null,
    l_nationID              int not null   
);

CREATE TABLE nation (
    n_nationID              int not null,
    n_nationName            varchar(15) not null
);

CREATE TABLE teams (
    t_teamID                int not null,
    t_teamName              char(15) not null,
    t_yearEstablished       varchar(152),
    t_wins                  int not null,
    t_losses                int not null,
    t_draws                 int not null,
    t_coachID               int not null,
    t_leagueID              int not null,
    t_homeID                int not null,
    t_awayID                int not null
);

CREATE TABLE players (
    p_playerID              int not null,
    p_playerName            varchar(25) not null,
    p_age                   int not null,
    p_position              varchar(4) not null,
    p_jerseyNumber          int not null,
    p_teamID                int not null
);

CREATE TABLE matches (
    m_matchID               int not null,
    m_date                  date not null,
    m_homeID                int not null,
    m_awayID                int not null
);

CREATE TABLE coaches (
    c_coachID               int not null,
    c_coachName             varchar(25) not null,
    c_teamID                int not null
);

CREATE TABLE stats (
    s_statsID               int not null,
    s_playerID              int not null,
    s_matchID               int not null,
    s_goalsScored           int not null,
    s_assists               int not null,
    s_yellowCards           int not null,
    s_redCards              int not null,
    s_saves                 int not null
);