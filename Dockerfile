FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080

WORKDIR /app

# Zainstaluj zależności
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Skopiuj projekt
COPY . .

# Zbierz statyczne pliki (jeśli używasz)
# Domyślne polecenie do uruchomienia Django (z gunicorn)
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8080"]