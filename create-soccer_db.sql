CREATE TABLE leagues (
    l_leagueID              int not null,
    l_leagueName            char(15) not null,
    l_nationID              int not null   
);

CREATE TABLE nation (
    n_nationID              int not null,
    n_nationName            varchar(50) not null
);

CREATE TABLE teams (
    t_teamID                int not null,
    t_teamName              char(15) not null,
    t_matchesPlayed         int not null,
    t_wins                  int not null,
    t_draws                 int not null,
    t_losses                int not null,
    t_goalsFor              int not null,
    t_goalsAgainst          int not null,
    t_goalsDifference       int not null,
    t_Points                int not null,
    t_topScorer             char(15) not null,
    t_topScorerGoals        int not null
);

CREATE TABLE players (
    p_playerID              int not null,
    p_playerName            varchar(25) not null,
    p_position              varchar(4) not null,
    p_teamName              char(15) not null,
    p_age                   int not null,
    p_born                  int not null
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
    c_nationName            varchar(25) not null,
    c_teamName              varchar(25) not null,
    c_age                   int not null,
    c_contractExpire        int not null
);

CREATE TABLE stats (
    s_playerID              int not null,
    s_matchesPlayed         int not null,
    s_starts                int not null,
    s_minutes               int not null,
    s_goals                 int not null,
    s_shots                 DECIMAL(7,2) not null,
    s_passCompleted         DECIMAL(7,2) not null,
    s_passAttempted         DECIMAL(7,2) not null,
    s_assists               DECIMAL(7,2) not null,
    s_interceptions         DECIMAL(7,2) not null,
    s_clearences            DECIMAL(7,2) not null,
    s_touches               DECIMAL(7,2) not null,
    s_yellowCards           int not null,
    s_redCards              int not null
);