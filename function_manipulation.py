from rootfinding import bissecao

def inv(f, a=0, b=1, xtol=1e-8, ytol=1e-8):
    """Retorna a função inversa de  f  no intervalo [a,b].
    A função inversa é garantida apenas para valores de  y  entre  f(a) e f(b)."""

    def func(y):
        def aux(x):
            return f(x) - y

        r, _ = bissecao(aux, a, b, xtol, ytol)
        return r

    return func
