#! utf-8

import numpy as np

# Regressão Polinomial
# --------------------
def reg_poly(xs, ys, grau):
    """Retorna a função da regressão polinomial dos pontos (xs,ys).
    """
    vander = np.vander(xs, grau+1) 
    coefs, *_ = np.linalg.lstsq(vander, ys, rcond=None)
    p = np.poly1d(coefs) 
    return p 

def regress_with_error(xs, ws, phis):
    """Regressão linear dos pontos  (xs,ys)  para a base de funções dada pela lista  phis,
    retornando os coeficientes e o erro da regressão."""
    M_list = []
    for x in xs:
        linha = []
        for phi in phis:
            linha.append( phi(x) )
        M_list.append(linha)
    M = np.asmatrix(M_list)
    coefs, err, *_ = np.linalg.lstsq(M, ws, rcond=None)
    return coefs, err
    

# Reconstruct
# -----------
def reconstruct(coefs, base):
    """Retorna a função correspondente aos coeficientes e à base escolhida de uma regressão.
    """
    def m(x):   
        ans = 0
        for beta, coef in zip(base, coefs):
            ans += coef * beta(x)
        return ans         
        
    return m
