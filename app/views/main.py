from flask import Blueprint, render_template

app = Blueprint('main_bp', __name__, template_folder='templates')


@app.route("/")
def menu_page() -> str:
    """ Главное меню """

    return render_template('index.html')
