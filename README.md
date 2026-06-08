# 📝 Notes App

A simple, clean note-taking web app built with Django and Bootstrap. Create, search, pin, edit, and delete notes through a friendly, responsive interface — built as a learning project to practice Django fundamentals (models, views, forms, templates, messages, and migrations).

## Features

- **Create, edit, and delete notes**, with a confirmation step before deleting
- **Pin / unpin notes** to keep important ones at the top of the list
- **Search** notes by title or content (case-insensitive, via `request.GET` + `Q` lookups)
- **Live note count** that reflects the current view (all notes or search results)
- **Clickable note cards** for quick navigation to note details
- **Created** and **last updated** timestamps on every note
- **Form validation** with clear, friendly error messages
- **Auto-dismissing success notifications** for create / edit / pin / delete actions
- Responsive **Bootstrap 5** UI with icons

## Tech Stack

- [Django](https://www.djangoproject.com/) 5.2
- [Bootstrap](https://getbootstrap.com/) 5 and [Bootstrap Icons](https://icons.getbootstrap.com/) (via CDN)
- SQLite (default development database)

## Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/kbvyshnav/note-taking-app.git
   cd note-taking-app
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```bash
   python manage.py migrate
   ```

5. (Optional) Create a superuser to use the Django admin
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server
   ```bash
   python manage.py runserver
   ```

7. Open http://127.0.0.1:8000/notes/ in your browser

## Project Structure

```
note-taking-app/
├── core/              # Project settings and root URL configuration
├── notes/             # Notes app: models, views, forms, urls, templates
│   ├── migrations/
│   └── templates/notes/
├── manage.py
└── requirements.txt
```

## Usage

- Click **New Note** to create a note
- Click anywhere on a note card to open its details
- Use the search bar to find notes by title or content
- Use the **Pin / Unpin**, **Edit**, and **Delete** controls to manage your notes
