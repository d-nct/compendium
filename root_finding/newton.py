#! utf-8

def newton(f, df, x0: float=0, prec: float=1e-8, ytol: float=1e-8, maxiter: int=100, verbose: bool=False):
    """Aplica o método de Newton na função  f  e retorna a aprox. da raiz (com o erro mínimo erro_min).

    Parameters
    ----------
    f : function
        Função a qual será aplicada o Método de Newton
    df : function
        Derivada de f.
    x0 : float, opcional
        Ponto inicial a ser vasculhado. Idealmente, está próximo da raiz. O padrão é 0.
    prec : float, optional
        Tamanho do passo de newton pequeno o suficiente para retornarmos um valor. O padrão é 1e-8.
    ytol : float, optional
        Tamanho da tolerância ao redor do eixo y para retornarmos um valor. O padrão é 1e-8.
    maxiter : int, optional
        Máximo de iterações da função. O padrão é 100.
    verbose : bool, optional
        Estabelece se irá retornar, também, uma lista com os x_n alcansados.

    Returns
    -------
        Se verbose=True:
        <raíz: float>, <número de iterações: int>, <[x_1, x_2, x_3, ...]: list>
        Se verbose=False:
        <raíz: float>, <número de iterações: int>
    """
    trace = [x0]
    num_iter = 0
    x_i = x0

    while num_iter <= maxiter:
        passo = f(x_i)/df(x_i)
        novo_x, num_iter = x_i - passo, num_iter + 1
        if verbose: trace.append(novo_x)
        x_i = novo_x
        if abs(passo) < prec or abs(f(x_i)) < ytol: 
            break
        

    if num_iter > maxiter:
        novo_x = None # Retornamos None para alertar o usuário que não encontramos uma raiz
    if verbose: return novo_x, num_iter, np.array(trace)
    else: return novo_x, num_iter
   
if __name__ == '__main__':
    import numpy as np
    
    def f(x): return x**2 - 2
    def df(x): return 2*x
    
    r, _ = newton(f,df)
    assert np.isclose(r, np.sqrt(2))
