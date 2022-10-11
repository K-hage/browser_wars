from os import path

parent_dir = path.dirname(path.abspath(__file__))

# путь к json данным экипировки
EQUIPMENT_DATA = path.join(parent_dir, 'data', 'equipment.json')
