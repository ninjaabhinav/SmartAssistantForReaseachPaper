from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import fitz  # PyMuPDF
import google.generativeai as genai
import json
import os

# 🔐 Configure Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY") # ← Replace with your actual key
model = genai.GenerativeModel(model_name="gemini-pro")

# 🚀 Initialize FastAPI app
app = FastAPI()

# 🌐 Allow frontend access (React CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📄 Extract text from uploaded file
def extract_text(filename, content):
    if filename.endswith(".pdf"):
        with open("temp.pdf", "wb") as f:
            f.write(content)
        doc = fitz.open("temp.pdf")
        text = "\n".join([page.get_text() for page in doc])
        doc.close()
        os.remove("temp.pdf")
    else:
        text = content.decode("utf-8")
    return text

# ✂️ Chunk large text
def get_chunks(text, max_chunk_size=3000):
    words = text.split()
    chunks, chunk = [], []
    for word in words:
        chunk.append(word)
        if len(" ".join(chunk)) > max_chunk_size:
            chunks.append(" ".join(chunk))
            chunk = []
    if chunk:
        chunks.append(" ".join(chunk))
    return chunks

# 📝 Summarize extracted text
def summarize_text(text):
    prompt = f"Summarize this text in around 150 words:\n{text}"
    response = model.generate_content(prompt)
    return response.text

# ❓ Ask a question
def ask_gemini(question, chunks):
    context = " ".join(chunks[:2])
    prompt = f"Using the context:\n{context}\nAnswer this: {question}"
    response = model.generate_content(prompt)
    return response.text, "Answer derived from uploaded content."

# 🧠 Generate challenge questions
def generate_questions(chunks):
    context = " ".join(chunks[:2])
    prompt = f"Using the following text:\n{context}\nCreate 3 MCQ questions."
    response = model.generate_content(prompt)
    return response.text

# ✅ Evaluate user's answer
def evaluate_answer(answer, user_response):
    prompt = f"Evaluate this response:\nAnswer: {answer}\nUser: {user_response}"
    response = model.generate_content(prompt)
    return response.text

# 🚩 Upload endpoint
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(file.filename, content)
    summary = summarize_text(text)
    chunks = get_chunks(text)
    return JSONResponse({"summary": summary, "chunks": chunks})

# ❓ Ask endpoint
@app.post("/ask/")
async def ask_route(question: str = Form(...), chunks: str = Form(...)):
    chunks = json.loads(chunks)
    answer, justification = ask_gemini(question, chunks)
    return JSONResponse({"answer": answer, "justification": justification})

# 💡 Challenge endpoint
@app.post("/challenge/")
async def challenge_route(chunks: str = Form(...)):
    chunks = json.loads(chunks)
    questions = generate_questions(chunks)
    return JSONResponse({"questions": questions})

# 🔍 Evaluate endpoint (optional)
@app.post("/evaluate/")
async def evaluate_route(answer: str = Form(...), user_response: str = Form(...)):
    evaluation = evaluate_answer(answer, user_response)
    return JSONResponse({"evaluation": evaluation})
