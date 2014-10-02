from app import app
from app.manager import ModelManager
from themes import ThemeManager
from flask import render_template, request

Theme = ThemeManager.get_theme(app.config['THEME'])

@app.route('/')
def index():
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    return render_template(Theme.get_template(page='index'),
                           page=page,
                           manager=ModelManager)