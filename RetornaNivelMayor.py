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


    def retornaNivelMayor(self):
        cont = 1
        valorNiv = 0
        if self.root is None:
            return None

        cola = queue.Queue()
        aux = queue.Queue()
        cola.put(self.root)
        while not cola.empty():
            while not aux.empty():
                    aux = cola
                    tmp = cola.get()
                    tmpau = aux.get()
                    if tmp.left is not None:
                        cola.put(tmp.left)


                    if tmp.right is not None:
                        cola.put(tmp.right)

                    valorNiv = valorNiv + tmpau.valor







if __name__ == '__main__':
    arbolito = ArbolBinario()
    arbolito.insertar(10)
    arbolito.insertar(3)
    arbolito.insertar(90)
    arbolito.insertar(9)
    arbolito.insertar(15)
    arbolito.insertar(2)

