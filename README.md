# Aplikacja webowa flask

## System webowy umożliwiający prowadzenie bloga z przepisami oraz udostępniający możliwość interkacji użytkowników z danymi przepisami (oceny, komentarze)

## Stack technologiczny
W skład aplikacji na chwilę obecną wchodzi:
- **Backend:** Python, Flask, Flask-Login, Flask-Admin, Flask-SQLAlchemy  
- **Frontend:** HTML, CSS, JavaScript, szablony Jinja2  
- **Baza danych:** SQLite 
- **DevOps:** Docker, Docker Compose, CI Workflow do automatycznej weryfikacji buildów 
- **Kontrola wersji:** Git z `.gitignore` dla plików środowiska i cache  

## Kluczowe funkcjonalnosi
Aplikacja na chwilę obecną umożliwia:
- dodawanie przepisów
- administracje zawartością strony poprzez panel administratora
- logowanie i uwierzytlenianie z użyciem **Flask-Login**

## Uruchomienie aplikacji
Po pobraniu repozytorium należy uruchomić docker-compose z użyciem komendy:
docker-compose up --build

Aplikacja zostanie uruchomiona na localhoście pod adresem