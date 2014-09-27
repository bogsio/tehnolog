from app import app
from app.manager import ModelManager
from themes import ThemeManager
from flask import render_template

Theme = ThemeManager.get_theme(app.config['THEME'])

@app.route('/')
def index():
    return render_template(Theme.get_template(page='index'),
                           manager=ModelManager)