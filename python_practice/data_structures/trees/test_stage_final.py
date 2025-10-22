"""
最終測試階段: 整合測試和實際應用
Final Testing Stage: Integration Tests and Practical Applications

學習目標：
- 驗證 BST 的整體功能
- 測試實際應用場景
- 確保所有功能正確協同工作
"""

import unittest
from binary_search_tree import BinarySearchTree
import random


class TestFinalStage(unittest.TestCase):
    """最終階段: 整合測試"""

    def test_complete_bst_workflow(self):
        """測試完整的 BST 工作流程"""
        bst = BinarySearchTree()

        # 1. 創建空樹
        self.assertTrue(bst.is_empty())

        # 2. 插入元素
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
        for value in values:
            bst.insert(value)

        # 3. 驗證大小
        self.assertEqual(bst.size(), len(values))

        # 4. 搜尋所有元素
        for value in values:
            self.assertTrue(bst.contains(value))

        # 5. 驗證最小值和最大值
        self.assertEqual(bst.get_min(), min(values))
        self.assertEqual(bst.get_max(), max(values))

        # 6. 驗證遍歷
        self.assertEqual(bst.inorder_traversal(), sorted(values))

        # 7. 刪除一些元素
        bst.delete(20)
        bst.delete(60)
        self.assertEqual(bst.size(), len(values) - 2)

        # 8. 驗證刪除後的正確性
        self.assertFalse(bst.contains(20))
        self.assertFalse(bst.contains(60))

    def test_dictionary_implementation(self):
        """測試 BST 作為字典實現（單詞排序）"""
        bst = BinarySearchTree()

        # 使用 ASCII 值作為數字（簡化版本）
        words = ["dog", "cat", "bird", "elephant", "ant"]
        # 插入單詞長度
        word_lengths = [len(word) for word in words]

        for length in word_lengths:
            bst.insert(length)

        # 驗證按長度排序
        result = bst.inorder_traversal()
        self.assertEqual(result, sorted(word_lengths))

    def test_range_query_simulation(self):
        """測試範圍查詢模擬（找出在某個範圍內的值）"""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]

        for value in values:
            bst.insert(value)

        # 獲取所有值並找出在 30-60 範圍內的
        all_values = bst.inorder_traversal()
        range_values = [v for v in all_values if 30 <= v <= 60]

        expected = [30, 35, 40, 45, 50, 55, 60]
        self.assertEqual(range_values, expected)

    def test_finding_kth_smallest(self):
        """測試找第 k 小的元素"""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]

        for value in values:
            bst.insert(value)

        # 中序遍歷給出排序序列
        sorted_values = bst.inorder_traversal()

        # 找第 3 小的元素（索引 2）
        k = 3
        kth_smallest = sorted_values[k - 1]
        self.assertEqual(kth_smallest, 30)

    def test_verify_bst_property_at_all_times(self):
        """測試在所有操作中始終保持 BST 性質"""
        bst = BinarySearchTree()
        random.seed(42)
        values = random.sample(range(1, 100), 20)

        # 插入隨機值
        for value in values:
            bst.insert(value)
            # 每次插入後驗證 BST 性質
            inorder = bst.inorder_traversal()
            self.assertEqual(inorder, sorted(inorder))

        # 隨機刪除一半的值
        to_delete = random.sample(values, 10)
        for value in to_delete:
            bst.delete(value)
            # 每次刪除後驗證 BST 性質
            inorder = bst.inorder_traversal()
            self.assertEqual(inorder, sorted(inorder))

    def test_duplicate_handling_consistency(self):
        """測試重複值處理的一致性"""
        bst = BinarySearchTree()

        # 插入相同的值多次
        for _ in range(5):
            bst.insert(10)

        # 大小應該只增加一次
        self.assertEqual(bst.size(), 1)

        # 刪除一次應該完全移除
        bst.delete(10)
        self.assertEqual(bst.size(), 0)
        self.assertFalse(bst.contains(10))

    def test_stress_test_many_operations(self):
        """壓力測試：大量操作"""
        bst = BinarySearchTree()
        random.seed(123)

        # 插入 100 個隨機值
        insert_values = random.sample(range(1, 201), 100)
        for value in insert_values:
            bst.insert(value)

        self.assertEqual(bst.size(), 100)

        # 搜尋所有插入的值
        for value in insert_values:
            self.assertTrue(bst.contains(value))

        # 驗證中序遍歷是排序的
        inorder = bst.inorder_traversal()
        self.assertEqual(inorder, sorted(inorder))

        # 刪除 50 個值
        delete_values = random.sample(insert_values, 50)
        for value in delete_values:
            bst.delete(value)

        self.assertEqual(bst.size(), 50)

        # 驗證刪除的值不存在
        for value in delete_values:
            self.assertFalse(bst.contains(value))

        # 驗證剩餘的值存在
        remaining = [v for v in insert_values if v not in delete_values]
        for value in remaining:
            self.assertTrue(bst.contains(value))

    def test_tree_balance_comparison(self):
        """測試平衡樹和不平衡樹的比較"""
        # 相對平衡的樹
        balanced = BinarySearchTree()
        balanced_values = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 93, 81]
        for value in balanced_values:
            balanced.insert(value)

        # 完全不平衡的樹（升序插入）
        unbalanced = BinarySearchTree()
        for i in range(1, 16):
            unbalanced.insert(i)

        # 驗證大小相同
        self.assertEqual(balanced.size(), unbalanced.size())

        # 但高度不同
        self.assertLess(balanced.get_height(), unbalanced.get_height())

        # 平衡樹的高度應該接近 log2(n)
        import math
        optimal_height = math.floor(math.log2(balanced.size()))
        self.assertLessEqual(balanced.get_height(), optimal_height + 2)

    def test_all_elements_reachable(self):
        """測試所有元素都可達"""
        bst = BinarySearchTree()
        values = list(range(1, 51))
        random.shuffle(values)

        for value in values:
            bst.insert(value)

        # 通過四種遍歷方式驗證所有元素
        inorder = set(bst.inorder_traversal())
        preorder = set(bst.preorder_traversal())
        postorder = set(bst.postorder_traversal())
        level_order = set(bst.level_order_traversal())

        expected = set(values)

        self.assertEqual(inorder, expected)
        self.assertEqual(preorder, expected)
        self.assertEqual(postorder, expected)
        self.assertEqual(level_order, expected)

    def test_practical_scenario_sorting(self):
        """測試實際場景：使用 BST 排序"""
        unsorted = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 72]

        # 使用 BST 排序
        bst = BinarySearchTree()
        for value in unsorted:
            bst.insert(value)

        sorted_result = bst.inorder_traversal()
        expected_sorted = sorted(unsorted)

        self.assertEqual(sorted_result, expected_sorted)

    def test_practical_scenario_deduplication(self):
        """測試實際場景：使用 BST 去重"""
        values_with_duplicates = [5, 3, 7, 3, 9, 5, 1, 7, 8, 1]

        # 使用 BST 去重
        bst = BinarySearchTree()
        for value in values_with_duplicates:
            bst.insert(value)

        unique_sorted = bst.inorder_traversal()
        expected = sorted(set(values_with_duplicates))

        self.assertEqual(unique_sorted, expected)

    def test_rebuild_tree_from_traversal(self):
        """測試從遍歷結果重建樹"""
        original_bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]

        for value in values:
            original_bst.insert(value)

        # 獲取前序遍歷
        preorder = original_bst.preorder_traversal()

        # 使用前序遍歷重建樹
        rebuilt_bst = BinarySearchTree()
        for value in preorder:
            rebuilt_bst.insert(value)

        # 驗證中序遍歷相同（因為插入順序相同）
        self.assertEqual(
            original_bst.inorder_traversal(),
            rebuilt_bst.inorder_traversal()
        )


