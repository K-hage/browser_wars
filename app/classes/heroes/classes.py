from dataclasses import dataclass

from app.classes.skills import Skill, FuryPunch, HardShot, HeadShot


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name='Воин',
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch()
)

ThiefClass = UnitClass(
    name='Разбойник',
    max_health=50.0,
    max_stamina=25.0,
    attack=1.5,
    stamina=1.2,
    armor=1.0,
    skill=HardShot()
)

HuntClass = UnitClass(
    name='Охотник',
    max_health=55.0,
    max_stamina=35.0,
    attack=1.3,
    stamina=0.8,
    armor=0.8,
    skill=HeadShot()
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass,
    HuntClass.name: HuntClass
}
