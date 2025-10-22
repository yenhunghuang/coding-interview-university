"""
測試階段 5: 最小值、最大值和高度
Testing Stage 5: Min, Max, and Height

學習目標：
- 理解如何在 BST 中找到最小值和最大值
- 理解樹的高度概念
- 學習平衡樹和不平衡樹的差異
"""

import unittest
from binary_search_tree import BinarySearchTree


class TestStage5(unittest.TestCase):
    """階段 5: 測試最小值、最大值和高度"""

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

    def test_get_min(self):
        """測試獲取最小值"""
        self.assertEqual(self.bst.get_min(), 3)

    def test_get_max(self):
        """測試獲取最大值"""
        self.assertEqual(self.bst.get_max(), 17)

    def test_min_on_empty_tree(self):
        """測試空樹的最小值"""
        empty_bst = BinarySearchTree()
        self.assertIsNone(empty_bst.get_min())

    def test_max_on_empty_tree(self):
        """測試空樹的最大值"""
        empty_bst = BinarySearchTree()
        self.assertIsNone(empty_bst.get_max())

    def test_min_max_on_single_node(self):
        """測試單節點樹的最小值和最大值"""
        single_bst = BinarySearchTree()
        single_bst.insert(10)
        self.assertEqual(single_bst.get_min(), 10)
        self.assertEqual(single_bst.get_max(), 10)

    def test_get_height_balanced_tree(self):
        """測試平衡樹的高度"""
        # 樹的高度應該是 2
        # 層級 0: 10
        # 層級 1: 5, 15
        # 層級 2: 3, 7, 12, 17
        self.assertEqual(self.bst.get_height(), 2)

    def test_height_on_empty_tree(self):
        """測試空樹的高度"""
        empty_bst = BinarySearchTree()
        self.assertEqual(empty_bst.get_height(), -1)

    def test_height_on_single_node(self):
        """測試單節點樹的高度"""
        single_bst = BinarySearchTree()
        single_bst.insert(10)
        self.assertEqual(single_bst.get_height(), 0)

    def test_height_unbalanced_tree_right_skewed(self):
        """測試右傾斜不平衡樹的高度"""
        # 插入升序數據會形成右傾斜樹
        #   1
        #    \
        #     2
        #      \
        #       3
        #        \
        #         4
        #          \
        #           5
        right_skewed = BinarySearchTree()
        for i in range(1, 6):
            right_skewed.insert(i)

        # 高度應該是 4（5個節點，高度為 n-1）
        self.assertEqual(right_skewed.get_height(), 4)

    def test_height_unbalanced_tree_left_skewed(self):
        """測試左傾斜不平衡樹的高度"""
        # 插入降序數據會形成左傾斜樹
        #         5
        #        /
        #       4
        #      /
        #     3
        #    /
        #   2
        #  /
        # 1
        left_skewed = BinarySearchTree()
        for i in range(5, 0, -1):
            left_skewed.insert(i)

        # 高度應該是 4
        self.assertEqual(left_skewed.get_height(), 4)

    def test_min_after_multiple_inserts(self):
        """測試多次插入後的最小值"""
        new_bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80, 10]
        for value in values:
            new_bst.insert(value)

        self.assertEqual(new_bst.get_min(), 10)

    def test_max_after_multiple_inserts(self):
        """測試多次插入後的最大值"""
        new_bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80, 90]
        for value in values:
            new_bst.insert(value)

        self.assertEqual(new_bst.get_max(), 90)

    def test_height_increases_with_inserts(self):
        """測試插入新值會增加高度"""
        new_bst = BinarySearchTree()
        self.assertEqual(new_bst.get_height(), -1)

        new_bst.insert(10)
        self.assertEqual(new_bst.get_height(), 0)

        new_bst.insert(5)
        self.assertEqual(new_bst.get_height(), 1)

        new_bst.insert(3)
        self.assertEqual(new_bst.get_height(), 2)

    def test_min_max_relationship(self):
        """測試最小值總是小於或等於最大值"""
        if not self.bst.is_empty():
            min_val = self.bst.get_min()
            max_val = self.bst.get_max()
            self.assertLessEqual(min_val, max_val)


def run_tests():
    """執行測試並顯示結果"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage5)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == '__main__':
    print("=" * 70)
    print("測試階段 5: 最小值、最大值和高度")
    print("Testing Stage 5: Min, Max, and Height")
    print("=" * 70)
    print()

    success = run_tests()

    print()
    if success:
        print("✓ 恭喜！所有測試通過！")
        print("✓ Congratulations! All tests passed!")
        print()
        print("下一步：執行 test_stage6.py 測試刪除操作")
        print("Next: Run test_stage6.py to test delete operations")
    else:
        print("✗ 有些測試失敗了，請檢查你的實作")
        print("✗ Some tests failed. Please check your implementation.")
