Campus Super Hub is a student-focused web dashboard designed to simplify everyday campus activities. 
It integrates an AI-powered email summarizer with multiple campus utilities such as mess menu viewing, 
student exchange modules, and database-backed campus service components.

The AI module summarizes long academic emails into short actionable information and categorizes them 
for easier understanding. The backend is built using FastAPI with a MySQL database layer, while the 
frontend uses HTML, CSS, and JavaScript.

## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **MySQL**
   - Install and start MySQL.
   - (Optional) Copy `.env.example` to `.env` and set `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` if different from defaults (`localhost`, `root`, `340515`, `campus_hub`).

3. **Create database and tables**
   ```bash
   python init_db.py
   ```

4. **Run the API**
   ```bash
   uvicorn main:app --reload
   ```
   API runs at `http://127.0.0.1:8000`. The summarizer and dashboard use this URL.

5. **Use the app**
   - Open `index.html` in a browser for the Mail Summarizer, or `dasboard.html` for the full Campus Super Hub. Summarize an email to save entries to the database; the dashboard shows recent summaries from the DB.
