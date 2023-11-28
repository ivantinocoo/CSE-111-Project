function fetchLeaguesAndDisplay() {
    fetch('/api/leagues')
        .then(response => response.json())
        .then(data => {
            const leaguesList = document.getElementById('leagues-list');
            data.leagues.forEach(league => {
                const listItem = document.createElement('p');
                listItem.textContent = `${league.l_leagueID} - ${league.l_leagueName}`;
                leaguesList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error:', error));
}