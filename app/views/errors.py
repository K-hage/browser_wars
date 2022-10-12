from flask import Blueprint, render_template

app = Blueprint('errors_bp', __name__, template_folder='templates')


@app.app_errorhandler(404)  # обработчик ошибки 404
def page_not_found(e):
    return render_template('404.html', error=e), 404


@app.app_errorhandler(500)  # обработчик ошибки 500
def server_error(e):
    return render_template('500.html', error=e), 500