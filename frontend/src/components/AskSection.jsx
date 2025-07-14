import { useState } from 'react';

export default function AskSection({ chunks }) {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  const handleAsk = async () => {
    const form = new FormData();
    form.append('question', question);
    form.append('chunks', JSON.stringify(chunks));

    const res = await fetch('http://127.0.0.1:8000/ask/', { method: 'POST', body: form });
    const data = await res.json();
    setResponse(`Answer: ${data.answer}

Justification: ${data.justification}`);
  };

  return (
    <div className="card">
      <h2>❓ Ask Anything</h2>
      <input type="text" value={question} onChange={(e) => setQuestion(e.target.value)} placeholder="Enter your question..." />
      <button onClick={handleAsk}>Ask</button>
      <pre>{response}</pre>
    </div>
  );
}
