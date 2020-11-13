#! utf-8

def busca_binaria (sequencia, elemento, inicio=0, fim=0):
    """Retorna o índice do elemento na dada sequência ordenada crescentemente.
    Se elemento não está na sequência, retorna -1.
    
    Exemplo
    -------
    >>> l = [2,4,6,8,10]
    >>> busca_binaria(l, 4)
    1
    >>> busca_binaria(l,0)
    -1
    """
    if len(sequencia) == 0: return -1
    
    elif len(sequencia) == 1: 
        if sequencia[0] == elemento:
            return 0
        else:
            return -1
    
    
    def aux(sequencia, elemento, inicio, fim):
        inicio = 0
        fim = len(sequencia) -1
        i = int(fim - inicio/2)
        
        
        if sequencia[i] == elemento:
            return i
        
        elif sequencia[i] > elemento:
            fim    = i
            return busca_binaria (sequencia[inicio:fim], elemento, inicio, fim)
        
        elif sequencia[i] < elemento:
            inicio = i
            return busca_binaria (sequencia[inicio:fim], elemento, inicio, fim)
			
    return aux(sequencia, elemento, 0, len(sequencia)-1)


if __name__ == '__main__':
	from doctest import testmod
	testmod()
	
	# Testes Direcionados
	# -------------------	
	l1 = range(100+1)
	assert busca_binaria(l1, 10)  == 10
	assert busca_binaria(l1, 100) == 100
	assert busca_binaria(l1, 0)   == 0
	
	l2 = [1]
	assert busca_binaria(l2, 1) == 0
	assert busca_binaria(l2, 0) == -1
	
	l3 = []
	assert busca_binaria(l3, 0) == -1
	
	# Testes Aleatórios
	# -----------------
	from random import randint	
	for _ in range(50):
	    lenght = randint(0, 100+1)
	    l4 = range(lenght)
	    alvo = randint(0, lenght+100)
	    if alvo >= lenght: # Se não podemos encontrar
	        assert busca_binaria(l4, alvo) == -1
	    elif alvo < lenght: # Se podemos encontrar
	        assert busca_binaria(l4, alvo) == alvo
