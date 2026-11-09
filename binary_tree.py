# Dwa spojrzenia na BinaryTree: key; left; right:
# 1. Jako węzeł:  klucz w węźle; lewe dziecko; prawe dziecko
# 2. Jako drzewo: Klucz w korzeniu; lewe poddrzewo; prawe poddrzewo


class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#########
    def copy(self):
        shallow_copy = BinaryTree(self.key)
        shallow_copy.left = BinaryTree(self.left.key)
        shallow_copy.right = BinaryTree(self.right.key)
        return shallow_copy
#########

    def height(self):

            if self.left is None and self.right is None:
                return 0 # set to 0 if counting the path, set to 1 if counting the nodes

            if self.left is None:
                left_height = 0
            else:
                left_height = self.left.height() + 1

            if self.right is None:
                right_height = 0
            else:
                right_height = self.right.height() + 1

            if left_height >= right_height:
                return left_height
            else:
                return right_height


    def count_leaves(self):
        if self.left is None and self.right is None:
            return 1

        if self.left is None:
            left_leaf_count = 0
        else:
            left_leaf_count = self.left.count_leaves()

        if self.right is None:
            right_leaf_count = 0
        else:
            right_leaf_count = self.right.count_leaves()

        return left_leaf_count + right_leaf_count

###############################

    def insert_left(self, key):
        t = BinaryTree(key)
        if self.left is None:
            self.left = t
        else:
            t.left = self.left
            self.left = t

    def insert_right(self, key):
        t = BinaryTree(key)
        if self.right is None:
            self.right = t
        else:
            t.right = self.right
            self.right = t

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def __str__(self):
        return f"[{self.key}; {self.left}; {self.right}]"


    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.key)

        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.key)

        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()

        print(self.key)


if __name__ == "__main__":
    r = BinaryTree('a')
    print(r)
    r.insert_left('b')
    print(r)
    r.get_left_child().insert_right('c')
    print(r)
