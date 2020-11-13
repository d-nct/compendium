#! utf-8

def menor_fator (num):
    fator = 2
    while num % fator != 0:
        fator = primo_maior_que (fator)
    return fator


def maior_fator_crescente (num):
    while True:
        fator = menor_fator(num)
        if fator < num:
            num //= fator
        else:
            return num


def fatora (num):
    """Retorna um dicionário associando o fator primo ao número de vezes que aparece compondo o num.
    """
    fatores = {}
    while num != 1:
        fator = int(maior_fator_crescente (num))
        try:
            fatores[fator] += 1
        except KeyError:
            fatores[fator] = 1
        num /= fator
    return fatores
