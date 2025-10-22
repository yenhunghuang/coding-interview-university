"""
測試階段 1: 節點創建和基本結構
Testing Stage 1: Node Creation and Basic Structure

學習目標：
- 理解 TreeNode 類別的基本結構
- 理解 BinarySearchTree 類別的初始化
- 學習如何創建節點和空樹
"""

import unittest
from tree_node import TreeNode
from binary_search_tree import BinarySearchTree


class TestStage1(unittest.TestCase):
    """階段 1: 測試節點創建和基本結構"""

    def test_create_tree_node(self):
        """測試創建樹節點"""
        node = TreeNode(10)
        self.assertEqual(node.value, 10)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_tree_node_with_children(self):
        """測試創建有子節點的樹節點"""
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)

        self.assertEqual(root.value, 10)
        self.assertEqual(root.left.value, 5)
        self.assertEqual(root.right.value, 15)

    def test_create_empty_bst(self):
        """測試創建空的 BST"""
        bst = BinarySearchTree()
        self.assertIsNone(bst.root)
        self.assertEqual(bst.size(), 0)

    def test_empty_tree_is_empty(self):
        """測試空樹的 is_empty 方法"""
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())

    def test_tree_node_str_representation(self):
        """測試節點的字串表示"""
        node = TreeNode(42)
        self.assertEqual(str(node), "42")

    def test_empty_tree_str_representation(self):
        """測試空樹的字串表示"""
        bst = BinarySearchTree()
        self.assertEqual(str(bst), "Empty BST")


def run_tests():
    """執行測試並顯示結果"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage1)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == '__main__':
    print("=" * 70)
    print("測試階段 1: 節點創建和基本結構")
    print("Testing Stage 1: Node Creation and Basic Structure")
    print("=" * 70)
    print()

    success = run_tests()

    print()
    if success:
        print("✓ 恭喜！所有測試通過！")
        print("✓ Congratulations! All tests passed!")
        print()
        print("下一步：執行 test_stage2.py 測試插入操作")
        print("Next: Run test_stage2.py to test insert operations")
    else:
        print("✗ 有些測試失敗了，請檢查你的實作")
        print("✗ Some tests failed. Please check your implementation.")
