from dotenv import load_dotenv
load_dotenv()

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


@app.get("/api/summaries")
def list_summaries(limit: int = 50):
    """Return recent email summaries from the database."""
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT id, subject, summary, category, priority, created_at
            FROM email_summaries
            ORDER BY created_at DESC
            LIMIT %s
            """,
            (limit,),
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        for row in rows:
            if row.get("created_at"):
                row["created_at"] = row["created_at"].isoformat()
        return {"summaries": rows}
    except Exception as e:
        return {"summaries": [], "error": str(e)}


@app.post("/api/summarize")
async def summarize(req: EmailRequest):
    result = summarize_email(req.text)

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO email_summaries (subject, summary, category, priority)
            VALUES (%s, %s, %s, %s)
            """,
            ("AI Email", result["summary"], result["category"], "Normal"),
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception:
        # API still returns the summary even if DB write fails (e.g. DB not set up)
        pass

    return result
