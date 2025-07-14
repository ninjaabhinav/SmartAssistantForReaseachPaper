# 🧠 Smart Research Assistant (React + FastAPI + Gemini AI)

An AI-powered research assistant web app that allows users to:

- 📤 Upload PDF or TXT files (like research papers)
- 📝 Automatically generate a 150-word summary
- 🤖 Ask questions from the document
- 🧠 Take a "Challenge Me" quiz based on the content

Built with **React (Vite)** for frontend, **FastAPI** for backend, and **Gemini AI** for language processing.

---

## 🚀 Features

- 📄 Upload and parse large research papers (PDF or TXT)
- ✨ Get a clean, AI-generated summary
- 🤔 Ask questions with real-time answers
- 🎯 Challenge yourself with AI-generated quiz questions
- 💬 Gemini Pro API integration for context-aware answers
- 💅 Responsive, minimal UI with loading indicators

---

## 📁 Project Structure
smart-assistant/
├── backend/ # FastAPI server
│ ├── main.py
│ └── requirements.txt
│
├── frontend/ # React + Vite frontend
│ ├── public/
│ │ └── index.html
│ ├── src/
│ │ ├── App.jsx
│ │ ├── main.jsx
│ │ ├── index.css / style.css
│ │ └── components/
│ │ ├── FileUpload.jsx
│ │ ├── SummaryCard.jsx
│ │ ├── AskSection.jsx
│ │ └── ChallengeSection.jsx
│ ├── package.json
│ └── vite.config.js


---

## 🛠️ Installation & Run Locally
## 📦 Frontend Setup Instructions (React + Vite)
🛠️ To set up the frontend:
Step 1: Navigate to the frontend directory
`cd frontend`
Step 2: Install dependencies and generate node_modules/
`npm install`
This command uses package.json to install all required packages.

Step 3: Run the development server
`npm run dev`
Your React app will be available at:
🔗 http://localhost:5173

🔒 Note on .gitignore
Make sure node_modules/ is excluded from version control by adding this line in .gitignore:

`node_modules/`

### ⚙️ Backend (FastAPI + Gemini)

`cd backend
pip install -r requirements.txt
uvicorn main:app --reload`

Backend runs on http://127.0.0.1:8000

Open Swagger docs: http://127.0.0.1:8000/docs

⚛️ Frontend (React)
`cd frontend
npm install
npm run dev`
Frontend runs on http://localhost:5173

🔑 Setup Gemini API
In main.py:
`genai.configure(api_key="YOUR_GEMINI_API_KEY")`
Get your API key from: https://makersuite.google.com/app/apikey


📄 License
MIT License. Use freely for learning and personal projects.

🙌 Author
Made with 💻 and ☕ by Abhinav Mishra
