"""
測試階段 6: 刪除操作
Testing Stage 6: Delete Operations

學習目標：
- 理解 BST 刪除的三種情況
- 學習如何在刪除後維護 BST 性質
- 理解後繼節點（successor）的概念
"""

import unittest
from binary_search_tree import BinarySearchTree


class TestStage6(unittest.TestCase):
    """階段 6: 測試刪除操作"""

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

    def test_delete_leaf_node(self):
        """測試刪除葉節點（無子節點）"""
        # 刪除葉節點 3
        self.bst.delete(3)
        self.assertEqual(self.bst.size(), 6)
        self.assertFalse(self.bst.contains(3))
        # 確保 BST 性質仍然維持
        self.assertEqual(self.bst.inorder_traversal(), [5, 7, 10, 12, 15, 17])

    def test_delete_node_with_one_child_left(self):
        """測試刪除只有左子節點的節點"""
        # 先建立一個特殊的樹
        new_bst = BinarySearchTree()
        new_bst.insert(10)
        new_bst.insert(5)
        new_bst.insert(3)
        # 刪除只有左子節點的節點 5
        new_bst.delete(5)
        self.assertEqual(new_bst.size(), 2)
        self.assertFalse(new_bst.contains(5))
        self.assertTrue(new_bst.contains(3))

    def test_delete_node_with_one_child_right(self):
        """測試刪除只有右子節點的節點"""
        # 先建立一個特殊的樹
        new_bst = BinarySearchTree()
        new_bst.insert(10)
        new_bst.insert(5)
        new_bst.insert(7)
        # 刪除只有右子節點的節點 5
        new_bst.delete(5)
        self.assertEqual(new_bst.size(), 2)
        self.assertFalse(new_bst.contains(5))
        self.assertTrue(new_bst.contains(7))

    def test_delete_node_with_two_children(self):
        """測試刪除有兩個子節點的節點"""
        # 刪除有兩個子節點的節點 5
        self.bst.delete(5)
        self.assertEqual(self.bst.size(), 6)
        self.assertFalse(self.bst.contains(5))
        # 確保 BST 性質仍然維持
        result = self.bst.inorder_traversal()
        self.assertEqual(result, sorted(result))

    def test_delete_root_node(self):
        """測試刪除根節點"""
        original_size = self.bst.size()
        self.bst.delete(10)
        self.assertEqual(self.bst.size(), original_size - 1)
        self.assertFalse(self.bst.contains(10))
        # 確保 BST 性質仍然維持
        result = self.bst.inorder_traversal()
        self.assertEqual(result, sorted(result))

    def test_delete_non_existing_value(self):
        """測試刪除不存在的值"""
        original_size = self.bst.size()
        self.bst.delete(100)
        # 大小不應改變
        self.assertEqual(self.bst.size(), original_size)

    def test_delete_from_empty_tree(self):
        """測試從空樹中刪除"""
        empty_bst = BinarySearchTree()
        empty_bst.delete(10)
        self.assertEqual(empty_bst.size(), 0)
        self.assertTrue(empty_bst.is_empty())

    def test_delete_all_nodes(self):
        """測試刪除所有節點"""
        values = [10, 5, 15, 3, 7, 12, 17]
        for value in values:
            self.bst.delete(value)

        self.assertEqual(self.bst.size(), 0)
        self.assertTrue(self.bst.is_empty())
        self.assertEqual(self.bst.inorder_traversal(), [])

    def test_delete_and_reinsert(self):
        """測試刪除後重新插入"""
        self.bst.delete(5)
        self.assertFalse(self.bst.contains(5))

        self.bst.insert(5)
        self.assertTrue(self.bst.contains(5))
        self.assertEqual(self.bst.size(), 7)

    def test_delete_maintains_bst_property(self):
        """測試刪除後仍維持 BST 性質"""
        # 刪除多個節點
        self.bst.delete(3)
        self.bst.delete(15)

        # 中序遍歷應該仍然是排序的
        result = self.bst.inorder_traversal()
        self.assertEqual(result, sorted(result))

    def test_delete_min_node(self):
        """測試刪除最小值節點"""
        min_val = self.bst.get_min()
        self.bst.delete(min_val)
        self.assertFalse(self.bst.contains(min_val))
        # 新的最小值應該是 5
        self.assertEqual(self.bst.get_min(), 5)

    def test_delete_max_node(self):
        """測試刪除最大值節點"""
        max_val = self.bst.get_max()
        self.bst.delete(max_val)
        self.assertFalse(self.bst.contains(max_val))
        # 新的最大值應該是 15
        self.assertEqual(self.bst.get_max(), 15)

    def test_delete_multiple_nodes_in_sequence(self):
        """測試連續刪除多個節點"""
        self.bst.delete(3)
        self.assertEqual(self.bst.size(), 6)

        self.bst.delete(7)
        self.assertEqual(self.bst.size(), 5)

        self.bst.delete(5)
        self.assertEqual(self.bst.size(), 4)

        # 確保剩餘節點仍然可以找到
        remaining = [10, 15, 12, 17]
        for value in remaining:
            self.assertTrue(self.bst.contains(value))

    def test_size_decreases_after_delete(self):
        """測試刪除後大小減少"""
        original_size = self.bst.size()
        self.bst.delete(5)
        self.assertEqual(self.bst.size(), original_size - 1)


def run_tests():
    """執行測試並顯示結果"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage6)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == '__main__':
    print("=" * 70)
    print("測試階段 6: 刪除操作")
    print("Testing Stage 6: Delete Operations")
    print("=" * 70)
    print()

    success = run_tests()

    print()
    if success:
        print("✓ 恭喜！所有測試通過！")
        print("✓ Congratulations! All tests passed!")
        print()
        print("下一步：執行 test_stage7.py 測試層序遍歷")
        print("Next: Run test_stage7.py to test level order traversal")
    else:
        print("✗ 有些測試失敗了，請檢查你的實作")
        print("✗ Some tests failed. Please check your implementation.")
