class Nodo(object):
    def __init__(self, valor, nodos = []):
        self.valor = valor
        self.nodos = nodos

def buscarEnArbol(nodo, valor):
    if len(nodo.nodos) == 0: 
        if nodo.valor == valor:
            return True
        else:
            return False
    else:
        if nodo.valor == valor:
            return True
        else:
            for n in nodo.nodos:
                if(buscarEnArbol(n, valor)):
                    return True
            return False
