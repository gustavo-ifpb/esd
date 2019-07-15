def novaPilha():
    return []

def contar(pilha):
    cont = 0
    for item in pilha:
        cont += 1
    return cont

def empilhar(pilha, item):
    pilha.append(item)

def desempilhar(pilha):
    if contar(pilha) > 0:
        return pilha.pop()
    return None

def removerCentral(pilha):
    tam = contar(pilha)
    # Pilha vazia!
    if tam == 0:
        return None
    rem = None
    # Criar pilha temporária
    p2 = []
    # Verificar se é par ou ímpar
    if tam % 2 == 0:
        # É par!
        for x in range((tam / 2) - 1):
            aux = desempilha(pilha)
            empilha(p2, aux)
        # Identifica maior
        c1 = desempilha(pilha)
        c2 = desempilha(pilha)
        if c1 > c2:
            rem = c1
            empilha(pilha, c2)
        else:
            rem = c2
            empilha(pilha, c1)    
    else:
        # É ímpar!
        for x in range(tam // 2):
            aux = desempilha(pilha)
            empilha(p2, aux)
        # Remove central
        rem = desempilha(pilha)
    # Re-empilha
    for x in range(contar(p2)):
        aux = desempilha(p2)
        empilha(pilha, aux)
    return rem