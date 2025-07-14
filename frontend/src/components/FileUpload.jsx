
export default function FileUpload({ setSummary, setChunks, setUploading, uploading }) {
  const handleUpload = async (e) => {
    e.preventDefault();
    const file = e.target.file.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    setUploading(true);
    const res = await fetch('http://127.0.0.1:8000/upload/', { method: 'POST', body: formData });
    const data = await res.json();
    setSummary(data.summary);
    setChunks(data.chunks);
    setUploading(false);
  };

  return (
    <form onSubmit={handleUpload} className="card">
      <input type="file" name="file" accept=".pdf,.txt" required />
      <button type="submit" disabled={uploading}>
        {uploading ? 'Uploading...' : 'Upload File'}
      </button>
    </form>
  );
}
