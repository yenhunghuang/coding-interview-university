"""
Binary Search Tree (BST) - 二元搜尋樹
實作完整的二元搜尋樹資料結構
"""

from tree_node import TreeNode
from collections import deque


class BinarySearchTree:
    """
    二元搜尋樹類別

    BST 性質:
    - 左子樹的所有節點值 < 根節點值
    - 右子樹的所有節點值 > 根節點值
    - 左右子樹也都是二元搜尋樹

    時間複雜度 (平均/最佳):
    - 搜尋: O(log n)
    - 插入: O(log n)
    - 刪除: O(log n)

    時間複雜度 (最壞 - 不平衡樹):
    - 搜尋: O(n)
    - 插入: O(n)
    - 刪除: O(n)
    """

    def __init__(self):
        """
        初始化空的二元搜尋樹
        """
        # TODO: 初始化根節點為 None
        self.root = None
        # TODO: 初始化節點計數為 0
        self._size = 0

    def insert(self, value):
        """
        插入新值到 BST

        參數:
            value: 要插入的值

        時間複雜度: O(log n) 平均, O(n) 最壞
        空間複雜度: O(log n) 因為遞迴呼叫堆疊
        """
        # TODO: 如果樹是空的，創建根節點
        if self.root is None:
            self.root = TreeNode(value)
            self._size += 1
            return

        # TODO: 否則使用輔助函數插入
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        遞迴輔助函數：插入值到以 node 為根的子樹

        參數:
            node: 當前節點
            value: 要插入的值

        返回:
            TreeNode: 更新後的節點
        """
        # TODO: 如果值小於當前節點，往左子樹插入
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
                self._size += 1
            else:
                self._insert_recursive(node.left, value)

        # TODO: 如果值大於當前節點，往右子樹插入
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
                self._size += 1
            else:
                self._insert_recursive(node.right, value)

        # TODO: 如果值等於當前節點，不做任何事（避免重複）
        # 如果允許重複值，可以選擇往左或往右插入

        return node

    def search(self, value):
        """
        在 BST 中搜尋值

        參數:
            value: 要搜尋的值

        返回:
            TreeNode: 找到的節點，如果不存在則返回 None

        時間複雜度: O(log n) 平均, O(n) 最壞
        空間複雜度: O(log n) 因為遞迴呼叫堆疊
        """
        # TODO: 使用輔助函數從根節點開始搜尋
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        遞迴輔助函數：在以 node 為根的子樹中搜尋值

        參數:
            node: 當前節點
            value: 要搜尋的值

        返回:
            TreeNode: 找到的節點或 None
        """
        # TODO: 基本情況：節點為空或找到值
        if node is None or node.value == value:
            return node

        # TODO: 如果值小於當前節點，往左子樹搜尋
        if value < node.value:
            return self._search_recursive(node.left, value)

        # TODO: 如果值大於當前節點，往右子樹搜尋
        return self._search_recursive(node.right, value)

    def contains(self, value):
        """
        檢查 BST 是否包含某值

        參數:
            value: 要檢查的值

        返回:
            bool: 如果存在返回 True，否則返回 False

        時間複雜度: O(log n) 平均, O(n) 最壞
        """
        # TODO: 使用 search 方法，如果找到節點則返回 True
        return self.search(value) is not None

    def delete(self, value):
        """
        從 BST 中刪除值

        參數:
            value: 要刪除的值

        時間複雜度: O(log n) 平均, O(n) 最壞
        空間複雜度: O(log n) 因為遞迴呼叫堆疊

        刪除情況:
        1. 葉節點（無子節點）：直接刪除
        2. 只有一個子節點：用子節點替換
        3. 有兩個子節點：用右子樹的最小值（或左子樹的最大值）替換
        """
        # TODO: 使用輔助函數刪除節點
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """
        遞迴輔助函數：刪除以 node 為根的子樹中的值

        參數:
            node: 當前節點
            value: 要刪除的值

        返回:
            TreeNode: 更新後的節點
        """
        # TODO: 基本情況：節點為空
        if node is None:
            return None

        # TODO: 遞迴尋找要刪除的節點
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # 找到要刪除的節點
            self._size -= 1

            # TODO: 情況 1: 葉節點或只有一個子節點
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # TODO: 情況 2: 有兩個子節點
            # 找到右子樹的最小值（後繼節點）
            min_node = self._find_min_node(node.right)
            # 用後繼節點的值替換當前節點的值
            node.value = min_node.value
            # 刪除後繼節點
            self._size += 1  # 因為下面會再減一次
            node.right = self._delete_recursive(node.right, min_node.value)

        return node

    def get_min(self):
        """
        找到 BST 中的最小值

        返回:
            最小值，如果樹為空則返回 None

        時間複雜度: O(log n) 平均, O(n) 最壞
        """
        # TODO: 檢查樹是否為空
        if self.root is None:
            return None

        # TODO: 最小值在最左邊的節點
        node = self._find_min_node(self.root)
        return node.value if node else None

    def _find_min_node(self, node):
        """
        輔助函數：找到以 node 為根的子樹中的最小節點

        參數:
            node: 起始節點

        返回:
            TreeNode: 最小值節點
        """
        # TODO: 一直往左走到底
        current = node
        while current.left is not None:
            current = current.left
        return current

    def get_max(self):
        """
        找到 BST 中的最大值

        返回:
            最大值，如果樹為空則返回 None

        時間複雜度: O(log n) 平均, O(n) 最壞
        """
        # TODO: 檢查樹是否為空
        if self.root is None:
            return None

        # TODO: 最大值在最右邊的節點
        node = self._find_max_node(self.root)
        return node.value if node else None

    def _find_max_node(self, node):
        """
        輔助函數：找到以 node 為根的子樹中的最大節點

        參數:
            node: 起始節點

        返回:
            TreeNode: 最大值節點
        """
        # TODO: 一直往右走到底
        current = node
        while current.right is not None:
            current = current.right
        return current

    def get_height(self):
        """
        計算 BST 的高度

        返回:
            int: 樹的高度（空樹高度為 -1，單節點高度為 0）

        時間複雜度: O(n) - 需要遍歷所有節點
        """
        # TODO: 使用輔助函數計算高度
        return self._calculate_height(self.root)

    def _calculate_height(self, node):
        """
        遞迴輔助函數：計算以 node 為根的子樹高度

        參數:
            node: 當前節點

        返回:
            int: 子樹高度
        """
        # TODO: 基本情況：空節點高度為 -1
        if node is None:
            return -1

        # TODO: 遞迴計算左右子樹高度，取最大值加 1
        left_height = self._calculate_height(node.left)
        right_height = self._calculate_height(node.right)
        return max(left_height, right_height) + 1

    def size(self):
        """
        返回 BST 中的節點數量

        返回:
            int: 節點數量

        時間複雜度: O(1)
        """
        # TODO: 返回節點計數
        return self._size

    def is_empty(self):
        """
        檢查 BST 是否為空

        返回:
            bool: 如果為空返回 True，否則返回 False

        時間複雜度: O(1)
        """
        # TODO: 檢查根節點是否為 None
        return self.root is None

    def inorder_traversal(self):
        """
        中序遍歷 (Inorder Traversal): 左 -> 根 -> 右

        對於 BST，中序遍歷會得到排序後的序列

        返回:
            list: 按中序排列的節點值列表

        時間複雜度: O(n)
        空間複雜度: O(n)
        """
        # TODO: 使用輔助函數進行中序遍歷
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """
        遞迴輔助函數：中序遍歷

        參數:
            node: 當前節點
            result: 儲存結果的列表
        """
        # TODO: 基本情況：節點為空
        if node is None:
            return

        # TODO: 遞迴順序：左 -> 根 -> 右
        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        """
        前序遍歷 (Preorder Traversal): 根 -> 左 -> 右

        用途：複製樹、序列化樹

        返回:
            list: 按前序排列的節點值列表

        時間複雜度: O(n)
        空間複雜度: O(n)
        """
        # TODO: 使用輔助函數進行前序遍歷
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        """
        遞迴輔助函數：前序遍歷

        參數:
            node: 當前節點
            result: 儲存結果的列表
        """
        # TODO: 基本情況：節點為空
        if node is None:
            return

        # TODO: 遞迴順序：根 -> 左 -> 右
        result.append(node.value)
        self._preorder_recursive(node.left, result)
        self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        """
        後序遍歷 (Postorder Traversal): 左 -> 右 -> 根

        用途：刪除樹、計算目錄大小

        返回:
            list: 按後序排列的節點值列表

        時間複雜度: O(n)
        空間複雜度: O(n)
        """
        # TODO: 使用輔助函數進行後序遍歷
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        """
        遞迴輔助函數：後序遍歷

        參數:
            node: 當前節點
            result: 儲存結果的列表
        """
        # TODO: 基本情況：節點為空
        if node is None:
            return

        # TODO: 遞迴順序：左 -> 右 -> 根
        self._postorder_recursive(node.left, result)
        self._postorder_recursive(node.right, result)
        result.append(node.value)

    def level_order_traversal(self):
        """
        層序遍歷 (Level Order Traversal): 逐層從左到右
        也稱為廣度優先搜尋 (BFS)

        用途：找到最短路徑、層級相關的問題

        返回:
            list: 按層序排列的節點值列表

        時間複雜度: O(n)
        空間複雜度: O(n) - 最壞情況下佇列會存儲一整層的節點
        """
        # TODO: 如果樹為空，返回空列表
        if self.root is None:
            return []

        result = []
        # TODO: 使用佇列（queue）進行 BFS
        queue = deque([self.root])

        while queue:
            # TODO: 從佇列前端取出節點
            node = queue.popleft()
            result.append(node.value)

            # TODO: 將左右子節點加入佇列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def __str__(self):
        """
        返回樹的字串表示（中序遍歷）
        """
        if self.is_empty():
            return "Empty BST"
        return f"BST: {self.inorder_traversal()}"

    def __repr__(self):
        """
        返回樹的詳細表示
        """
        return f"BinarySearchTree(size={self.size()}, height={self.get_height()})"
