import React, { useState } from 'react';

export default function ChallengeSection({ chunks }) {
  const [questions, setQuestions] = useState('');

  const handleChallenge = async () => {
    const form = new FormData();
    form.append('chunks', JSON.stringify(chunks));

    const res = await fetch('http://127.0.0.1:8000/challenge/', { method: 'POST', body: form });
    const data = await res.json();
    setQuestions(data.questions);
  };

  return (
    <div className="card">
      <h2>🧠 Challenge Me</h2>
      <button onClick={handleChallenge}>Generate Questions</button>
      <pre>{questions}</pre>
    </div>
  );
}
