# BWGI
## Computed Property

Este é um decorator chamado computed_property, análogo ao property. Este decorator aceita múltiplos atributos dos quais ele depende, e cachea o valor da property enquanto o valor desses atributos permanecer inalterado.

Ele também aceita atributos que não pertencem ao objeto em questão (ignorando-os neste caso).

Assim como o property este decorator tem seus métodos setter e deleter, e trata corretamente _docstrings_.

## Conceito

Para viabilizar o desenvolvimento dessa solução foram utilizados os conceitos de descriptors e decorators. 

## Usando o decorator computed_property

Para utilizar o decorator computed_property basta importá-lo e decorar a propriedade desejada (como pode ser visto no exemplo).

O arquivo _example.py_ contém um exemplo de implementação utilizando o decorator. 