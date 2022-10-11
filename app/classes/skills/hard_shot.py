from .base import Skill


class HardShot(Skill):
    name = "Мощный укол"
    stamina = 5
    damage = 15

    def skill_effect(self) -> str:
        """ Расчет нанесенного урона умения, и расхода выносливости противника """

        self.target.get_damage(self.damage)
        self.user.stamina -= self.stamina

        return f'{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику.'
