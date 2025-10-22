"""
測試階段 4: 遍歷操作（中序、前序、後序）
Testing Stage 4: Traversal Operations (Inorder, Preorder, Postorder)

學習目標：
- 理解三種深度優先搜尋（DFS）遍歷方式
- 理解中序遍歷對 BST 的特殊意義（有序序列）
- 學習不同遍歷方式的應用場景
"""

import unittest
from binary_search_tree import BinarySearchTree


class TestStage4(unittest.TestCase):
    """階段 4: 測試遍歷操作"""

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

    def test_inorder_traversal(self):
        """
        測試中序遍歷（左 -> 根 -> 右）
        對於 BST，中序遍歷會得到排序後的序列
        """
        result = self.bst.inorder_traversal()
        expected = [3, 5, 7, 10, 12, 15, 17]
        self.assertEqual(result, expected)

    def test_inorder_gives_sorted_sequence(self):
        """測試中序遍歷是否給出排序後的序列"""
        result = self.bst.inorder_traversal()
        # 檢查是否已排序
        self.assertEqual(result, sorted(result))

    def test_preorder_traversal(self):
        """
        測試前序遍歷（根 -> 左 -> 右）
        前序遍歷可用於複製樹或序列化
        """
        result = self.bst.preorder_traversal()
        expected = [10, 5, 3, 7, 15, 12, 17]
        self.assertEqual(result, expected)

    def test_postorder_traversal(self):
        """
        測試後序遍歷（左 -> 右 -> 根）
        後序遍歷可用於刪除樹或計算後序表達式
        """
        result = self.bst.postorder_traversal()
        expected = [3, 7, 5, 12, 17, 15, 10]
        self.assertEqual(result, expected)

    def test_traversal_on_empty_tree(self):
        """測試空樹的遍歷"""
        empty_bst = BinarySearchTree()
        self.assertEqual(empty_bst.inorder_traversal(), [])
        self.assertEqual(empty_bst.preorder_traversal(), [])
        self.assertEqual(empty_bst.postorder_traversal(), [])

    def test_traversal_on_single_node(self):
        """測試單節點樹的遍歷"""
        single_bst = BinarySearchTree()
        single_bst.insert(10)

        self.assertEqual(single_bst.inorder_traversal(), [10])
        self.assertEqual(single_bst.preorder_traversal(), [10])
        self.assertEqual(single_bst.postorder_traversal(), [10])

    def test_inorder_with_random_insertions(self):
        """測試隨機插入後的中序遍歷"""
        new_bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            new_bst.insert(value)

        result = new_bst.inorder_traversal()
        # 應該得到排序後的序列
        self.assertEqual(result, sorted(values))

    def test_preorder_root_first(self):
        """測試前序遍歷的第一個元素是根節點"""
        result = self.bst.preorder_traversal()
        self.assertEqual(result[0], self.bst.root.value)

    def test_postorder_root_last(self):
        """測試後序遍歷的最後一個元素是根節點"""
        result = self.bst.postorder_traversal()
        self.assertEqual(result[-1], self.bst.root.value)

    def test_all_traversals_same_length(self):
        """測試所有遍歷方式得到的列表長度相同"""
        inorder = self.bst.inorder_traversal()
        preorder = self.bst.preorder_traversal()
        postorder = self.bst.postorder_traversal()

        self.assertEqual(len(inorder), len(preorder))
        self.assertEqual(len(inorder), len(postorder))
        self.assertEqual(len(inorder), self.bst.size())

    def test_traversals_contain_all_values(self):
        """測試所有遍歷方式都包含所有值"""
        values = [10, 5, 15, 3, 7, 12, 17]

        inorder = self.bst.inorder_traversal()
        preorder = self.bst.preorder_traversal()
        postorder = self.bst.postorder_traversal()

        self.assertEqual(set(inorder), set(values))
        self.assertEqual(set(preorder), set(values))
        self.assertEqual(set(postorder), set(values))


def run_tests():
    """執行測試並顯示結果"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage4)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == '__main__':
    print("=" * 70)
    print("測試階段 4: 遍歷操作（中序、前序、後序）")
    print("Testing Stage 4: Traversal Operations (Inorder, Preorder, Postorder)")
    print("=" * 70)
    print()

    success = run_tests()

    print()
    if success:
        print("✓ 恭喜！所有測試通過！")
        print("✓ Congratulations! All tests passed!")
        print()
        print("下一步：執行 test_stage5.py 測試最小值、最大值和高度")
        print("Next: Run test_stage5.py to test min, max, and height")
    else:
        print("✗ 有些測試失敗了，請檢查你的實作")
        print("✗ Some tests failed. Please check your implementation.")
