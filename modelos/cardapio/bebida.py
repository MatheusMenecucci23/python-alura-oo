from modelos.cardapio.item_cardapio import ItemCardapio

#herdando o ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        #classe ItemCardapio é a classe base que estamos reaproveitando os atributos
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome

    #método abstrato
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)
