# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:32:30 2020

@author: amdshtar
"""

##### Recursão
cache_fib = {}
def fib_recursiva(n):
    """Retorna o n-ésimo elemento da sequência de Fibonacci.
    """
    assert n >= 0 and isinstance(n, int), "Estamos trabalhando com fib positivo."
    
    #memoização
    if n in cache_fib:
        return cache_fib[n]
    
    #caso-base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    #recursão
    result = fib_recursiva(n-1) + fib_recursiva(n-2)
    cache_fib[n] = result
    return result

##### Geradores
def take(n, g):
    """Gera até os n primeiros elementos do gerador g."""
    if n <= 0:
        return
    for i,v in enumerate(g):
        yield v # /0
        if i > n-2: # start from zero, stop at *previous iteration*
            return

def fib_generator(): #f_{i} = f_{i-1} + f_{i-2}
    i = 0
    while True:
        if i == 0:
            yield 1
            ultimo =1
            i += 1
            
            
        if i <= 1:
            yield 1
            ultimo = 1
            penultimo = 1
            i += 1
        
        else:
            yield ultimo + penultimo
            ultimo, penultimo = ultimo + penultimo, ultimo
            i += 1

def gen_fib_com (d):
    """ Retorna o gerador de números de Fibonacci com exatamente d dígitos.
    """
    primeira_vez = True
    if primeira_vez:
        ultimo = next(fib_generator())
        if len(str(ultimo)) == d:
            yield ultimo
            primeira_vez = False
        primeira_vez = False
    
    while len(str(ultimo)) == d:
        ultimo, penultimo = next(fib_generator()), ultimo
        yield penultimo
    return

def gen_fib_ate (d):
    """ Retorna o gerador de números de Fibonacci com até d dígitos.
    """
    primeira_vez = True
    if primeira_vez:
        ultimo = next(fib_generator())
        if len(str(ultimo)) <= d:
            yield ultimo
            primeira_vez = False
        primeira_vez = False
    
    while len(str(ultimo)) <= d:
        ultimo, penultimo = next(fib_generator()), ultimo
        yield penultimo
    return

##### Sequência
def fibo_rec (n):
    """Retorna um dicionário com a Sequência de Fibonacci até seu n-ésimo termo, associando o k-ésimo termo ao k-ésimo valor.
    """
    return {k: fib_recursiva(k) for k in range(n+1)}

def fibo_gen (n):
    """Retorna um dicionário com a Sequência de Fibonacci até seu n-ésimo termo, associando o k-ésimo termo ao k-ésimo valor.
    """
    return {k: v for k,v in enumerate(take(n, fib_generator()))}

#>>> %timeit fibo_gen(2000)
#1.1 ms ± 48.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
#
#>>> %timeit fibo_rec(2000)
#840 µs ± 13.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

#>>> D = fibo_rec(20000) ou fibo_gen(20000)
#>>> sys.getsizeof(D)
#589928 bytes