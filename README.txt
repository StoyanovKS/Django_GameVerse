## Prerequisites
- Python 3.12+
- PostgreSQL running (DB config is in settings.py)

## Setup
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

## Initialize DB
python manage.py makemigrations
python manage.py migrate

## Run
python manage.py runserver