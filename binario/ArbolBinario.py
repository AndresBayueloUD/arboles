class Nodo(object):

    def __init__(self, valor, nodoLeft=None, nodoRight=None):
        self.valor = valor
        self.nodoLeft = nodoLeft
        self.nodoRight = nodoRight
    
class Hoja(object):
     def __init__(self, valor):
        self.valor = valor

def buscarEnArbol(nodo, valor):
    if isinstance(nodo, Hoja):
        if nodo.valor == valor:
            return True
        else:
            return False
    if isinstance(nodo, Nodo):
        if nodo.valor == valor:
            return True
        else:
            if valor < nodo.valor:
                return buscarEnArbol(nodo.nodoLeft, valor)
            else:
                return buscarEnArbol(nodo.nodoRight, valor)
            
def contarNodos(nodo):
    if nodo is None:
        return 0
    if isinstance(nodo, Hoja):
        return 0
    if isinstance(nodo, Nodo):
        return 1 + contarNodos(nodo.nodoLeft) + contarNodos(nodo.nodoRight)

def contarHojas(nodo):
    if nodo is None:
        return 0
    if isinstance(nodo, Hoja):
        return 1
    if isinstance(nodo, Nodo):
        return contarHojas(nodo.nodoLeft) + contarHojas(nodo.nodoRight)

def contarElementos(nodo):
    if nodo is None:
        return 0
    if isinstance(nodo, Hoja):
        return 1
    if isinstance(nodo, Nodo):
        return 1 + contarElementos(nodo.nodoLeft) + contarElementos(nodo.nodoRight)

def insertarElemento(nodo, valor):
    if nodo is None:
        return Hoja(valor)
    if isinstance(nodo, Hoja):
        if valor <= nodo.valor:
            return Nodo(nodo.valor, Hoja(valor), None)
        if valor > nodo.valor:
            return Nodo(nodo.valor, None, Hoja(valor))
    if isinstance(nodo, Nodo):
        if valor <= nodo.valor:
            return Nodo(nodo.valor, insertarElemento(nodo.nodoLeft, valor), nodo.nodoRight)
        if valor > nodo.valor:
            return Nodo(nodo.valor, nodo.nodoLeft, insertarElemento(nodo.nodoRight, valor))

def preOrden(nodo):
    if nodo is None:
        return []
    if isinstance(nodo, Hoja):
        return [nodo.valor]
    if isinstance(nodo, Nodo):
        return [nodo.valor] + preOrden(nodo.nodoLeft) + preOrden(nodo.nodoRight)

def posOrden(nodo):
    if nodo is None:
        return []
    if isinstance(nodo, Hoja):
        return [nodo.valor]
    if isinstance(nodo, Nodo):
        return posOrden(nodo.nodoLeft) + posOrden(nodo.nodoRight) + [nodo.valor]

def enOrden(nodo):
    if nodo is None:
        return []
    if isinstance(nodo, Hoja):
        return [nodo.valor]
    if isinstance(nodo, Nodo):
        return enOrden(nodo.nodoLeft) + [nodo.valor] + enOrden(nodo.nodoRight)