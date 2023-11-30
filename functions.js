// Fetch leagues and populate the League filter dropdown
function fetchLeagues() {
    fetch('/api/leagues')
        .then(response => response.json())
        .then(data => {
            const leaguesDropdown = document.getElementById('league-filter');
            data.leagues.forEach(league => {
                const option = document.createElement('option');
                option.value = league[0]; // Assuming ID is the first element
                option.textContent = league[1]; // Assuming name is the second element
                leaguesDropdown.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching leagues:', error));
}

// Call the fetchLeagues function to populate the League filter on page load
document.addEventListener('DOMContentLoaded', fetchLeagues);

// Function to fetch teams based on the selected league
document.getElementById('league-filter').addEventListener('change', function() {
    const selectedLeagueId = this.value;
    fetchTeamsByLeague(selectedLeagueId);
});

function fetchTeamsByLeague(selectedLeagueId) {
    fetch('/api/teams-by-league', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ selected_league_id: selectedLeagueId })
    })
    .then(response => response.json())
    .then(data => {
        const teamsDropdown = document.getElementById('team-filter');
        teamsDropdown.innerHTML = ''; // Clear existing options
        data.teams.forEach(team => {
            const option = document.createElement('option');
            option.value = team[0]; // Assuming ID is the first element
            option.textContent = team[1]; // Assuming name is the second element
            teamsDropdown.appendChild(option);
        });
    })
    .catch(error => console.error('Error fetching teams by league:', error));
}