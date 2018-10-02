import ArbolN as an
from ArbolN import Nodo

def main():
    arbol = Nodo(2, [Nodo(4, [Nodo(12), Nodo(24), Nodo(40)]), Nodo(8, [Nodo(15), Nodo(32)]), Nodo(5, [Nodo(25), Nodo(50)])])
    print(an.buscarEnArbol(arbol, 30))

if __name__ == "__main__":
    main()