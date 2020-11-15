#! utf-8

def crivo (n):
    """Retorna o conjunto de primos até  n, utilizando o método do Crivo de Erastótenes.
    Ressalta-se que n representa o intervalo semiaberto [0,n[
    
    Exemplo
    -------
    >>> crivo (10)
    {2, 3, 5, 7}
    >>> crivo (7)
    {2, 3, 5}
    """
    assert (isinstance(n, int)), "Para que a função funcione, n deve ser inteiro."
    #1. cria lista de tamanho n, com elementos True
    #2. caso base para evitar divisão por 0 e porque divisão por 1 não é critério para verificação de primos
    #3. percorremos a lista
    #3.1. se L[i] == True
    #3.2. seus múltiplos (a partir de i**2) viram False
    #4. retorna o conjunto de primos
    
    primos = set({})
    #1.
    L = [True for x in range (n)]
    #2.
    L[0], L[1] = False, False
    #3.
    for i in range (n):
        #3.1
        if L[i] == True:
            primos.add(i)
            for j in range (i**2, n):
                if j % i == 0:
                    L[j] = False
    return primos
    

cache_primos = {}
def eh_primo(p: int) -> int:
    """Verifica se p é primo. Retorna True se for primo e False se não for.
    
    Exemplo
    -------
    >>> eh_primo(10)
    False
    >>> eh_primo (5)
    True
    """
    assert (isinstance(p, int)), "A entrada de p deve ser um número inteiro"
    #0. condições básicas para n não ser primo
    #1. criar uma lista com os inteiros menores que raiz de p
    #2. verificar se algum dos números da lista divide p
    #3.1. caso sim, retornar False
    #3.2. caso não, retornar True
    
    if p in cache_primos:
        return cache_primos[p]
    
    #0.
    casos_base = {1,2,3} #O 3 fica inserido nos casos base devido à forma que o programa foi escrito: se p == 3, em 1., o range é nulo.
    if p in casos_base:
        return True
        
    if p % 2 == 0:
        return False
    
    #1.
    N = [2*x-1 for x in range (2, int((p+1)/2))] #2*x-1 pois os pares já foram descartados em 0.
    
    #2.
    for num in N:
        #3.1.
        if p % num == 0:
            cache_primos[p] = False
            return False
    #3.2.
    cache_primos[p] = True
    return True

def n_ésimo_primo (n):
    """Retorna o n-ésimo primo.
    Sequência dos primos: 2, 3, 5, 7, 11, 13...
    
    Exemplo
    -------
    >>> n_ésimo_primo (6)
    13
    """
    maior_primo = 0
    for x in range (n +1):
        maior_primo = primo_maior_que(maior_primo)
    return maior_primo


def primo_maior_que (n: int) -> int:
    """"Retorna o primeiro primo estritamente maior que n.
    
    Exemplo
    -------
    >>> primo_maior_que(10)
    11
    >>> primo_maior_que(5)
    7
    """
    n += 1 # testar n não é o objetivo da função.
    while not eh_primo (n):
        n += 1
    
    return n
    
    
def primos_conhecidos ():
    """Retorna o conjunto doss primos conhecidos (por mim)
    """
    with open ('primos.txt', 'r') as f:
        primos = {int(x[:-1]) for x in f.readlines()}
    return primos
    
    
def atualiza_primos():
    """Atualiza os primos conhecidos (por mim)
    """
    primos = primos_conhecidos()
        
    with open ('primos.txt', 'w') as f:
        novos_primos = list(cache_primos.union(primos))
        novos_primos.sort()
        for x in novos_primos:
            f.write(f'{x}\n')
          
          
if __name__ == '__main__':
	from doctest import testmod
	testmod()
