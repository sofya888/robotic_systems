class ExpressionTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def evaluate(self):
        """Вычисление значения выражения"""
        if self.value.isdigit():
            return int(self.value)

        left_val = self.left.evaluate()
        right_val = self.right.evaluate()

        if self.value == '+':
            return left_val + right_val
        elif self.value == '-':
            return left_val - right_val
        elif self.value == '*':
            return left_val * right_val
        elif self.value == '/':
            return left_val / right_val

    @staticmethod
    def build_from_postfix(expression):
        """Построение дерева из постфиксной записи"""
        stack = []
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                stack.append(ExpressionTree(token))
            else:
                right = stack.pop()
                left = stack.pop()
                node = ExpressionTree(token)
                node.left = left
                node.right = right
                stack.append(node)

        return stack.pop()


# Пример: (3 + 4) * 5 в постфиксной записи: 3 4 + 5 *
expr_tree = ExpressionTree.build_from_postfix("3 4 + 5 *")
print(f"Результат: {expr_tree.evaluate()}")  # 35