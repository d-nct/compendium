#! utf-8

from os import listdir

__all__ = []
for x in listdir('/home/danieln/python/compendium'):
    if '.py' in x and '__main__.py' != x: # Apenas pastas
        __all__.append(x)
