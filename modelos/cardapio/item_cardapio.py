#método abstrato
from abc import ABC,abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    #todas as classes derivadas precisam implementar esse método
    @abstractmethod
    def aplicar_desconto(self):
        pass
