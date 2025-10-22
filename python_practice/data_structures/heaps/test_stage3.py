"""
測試階段 3：提取最小值和向下調整
================================

測試目標：
1. extract_min() 方法
2. _heapify_down() 方法
3. 提取後的堆積性質維護

學習重點：
- 理解提取操作的步驟
- 掌握 heapify_down 的邏輯
- 理解堆積的重建過程

提取過程：
1. 儲存根節點（最小值）
2. 將最後一個元素移到根節點
3. 移除最後一個元素
4. 與子節點比較
5. 如果大於較小的子節點則交換
6. 重複直到滿足堆積性質

視覺化範例：
初始堆積：[1, 3, 7, 5, 8]
    1
   / \
  3   7
 / \
5   8

提取 1：
1. 移除 1，將 8 移到根
[8, 3, 7, 5]
    8
   / \
  3   7
 /
5

2. heapify_down(0)：8 > 3，交換
[3, 8, 7, 5]
    3
   / \
  8   7
 /
5

3. heapify_down(1)：8 > 5，交換
[3, 5, 7, 8]
    3
   / \
  5   7
 /
8
"""

import pytest
from heap import MinHeap


class TestStage3:
    """階段 3：提取最小值和向下調整測試"""

    def test_extract_min_single_element(self):
        """測試提取唯一元素"""
        heap = MinHeap()
        heap.insert(5)

        min_val = heap.extract_min()

        assert min_val == 5
        assert heap.size() == 0
        assert heap.is_empty() is True

    def test_extract_min_two_elements(self):
        """測試提取兩個元素"""
        heap = MinHeap()
        heap.insert(5)
        heap.insert(3)

        assert heap.extract_min() == 3
        assert heap.size() == 1
        assert heap.extract_min() == 5
        assert heap.size() == 0

    def test_extract_min_multiple_elements(self):
        """測試從多個元素中提取最小值"""
        heap = MinHeap()
        elements = [5, 3, 7, 1, 9, 4, 6]

        for elem in elements:
            heap.insert(elem)

        # 提取最小值應該是 1
        assert heap.extract_min() == 1
        assert heap.size() == 6

        # 下一個最小值應該是 3
        assert heap.peek_min() == 3

    def test_extract_all_elements_in_order(self):
        """測試提取所有元素應該是遞增順序"""
        heap = MinHeap()
        elements = [15, 10, 20, 8, 12, 25, 18, 5]

        for elem in elements:
            heap.insert(elem)

        # 提取所有元素
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_min())

        # 應該是排序後的結果
        assert extracted == sorted(elements)

    def test_extract_min_empty_heap(self):
        """測試從空堆積提取應該拋出例外"""
        heap = MinHeap()

        with pytest.raises(IndexError):
            heap.extract_min()

    def test_extract_min_with_duplicates(self):
        """測試提取重複元素"""
        heap = MinHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(3)
        heap.insert(5)

        assert heap.extract_min() == 3
        assert heap.extract_min() == 3
        assert heap.extract_min() == 5
        assert heap.extract_min() == 5

    def test_heap_property_after_extract(self):
        """
        測試提取後堆積性質

        每次提取後，剩餘元素仍應滿足堆積性質
        """
        heap = MinHeap()
        elements = [15, 10, 20, 8, 12, 25, 18]

        for elem in elements:
            heap.insert(elem)

        # 提取幾個元素
        heap.extract_min()
        heap.extract_min()

        # 驗證剩餘元素的堆積性質
        heap_array = heap.get_heap()

        for i in range(len(heap_array)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap_array):
                assert heap_array[i] <= heap_array[left], \
                    f"父節點 {heap_array[i]} > 左子節點 {heap_array[left]}"

            if right < len(heap_array):
                assert heap_array[i] <= heap_array[right], \
                    f"父節點 {heap_array[i]} > 右子節點 {heap_array[right]}"

    def test_extract_negative_numbers(self):
        """測試提取負數"""
        heap = MinHeap()
        heap.insert(0)
        heap.insert(-5)
        heap.insert(10)
        heap.insert(-3)

        assert heap.extract_min() == -5
        assert heap.extract_min() == -3
        assert heap.extract_min() == 0
        assert heap.extract_min() == 10

    def test_interleaved_insert_and_extract(self):
        """測試交錯插入和提取"""
        heap = MinHeap()

        heap.insert(5)
        heap.insert(3)
        assert heap.extract_min() == 3  # [5]

        heap.insert(7)
        heap.insert(1)
        assert heap.extract_min() == 1  # [5, 7]

        heap.insert(4)
        assert heap.extract_min() == 4  # [5, 7]
        assert heap.extract_min() == 5  # [7]

    def test_extract_descending_sequence(self):
        """測試從遞減序列提取"""
        heap = MinHeap()

        # 插入遞減序列
        for i in range(10, 0, -1):
            heap.insert(i)

        # 提取應該得到遞增序列
        for i in range(1, 11):
            assert heap.extract_min() == i


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
