# -------------------------
# PILA
# -------------------------
class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        return list(reversed(self.items))  # de arriba hacia abajo


# -------------------------
# ÁRBOL BINARIO
# -------------------------
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.root = None

    def insertar(self, valor):
        self.root = self._insertar(self.root, valor)

    def _insertar(self, actual, valor):
        if actual is None:
            return NodoArbol(valor)
        if valor < actual.valor:
            actual.izq = self._insertar(actual.izq, valor)
        else:
            actual.der = self._insertar(actual.der, valor)
        return actual

    def inorden(self, nodo=None):
        if nodo is None:
            nodo = self.root
        if nodo:
            return self.inorden(nodo.izq) + [nodo.valor] + self.inorden(nodo.der)
        return []


# -------------------------
# GRAFO
# -------------------------
class Grafo:
    def __init__(self):
        self.lista = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.lista:
            self.lista[nodo] = []

    def agregar_arista(self, origen, destino):
        if origen in self.lista and destino in self.lista:
            self.lista[origen].append(destino)

    def mostrar(self):
        return self.lista
