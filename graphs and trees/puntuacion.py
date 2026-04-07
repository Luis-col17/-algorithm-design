class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(nodo.derecha, valor)


    def minimo(self):
        actual = self.raiz
        while actual.izquierda:
            actual = actual.izquierda
        return actual.valor


    def maximo(self):
        actual = self.raiz
        while actual.derecha:
            actual = actual.derecha
        return actual.valor

    def top_n(self, n):
        resultado = []

        def recorrer(nodo):
            if nodo is None or len(resultado) >= n:
                return
            
            recorrer(nodo.derecha)  # primero los mayores
            
            if len(resultado) < n:
                resultado.append(nodo.valor)
            
            recorrer(nodo.izquierda)

        recorrer(self.raiz)
        return resultado
    
torneo = BST()

puntos = [3200, 4100, 1800, 5000, 2700, 3900, 4600]

for p in puntos:
    torneo.insertar(p)

print("Mínimo:", torneo.minimo())     # 1800
print("Máximo:", torneo.maximo())     # 5000
print("Top 3:", torneo.top_n(3))      # [5000, 4600, 4100]