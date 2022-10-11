from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug import Response

from app.classes.equipment import Equipment
from app.classes.heroes import unit_classes, PlayerUnit, EnemyUnit
from app.views.fight import heroes

app = Blueprint('choose_bp', __name__, template_folder='templates')

equipment = Equipment()
weapons = equipment.get_weapons_names()
armors = equipment.get_armors_names()


@app.route("/hero/", methods=['post', 'get'])
def choose_hero() -> Response | str:
    """
    Выбор героя
    GET - меню параметров героя
    POST - создание героя
    """

    if request.method == 'GET':
        result = {
            'header': 'Выберите героя',
            'classes': unit_classes,
            'weapons': weapons,
            'armors': armors
        }
        return render_template('hero_choosing.html', result=result)

    elif request.method == 'POST':

        name = request.form['name']
        hero = request.form['unit_class']
        armor = request.form['armor']
        weapon = request.form['weapon']
        player = PlayerUnit(name=name, unit_class=unit_classes[hero])

        # снаряжаем броней
        player.equip_armor(equipment.get_armor(armor))

        # снаряжаем оружием
        player.equip_weapon(equipment.get_weapon(weapon))
        heroes['player'] = player

        return redirect(url_for('choose_bp.choose_enemy'))


@app.route("/enemy/", methods=['post', 'get'])
def choose_enemy() -> Response | str:
    """
    Выбор противника
    GET - меню параметров противника
    POST - создание противника
    """

    if request.method == 'GET':
        result = {
            'header': 'Выберите противника',
            'classes': unit_classes,
            'weapons': weapons,
            'armors': armors
        }
        return render_template('hero_choosing.html', result=result)

    elif request.method == 'POST':

        name = request.form['name']
        hero = request.form['unit_class']
        armor = request.form['armor']
        weapon = request.form['weapon']
        enemy = EnemyUnit(name=name, unit_class=unit_classes[hero])

        # снаряжаем броней
        enemy.equip_armor(equipment.get_armor(armor))

        # снаряжаем оружием
        enemy.equip_weapon(equipment.get_weapon(weapon))
        heroes['enemy'] = enemy

        return redirect(url_for('fight_bp.start_fight'))
