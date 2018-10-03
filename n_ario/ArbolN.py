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
            return buscarEnArbol(nodo.nodos[0], valor) or buscarEnArbol2(nodo.nodos[1:len(nodo.nodos)], valor)

def buscarEnArbol2(nodos, valor):
    if len(nodos) == 0:
        return False
    else:
        return buscarEnArbol(nodos[0], valor) or buscarEnArbol2(nodos[1:len(nodos)], valor)