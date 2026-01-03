import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const baseUrl = codespace
    ? `https://${codespace}-8000.app.github.dev/api/leaderboard/`
    : '/api/leaderboard/';

  useEffect(() => {
    console.log('Fetching from:', baseUrl);
    fetch(baseUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboard(results);
        console.log('Fetched leaderboard:', results);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [baseUrl]);

  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {leaderboard.map((l, i) => (
          <li key={i}>{l.team}: {l.points} points</li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;
