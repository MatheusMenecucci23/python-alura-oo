# README - Sistema de Gestão de Restaurantes

## Visão Geral

Este projeto é um sistema simples de gestão de restaurantes desenvolvido em Python. Ele permite criar instâncias de restaurantes, gerenciar seu status, receber avaliações e listar todos os restaurantes cadastrados com suas respectivas categorias e médias de avaliações.

## Estrutura do Código

### Classe `Restaurante`

A classe `Restaurante` possui os seguintes atributos e métodos:

- **Atributos**
  - `nome`: Nome do restaurante.
  - `categoria`: Categoria do restaurante (ex: Gourmet, Pizza).
  - `_ativo`: Estado do restaurante (ativo ou inativo).
  - `_avaliacao`: Lista de avaliações recebidas.
  - `restaurantes`: Lista de todos os restaurantes cadastrados.

- **Métodos**
  - `__init__(self, nome, categoria)`: Inicializa a instância do restaurante com nome e categoria.
  - `__str__(self)`: Define a representação em string do objeto.
  - `media_avaliacoes(self)`: Calcula e retorna a média das avaliações recebidas.
  - `listar_restaurantes(cls)`: Lista todos os restaurantes cadastrados com suas informações.
  - `ativo(self)`: Retorna o estado atual do restaurante (ativo ou inativo).
  - `alternar_estado(self)`: Alterna o estado do restaurante entre ativo e inativo.
  - `receber_avaliacao(self, cliente, nota)`: Adiciona uma avaliação ao restaurante.

### Classe `Avaliacao`

A classe `Avaliacao` deve ser implementada no módulo `modelos/avaliacao.py`. Esta classe representa uma avaliação recebida por um restaurante, contendo o nome do cliente e a nota da avaliação.




## Explicação de `@property` e `@classmethod`

### `@property`

A palavra-chave `@property` é usada para definir métodos em uma classe que agem como atributos. Isso permite que você acesse o método como se fosse um atributo, sem precisar chamá-lo com parênteses.


## Explicação de `@classmethod`

### `@classmethod`

A palavra-chave `@classmethod` é usada para definir métodos que pertencem à classe e não a uma instância específica da classe. Isso significa que o método pode acessar e modificar a classe em si e não apenas os objetos criados a partir dela.

