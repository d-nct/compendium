#! utf-8

def df_num(f, x: float, h: float=1e-10):
    """Retorna a derivada numérica de  f  no ponto  x, com aproximação de  h.
    
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
        p é o valor da derivada numérica f'(x).
    """
    return (f(x+h) - f(x)) / h


if __name__ == '__main__':
    import numpy as np
        
    def f(x): return x**2
    def ans(x): return 2*x
    
    assert np.isclose( df(f,0), 0 )
    
    for _ in range(50+1):
        n = np.random.randint(-10, 10)
        assert np.isclose( df(f,n), ans(n) )
