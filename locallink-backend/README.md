# LocalLink Backend

Django + DRF + PostgreSQL. See `docs/decisions.md` for the agreed architecture.

## Setup (Windows PowerShell / Linux / macOS)

```bash
# 1. Virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements/dev.txt

# 2. Environment file
cp .env.example .env               # Windows: copy .env.example .env
# edit .env: set DJANGO_SECRET_KEY and the Postgres password (in BOTH places)

# 3. Database (Docker, Postgres only)
docker compose up -d

# 4. Verify
python manage.py check
pytest
python manage.py runserver
# then open http://127.0.0.1:8000/api/v1/health/
```

> Do NOT run `migrate` yet. The custom User model must exist before the first migration.
