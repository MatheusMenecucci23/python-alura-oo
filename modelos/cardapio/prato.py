from modelos.cardapio.item_cardapio import ItemCardapio

#herdando o ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        #herdando os atributos do item pai
        super().__init__(nome, preco)
        #personalizando a classe prato
        self.descricao = descricao

    def __str__(self):
        return self._nome