#! utf-8

import numpy as np

def int_cauchy (f, a: float, b: float, N: float=1e4):
    """Retorna a integral definida de uma função vetorizada  f.
    
    Parameters
    ----------
    f : function
        Função a ser integrada;
    a : float
        Inicio do intervalo em que a integral será apreciada;
    b : float
        Final do intervalo em que a integral será apreciada;
    N : float, optional
        Número de subintervalos. O padrão é 1e4.
    
    Returns
    -------
    x : float
        Valor da integral em [a, b].
    """
    assert N > 0
    l, h = np.linspace(a, b, num=N, endpoint=False, retstep=True) # endpoint faz com que gere todos os x_k de x_0 até x_N-1
    return np.sum(f(l)) * h # np.sum  é mais rápido que  sum  pois é mais específico (otimizado)
