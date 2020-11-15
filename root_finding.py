#! utf-8

# Bissection
# ----------
def bissecao(f, a: float, b: float, xtol=1e-8, ytol=1e-8, verbose=False):
    """Encontra uma raíz de  f  no intervalo  [a,b] pelo método da bisseção.

    Parâmetros
    ----------
    f : function
        Função a ser utilizada.
    a  : float
        Extremidade esquerda do intervalo em que será procurada uma raiz.
    b  : float
        Extremidade direita do intervalo em que será procurada uma raiz.
    xtol  : int/float, opcional
        Tolerância ao redor da raiz no eixo x. O padrão é 1e-8.
    ytol  : int/float, opcional
        Tolerância ao redor da raiz no eixo y. O padrão é 1e-8.
    verbose  : bool, opcional
        Se True, retorna como terceiro valor uma lista com as extremidades dos intervalos construídos da forma: [(a_1,b_1), (a_2,b_2), ...]

    Retorno
    -------
    Se verbose=False: retorna a tupla da forma (<raiz>, <numero_de_bissecoes>)
    se verbose=True:  retorna a tupla da forma (<raiz>, <numero_de_bissecoes>, [(a_1,b_1), (a_2,b_2), ...])
    """
    def passo_da_bissecao(f, a: float, b: float):
        """Retorna o novo intervalo após uma etapa da bisseção da função f,
        da forma (a,m) ou (m,b) segundo em qual seja possível garantir uma raiz de f.
        """
        m = (a + b) / 2
        if f(m) * f(a) < 0:
            return a, m
        else:
            return m, b
        
        
    a0, b0 = a, b
    intervalos = [(a, b)]
    num_bissecoes = 0
    achei = False
    while not abs(b - a) < xtol and not abs(f((a + b) / 2)) <= ytol:  # Para que a função saia do laço, será necessário que sejam satisfeitos pelo menos um dos critérios de parada!
        # Verificamos se as extremidades do intervalo são raiz
        if f(a) == 0:
            valor_final, achei = a, True
            break
        elif f(b) == 0:
            valor_final, achei = b, True
            break

        # Fazemos uma bicessão
        a, b = passo_da_bissecao(f, a, b)
        num_bissecoes += 1  # Atualizamos o número de vezes que foram feitas bicessões
        if verbose:
            intervalos.append((a, b))
    # Se chegamos até aqui, é porque já podemos parar!
    if not achei:
        valor_final = (a + b) / 2
    if abs(f(valor_final)) > 1:  # Fazemos a prova real com uma tolerância muito grande porque a bisseção sempre encontra algum valor porque o intervalo fica pequeno o suficiente para passar na xtol. Dessa forma, avisamos ao usuário que o número obtido não se trata de uma raiz.
        # raise ValueError(f'Não foi possível encontrar uma raiz de {f} no intervalo [{a0}, {b0}].')
        print(f'Não foi possível encontrar uma raiz de {f} no intervalo [{a0}, {b0}].')
        valor_final = None
    if verbose:
        intervalos.append((a, b))
        return valor_final, num_bissecoes, intervalos
    else:
        return valor_final, num_bissecoes



def bissect_geq(l, v: float) -> int:
    """First index  k  on an increasing list  l  such that  l[k] >= v.
    Returns  len(l)  if  l[-1] < v."""
    assert len(l) != 0, "A lista não pode ser indexada."
    if l[-1] < v: return len(l)  # "caso base"
    if l[0] >= v: return 0  # problema na verificação do l[a-1], pois acaba com a ordem da verificação.

    a, b = 0, len(l)

    while True:
        meio = (a + b) // 2
        v_meio = l[meio]
        if v_meio > v:  # Indica que o alvo está na primeira metade da lista.
            if l[a - 1] < v and l[a] >= v: return a  # Verificamos as extremidades do intervalo
            if l[b - 1] < v and l[b] >= v: return b
            b, meio = meio, (a + meio) // 2
        elif v_meio <= v:  # Indica que o alvo está na segunda metade da lista.
            if l[a - 1] < v and l[a] >= v: return a
            if l[b - 1] < v and l[b] >= v: return b
            a, meio = meio, (meio + b) // 2


# Newton Method
# -------------
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
