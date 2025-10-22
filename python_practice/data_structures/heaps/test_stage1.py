"""
測試階段 1：初始化和輔助方法
============================

測試目標：
1. 堆積的初始化
2. size() 方法
3. is_empty() 方法
4. 索引計算輔助方法：_parent(), _left_child(), _right_child()

學習重點：
- 理解堆積的陣列表示
- 掌握父子節點的索引關係
- 理解完全二元樹的性質

索引關係公式：
- 父節點：(i - 1) // 2
- 左子節點：2 * i + 1
- 右子節點：2 * i + 2
"""

import pytest
from heap import MinHeap


class TestStage1:
    """階段 1：基本初始化和輔助方法測試"""

    def test_initialization_default(self):
        """測試預設初始化"""
        heap = MinHeap()
        assert heap.size() == 0
        assert heap.is_empty() is True

    def test_initialization_with_capacity(self):
        """測試有容量限制的初始化"""
        heap = MinHeap(capacity=10)
        assert heap.size() == 0
        assert heap.is_empty() is True

    def test_size_method(self):
        """測試 size() 方法"""
        heap = MinHeap()
        assert heap.size() == 0

    def test_is_empty_true(self):
        """測試 is_empty() 在空堆積時回傳 True"""
        heap = MinHeap()
        assert heap.is_empty() is True

    def test_parent_index(self):
        """
        測試 _parent() 方法

        陣列視圖：[0, 1, 2, 3, 4, 5, 6]
        樹狀視圖：
                0
              /   \
             1     2
            / \   / \
           3   4 5   6
        """
        heap = MinHeap()

        # 索引 1 和 2 的父節點是 0
        assert heap._parent(1) == 0
        assert heap._parent(2) == 0

        # 索引 3 和 4 的父節點是 1
        assert heap._parent(3) == 1
        assert heap._parent(4) == 1

        # 索引 5 和 6 的父節點是 2
        assert heap._parent(5) == 2
        assert heap._parent(6) == 2

    def test_left_child_index(self):
        """
        測試 _left_child() 方法

        陣列視圖：[0, 1, 2, 3, 4, 5, 6]
        索引 0 的左子節點是 1
        索引 1 的左子節點是 3
        索引 2 的左子節點是 5
        """
        heap = MinHeap()

        assert heap._left_child(0) == 1
        assert heap._left_child(1) == 3
        assert heap._left_child(2) == 5

    def test_right_child_index(self):
        """
        測試 _right_child() 方法

        陣列視圖：[0, 1, 2, 3, 4, 5, 6]
        索引 0 的右子節點是 2
        索引 1 的右子節點是 4
        索引 2 的右子節點是 6
        """
        heap = MinHeap()

        assert heap._right_child(0) == 2
        assert heap._right_child(1) == 4
        assert heap._right_child(2) == 6

    def test_len_builtin(self):
        """測試內建 len() 函數"""
        heap = MinHeap()
        assert len(heap) == 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
