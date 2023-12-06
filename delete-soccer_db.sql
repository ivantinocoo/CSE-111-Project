-- Delete data from the 'nation' table
--DELETE FROM nation WHERE n_nationID = ;

-- Delete data from the 'leagues' table
--DELETE FROM leagues WHERE l_leagueID = 3;

-- Delete data from the 'teams' table
ALTER TABLE teams DROP COLUMN t_topScorer;
ALTER TABLE teams DROP COLUMN t_topScorerGoals;
--DELETE FROM teams WHERE t_teamID = 3;

-- Delete data from the 'players' table
AlTER TABLE players
DROP COLUMN p_teamName;
--DELETE FROM players WHERE p_playerID = 3;

-- Delete data from the 'matches' table
--DELETE FROM matches WHERE m_date = '2023-11-02';

-- Delete data from the 'coaches' table
--DELETE FROM coaches WHERE c_coachID = 3;
ALTER TABLE coaches
DROP COLUMN c_nationName;

ALTER TABLE coaches
DROP COLUMN c_teamName;

-- Delete data from the 'stats' table
--DELETE FROM stats WHERE s_playerID = 3;