from flask import Blueprint, render_template, redirect, Response
from app.container import arena, heroes

app = Blueprint('fight_bp', __name__, template_folder='templates')


@app.route("/")
def start_fight() -> str:
    """ Начало боя """

    arena.start_game(player=heroes['player'], enemy=heroes['enemy'])
    return render_template('fight.html', heroes=heroes, battle_result='Бой начался')


@app.route("/hit/")
def hit() -> str:
    """ Кнопка нанесения удара"""

    if arena.game_is_running:
        result = arena.player_hit()
        return render_template('fight.html', heroes=heroes, result=result)
    else:
        battle_result = arena.battle_result
        return render_template('fight.html', heroes=heroes, battle_result=battle_result)


@app.route("/use-skill/")
def use_skill() -> str:
    """ Кнопка использования умения"""

    if arena.game_is_running:
        result = arena.player_use_skill()
        return render_template('fight.html', heroes=heroes, result=result)
    else:
        battle_result = arena.battle_result
        return render_template('fight.html', heroes=heroes, battle_result=battle_result)


@app.route("/pass-turn/")
def pass_turn() -> str:
    """ Кнопка пропуска хода """

    if arena.game_is_running:
        result = arena.next_turn()
        return render_template('fight.html', heroes=heroes, result=result)
    else:
        battle_result = arena.battle_result
        return render_template('fight.html', heroes=heroes, battle_result=battle_result)


@app.route("/end-fight/")
def end_fight() -> Response:
    """ Кнопка завершения игры """

    return redirect('main_bp.menu_page')
