import operator
from stack import Stack
from binary_tree import BinaryTree


class Parser:
    opers = {'*': operator.mul, '/': operator.truediv,
             '+': operator.add, '-': operator.sub}

    def __init__(self, infix_expr):  # infix_expr - split
        self.ast = self.make_ast(infix_expr)

#############
    def __add__(self, other):
        return Parser(f'( {self.get_expr()} + {other.get_expr()} )')

    def __sub__(self, other):
        return Parser(f'( {self.get_expr()} - {other.get_expr()} )')

    def __mul__(self, other):
        return Parser(f'( {self.get_expr()} * {other.get_expr()} )')

    def __truediv__(self, other):
        if other.eval() == 0:
            print("Divide by zero error")
            return
        return Parser(f'( {self.get_expr()} / {other.get_expr()} )')

############

    def make_ast(self, infix_expr):
        stack = Stack()

        new_tree = BinaryTree('')
        current_tree = new_tree

        for token in infix_expr.split():
            if token == '(':
                current_tree.insert_left('')
                stack.push(current_tree)
                current_tree = current_tree.get_left_child()
            elif token in ['+', '-', '*', '/']:
                current_tree = stack.pop()  # peek
                current_tree.set_root_val(token)
                current_tree.insert_right('')
                stack.push(current_tree)
                current_tree = current_tree.get_right_child()
            elif token == ')':
                current_tree = stack.pop()
            else:
                try:
                    current_tree.set_root_val(int(token))
                except ValueError:
                    raise ValueError(f"Token '{token}' is not a valid integer.")

        assert current_tree is new_tree
        return new_tree

    def eval(self):
        def eval_node(tree):  # BinaryTree/None
            if tree is not None:
                res1 = eval_node(tree.get_left_child())
                res2 = eval_node(tree.get_right_child())
                if res1 is not None and res2 is not None:
                    return Parser.opers[tree.get_root_val()](res1, res2)
                else:
                    return tree.get_root_val()
            return None

        return eval_node(self.ast)

    def get_expr(self):
        def get_node_list(tree):  # BinaryTree
            if tree.get_left_child() is None:  # Węzeł to liczba
                return [str(tree.get_root_val())]
            values = ['(']
            values.extend(get_node_list(tree.get_left_child()))
            values.append(tree.get_root_val())
            values.extend(get_node_list(tree.get_right_child()))
            values.append(')')
            return values

        return " ".join(get_node_list(self.ast))


if __name__ == "__main__":
    pt = Parser("( ( ( 10 + 5 ) * 3 ) + ( 4 * 3 ) )")
    print(pt.eval())
    print(pt.get_expr())
    print(pt.ast)

    pt = Parser("( 1 + ( 2 * 3 ) )")
    # print(pt.get_expr())
    # pt.ast.preorder()  # NP
    # pt.ast.inorder()   # ONP
    # pt.ast.postorder() # infiksowo, ale nawiasy się gubią
