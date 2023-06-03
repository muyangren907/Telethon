from .client.mingancihuiclient import dxdmgchClient
from .network import connection
from .tl.custom import Button
from .tl import patched as _  # import for its side-effects
from . import version, events, utils, errors, types, functions, custom

__version__ = version.__version__

__all__ = [
    'dxdmgchClient', 'Button',
    'types', 'functions', 'custom', 'errors',
    'events', 'utils', 'connection'
]
