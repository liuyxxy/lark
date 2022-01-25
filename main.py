import sys
from lark import Lark, Transformer
from test import parser, TreeToTest

if __name__ == '__main__':
    
    with open(sys.argv[1]) as f:
        tree = parser.parse(f.read()[0:])
        print(TreeToTest().transform(tree))