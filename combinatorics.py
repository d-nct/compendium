cache_elemento = {}
def combination (i, j):
    """Retorna a combinação de  i  elementos escolhendo  j.
    """
    assert (i >= 0 or j >= 0 or j <= i), "Esse elemento não existe!"
    
    if (i,j) in cache_elemento:
        return cache_elemento[(i,j)]
    
    # estabelecemos os caso base
    if i == j or j == 0:
        return 1

    # e a recorrência
    else:
        result = pascal_elemento_memoizada(i-1,j) + pascal_elemento_memoizada (i-1,j-1)
        cache_elemento[(i,j)] = result
        return result
