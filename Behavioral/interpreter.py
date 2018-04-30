__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'

from abc import ABCMeta, abstractmethod


class AbstractExpression(object):
    """
    Declare an abstract Interpret operation that is common to all nodes
    in the abstract syntax tree.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def interpret(self):
        pass


class NonterminalExpression(AbstractExpression):
    """
    Implement an Interpret operation for nonterminal symbols in the grammar.
    """

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        self._expression.interpret()


class TerminalExpression(AbstractExpression):
    """
    Implement an Interpret operation associated with terminal symbols in
    the grammar.
    """

    def interpret(self):
        pass


if __name__ == "__main__":
    abstract_syntax_tree = NonterminalExpression(TerminalExpression())
    abstract_syntax_tree.interpret()
