from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        #atributo protegido _
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)


    #indicando como o objeto vai ter a representação dele como string
    def __str__(self):
        return self._nome | self._categoria
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas, 1)
        return media            


    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    #indicando que é um método da classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacão'.ljust(24)} | {'Status'} ')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |{str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo} ')
    
    #decorator que pega o atributo e modifica a forma do atributo ser lido
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0< nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        #
        for i,item in enumerate(self._cardapio, start=1):
            #se tiver o atributo has attribute
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome{item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome{item._nome} | Preço: R${item._preco} | Descrição: {item.tamanho}'
                print(mensagem_bebida)

# #instanciando um objeto
# restaurante_praca = Restaurante('Praça','Gourmet')
# restaurante_pizza = Restaurante('Pizza', 'Pizza')

# restaurantes = [restaurante_praca,restaurante_praca]

# #mostra todos os atributos e métodos
# print(dir(restaurante_praca))
# print("----------------------")
# #mostra todos os atributos
# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))
# print("----------------------")
# #chamando método
# Restaurante.listar_restaurantes()