#! utf-8

def df(f, x: float, h: float=1e-6):
    """Retorna a derivada numérica central de  f  no ponto  x, com aproximação de  h.
    
    Parameters
    ----------
    f : function
        Função a ser derivada em  x.
    x : float
        Ponto em que  f  será derivada.
    h : float, optional
        Equivalente ao dh da derivada. Não utilize h <= 1e-16. O padrão é 1e-10.
    
    Returns
    -------
    p: float
        p é o valor da derivada numérica central f'(x).
    """
    return (f(x+h) - f(x-h)) / (2*h)


if __name__ == '__main__':
    import numpy as np
    from random import randint
        
    def f(x):   return x**2
    def ans(x): return 2*x
    
    assert np.isclose( df(f,0), ans(0) )
    assert np.isclose( df(f,3), ans(3) )
