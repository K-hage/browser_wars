from .choose import app as choose_bp
from .fight import app as fight_bp
from .main import app as main_bp
from .errors import app as errors_bp

__all__ = [
    'choose_bp',
    'fight_bp',
    'main_bp',
    'errors_bp'
]
