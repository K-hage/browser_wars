from flask import Blueprint, render_template
from app.classes.arena import Arena
from app.classes.heroes import BaseUnit

app = Blueprint('fight_bp', __name__, template_folder='templates')

arena = Arena()
heroes = {
    "player": BaseUnit,
    "enemy": BaseUnit
}


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
def end_fight() -> str:
    """ Кнопка завершения игры """

    return render_template("index.html")
