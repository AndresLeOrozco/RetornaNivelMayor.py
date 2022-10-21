import queue


class Nodo:
    def __init__(self, val=None):
        self.valor = val
        self.left = None
        self.right = None


class ArbolBinario:
    def __init__(self):
        self.root = None

    def insertar(self, key):
        # if root == nullptr
        if self.root is None:
            self.root = Nodo(key)
            return

        cola = queue.Queue()

        cola.put(self.root)
        while not cola.empty():
            tmp = cola.get()
            if tmp.left is not None:
                cola.put(tmp.left)
            else:
                tmp.left = Nodo(key)
                return
            if tmp.right is not None:
                cola.put(tmp.right)
            else:
                tmp.right = Nodo(key)
                return

    def RetornaAncestros(self, node, nodo):

        lis = []
        if nodo is None:
            return None
        if nodo.valor == node.valor:
            return lis

        listI = self.RetornaAncestros(node, nodo.left)
        if listI is not None:
            listI.append(nodo)
            return listI
        listD = self.RetornaAncestros(node, nodo.right)
        if listD is not None:
            listD.append(nodo)
            return listD
        return None


if __name__ == '__main__':
    arbolito = ArbolBinario()
    arbolito.insertar(10)
    arbolito.insertar(3)
    arbolito.insertar(90)
    arbolito.insertar(9)
    arbolito.insertar(15)
    arbolito.insertar(2)
    arbolito.insertar(6)
    arbolito.insertar(32)
    nodo = Nodo(32)
    Ancestors = arbolito.RetornaAncestros(nodo, arbolito.root)
    if Ancestors is not None:
        for x in Ancestors:
            print(x.valor, end=" ")
    else:
        print("No existe el valor buscado")
