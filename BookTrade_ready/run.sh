#!/usr/bin/env bash
set -e
python3 -m venv venv
source venv/bin/activate
pip install --no-cache-dir -r requirements.txt
flask db init || true
flask db migrate -m "init" || true
flask db upgrade
python scripts/seed_data.py
python run.py