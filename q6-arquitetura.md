De modo abstrato, o compilador é um programa que converte código de uma
linguagem para outra. Como se fosse uma função do tipo `compilador(str) -> str`.
No caso de compiladores que emitem código de máquina ou bytecode, seria mais
preciso dizer `compilador(str) -> bytes`, mas a idéia básica é a mesma.

De forma geral o processo é dividido em etapas como abaixo

```python
def compilador(x1: str) -> str | bytes:
    x2 = lex(x1)        # análise léxica
    x3 = parse(x2)      # análise sintática
    x4 = analysis(x3)   # análise semântica
    x5 = optimize(x4)   # otimização
    x6 = codegen(x5)    # geração de código
    return x6
```

Defina brevemente o que cada uma dessas etapas realizam e marque quais seriam os
tipos de entrada e saída de cada uma dessas funções. Explique de forma clara o
que eles representam. Você pode usar exemplos de linguagens e/ou compiladores
conhecidos para ilustrar sua resposta. Salve sua resposta nesse arquivo.

# lex(x1: str) -> list\[Token]

Lê o fluxo de caracteres do código-fonte e agrupa em unidades significativas chamadas tokens Cada token representa um lexema, como identificadores, palavras-chave, operadores e literais. O analisador léxico também descarta espaços em branco e comentários.

# parse(x2: list\[Token]) -> Tree

Recebe a lista de tokens e constrói uma arvore de derivação ou árvore sintática que representa a estrutura gramatical do programa. A análise sintática verifica se os tokens estão em uma ordem válida segundo a gramática da linguagem.

# analysis(x3: Tree) -> AnnotatedTree

Utiliza a árvore sintática para verificar restrições semânticas da linguagem, como verificação de tipos, uso correto de variáveis e coerções. Adiciona anotações à árvore ou usa uma tabela de símbolos para registrar atributos.

# optimize(x4: AnnotatedTree) -> AnnotatedTree

Transforma a representação intermediária para uma versão mais eficiente, preservando sua semântica. Pode eliminar código morto, simplificar expressões ou reorganizar operações para melhor desempenho.

# codegen(x5: AnnotatedTree) -> str | bytes

Gera o código alvo, que pode ser assembly, bytecode ou código de máquina. A geração de código leva em conta instruções da arquitetura alvo, alocação de registradores e geração de instruções otimizadas.

