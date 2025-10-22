"""
測試階段 4：完整堆積性質維護
============================

測試目標：
1. 複雜的插入和提取序列
2. 堆積性質在各種操作下的維護
3. 壓力測試

學習重點：
- 驗證堆積性質的完整性
- 處理複雜操作序列
- 理解堆積的穩定性

堆積性質：
對於最小堆積中的任意節點 i：
- heap[i] <= heap[2*i + 1]（如果左子節點存在）
- heap[i] <= heap[2*i + 2]（如果右子節點存在）
"""

import pytest
import random
from heap import MinHeap


class TestStage4:
    """階段 4：完整堆積性質維護測試"""

    def verify_heap_property(self, heap):
        """
        輔助方法：驗證堆積性質

        檢查每個父節點是否都小於或等於其子節點
        """
        heap_array = heap.get_heap()

        for i in range(len(heap_array)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap_array):
                assert heap_array[i] <= heap_array[left], \
                    f"堆積性質違反：父節點 heap[{i}]={heap_array[i]} > " \
                    f"左子節點 heap[{left}]={heap_array[left]}"

            if right < len(heap_array):
                assert heap_array[i] <= heap_array[right], \
                    f"堆積性質違反：父節點 heap[{i}]={heap_array[i]} > " \
                    f"右子節點 heap[{right}]={heap_array[right]}"

    def test_random_inserts_maintain_property(self):
        """測試隨機插入維護堆積性質"""
        heap = MinHeap()
        random.seed(42)

        # 插入 20 個隨機數
        for _ in range(20):
            heap.insert(random.randint(1, 100))
            self.verify_heap_property(heap)

    def test_complex_operation_sequence(self):
        """測試複雜操作序列"""
        heap = MinHeap()

        # 插入一些元素
        for val in [10, 5, 15, 3, 7, 20, 12]:
            heap.insert(val)

        self.verify_heap_property(heap)

        # 提取一些元素
        heap.extract_min()
        heap.extract_min()
        self.verify_heap_property(heap)

        # 再插入一些元素
        for val in [2, 8, 18]:
            heap.insert(val)

        self.verify_heap_property(heap)

        # 再提取一些元素
        heap.extract_min()
        self.verify_heap_property(heap)

    def test_alternating_operations(self):
        """測試交替進行插入和提取"""
        heap = MinHeap()

        operations = [
            ('insert', 10),
            ('insert', 5),
            ('extract', None),
            ('insert', 15),
            ('insert', 3),
            ('extract', None),
            ('insert', 7),
            ('extract', None),
            ('insert', 20),
            ('insert', 12),
        ]

        for op, value in operations:
            if op == 'insert':
                heap.insert(value)
            else:
                if not heap.is_empty():
                    heap.extract_min()

            if not heap.is_empty():
                self.verify_heap_property(heap)

    def test_large_heap(self):
        """測試大型堆積"""
        heap = MinHeap()

        # 插入 100 個元素
        for i in range(100, 0, -1):
            heap.insert(i)

        assert heap.size() == 100
        self.verify_heap_property(heap)

        # 提取一半元素
        for i in range(1, 51):
            assert heap.extract_min() == i

        assert heap.size() == 50
        self.verify_heap_property(heap)

    def test_repeated_min_element(self):
        """測試重複的最小元素"""
        heap = MinHeap()

        # 插入多個相同的最小值
        elements = [5, 1, 10, 1, 3, 1, 7]
        for elem in elements:
            heap.insert(elem)

        self.verify_heap_property(heap)

        # 提取所有的 1
        assert heap.extract_min() == 1
        assert heap.extract_min() == 1
        assert heap.extract_min() == 1

        # 剩餘元素仍滿足堆積性質
        self.verify_heap_property(heap)

    def test_stress_test_random_operations(self):
        """壓力測試：隨機操作"""
        heap = MinHeap()
        random.seed(123)
        inserted = []

        # 執行 100 次隨機操作
        for _ in range(100):
            if random.random() < 0.7 or heap.is_empty():
                # 70% 機率插入
                val = random.randint(1, 1000)
                heap.insert(val)
                inserted.append(val)
            else:
                # 30% 機率提取
                min_val = heap.extract_min()
                assert min_val == min(inserted)
                inserted.remove(min_val)

            # 每次操作後驗證堆積性質
            if not heap.is_empty():
                self.verify_heap_property(heap)
                assert heap.peek_min() == min(inserted)

    def test_build_heap_and_extract_all(self):
        """測試建立堆積並提取所有元素"""
        heap = MinHeap()
        elements = [23, 17, 31, 45, 12, 8, 19, 5, 29]

        # 建立堆積
        for elem in elements:
            heap.insert(elem)

        self.verify_heap_property(heap)

        # 提取所有元素應該得到排序結果
        sorted_elements = []
        while not heap.is_empty():
            sorted_elements.append(heap.extract_min())

        assert sorted_elements == sorted(elements)

    def test_heap_with_float_values(self):
        """測試浮點數值"""
        heap = MinHeap()

        floats = [3.14, 2.71, 1.41, 0.5, 2.0, 1.73]
        for f in floats:
            heap.insert(f)

        self.verify_heap_property(heap)

        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_min())

        assert extracted == sorted(floats)

    def test_stability_under_duplicates(self):
        """測試重複元素下的穩定性"""
        heap = MinHeap()

        # 插入許多重複元素
        elements = [5] * 10 + [3] * 10 + [7] * 10
        random.shuffle(elements)

        for elem in elements:
            heap.insert(elem)

        self.verify_heap_property(heap)

        # 提取所有元素
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_min())

        assert extracted == sorted(elements)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
