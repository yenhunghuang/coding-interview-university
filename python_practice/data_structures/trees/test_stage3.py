"""
測試階段 3: 搜尋操作
Testing Stage 3: Search Operations

學習目標：
- 理解 BST 的搜尋邏輯
- 學習如何利用 BST 性質進行高效搜尋
- 理解 search 和 contains 方法的差異
"""

import unittest
from binary_search_tree import BinarySearchTree


class TestStage3(unittest.TestCase):
    """階段 3: 測試搜尋操作"""

    def setUp(self):
        """每個測試前創建並初始化 BST"""
        self.bst = BinarySearchTree()
        # 建立一個測試用的 BST
        #       10
        #      /  \
        #     5    15
        #    / \   / \
        #   3   7 12  17
        values = [10, 5, 15, 3, 7, 12, 17]
        for value in values:
            self.bst.insert(value)

    def test_search_existing_value_root(self):
        """測試搜尋存在的值（根節點）"""
        node = self.bst.search(10)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 10)

    def test_search_existing_value_left(self):
        """測試搜尋存在的值（左子樹）"""
        node = self.bst.search(5)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 5)

    def test_search_existing_value_right(self):
        """測試搜尋存在的值（右子樹）"""
        node = self.bst.search(15)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 15)

    def test_search_existing_value_leaf(self):
        """測試搜尋存在的值（葉節點）"""
        node = self.bst.search(3)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 3)

    def test_search_non_existing_value(self):
        """測試搜尋不存在的值"""
        node = self.bst.search(100)
        self.assertIsNone(node)

    def test_search_in_empty_tree(self):
        """測試在空樹中搜尋"""
        empty_bst = BinarySearchTree()
        node = empty_bst.search(10)
        self.assertIsNone(node)

    def test_contains_existing_values(self):
        """測試 contains 方法（存在的值）"""
        self.assertTrue(self.bst.contains(10))
        self.assertTrue(self.bst.contains(5))
        self.assertTrue(self.bst.contains(15))
        self.assertTrue(self.bst.contains(3))
        self.assertTrue(self.bst.contains(7))
        self.assertTrue(self.bst.contains(12))
        self.assertTrue(self.bst.contains(17))

    def test_contains_non_existing_values(self):
        """測試 contains 方法（不存在的值）"""
        self.assertFalse(self.bst.contains(1))
        self.assertFalse(self.bst.contains(4))
        self.assertFalse(self.bst.contains(8))
        self.assertFalse(self.bst.contains(100))

    def test_contains_in_empty_tree(self):
        """測試在空樹中使用 contains"""
        empty_bst = BinarySearchTree()
        self.assertFalse(empty_bst.contains(10))

    def test_search_all_inserted_values(self):
        """測試搜尋所有插入的值"""
        values = [10, 5, 15, 3, 7, 12, 17]
        for value in values:
            node = self.bst.search(value)
            self.assertIsNotNone(node)
            self.assertEqual(node.value, value)

    def test_search_after_multiple_inserts(self):
        """測試在多次插入後搜尋"""
        new_bst = BinarySearchTree()
        values = list(range(1, 11))
        for value in values:
            new_bst.insert(value)

        for value in values:
            self.assertTrue(new_bst.contains(value))


def run_tests():
    """執行測試並顯示結果"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage3)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == '__main__':
    print("=" * 70)
    print("測試階段 3: 搜尋操作")
    print("Testing Stage 3: Search Operations")
    print("=" * 70)
    print()

    success = run_tests()

    print()
    if success:
        print("✓ 恭喜！所有測試通過！")
        print("✓ Congratulations! All tests passed!")
        print()
        print("下一步：執行 test_stage4.py 測試遍歷操作")
        print("Next: Run test_stage4.py to test traversal operations")
    else:
        print("✗ 有些測試失敗了，請檢查你的實作")
        print("✗ Some tests failed. Please check your implementation.")
