def mod(path):
    from os import listdir
    
    l = listdir(path)
    
    var = []
    for x in l:
        if not '.' in x: # Apenas pastas
            var.append(x)

__all__ = mod('/home/danieln/python/compendium')

def pol5(x): return x**5 - x - 1