"""
測試階段 5：邊界條件和錯誤處理
==============================

測試目標：
1. 空堆積操作
2. 單元素堆積
3. 容量限制
4. 異常情況處理
5. 邊界值測試

學習重點：
- 了解邊界條件的重要性
- 掌握錯誤處理機制
- 提高程式的健壯性

常見邊界條件：
- 空集合操作
- 單元素操作
- 滿容量操作
- 極值（最大/最小整數）
- 特殊值（0、負數）
"""

import pytest
import sys
from heap import MinHeap


class TestStage5:
    """階段 5：邊界條件和錯誤處理測試"""

    # ===== 空堆積測試 =====

    def test_peek_empty_heap_raises_error(self):
        """測試空堆積 peek 拋出錯誤"""
        heap = MinHeap()

        with pytest.raises(IndexError):
            heap.peek_min()

    def test_extract_empty_heap_raises_error(self):
        """測試空堆積 extract 拋出錯誤"""
        heap = MinHeap()

        with pytest.raises(IndexError):
            heap.extract_min()

    def test_empty_heap_size(self):
        """測試空堆積的大小"""
        heap = MinHeap()

        assert heap.size() == 0
        assert heap.is_empty() is True
        assert len(heap) == 0

    def test_empty_heap_representation(self):
        """測試空堆積的字串表示"""
        heap = MinHeap()

        repr_str = repr(heap)
        assert 'MinHeap' in repr_str

    # ===== 單元素堆積測試 =====

    def test_single_element_operations(self):
        """測試單元素堆積的所有操作"""
        heap = MinHeap()
        heap.insert(42)

        assert heap.size() == 1
        assert heap.is_empty() is False
        assert heap.peek_min() == 42

        extracted = heap.extract_min()
        assert extracted == 42
        assert heap.is_empty() is True

    def test_single_element_multiple_peeks(self):
        """測試單元素堆積的多次 peek"""
        heap = MinHeap()
        heap.insert(10)

        for _ in range(5):
            assert heap.peek_min() == 10

        assert heap.size() == 1

    # ===== 容量限制測試 =====

    def test_capacity_zero(self):
        """測試容量為 0 的堆積"""
        heap = MinHeap(capacity=0)

        with pytest.raises(OverflowError):
            heap.insert(1)

    def test_capacity_one(self):
        """測試容量為 1 的堆積"""
        heap = MinHeap(capacity=1)
        heap.insert(5)

        assert heap.size() == 1
        assert heap.peek_min() == 5

        with pytest.raises(OverflowError):
            heap.insert(3)

    def test_fill_to_capacity(self):
        """測試填滿堆積容量"""
        capacity = 5
        heap = MinHeap(capacity=capacity)

        # 填滿堆積
        for i in range(capacity):
            heap.insert(i)

        assert heap.size() == capacity

        # 嘗試再插入應該失敗
        with pytest.raises(OverflowError):
            heap.insert(999)

    def test_capacity_after_extract(self):
        """測試提取後可以再次插入"""
        heap = MinHeap(capacity=3)

        heap.insert(1)
        heap.insert(2)
        heap.insert(3)

        # 提取一個元素
        heap.extract_min()

        # 現在應該可以再插入
        heap.insert(4)
        assert heap.size() == 3

    # ===== 極值測試 =====

    def test_max_integer(self):
        """測試最大整數值"""
        heap = MinHeap()

        heap.insert(sys.maxsize)
        heap.insert(sys.maxsize - 1)
        heap.insert(sys.maxsize)

        assert heap.extract_min() == sys.maxsize - 1

    def test_min_integer(self):
        """測試最小整數值"""
        heap = MinHeap()

        heap.insert(-sys.maxsize)
        heap.insert(-sys.maxsize + 1)
        heap.insert(-sys.maxsize)

        assert heap.extract_min() == -sys.maxsize

    def test_mixed_extreme_values(self):
        """測試混合極值"""
        heap = MinHeap()

        heap.insert(0)
        heap.insert(sys.maxsize)
        heap.insert(-sys.maxsize)
        heap.insert(1)
        heap.insert(-1)

        assert heap.extract_min() == -sys.maxsize
        assert heap.extract_min() == -1
        assert heap.extract_min() == 0
        assert heap.extract_min() == 1
        assert heap.extract_min() == sys.maxsize

    # ===== 特殊值測試 =====

    def test_all_zeros(self):
        """測試全部為零的情況"""
        heap = MinHeap()

        for _ in range(5):
            heap.insert(0)

        assert heap.size() == 5

        for _ in range(5):
            assert heap.extract_min() == 0

    def test_all_same_value(self):
        """測試所有元素相同"""
        heap = MinHeap()
        value = 42

        for _ in range(10):
            heap.insert(value)

        assert heap.size() == 10

        for _ in range(10):
            assert heap.extract_min() == value

    def test_alternating_positive_negative(self):
        """測試正負交替"""
        heap = MinHeap()

        for i in range(-10, 10):
            heap.insert(i)

        # 應該按照從小到大提取
        for i in range(-10, 10):
            assert heap.extract_min() == i

    # ===== 提取到空測試 =====

    def test_extract_until_empty(self):
        """測試提取直到空"""
        heap = MinHeap()

        for i in range(10):
            heap.insert(i)

        # 提取所有元素
        for i in range(10):
            assert heap.extract_min() == i

        # 堆積應該為空
        assert heap.is_empty() is True

        # 再次提取應該拋出錯誤
        with pytest.raises(IndexError):
            heap.extract_min()

    # ===== 重複操作測試 =====

    def test_repeated_insert_and_extract(self):
        """測試重複插入和提取"""
        heap = MinHeap()

        # 多次循環
        for cycle in range(3):
            # 插入一些元素
            for i in range(5):
                heap.insert(cycle * 5 + i)

            # 提取一些元素
            for _ in range(3):
                heap.extract_min()

    def test_insert_after_empty(self):
        """測試清空後再插入"""
        heap = MinHeap()

        # 第一輪
        heap.insert(5)
        heap.insert(3)
        heap.extract_min()
        heap.extract_min()

        assert heap.is_empty() is True

        # 第二輪
        heap.insert(10)
        heap.insert(7)

        assert heap.size() == 2
        assert heap.peek_min() == 7

    # ===== 浮點數精度測試 =====

    def test_float_precision(self):
        """測試浮點數精度"""
        heap = MinHeap()

        heap.insert(0.1 + 0.2)  # 可能有精度問題
        heap.insert(0.3)
        heap.insert(0.1)

        # 應該能正確處理
        assert heap.extract_min() == 0.1

    def test_very_small_floats(self):
        """測試很小的浮點數"""
        heap = MinHeap()

        heap.insert(1e-10)
        heap.insert(1e-11)
        heap.insert(1e-9)

        assert heap.extract_min() == 1e-11


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
