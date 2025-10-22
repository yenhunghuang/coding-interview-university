"""
最終測試階段：整合測試和綜合評估
================================

測試目標：
1. 完整功能整合測試
2. 複雜場景模擬
3. 效能驗證
4. 程式碼品質檢查

學習重點：
- 綜合運用所有堆積操作
- 解決實際問題
- 理解堆積的優勢和限制
- 驗證學習成果

此階段確保：
- 所有功能正確運作
- 堆積性質始終維護
- 效能符合預期
- 程式碼品質達標
"""

import pytest
import random
import time
from heap import MinHeap, heapify, heap_sort, find_kth_smallest


class TestFinalIntegration:
    """最終整合測試"""

    def verify_heap_property(self, heap):
        """驗證堆積性質的輔助方法"""
        heap_array = heap.get_heap()

        for i in range(len(heap_array)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap_array):
                assert heap_array[i] <= heap_array[left], \
                    f"堆積性質違反：heap[{i}]={heap_array[i]} > heap[{left}]={heap_array[left]}"

            if right < len(heap_array):
                assert heap_array[i] <= heap_array[right], \
                    f"堆積性質違反：heap[{i}]={heap_array[i]} > heap[{right}]={heap_array[right]}"

    # ===== 完整功能測試 =====

    def test_complete_workflow(self):
        """測試完整工作流程"""
        heap = MinHeap()

        # 階段 1: 建立堆積
        elements = [20, 15, 30, 10, 25, 5, 40, 35]
        for elem in elements:
            heap.insert(elem)

        assert heap.size() == 8
        self.verify_heap_property(heap)

        # 階段 2: 查看最小值
        assert heap.peek_min() == 5

        # 階段 3: 提取部分元素
        extracted = []
        for _ in range(3):
            extracted.append(heap.extract_min())

        assert extracted == [5, 10, 15]
        assert heap.size() == 5
        self.verify_heap_property(heap)

        # 階段 4: 加入新元素
        heap.insert(12)
        heap.insert(8)

        assert heap.size() == 7
        self.verify_heap_property(heap)

        # 階段 5: 提取所有剩餘元素
        remaining = []
        while not heap.is_empty():
            remaining.append(heap.extract_min())

        assert remaining == sorted(remaining)

    def test_stress_test_large_dataset(self):
        """大型資料集壓力測試"""
        heap = MinHeap()
        random.seed(100)

        n = 1000
        elements = [random.randint(1, 10000) for _ in range(n)]

        # 插入所有元素
        for elem in elements:
            heap.insert(elem)

        assert heap.size() == n
        self.verify_heap_property(heap)

        # 提取所有元素應該是排序的
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_min())

        assert len(extracted) == n
        assert extracted == sorted(elements)

    def test_mixed_operations_complex_scenario(self):
        """複雜場景混合操作測試"""
        heap = MinHeap()
        random.seed(200)

        # 模擬複雜的使用場景
        for iteration in range(10):
            # 加入一批元素
            for _ in range(random.randint(5, 15)):
                heap.insert(random.randint(1, 100))

            self.verify_heap_property(heap)

            # 提取一些元素
            to_extract = min(random.randint(2, 8), heap.size())
            for _ in range(to_extract):
                heap.extract_min()

            if not heap.is_empty():
                self.verify_heap_property(heap)

    # ===== 實際問題解決測試 =====

    def test_find_median_in_stream(self):
        """
        問題：在資料串流中找中位數

        解法：使用兩個堆積
        - 最大堆積：儲存較小的一半（這裡用負數模擬）
        - 最小堆積：儲存較大的一半

        這裡簡化為只測試最小堆積的基本功能
        """
        min_heap = MinHeap()
        stream = [5, 15, 1, 3, 10, 8]

        for num in stream:
            min_heap.insert(num)

        # 提取到中位數位置
        sorted_list = []
        while not min_heap.is_empty():
            sorted_list.append(min_heap.extract_min())

        assert sorted_list == sorted(stream)
        median_index = len(sorted_list) // 2
        assert sorted_list[median_index] == 8

    def test_task_scheduler(self):
        """
        問題：任務排程器

        場景：根據優先權執行任務
        """
        scheduler = MinHeap()

        # 任務：(優先權, 任務名稱, 執行時間)
        tasks = [
            (3, 'Email Processing', 5),
            (1, 'Critical Bug Fix', 10),
            (2, 'Database Backup', 15),
            (1, 'Security Update', 8),
            (4, 'Report Generation', 20),
        ]

        # 加入所有任務
        for task in tasks:
            scheduler.insert(task)

        # 按優先權執行
        execution_order = []
        while not scheduler.is_empty():
            priority, name, duration = scheduler.extract_min()
            execution_order.append(name)

        # 驗證高優先權任務先執行
        assert execution_order[0] in ['Critical Bug Fix', 'Security Update']
        assert execution_order[1] in ['Critical Bug Fix', 'Security Update']
        assert execution_order[2] == 'Database Backup'

    def test_merge_sorted_lists(self):
        """
        問題：合併 K 個已排序串列

        應用：外部排序、資料庫合併
        """
        lists = [
            [1, 4, 7, 10],
            [2, 5, 8, 11],
            [3, 6, 9, 12],
            [0, 13, 14, 15]
        ]

        heap = MinHeap()

        # 將所有元素加入堆積
        for lst in lists:
            for num in lst:
                heap.insert(num)

        # 提取所有元素
        merged = []
        while not heap.is_empty():
            merged.append(heap.extract_min())

        # 驗證結果
        expected = sorted([num for lst in lists for num in lst])
        assert merged == expected

    def test_top_k_frequent_elements(self):
        """
        問題：找出前 K 個最小的不同元素

        應用：資料分析、統計
        """
        data = [1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5]
        k = 3

        # 提取唯一元素
        unique = list(set(data))

        # 使用堆積找前 K 個最小
        heap = MinHeap()
        for num in unique:
            heap.insert(num)

        top_k = []
        for _ in range(min(k, len(unique))):
            top_k.append(heap.extract_min())

        assert top_k == [1, 2, 3]

    # ===== 效能驗證測試 =====

    def test_insert_performance(self):
        """驗證插入操作的效能"""
        heap = MinHeap()

        start_time = time.time()

        # 插入 10000 個元素
        for i in range(10000):
            heap.insert(i)

        elapsed = time.time() - start_time

        # 應該在合理時間內完成
        assert elapsed < 1.0, f"插入效能不佳: {elapsed:.3f}秒"
        assert heap.size() == 10000

    def test_extract_performance(self):
        """驗證提取操作的效能"""
        heap = MinHeap()

        # 先插入元素
        for i in range(10000):
            heap.insert(i)

        start_time = time.time()

        # 提取所有元素
        while not heap.is_empty():
            heap.extract_min()

        elapsed = time.time() - start_time

        # 應該在合理時間內完成
        assert elapsed < 1.0, f"提取效能不佳: {elapsed:.3f}秒"

    def test_heap_sort_vs_builtin_sort_performance(self):
        """比較堆積排序與內建排序的效能"""
        random.seed(300)
        arr = [random.randint(1, 10000) for _ in range(1000)]

        # 堆積排序
        start = time.time()
        heap_sorted = heap_sort(arr.copy())
        heap_time = time.time() - start

        # 內建排序
        start = time.time()
        builtin_sorted = sorted(arr)
        builtin_time = time.time() - start

        print(f"\n堆積排序時間: {heap_time:.6f}秒")
        print(f"內建排序時間: {builtin_time:.6f}秒")

        # 結果應該相同
        assert heap_sorted == builtin_sorted

    # ===== 邊界和異常情況整合測試 =====

    def test_comprehensive_edge_cases(self):
        """綜合邊界情況測試"""
        heap = MinHeap()

        # 測試 1: 空堆積操作
        assert heap.is_empty()

        with pytest.raises(IndexError):
            heap.peek_min()

        with pytest.raises(IndexError):
            heap.extract_min()

        # 測試 2: 單元素
        heap.insert(42)
        assert heap.peek_min() == 42
        assert heap.extract_min() == 42
        assert heap.is_empty()

        # 測試 3: 大量重複元素
        for _ in range(100):
            heap.insert(5)

        assert heap.size() == 100

        for _ in range(100):
            assert heap.extract_min() == 5

        assert heap.is_empty()

        # 測試 4: 極值
        heap.insert(0)
        heap.insert(-1000000)
        heap.insert(1000000)

        assert heap.extract_min() == -1000000
        assert heap.extract_min() == 0
        assert heap.extract_min() == 1000000

    def test_heap_with_custom_objects(self):
        """測試堆積處理自訂物件（使用 tuple）"""
        heap = MinHeap()

        # 使用 tuple 表示優先權和資料
        items = [
            (5, 'Low priority'),
            (1, 'High priority'),
            (3, 'Medium priority'),
            (1, 'Another high priority'),
        ]

        for item in items:
            heap.insert(item)

        # 提取應該按第一個元素（優先權）排序
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_min())

        assert extracted[0][0] == 1
        assert extracted[1][0] == 1
        assert extracted[2][0] == 3
        assert extracted[3][0] == 5

    # ===== 最終驗證 =====

    def test_all_features_integration(self):
        """所有功能整合測試"""
        # 1. 建立並填充堆積
        heap = MinHeap(capacity=100)

        random.seed(500)
        test_data = [random.randint(1, 100) for _ in range(50)]

        for val in test_data:
            heap.insert(val)

        # 2. 驗證基本屬性
        assert heap.size() == 50
        assert not heap.is_empty()
        assert len(heap) == 50
        self.verify_heap_property(heap)

        # 3. Peek 操作
        min_val = heap.peek_min()
        assert min_val == min(test_data)

        # 4. 提取操作
        extracted_vals = []
        for _ in range(10):
            extracted_vals.append(heap.extract_min())

        assert extracted_vals == sorted(extracted_vals)
        assert heap.size() == 40

        # 5. 繼續插入
        for val in [5, 15, 25]:
            heap.insert(val)

        assert heap.size() == 43
        self.verify_heap_property(heap)

        # 6. 提取所有剩餘元素
        remaining = []
        while not heap.is_empty():
            remaining.append(heap.extract_min())

        assert remaining == sorted(remaining)

        # 7. 驗證最終狀態
        assert heap.size() == 0
        assert heap.is_empty()

    def test_readme_examples(self):
        """測試 README 中的範例程式碼"""
        # 範例 1: 基本使用
        heap = MinHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(7)
        heap.insert(1)

        assert heap.peek_min() == 1
        assert heap.extract_min() == 1
        assert heap.extract_min() == 3

        # 範例 2: 堆積排序
        arr = [9, 5, 6, 2, 3]
        sorted_arr = heap_sort(arr)
        assert sorted_arr == [2, 3, 5, 6, 9]

        # 範例 3: 找第 K 小
        arr = [7, 10, 4, 3, 20, 15]
        kth = find_kth_smallest(arr, 3)
        assert kth == 7


if __name__ == '__main__':
    # 執行所有測試並顯示詳細結果
    pytest.main([__file__, '-v', '--tb=short'])

    print("\n" + "="*70)
    print("恭喜！如果所有測試都通過，表示你已經完整掌握了堆積資料結構！")
    print("="*70)
    print("\n下一步建議：")
    print("1. 實作 Max Heap（最大堆積）")
    print("2. 嘗試解決 LeetCode 上的堆積相關題目")
    print("3. 研究優先權佇列的進階應用")
    print("4. 學習其他堆積變體（二項堆積、費氏堆積等）")
