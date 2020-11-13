#! utf-8

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
