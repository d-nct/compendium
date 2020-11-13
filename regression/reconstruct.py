#! utf-8

def reconstruct(coefs, base):
    """Retorna a função correspondente aos coeficientes e à base escolhida de uma regressão.
    """
    def m(x):   
        ans = 0
        for beta, coef in zip(base, coefs):
            ans += coef * beta(x)
        return ans         
        
    return m
