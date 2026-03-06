Este projeto consiste em uma calculadora simples feita em Python que permite realizar operações matemáticas básicas pelo terminal.

O programa pede dois números e o sinal da operação desejada, faz o cálculo e mostra o resultado na tela.

As operações disponíveis são:

Soma

Subtração

Multiplicação

Divisão

Porcentagem

O programa também faz algumas verificações simples, como impedir divisão por zero e avisar quando uma operação inválida é digitada.

Funcionalidades

Realizar operações matemáticas básicas no terminal.

Aceitar diferentes símbolos para a mesma operação (por exemplo * ou x para multiplicação e / ou : para divisão).

Verificar divisão por zero.

Calcular porcentagem simples.

Aceitar números decimais com vírgula ou ponto.

Mostrar o resultado da operação de forma clara.

Avisar quando uma operação inválida é digitada.

Lógica utilizada

O programa pede ao usuário:

O primeiro número

O sinal da operação

O segundo número

Depois disso, o código usa estruturas condicionais (if, elif e else) para descobrir qual operação o usuário escolheu.

Dependendo do sinal digitado, ele faz o cálculo correspondente:

+ para soma

- para subtração

* ou x para multiplicação

/ ou : para divisão

% para porcentagem

Também existe uma verificação para impedir divisão por zero, que é uma operação indefinida.

Além disso, antes de transformar os valores em números, o programa troca vírgula por ponto, permitindo digitar números decimais no padrão brasileiro.

Exemplo de uso

O usuário informa:

Primeiro número

Sinal da operação

Segundo número

Exemplo de entrada:

10
*
5

O programa retorna:

Resultado da operação = 50
