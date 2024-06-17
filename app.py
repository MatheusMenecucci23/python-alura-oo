
#importando arquivos
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

#criando restaurante
restaurante_praca = Restaurante('praça','Gourmet')

#criando bebida e suco
bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato("Paozinho", 2.0, 'O melhor pão da cidade')

#aplicando o desconto classe abstrata
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

#adicionando no cardapio
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()