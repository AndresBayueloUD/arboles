import ArbolBinario as ab
from ArbolBinario import Nodo, Hoja

def main():
    arbol = Nodo(12, 
        Nodo(8,
            Hoja(4), Nodo(10,
                Hoja(9), Hoja(11)
                )
            ),
        Nodo(25,
            Hoja(17), Nodo(30,
                Hoja(28), Hoja(50)
                )
            )
        )

    #print(ab.buscarEnArbol(arbol,50))
    #print(ab.contarNodos(arbol))
    #print(ab.contarHojas(arbol))
    #print(ab.contarElementos(arbol))
    arbol = ab.insertarElemento(arbol,15)
    print(ab.buscarEnArbol(arbol,15))
    #print(ab.preOrden(arbol))
    #print(ab.posOrden(arbol))
    #print(ab.enOrden(arbol))

if __name__ == "__main__":
    main()