def run_tests():
    """執行測試並顯示結果"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFinalStage)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == '__main__':
    print("=" * 70)
    print("最終測試階段: 整合測試和實際應用")
    print("Final Testing Stage: Integration Tests and Practical Applications")
    print("=" * 70)
    print()

    success = run_tests()

    print()
    print("=" * 70)
    if success:
        print("✓✓✓ 恭喜！所有測試通過！✓✓✓")
        print("✓✓✓ Congratulations! All tests passed! ✓✓✓")
        print()
        print("你已經完成了二元搜尋樹的學習！")
        print("You have completed learning Binary Search Trees!")
        print()
        print("下一步建議：")
        print("Next steps:")
        print("1. 閱讀 TREE_LEARNING_GUIDE.md 深入理解 BST")
        print("   Read TREE_LEARNING_GUIDE.md for deeper understanding")
        print("2. 嘗試實作自平衡樹（AVL Tree 或 Red-Black Tree）")
        print("   Try implementing self-balancing trees (AVL or Red-Black)")
        print("3. 解決 LeetCode 上的樹相關問題")
        print("   Solve tree-related problems on LeetCode")
    else:
        print("✗ 有些測試失敗了，請檢查你的實作")
        print("✗ Some tests failed. Please check your implementation.")
    print("=" * 70)
