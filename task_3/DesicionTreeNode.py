class DecisionTreeNode:
    def __init__(self, feature=None, threshold=None, value=None, left=None, right=None):
        self.feature = feature  # Индекс признака для разделения
        self.threshold = threshold  # Пороговое значение
        self.value = value  # Значение для листового узла
        self.left = left  # Левое поддерево (<= threshold)
        self.right = right  # Правое поддерево (> threshold)

    def is_leaf(self):
        return self.value is not None


class SimpleDecisionTree:
    def __init__(self, max_depth=5):
        self.max_depth = max_depth
        self.root = None

    def fit(self, X, y):
        """Обучение дерева"""
        self.root = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        # Базовые случаи для остановки
        if depth >= self.max_depth or len(set(y)) == 1:
            return DecisionTreeNode(value=self._most_common_label(y))

        # Находим лучшее разделение
        best_feature, best_threshold = self._best_split(X, y)

        if best_feature is None:
            return DecisionTreeNode(value=self._most_common_label(y))

        # Разделяем данные
        left_mask = X[:, best_feature] <= best_threshold
        right_mask = ~left_mask

        # Рекурсивно строим поддеревья
        left = self._build_tree(X[left_mask], y[left_mask], depth + 1)
        right = self._build_tree(X[right_mask], y[right_mask], depth + 1)

        return DecisionTreeNode(
            feature=best_feature,
            threshold=best_threshold,
            left=left,
            right=right
        )

    def predict(self, X):
        """Предсказание для нескольких образцов"""
        return [self._predict_sample(x, self.root) for x in X]

    def _predict_sample(self, x, node):
        if node.is_leaf():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._predict_sample(x, node.left)
        else:
            return self._predict_sample(x, node.right)

    def _best_split(self, X, y):
        # Упрощенная реализация поиска лучшего разделения
        best_gain = -1
        best_feature = None
        best_threshold = None

        for feature in range(X.shape[1]):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                gain = self._information_gain(y, X[:, feature], threshold)

                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold

    def _information_gain(self, y, feature, threshold):
        # Упрощенный расчет информационного прироста
        left_mask = feature <= threshold
        right_mask = ~left_mask

        if sum(left_mask) == 0 or sum(right_mask) == 0:
            return 0

        n = len(y)
        n_left, n_right = sum(left_mask), sum(right_mask)

        # Энтропия родителя
        parent_entropy = self._entropy(y)

        # Взвешенная энтропия детей
        left_entropy = self._entropy(y[left_mask])
        right_entropy = self._entropy(y[right_mask])
        child_entropy = (n_left / n) * left_entropy + (n_right / n) * right_entropy

        return parent_entropy - child_entropy

    def _entropy(self, y):
        """Расчет энтропии"""
        proportions = np.bincount(y) / len(y)
        return -np.sum([p * np.log2(p) for p in proportions if p > 0])

    def _most_common_label(self, y):
        """Наиболее частый класс"""
        return np.bincount(y).argmax()


import numpy as np
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=100, n_features=4, random_state=42)
tree = SimpleDecisionTree(max_depth=3)
tree.fit(X, y)
predictions = tree.predict(X)


def show_tree(node, depth=0):
    indent = "  " * depth
    if node.is_leaf():
        print(f"{indent}Leaf -> class={node.value}")
    else:
        print(f"{indent}Node: X[{node.feature}] <= {node.threshold}")
        show_tree(node.left, depth+1)
        print(f"{indent}Node: X[{node.feature}]  > {node.threshold}")
        show_tree(node.right, depth+1)

show_tree(tree.root)
