"""
測試階段 7: 層序遍歷（廣度優先搜尋）
Testing Stage 7: Level Order Traversal (BFS)

學習目標：
- 理解廣度優先搜尋（BFS）
- 學習使用佇列（Queue）進行層序遍歷
- 理解 BFS 和 DFS 的差異
"""

import unittest
from binary_search_tree import BinarySearchTree


class TestStage7(unittest.TestCase):
    """階段 7: 測試層序遍歷"""

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

    def test_level_order_traversal(self):
        """
        測試層序遍歷
        應該逐層從左到右訪問節點
        """
        result = self.bst.level_order_traversal()
        expected = [10, 5, 15, 3, 7, 12, 17]
        self.assertEqual(result, expected)

    def test_level_order_on_empty_tree(self):
        """測試空樹的層序遍歷"""
        empty_bst = BinarySearchTree()
        self.assertEqual(empty_bst.level_order_traversal(), [])

    def test_level_order_on_single_node(self):
        """測試單節點樹的層序遍歷"""
        single_bst = BinarySearchTree()
        single_bst.insert(10)
        self.assertEqual(single_bst.level_order_traversal(), [10])

    def test_level_order_vs_inorder(self):
        """測試層序遍歷與中序遍歷的差異"""
        level_order = self.bst.level_order_traversal()
        inorder = self.bst.inorder_traversal()
        # 對於這個樹，結果應該不同
        self.assertNotEqual(level_order, inorder)

    def test_level_order_right_skewed_tree(self):
        """測試右傾斜樹的層序遍歷"""
        #   1
        #    \
        #     2
        #      \
        #       3
        #        \
        #         4
        right_skewed = BinarySearchTree()
        for i in range(1, 5):
            right_skewed.insert(i)

        result = right_skewed.level_order_traversal()
        expected = [1, 2, 3, 4]
        self.assertEqual(result, expected)

    def test_level_order_left_skewed_tree(self):
        """測試左傾斜樹的層序遍歷"""
        #       4
        #      /
        #     3
        #    /
        #   2
        #  /
        # 1
        left_skewed = BinarySearchTree()
        for i in range(4, 0, -1):
            left_skewed.insert(i)

        result = left_skewed.level_order_traversal()
        expected = [4, 3, 2, 1]
        self.assertEqual(result, expected)

    def test_level_order_complete_tree(self):
        """測試完全二元樹的層序遍歷"""
        #       10
        #      /  \
        #     5    15
        #    / \   /
        #   3   7 12
        complete_bst = BinarySearchTree()
        values = [10, 5, 15, 3, 7, 12]
        for value in values:
            complete_bst.insert(value)

        result = complete_bst.level_order_traversal()
        expected = [10, 5, 15, 3, 7, 12]
        self.assertEqual(result, expected)

    def test_level_order_root_first(self):
        """測試層序遍歷的第一個元素是根節點"""
        result = self.bst.level_order_traversal()
        self.assertEqual(result[0], self.bst.root.value)

    def test_level_order_same_length_as_other_traversals(self):
        """測試層序遍歷的長度與其他遍歷方式相同"""
        level_order = self.bst.level_order_traversal()
        inorder = self.bst.inorder_traversal()
        preorder = self.bst.preorder_traversal()
        postorder = self.bst.postorder_traversal()

        self.assertEqual(len(level_order), len(inorder))
        self.assertEqual(len(level_order), len(preorder))
        self.assertEqual(len(level_order), len(postorder))

    def test_level_order_contains_all_values(self):
        """測試層序遍歷包含所有值"""
        values = [10, 5, 15, 3, 7, 12, 17]
        result = self.bst.level_order_traversal()
        self.assertEqual(set(result), set(values))

    def test_level_order_after_delete(self):
        """測試刪除節點後的層序遍歷"""
        self.bst.delete(3)
        result = self.bst.level_order_traversal()
        self.assertNotIn(3, result)
        # 確保其他節點仍在
        remaining = [10, 5, 15, 7, 12, 17]
        for value in remaining:
            self.assertIn(value, result)

    def test_level_order_large_tree(self):
        """測試較大樹的層序遍歷"""
        large_bst = BinarySearchTree()
        values = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43]
        for value in values:
            large_bst.insert(value)

        result = large_bst.level_order_traversal()
        # 第一個應該是根
        self.assertEqual(result[0], 50)
        # 第二層應該是 25 和 75
        self.assertEqual(result[1:3], [25, 75])
        # 所有值都應該存在
        self.assertEqual(set(result), set(values))


def run_tests():
    """執行測試並顯示結果"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage7)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == '__main__':
    print("=" * 70)
    print("測試階段 7: 層序遍歷（廣度優先搜尋）")
    print("Testing Stage 7: Level Order Traversal (BFS)")
    print("=" * 70)
    print()

    success = run_tests()

    print()
    if success:
        print("✓ 恭喜！所有測試通過！")
        print("✓ Congratulations! All tests passed!")
        print()
        print("下一步：執行 test_stage8.py 測試複雜操作")
        print("Next: Run test_stage8.py to test complex operations")
    else:
        print("✗ 有些測試失敗了，請檢查你的實作")
        print("✗ Some tests failed. Please check your implementation.")
