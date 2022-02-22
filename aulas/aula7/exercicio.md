# Exercício da aula 6
## Proposta
Faça uma calculadora que receba como entrada (input) dois números de ponto flutuante (float, ou decimal) e o tipo de operação (soma, subtração, multiplicação ou divisão).

O recebimento dos números, o tipo de operação (soma, multiplicação, etc) e os cálculos devem ser feitos com funções que retornem os valores coletados ou calculados.

Verifique se os números digitados realmente são do tipo float e a operação digitada também é válida. Procure usar um bloco try ... except e algumas raise exceptions para printar qual foi o erro ocorrido e encerrar o código (no caso de algo inválido ser inserido), ou printar o resultado da operaçõ em caso de sucesso.

Exemplo em caso de sucesso:

```bash
Digite o primeiro valor: <7>
Digite o segundo valor: <3>
Digite o tipo de operação: <->

Resultado:
7 - 3 = 4
```

Exemplo em caso de erro:

```bash
Digite o primeiro valor: <7>
Digite o segundo valor: <a>
Digite o tipo de operação: </>

Erro detectado: segundo número é inválido!
Encerrando execução.
```

Dica: reveja o exercício da aula 4.