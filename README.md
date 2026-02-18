Campus Super Hub / AIfusion is a student-focused web dashboard designed to simplify everyday campus activities.  
It integrates an AI‑style email summarizer with multiple campus utilities such as mess menu viewing, student
exchange modules, and database‑backed campus service components.

The mail summarizer condenses long academic emails into short actionable information and categorizes them
for easier understanding. The backend is built using **FastAPI** with a **MySQL** database layer, while the
frontend uses plain **HTML + CSS + JavaScript**.

---

## Local development

1. **Create and activate a virtualenv (recommended)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # on Windows
   # source .venv/bin/activate  # on macOS / Linux
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MySQL**

   - Install and start MySQL (local or remote).
   - Copy `.env.example` to `.env` and set:
     - `DB_HOST`
     - `DB_USER`
     - `DB_PASSWORD`
     - `DB_NAME`

4. **Create database and tables**

   ```bash
   python init_db.py
   ```

5. **Run the FastAPI app (serves API + frontend)**

   ```bash
   uvicorn main:app --reload
   ```

   - API base: `http://127.0.0.1:8000`
   - Frontend:
     - Mail summarizer UI: `http://127.0.0.1:8000/`
     - Campus Super Hub dashboard: `http://127.0.0.1:8000/dasboard.html`

   The frontend JavaScript automatically talks to the same origin in this setup.

---

## Deploying on Render.com

This repo includes a `render.yaml` so you can create the service from the Render dashboard with one click.

### 1. Push to GitHub

1. Commit your changes locally.
2. Push the repository to GitHub (e.g. `main` branch).

### 2. Create a Web Service on Render

1. Go to the Render dashboard and choose **New → Web Service**.
2. Select this GitHub repository.
3. Render will detect `render.yaml` and pre‑configure a **Python Web Service** with:
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Health check path: `/api/health`

### 3. Configure environment variables

In the Render service settings, add these environment variables under **Environment**:

- `DB_HOST` – hostname or IP of your MySQL server
- `DB_USER` – database username
- `DB_PASSWORD` – database password
- `DB_NAME` – database name (e.g. `campus_hub`)

> Render does not host MySQL natively – you can point these variables to any accessible MySQL instance
> (cloud provider, campus server, etc.).

### 4. Initialize the database on Render (optional)

If the target MySQL database is empty, run this once from Render:

1. Open the service → **Shell**.
2. Run:

   ```bash
   python init_db.py
   ```

This will create the `email_summaries` and `mess_menu` tables.

### 5. Use the deployed app

Once the deploy is green:

- Open the Render URL (e.g. `https://aifusion-campus-hub.onrender.com/`) for the **Mail Summarizer UI**.
- Visit `/dasboard.html` on the same domain for the **Campus Super Hub dashboard**.

The dashboard will call the backend API at the same origin, and recent summaries are loaded from the MySQL database.
