# **Curso de Python**
Curso de Python 3.8.9 em Windows 7.

<br>

# **Preparação do ambiente**

## **Verificar a arquitetura do computador**
Isso é necessário para saber quais versões deverão ser baixadas e instaladas dos programas que serão usados. Podem ser um dos dois casos:
- 32 bits é x64
- 64 bits é x86

Para verificar, basta fazer o seguinte:
1. Abrir o `Explorador de Arquivos`
2. Clicar com o botão direito do mouse em `Computador`
3. Clicar em `Propriedades`

<center><img src="images\abrindo_configuracao_pc.png" alt="Abrindo a configuração do PC" width="600px" height="auto"></center>
<br>
<center><img src="images\verificando_configuracao_pc.png" alt="Checando o tipo de arquitetura" width="600px" height="auto"></center>
<br>

## **Instalar Python 3.8.9**
Visite o site https://www.python.org/downloads/release/python-389/

Vá até o final da página e baixe a vesão de acordo com a arquitetura do seu processador:

<center><img src="images\versao_python.PNG" alt="Baixando Python" width="900px" height="auto"></center>
<br>


## Criando variáveis de ambiente para usar o Python
**`TODO na VM`**
<br>

## Baixando o pip
No prompt de comando, executar o seguinte comando:
```bash
cd <diretório até o comando>\Aula_Python\get-pip.py
```

Ex:
```bash
cd C:\Users\LH\Desktop\Aula_Python
```

Execute o script para instalar o pip:
```bash
python .\get-pip.py
```
<br>

## Criando variáveis de ambiente para usar o Python
**`TODO na VM`**
<br>

## **Instalar Git** 
Visite o site http://git-scm.com/download/win

`OBS: cuidado com as opções na instalação, pode haver a necessidade de definir o VSCode como editor padrão do Git`

<center><img src="images\versao_git.png" alt="Baixando Git" width="600px" height="auto"></center>
<br>

## **Instalar VSCode**
Visite o site https://code.visualstudio.com/download

Clique no botão de download para Windows e realize a instalação.
<br>

## **Instalar extensões úteis do VSCode**

## Extensão de Markdown
Abrir a aba `Extensions` do VSCode, digitar markdown e instalar a extensão:
<center><img src="images\extensao_markdown.png" width="600px" height="auto"></center>
<br>

## Extensão de PDF
Abrir a aba `Extensions` do VSCode, digitar pdf e instalar a extensão:
<center><img src="images\extensao_pdf.png" width="600px" height="auto"></center>
<br>

## Extensão de Python
Abrir a aba `Extensions` do VSCode, digitar python e instalar a extensão:
<center><img src="images\extensao_python.png" width="600px" height="auto"></center>
<br>

## Criando ambiente virtual com venv
O `venv` permite que um ambiente virtual do Python seja criado, de forma que este seja isolado e possa ser deletado mais facilmente.

Execute o comando `<diretório do python>\python -m venv <diretório do venv>` para criar o venv. Exemplo:

``` cmd
C:\Users\LH\AppData\Local\Programs\Python\Python310\python.exe -m venv C:\Users\LH\Desktop\Aula_Python\projetos
```

<br>

# **Aula 1**
## Escopo
- Apresentação da linguagem
- Comentários
- Declaração de variáveis
- Input e print
- Tipos de variáveis
    - int
    - float
    - string
    - bool
- Conversão de variáveis

<br>

# **Aula 2**
## Escopo
- Operadores numéricos
    - Adição
    - Substração
    - Multiplicação
    - Divisão
    - Potenciação
- Operadores condicionais
    - Maior
    - Menor
    - Igual
    - Diferente
    - Maior ou igual
    - Menor ou igual
- Operadores booleanos
    - And
    - Or
    - Not

# **Aula 3**
## Escopo
- Aprofundamento em strings
- Concatenação
- Uso de indexes
- Funções úteis
    - len()
    - split()
    - find()
    - replace()

<br>

# **Aula 4**
## Escopo
- Condicionais
- if, elif, else
- try, except, else, finally
- Raise exception
<br>

# **Aula 5**
## Escopo
- Conceito de arrays (só vetores)
- Loops
    - While
    - For
- Listas
    - Fatiamento de listas
    - Concatenação de listas
    - Operações com listas

<br>

# **Aula 6**
## Escopo
- Aprofundamento de listas (matrizes)
- Dicionários
- Tuplas

<br>

# **Aula 7**
## Escopo
- Funções
- Declaração
- Retorno
- Passagem de parâmetros

<br>

# **Aula 8**
## Escopo
- Leitura e escrita de arquivos
    - TXT
    - JSON
    - PDF

<br>

# **Aula 9**
## Escopo
- PIP
- Bibliotecas
    - SciPy
    - NumPy
    - math
    - Mathplotlib
    - Pandas

<br>

# **Aula 10**
## Escopo
- Gráficos e análise de dados com pandas