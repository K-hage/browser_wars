from typing import Optional, Dict, Any

from app.classes.heroes import BaseUnit


class BaseSingleton(type):
    _instances: Dict[Any, Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Dict:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False
    battle_result = ''

    def start_game(self, player: BaseUnit, enemy: BaseUnit) -> None:
        """ Начала игры: создаем персонажей, запускаем игру """

        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def _check_players_hp(self) -> Optional[str]:
        """ Проверка здоровья """

        if self.player.health_points > 0 and self.enemy.health_points > 0:
            return None

        if self.player.hp <= 0 and self.enemy.hp <= 0:
            self.battle_result = 'Ничья'

        elif self.player.hp <= 0:
            self.battle_result = 'Поражение'

        else:
            self.battle_result = 'Победа'

        return self._end_game()

    def _stamina_regeneration(self) -> None:
        """ Регенерация выносливости """

        units = (self.player, self.enemy)
        for unit in units:
            if unit.stamina + self.STAMINA_PER_ROUND > unit.unit_class.max_stamina:
                unit.stamina = unit.unit_class.max_stamina
            else:
                unit.stamina += self.STAMINA_PER_ROUND

    def next_turn(self) -> Optional[str]:
        """ Следующий ход """

        if self.game_is_running:
            self._stamina_regeneration()
            result = self.enemy.hit(self.player)
            self._check_players_hp()
            return result

    def _end_game(self) -> str:
        """ Кнопка завершения игры """

        self._instances: Dict[Any, Any] = {}
        self.game_is_running = False
        return self.battle_result

    def player_hit(self) -> str:
        """ Кнопка удара игрока """

        result = self.player.hit(self.enemy)
        enemy_result = self.next_turn()

        return f'{result}<br>{enemy_result}'

    def player_use_skill(self) -> str:
        """ Кнопка использования умения игрока """

        result = self.player.use_skill(self.enemy)
        enemy_result = self.next_turn()

        return f'{result}<br>{enemy_result}'
