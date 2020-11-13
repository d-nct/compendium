#! utf-8

def secante(f, a, b, xtol=1e-8, maxiter=100):
    """ Método da secante para a função  f  no intervalo  [a,b].

        Retorna um número  z  e as listas de extremidades esquerda e direita produzidas ao longo do algoritmo,
        que para quando o último passo é menor do que  xtol, ou depois de  maxiter  iterações.
    """
    def passo_secante(f, a, b): 
        """Dada a função  f, e o intervalo [a, b], aplica um passo do método da secante."""
        fa, fb = f(a), f(b) # Declaração de variaveis auxiliares
        return (a*fb - b*fa)/(fb - fa)
    
    # Estrutura recursiva
    def aux(f, a, b, xtol, num_iter, l, r):
        z = passo_secante(f, a, b) # Fazemos o passo
        num_iter += 1 # Atualizamos o número de iterações
        
        l.append(a)
        r.append(b)
        
        if abs(z - b) < xtol or num_iter == maxiter: return z, l, r # Atende aos critérios de parada
        else: return aux(f, b, z, xtol, num_iter, l, r)

    z, l, r = aux(f,a,b, xtol, 0, [], [])
    return z, np.array(l), np.array(r)
