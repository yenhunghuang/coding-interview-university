"""
測試階段 2：插入操作和向上調整
==============================

測試目標：
1. insert() 方法
2. peek_min() 方法
3. _heapify_up() 方法
4. 容量限制檢查

學習重點：
- 理解插入操作的步驟
- 掌握 heapify_up 的邏輯
- 理解堆積性質的維護
- 處理容量限制

插入過程：
1. 將元素加到陣列末端
2. 與父節點比較
3. 如果小於父節點則交換
4. 重複直到滿足堆積性質

視覺化範例：
插入順序：5, 3, 7, 1

步驟 1: 插入 5
[5]

步驟 2: 插入 3
[5, 3] -> [3, 5] (heapify_up)
    3
   /
  5

步驟 3: 插入 7
[3, 5, 7] (已滿足堆積性質)
    3
   / \
  5   7

步驟 4: 插入 1
[3, 5, 7, 1] -> [3, 1, 7, 5] -> [1, 3, 7, 5]
    1
   / \
  3   7
 /
5
"""

import pytest
from heap import MinHeap


class TestStage2:
    """階段 2：插入操作和堆積化測試"""

    def test_insert_single_element(self):
        """測試插入單個元素"""
        heap = MinHeap()
        heap.insert(5)

        assert heap.size() == 1
        assert heap.is_empty() is False
        assert heap.peek_min() == 5

    def test_insert_two_elements_no_swap(self):
        """測試插入兩個元素（不需交換）"""
        heap = MinHeap()
        heap.insert(3)
        heap.insert(5)

        assert heap.size() == 2
        assert heap.peek_min() == 3

    def test_insert_two_elements_with_swap(self):
        """測試插入兩個元素（需要交換）"""
        heap = MinHeap()
        heap.insert(5)
        heap.insert(3)

        assert heap.size() == 2
        assert heap.peek_min() == 3

    def test_insert_multiple_elements(self):
        """測試插入多個元素"""
        heap = MinHeap()
        elements = [5, 3, 7, 1, 9, 4, 6]

        for elem in elements:
            heap.insert(elem)

        assert heap.size() == 7
        assert heap.peek_min() == 1

    def test_insert_ascending_order(self):
        """測試插入遞增序列"""
        heap = MinHeap()
        for i in range(1, 6):
            heap.insert(i)

        assert heap.size() == 5
        assert heap.peek_min() == 1

    def test_insert_descending_order(self):
        """測試插入遞減序列（每次都需要 heapify_up）"""
        heap = MinHeap()
        for i in range(5, 0, -1):
            heap.insert(i)

        assert heap.size() == 5
        assert heap.peek_min() == 1

    def test_insert_duplicates(self):
        """測試插入重複元素"""
        heap = MinHeap()
        heap.insert(5)
        heap.insert(5)
        heap.insert(5)

        assert heap.size() == 3
        assert heap.peek_min() == 5

    def test_insert_negative_numbers(self):
        """測試插入負數"""
        heap = MinHeap()
        heap.insert(0)
        heap.insert(-5)
        heap.insert(10)
        heap.insert(-3)

        assert heap.peek_min() == -5

    def test_peek_min_maintains_heap(self):
        """測試 peek_min() 不會改變堆積"""
        heap = MinHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(7)

        # 多次 peek 應該得到相同結果
        assert heap.peek_min() == 3
        assert heap.peek_min() == 3
        assert heap.size() == 3

    def test_peek_min_empty_heap(self):
        """測試在空堆積上 peek_min() 應該拋出例外"""
        heap = MinHeap()

        with pytest.raises(IndexError):
            heap.peek_min()

    def test_capacity_limit(self):
        """測試容量限制"""
        heap = MinHeap(capacity=3)
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)

        # 第 4 個元素應該無法插入
        with pytest.raises(OverflowError):
            heap.insert(4)

    def test_heap_property_after_multiple_inserts(self):
        """
        測試多次插入後堆積性質

        檢查內部陣列是否滿足堆積性質：
        每個父節點都小於或等於其子節點
        """
        heap = MinHeap()
        elements = [15, 10, 20, 8, 12, 25, 18]

        for elem in elements:
            heap.insert(elem)

        # 取得堆積的內部表示
        heap_array = heap.get_heap()

        # 驗證堆積性質
        for i in range(len(heap_array)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap_array):
                assert heap_array[i] <= heap_array[left], \
                    f"父節點 {heap_array[i]} > 左子節點 {heap_array[left]}"

            if right < len(heap_array):
                assert heap_array[i] <= heap_array[right], \
                    f"父節點 {heap_array[i]} > 右子節點 {heap_array[right]}"

    def test_insert_zero(self):
        """測試插入零"""
        heap = MinHeap()
        heap.insert(5)
        heap.insert(0)
        heap.insert(3)

        assert heap.peek_min() == 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
