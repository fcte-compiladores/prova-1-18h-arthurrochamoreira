#  Edite​ a​ ​classe​ LoxTransformer nesse​ ​arquivo.​ Boa prova!
"""
Implementa o transformador da árvore sintática que converte entre as representações

    lark.Tree -> lox.ast.Node.

A resolução de vários exercícios requer a modificação ou implementação de vários
métodos desta classe.
"""

from typing import Callable

from lark import Transformer, v_args

from . import runtime as op
from .ast import *  # inclui BinOp, Var, Literal, Call, Assign, VarDef, Print, Block, UnaryOp, Getattr, List

def op_handler(op: Callable):
    """
    Fábrica de métodos que lidam com operações binárias na árvore sintática.

    Recebe a função que implementa a operação em tempo de execução.
    """
    def method(self, left, right):
        return BinOp(left, right, op)
    return method

@v_args(inline=True)
class LoxTransformer(Transformer):
    # Regra inicial: retorna um Program contendo todos os statements
    def start(self, *stmts):
        print("START FOI CHAMADO!", stmts)
        return Program(list(stmts))


    # Operações matemáticas básicas
    mul = op_handler(op.mul)
    div = op_handler(op.truediv)
    sub = op_handler(op.sub)
    add = op_handler(op.add)

    # Comparações
    gt = op_handler(op.gt)
    lt = op_handler(op.lt)
    ge = op_handler(op.ge)
    le = op_handler(op.le)
    eq = op_handler(op.eq)
    ne = op_handler(op.ne)

    # Operações unárias
    def not_(self, expr):
        return UnaryOp(op.not_, expr)

    def neg(self, expr):
        return UnaryOp(op.neg, expr)

    # Chamadas e parâmetros
    def call(self, name, *params):
        params = list(params)
        return Call(name.name, params)

    def params(self, *args):
        return list(args)

    # Atribuições e definições
    def assign(self, name: Var, value: Expr):
        return Assign(name.name, value)

    def var_def(self, name: Var, expr: Expr | None = None):
        return VarDef(name.name, expr)

    def list(self, *elems):
        return List(list(elems))

    # Comandos
    def print_cmd(self, expr):
        return Print(expr)

    def block(self, *stmts: Stmt):
        return Block(list(stmts))
    
    def while_cmd(self, cond, body):
        return While(cond, body)

    # Tokens
    def VAR(self, token):
        return Var(str(token))

    def NUMBER(self, token):
        return Literal(float(token))

    def STRING(self, token):
        return Literal(str(token)[1:-1])

    def NIL(self, _):
        return Literal(None)

    def BOOL(self, token):
        return Literal(token == "true")

    # Acesso a atributos
    def getattr(self, obj, name):
        return Getattr(obj=obj, name=name.name)
