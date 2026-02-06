from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import summarize_email
from db import get_connection

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class EmailRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "AI Mail Summarizer API is running"}

@app.post("/api/summarize")
async def summarize(req: EmailRequest):
    result = summarize_email(req.text)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO email_summaries (subject, summary, category, priority)
        VALUES (%s, %s, %s, %s)
    """, ("AI Email", result["summary"], result["category"], "Normal"))

    conn.commit()
    cursor.close()
    conn.close()

    return result
