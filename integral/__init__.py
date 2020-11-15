from os import listdir

l = listdir('/home/danieln/python/compendium/integral')

__all__ = []
for x in l:
    if '.py' in x: # Apenas .py
        __all__.append(x[:-3])

__all__.remove('__init__')