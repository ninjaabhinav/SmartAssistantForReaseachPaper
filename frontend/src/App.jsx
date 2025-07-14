import { useState } from 'react';
import AskSection from './components/AskSection';
import ChallengeSection from './components/ChallengeSection';
import FileUpload from './components/FileUpload';
import SummaryCard from './components/SummaryCard';

export default function App() {
  const [summary, setSummary] = useState('');
  const [chunks, setChunks] = useState([]);
  const [uploading, setUploading] = useState(false);

  return (
    <div className="container">
      <h1>📄 Smart Research Assistant</h1>
      <FileUpload
        setSummary={setSummary}
        setChunks={setChunks}
        setUploading={setUploading}
        uploading={uploading}
      />
      {summary && <SummaryCard summary={summary} />}
      {chunks.length > 0 && (
        <>
          <AskSection chunks={chunks} />
          <ChallengeSection chunks={chunks} />
        </>
      )}
    </div>
  );
}
