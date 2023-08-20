__version__ = '0.0.1'

from waffle_factory.hub import start
from waffle_factory.models import trainer
from waffle_factory.utils import SETTINGS as settings

__all__ =  'start', 'settings', 'trainer'  # allow simpler import
