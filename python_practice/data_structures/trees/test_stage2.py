"""
測試階段 2: 插入操作
Testing Stage 2: Insert Operations

學習目標：
- 理解 BST 的插入邏輯
- 理解 BST 的性質（左小右大）
- 學習如何維護 BST 的結構
"""

import unittest
from binary_search_tree import BinarySearchTree


class TestStage2(unittest.TestCase):
    """階段 2: 測試插入操作"""

    def setUp(self):
        """每個測試前創建新的 BST"""
        self.bst = BinarySearchTree()

    def test_insert_into_empty_tree(self):
        """測試向空樹插入第一個節點"""
        self.bst.insert(10)
        self.assertIsNotNone(self.bst.root)
        self.assertEqual(self.bst.root.value, 10)
        self.assertEqual(self.bst.size(), 1)

    def test_insert_smaller_value(self):
        """測試插入較小的值（應該在左邊）"""
        self.bst.insert(10)
        self.bst.insert(5)
        self.assertEqual(self.bst.root.left.value, 5)
        self.assertEqual(self.bst.size(), 2)

    def test_insert_larger_value(self):
        """測試插入較大的值（應該在右邊）"""
        self.bst.insert(10)
        self.bst.insert(15)
        self.assertEqual(self.bst.root.right.value, 15)
        self.assertEqual(self.bst.size(), 2)

    def test_insert_multiple_values(self):
        """測試插入多個值"""
        values = [10, 5, 15, 3, 7, 12, 17]
        for value in values:
            self.bst.insert(value)

        self.assertEqual(self.bst.size(), 7)
        self.assertEqual(self.bst.root.value, 10)
        self.assertEqual(self.bst.root.left.value, 5)
        self.assertEqual(self.bst.root.right.value, 15)

    def test_insert_maintains_bst_property(self):
        """測試插入後仍然維持 BST 性質"""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(12)
        self.bst.insert(17)

        # 檢查左子樹
        self.assertLess(self.bst.root.left.value, self.bst.root.value)
        self.assertLess(self.bst.root.left.left.value, self.bst.root.left.value)
        self.assertGreater(self.bst.root.left.right.value, self.bst.root.left.value)

        # 檢查右子樹
        self.assertGreater(self.bst.root.right.value, self.bst.root.value)
        self.assertLess(self.bst.root.right.left.value, self.bst.root.right.value)
        self.assertGreater(self.bst.root.right.right.value, self.bst.root.right.value)

    def test_insert_duplicate_value(self):
        """測試插入重複值（不應增加大小）"""
        self.bst.insert(10)
        self.bst.insert(10)
        self.assertEqual(self.bst.size(), 1)

    def test_tree_not_empty_after_insert(self):
        """測試插入後樹不為空"""
        self.bst.insert(10)
        self.assertFalse(self.bst.is_empty())

    def test_insert_ascending_order(self):
        """測試按升序插入（會形成不平衡的樹）"""
        for i in range(1, 6):
            self.bst.insert(i)

        self.assertEqual(self.bst.size(), 5)
        # 樹會向右傾斜
        self.assertIsNone(self.bst.root.left)
        self.assertIsNotNone(self.bst.root.right)

    def test_insert_descending_order(self):
        """測試按降序插入（會形成不平衡的樹）"""
        for i in range(5, 0, -1):
            self.bst.insert(i)

        self.assertEqual(self.bst.size(), 5)
        # 樹會向左傾斜
        self.assertIsNotNone(self.bst.root.left)
        self.assertIsNone(self.bst.root.right)


def run_tests():
    """執行測試並顯示結果"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage2)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == '__main__':
    print("=" * 70)
    print("測試階段 2: 插入操作")
    print("Testing Stage 2: Insert Operations")
    print("=" * 70)
    print()

    success = run_tests()

    print()
    if success:
        print("✓ 恭喜！所有測試通過！")
        print("✓ Congratulations! All tests passed!")
        print()
        print("下一步：執行 test_stage3.py 測試搜尋操作")
        print("Next: Run test_stage3.py to test search operations")
    else:
        print("✗ 有些測試失敗了，請檢查你的實作")
        print("✗ Some tests failed. Please check your implementation.")
