"""
測試階段 8: 複雜操作和邊界情況
Testing Stage 8: Complex Operations and Edge Cases

學習目標：
- 測試多種操作的組合
- 處理邊界情況和特殊情況
- 驗證 BST 在各種情況下的正確性
"""

import unittest
from binary_search_tree import BinarySearchTree


class TestStage8(unittest.TestCase):
    """階段 8: 測試複雜操作和邊界情況"""

    def test_insert_search_delete_cycle(self):
        """測試插入、搜尋、刪除的循環"""
        bst = BinarySearchTree()

        # 插入
        bst.insert(10)
        self.assertTrue(bst.contains(10))

        # 刪除
        bst.delete(10)
        self.assertFalse(bst.contains(10))

        # 再次插入
        bst.insert(10)
        self.assertTrue(bst.contains(10))

    def test_large_number_of_insertions(self):
        """測試大量插入操作"""
        bst = BinarySearchTree()
        values = list(range(1, 101))

        for value in values:
            bst.insert(value)

        self.assertEqual(bst.size(), 100)
        # 中序遍歷應該是排序的
        result = bst.inorder_traversal()
        self.assertEqual(result, sorted(values))

    def test_duplicate_insertions(self):
        """測試重複插入"""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(10)
        bst.insert(10)

        # 大小應該只有 1
        self.assertEqual(bst.size(), 1)

    def test_negative_numbers(self):
        """測試負數"""
        bst = BinarySearchTree()
        values = [-10, -5, 0, 5, 10]

        for value in values:
            bst.insert(value)

        self.assertEqual(bst.size(), 5)
        self.assertEqual(bst.get_min(), -10)
        self.assertEqual(bst.get_max(), 10)
        self.assertEqual(bst.inorder_traversal(), values)

    def test_mixed_operations(self):
        """測試混合操作"""
        bst = BinarySearchTree()

        # 插入一些值
        bst.insert(50)
        bst.insert(30)
        bst.insert(70)
        self.assertEqual(bst.size(), 3)

        # 刪除一個值
        bst.delete(30)
        self.assertEqual(bst.size(), 2)

        # 插入更多值
        bst.insert(40)
        bst.insert(60)
        bst.insert(80)
        self.assertEqual(bst.size(), 5)

        # 檢查搜尋
        self.assertTrue(bst.contains(50))
        self.assertFalse(bst.contains(30))
        self.assertTrue(bst.contains(40))

    def test_delete_and_verify_structure(self):
        """測試刪除後驗證結構"""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            bst.insert(value)

        # 刪除有兩個子節點的節點
        bst.delete(30)

        # 驗證剩餘節點
        remaining = [50, 70, 20, 40, 60, 80]
        result = bst.inorder_traversal()
        self.assertEqual(result, sorted(remaining))

    def test_height_after_operations(self):
        """測試各種操作後的高度變化"""
        bst = BinarySearchTree()

        # 空樹高度為 -1
        self.assertEqual(bst.get_height(), -1)

        # 插入根節點
        bst.insert(10)
        self.assertEqual(bst.get_height(), 0)

        # 插入子節點
        bst.insert(5)
        bst.insert(15)
        self.assertEqual(bst.get_height(), 1)

        # 插入更多節點
        bst.insert(3)
        self.assertEqual(bst.get_height(), 2)

    def test_all_traversal_methods_consistency(self):
        """測試所有遍歷方法的一致性"""
        bst = BinarySearchTree()
        values = [10, 5, 15, 3, 7, 12, 17]
        for value in values:
            bst.insert(value)

        inorder = bst.inorder_traversal()
        preorder = bst.preorder_traversal()
        postorder = bst.postorder_traversal()
        level_order = bst.level_order_traversal()

        # 所有遍歷應該包含相同的元素
        self.assertEqual(set(inorder), set(preorder))
        self.assertEqual(set(inorder), set(postorder))
        self.assertEqual(set(inorder), set(level_order))
        self.assertEqual(set(inorder), set(values))

    def test_min_max_after_delete_operations(self):
        """測試刪除操作後的最小值和最大值"""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            bst.insert(value)

        # 刪除最小值
        bst.delete(20)
        self.assertEqual(bst.get_min(), 30)

        # 刪除最大值
        bst.delete(80)
        self.assertEqual(bst.get_max(), 70)

    def test_empty_after_deleting_all(self):
        """測試刪除所有節點後樹為空"""
        bst = BinarySearchTree()
        values = [10, 5, 15]
        for value in values:
            bst.insert(value)

        for value in values:
            bst.delete(value)

        self.assertTrue(bst.is_empty())
        self.assertEqual(bst.size(), 0)
        self.assertIsNone(bst.get_min())
        self.assertIsNone(bst.get_max())
        self.assertEqual(bst.get_height(), -1)

    def test_search_performance_balanced_vs_unbalanced(self):
        """測試平衡樹和不平衡樹的搜尋（概念驗證）"""
        # 平衡樹
        balanced = BinarySearchTree()
        balanced_values = [50, 25, 75, 12, 37, 62, 87]
        for value in balanced_values:
            balanced.insert(value)

        # 不平衡樹（右傾斜）
        unbalanced = BinarySearchTree()
        for i in range(1, 8):
            unbalanced.insert(i)

        # 兩者都應該能找到值
        self.assertTrue(balanced.contains(87))
        self.assertTrue(unbalanced.contains(7))

        # 但高度不同
        self.assertLess(balanced.get_height(), unbalanced.get_height())

    def test_str_and_repr_methods(self):
        """測試字串表示方法"""
        bst = BinarySearchTree()

        # 空樹
        self.assertEqual(str(bst), "Empty BST")

        # 插入值後
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)

        str_result = str(bst)
        self.assertIn("BST", str_result)

        repr_result = repr(bst)
        self.assertIn("BinarySearchTree", repr_result)
        self.assertIn("size=3", repr_result)

    def test_identical_values_different_insertion_orders(self):
        """測試相同的值但不同的插入順序"""
        bst1 = BinarySearchTree()
        bst2 = BinarySearchTree()

        values1 = [10, 5, 15, 3, 7, 12, 17]
        values2 = [3, 5, 7, 10, 12, 15, 17]

        for value in values1:
            bst1.insert(value)

        for value in values2:
            bst2.insert(value)

        # 中序遍歷應該相同
        self.assertEqual(bst1.inorder_traversal(), bst2.inorder_traversal())

        # 但樹的結構可能不同
        self.assertNotEqual(bst1.get_height(), bst2.get_height())

    def test_floating_point_values(self):
        """測試浮點數值"""
        bst = BinarySearchTree()
        values = [10.5, 5.2, 15.8, 3.1, 7.9]

        for value in values:
            bst.insert(value)

        self.assertEqual(bst.size(), 5)
        self.assertEqual(bst.get_min(), 3.1)
        self.assertEqual(bst.get_max(), 15.8)


def run_tests():
    """執行測試並顯示結果"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage8)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == '__main__':
    print("=" * 70)
    print("測試階段 8: 複雜操作和邊界情況")
    print("Testing Stage 8: Complex Operations and Edge Cases")
    print("=" * 70)
    print()

    success = run_tests()

    print()
    if success:
        print("✓ 恭喜！所有測試通過！")
        print("✓ Congratulations! All tests passed!")
        print()
        print("下一步：執行 test_stage_final.py 進行最終整合測試")
        print("Next: Run test_stage_final.py for final integration tests")
    else:
        print("✗ 有些測試失敗了，請檢查你的實作")
        print("✗ Some tests failed. Please check your implementation.")
