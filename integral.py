#! utf-8

import numpy as np

# Método de Cauchy
# ----------------
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
    

# Métododo Trapézio
# -----------------
def int_trap (f, a: float, b: float, N: int=1e4) -> float:
    """Retorna a integral definida de uma função vetorizada  f.
    
    Parameters
    ----------
    f : function
        Função a ser integrada;
    a : float
        Inicio do intervalo em que a integral será apreciada;
    b : float
        Final do intervalo em que a integral será apreciada;
    N : int, optional
        Número de retângulos. O padrão é 1e4.
    
    Returns
    -------
    x : float
        Valor da integral em [a, b].
    """
    assert N > 0
    l, h = np.linspace(a, b, num=N, endpoint=False, retstep=True)
    return np.sum(f(l)) * h + (f(b) - f(a)) * h/2


# Método do Ponto Médio
# ---------------------
def int_midp (f, a: float, b: float, N: int=1e4) -> float:
    """Retorna a integral definida de uma função vetorizada  f no intervalo  [a,b] com N retângulos centrados nos pontos médios.
    
    Parameters
    ----------
    f : function
        Função a ser integrada;
    a : float
        Inicio do intervalo em que a integral será apreciada;
    b : float
        Final do intervalo em que a integral será apreciada;
    N : int, optional
        Número de retângulos. O padrão é 1e4.
    
    Returns
    -------
    x : float
        Valor da integral em [a, b].
    """
    assert N > 0
    l, h = np.linspace(a, b, num=N, endpoint=False, retstep=True)
    mids = l + h/2
    return np.sum(f(mids)) * h
    

# Método de Simpson
# -----------------
def int_simpson (f, a: float, b: float, N: int=1e4) -> float:
    """Retorna a integral definida de uma função vetorizada  f no intervalo  [a,b]  com N > 0 
    subintervalos.
    
    Parameters
    ----------
    f : function
        Função a ser integrada;
    a : float
        Inicio do intervalo em que a integral será apreciada;
    b : float
        Final do intervalo em que a integral será apreciada;
    N : int, optional
        Número de subintervalos. O padrão é 1e4.
    
    Returns
    -------
    x : float
        Valor da integral em [a, b].
    """
    assert N > 0
    l, h = np.linspace(a,b, num=N, endpoint=False, retstep=True)
    mids = l + h/2
    return ( 4*np.sum(f(mids)) + 2*np.sum(f(l)) + (f(b) - f(a)) ) * h/6


# Nós de Chebyschev e Divisão do Intervalo
# ----------------------------------------
c16 = np.array([0.9951847266721969,
0.9569403357322088,
0.881921264348355,
0.773010453362737,
0.6343932841636455,
0.4713967368259978,
0.29028467725446233,
0.09801714032956077,
-0.09801714032956065,
-0.29028467725446216,
-0.4713967368259977,
-0.6343932841636454,
-0.773010453362737,
-0.8819212643483549,
-0.9569403357322088,
-0.9951847266721968,
])

w16 = np.array([0.016802755230667654,
0.05833646406882406,
0.09171831320616108,
0.1251296181573093,
0.15139246163822329,
0.17341941177110334,
0.18774972811543006,
0.19545124781253848,
0.1954512478115949,
0.18774972811610163,
0.1734194117707848,
0.15139246163829367,
0.12512961815734253,
0.09171831320610976,
0.05833646406886149,
0.016802755230654203,
])

def cheby16(f,a,b,n):
    """Integrates f over [a,b], subdividing in n equal intervals, using 16 Chebyshev points in each."""
    if n == 1:
        ts = np.array([a])
        h  = (b-a)
    else:
        ts, h = np.linspace(a,b,num=n, endpoint=False, retstep=True)

    xs = (c16+1)*h/2
    xs = xs.reshape((1,-1))
    ts = ts.reshape((-1,1))
    all_ts = ts + xs
    all_fts = f(all_ts)
    return np.sum(np.dot(all_fts,w16))*h/2
