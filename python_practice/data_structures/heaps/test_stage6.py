"""
測試階段 6：堆積排序和進階操作
==============================

測試目標：
1. 堆積排序實作
2. 從陣列建立堆積（heapify）
3. 找第 K 小元素
4. 進階應用場景

學習重點：
- 理解堆積排序演算法
- 掌握 heapify 的效率優勢
- 學習堆積的實際應用
- 比較不同排序方法的效能

堆積排序步驟：
1. 建立最大堆積（或最小堆積）
2. 將根節點與最後一個節點交換
3. 縮小堆積範圍
4. 重新調整堆積
5. 重複步驟 2-4

時間複雜度：O(n log n)
空間複雜度：O(1) - 原地排序
"""

import pytest
import time
from heap import MinHeap, heapify, heap_sort, find_kth_smallest


class TestStage6:
    """階段 6：堆積排序和進階操作測試"""

    # ===== Heapify 測試 =====

    def test_heapify_empty_array(self):
        """測試 heapify 空陣列"""
        arr = []
        heapify(arr)
        assert arr == []

    def test_heapify_single_element(self):
        """測試 heapify 單一元素"""
        arr = [5]
        heapify(arr)
        assert arr == [5]

    def test_heapify_sorted_array(self):
        """測試 heapify 已排序陣列"""
        arr = [1, 2, 3, 4, 5]
        heapify(arr)

        # 驗證堆積性質
        for i in range(len(arr)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(arr):
                assert arr[i] <= arr[left]

            if right < len(arr):
                assert arr[i] <= arr[right]

    def test_heapify_reverse_sorted_array(self):
        """測試 heapify 反向排序陣列"""
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        heapify(arr)

        # 驗證堆積性質
        for i in range(len(arr)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(arr):
                assert arr[i] <= arr[left]

            if right < len(arr):
                assert arr[i] <= arr[right]

    def test_heapify_random_array(self):
        """測試 heapify 隨機陣列"""
        arr = [15, 10, 20, 8, 12, 25, 18, 5, 30]
        heapify(arr)

        # 驗證堆積性質
        for i in range(len(arr)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(arr):
                assert arr[i] <= arr[left]

            if right < len(arr):
                assert arr[i] <= arr[right]

    def test_heapify_with_duplicates(self):
        """測試 heapify 有重複元素的陣列"""
        arr = [5, 3, 7, 3, 1, 5, 2]
        heapify(arr)

        # 驗證堆積性質
        for i in range(len(arr)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(arr):
                assert arr[i] <= arr[left]

            if right < len(arr):
                assert arr[i] <= arr[right]

    # ===== 堆積排序測試 =====

    def test_heap_sort_empty_array(self):
        """測試堆積排序空陣列"""
        arr = []
        result = heap_sort(arr)
        assert result == []

    def test_heap_sort_single_element(self):
        """測試堆積排序單一元素"""
        arr = [5]
        result = heap_sort(arr)
        assert result == [5]

    def test_heap_sort_sorted_array(self):
        """測試堆積排序已排序陣列"""
        arr = [1, 2, 3, 4, 5]
        result = heap_sort(arr)
        assert result == [1, 2, 3, 4, 5]

    def test_heap_sort_reverse_sorted_array(self):
        """測試堆積排序反向排序陣列"""
        arr = [5, 4, 3, 2, 1]
        result = heap_sort(arr)
        assert result == [1, 2, 3, 4, 5]

    def test_heap_sort_random_array(self):
        """測試堆積排序隨機陣列"""
        arr = [15, 10, 20, 8, 12, 25, 18, 5, 30]
        result = heap_sort(arr)
        assert result == sorted(arr)

    def test_heap_sort_with_duplicates(self):
        """測試堆積排序有重複元素"""
        arr = [5, 3, 7, 3, 1, 5, 2, 1]
        result = heap_sort(arr)
        assert result == sorted(arr)

    def test_heap_sort_negative_numbers(self):
        """測試堆積排序負數"""
        arr = [3, -1, 4, -5, 2, 0, -3]
        result = heap_sort(arr)
        assert result == sorted(arr)

    def test_heap_sort_large_array(self):
        """測試堆積排序大型陣列"""
        arr = list(range(100, 0, -1))
        result = heap_sort(arr)
        assert result == list(range(1, 101))

    # ===== 找第 K 小元素測試 =====

    def test_kth_smallest_first_element(self):
        """測試找第 1 小（最小）元素"""
        arr = [7, 10, 4, 3, 20, 15]
        result = find_kth_smallest(arr, 1)
        assert result == 3

    def test_kth_smallest_last_element(self):
        """測試找最後一個（最大）元素"""
        arr = [7, 10, 4, 3, 20, 15]
        result = find_kth_smallest(arr, 6)
        assert result == 20

    def test_kth_smallest_middle_element(self):
        """測試找中間元素"""
        arr = [7, 10, 4, 3, 20, 15]
        result = find_kth_smallest(arr, 3)
        assert result == 7

    def test_kth_smallest_with_duplicates(self):
        """測試有重複元素時找第 K 小"""
        arr = [5, 3, 7, 3, 1, 5, 2]
        result = find_kth_smallest(arr, 3)
        # 排序後: [1, 2, 3, 3, 5, 5, 7]
        # 第 3 小是 3
        assert result == 3

    def test_kth_smallest_single_element(self):
        """測試單一元素陣列"""
        arr = [42]
        result = find_kth_smallest(arr, 1)
        assert result == 42

    def test_kth_smallest_all_same(self):
        """測試所有元素相同"""
        arr = [5, 5, 5, 5, 5]
        result = find_kth_smallest(arr, 3)
        assert result == 5

    # ===== 效能比較測試 =====

    def test_heap_vs_builtin_sort_correctness(self):
        """測試堆積排序與內建排序的正確性比較"""
        import random
        random.seed(42)

        arr = [random.randint(1, 1000) for _ in range(100)]

        heap_sorted = heap_sort(arr.copy())
        builtin_sorted = sorted(arr)

        assert heap_sorted == builtin_sorted

    def test_heapify_vs_repeated_insert(self):
        """
        測試 heapify 與逐個插入的效能差異

        Heapify: O(n)
        逐個插入: O(n log n)
        """
        import random
        random.seed(42)

        arr = [random.randint(1, 1000) for _ in range(100)]

        # 方法 1: 使用 heapify
        start = time.time()
        arr_copy = arr.copy()
        heapify(arr_copy)
        heapify_time = time.time() - start

        # 方法 2: 逐個插入
        start = time.time()
        heap = MinHeap()
        for val in arr:
            heap.insert(val)
        insert_time = time.time() - start

        # Heapify 應該更快（雖然在小資料集上可能看不出來）
        print(f"\nHeapify time: {heapify_time:.6f}s")
        print(f"Insert time: {insert_time:.6f}s")

        # 兩種方法都應該產生有效的堆積
        # 驗證 heapify 結果
        for i in range(len(arr_copy)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(arr_copy):
                assert arr_copy[i] <= arr_copy[left]

            if right < len(arr_copy):
                assert arr_copy[i] <= arr_copy[right]

    # ===== 實際應用場景測試 =====

    def test_streaming_median_simulation(self):
        """
        模擬串流中位數計算

        使用兩個堆積：
        - 最大堆積（左半部）
        - 最小堆積（右半部）
        """
        min_heap = MinHeap()  # 儲存較大的一半

        # 簡單測試：只使用最小堆積找最小值
        for val in [5, 15, 1, 3, 10]:
            min_heap.insert(val)

        # 持續提取最小值
        values = []
        while not min_heap.is_empty():
            values.append(min_heap.extract_min())

        assert values == [1, 3, 5, 10, 15]

    def test_top_k_elements(self):
        """
        測試找出前 K 個最小元素

        應用：找出排行榜前 K 名
        """
        arr = [15, 20, 5, 8, 12, 3, 25, 10]
        k = 3

        heap = MinHeap()
        for val in arr:
            heap.insert(val)

        top_k = []
        for _ in range(k):
            top_k.append(heap.extract_min())

        assert top_k == [3, 5, 8]

    def test_merge_k_sorted_arrays(self):
        """
        測試合併 K 個已排序陣列

        使用堆積可以有效率地合併多個已排序陣列
        """
        arrays = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]

        heap = MinHeap()

        # 將所有元素加入堆積
        for arr in arrays:
            for val in arr:
                heap.insert(val)

        # 提取所有元素得到合併結果
        merged = []
        while not heap.is_empty():
            merged.append(heap.extract_min())

        assert merged == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_priority_queue_simulation(self):
        """
        模擬優先權佇列

        應用：任務排程、事件處理
        """
        # 使用堆積實作優先權佇列（數字越小優先權越高）
        pq = MinHeap()

        # 加入任務（優先權, 任務ID）
        tasks = [
            (5, 'Task A'),
            (1, 'Task B'),
            (3, 'Task C'),
            (2, 'Task D'),
            (4, 'Task E')
        ]

        for priority, task_id in tasks:
            pq.insert((priority, task_id))

        # 按優先權處理任務
        processed = []
        while not pq.is_empty():
            priority, task_id = pq.extract_min()
            processed.append(task_id)

        assert processed == ['Task B', 'Task D', 'Task C', 'Task E', 'Task A']


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
