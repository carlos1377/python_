# python_ :snake:

Este é um repositório criado com o propósito inicial de permitir que eu estude em casa e no trabalho sem a necessidade de me mandar os arquivos e aprender um pouco sobre o Git. Com o passar do tempo percebi que existem muitos conteúdos na programação, alguns deles bem complexos, então estarei dedicando uma parte do meu tempo para transcrever os meus códigos em um grande resumão doque eu vi no curso que estou fazendo de Python, para uso meu e de quem quer que veja este repositório.

## Valores Truthy e Falsy

São os valores que o Python considera True ou False por mais que não sejam valores booleanos, como:
```python
if not '':
    print('truthy')
else:
    print('falsy')
```
Neste exemplo o if vai testar se a string vazia é True ou False, oque não retornaria nada.

Os dados como strings, dicts, sets, ranges(0), listas vazias/os e números que representam 0 são entendidos como não valores, que resultam em um resultado Falsy(False). Os valores Truthys(True) são todas as sequências ou coleções não vazias e valores numéricos diferentes de 0.

<!-- ## Funções
Pretendo voltar e falar sobre Decorators e Generators functions mais adiante, mu

### Decorators

### Generators -->

## OOP

Um dos principais paradigmas da programação, baseado em classes e objetos. Irei abordar seus pilares e algumas boas práticas.

### Encapsulamento