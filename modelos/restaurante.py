from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        #atributo protegido _
        self._ativo = False
        self._avaliacao = []
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