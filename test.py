from parse_tree import Parser

pt1 = Parser("( ( ( 10 + 5 ) * 3 ) + ( 4 * 3 ) )")
print(pt1.get_expr())
print(pt1.eval())
# print(pt1.ast)

pt2 = Parser("( ( 1 + ( 2 * 3 ) ) - 5 )")
print(pt2.get_expr())
print(pt2.eval())

pt3 = pt1.__add__(pt2)

print(pt3.get_expr())
print(pt3.eval())
# print(pt3.ast)