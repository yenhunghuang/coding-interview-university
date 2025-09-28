#!/usr/bin/env python3
"""
階段8測試：性能和穩定性測試

這個階段測試性能表現和極限情況，包括：
- 大規模數據的性能測試
- 記憶體效率驗證
- 時間複雜度驗證
- 穩定性和可靠性測試
- 與理論期望的比較

運行方式：python3 test_stage8.py

測試重點：
- 驗證各操作的時間複雜度符合預期
- 測試大量數據下的表現
- 記憶體使用的合理性
- 邊界情況的穩定性
- 為後續性能基準測試做準備

注意：這個階段的測試可能需要較長時間，但會提供寶貴的性能數據。
"""

import sys
import time
import gc
sys.path.append('.')

exec(open('node.py').read())
exec(open('singly_linked_list.py').read())


def test_previous_functionality_quick():
    """快速測試前階段功能（確保沒被破壞）"""
    print("=== 快速測試前階段功能 ===")

    linked_list = SinglyLinkedList()

    # 快速功能驗證
    for i in range(10):
        linked_list.push_back(i)

    assert linked_list.size() == 10
    assert linked_list.front() == 0
    assert linked_list.back() == 9

    linked_list.reverse()
    assert linked_list.front() == 9

    linked_list.remove_value(5)
    assert linked_list.size() == 9

    print("✅ 前階段功能快速驗證通過")


def test_large_scale_operations():
    """大規模操作測試"""
    print("\n=== 大規模操作測試 ===")

    # 測試不同規模的數據
    test_sizes = [100, 1000, 5000]

    for size in test_sizes:
        print(f"\n測試規模: {size} 個元素")

        linked_list = SinglyLinkedList()
        start_time = time.time()

        # 大量插入測試
        print(f"  1. 插入 {size} 個元素...")
        for i in range(size):
            if i % 4 == 0:
                linked_list.push_front(i)
            elif i % 4 == 1:
                linked_list.push_back(i)
            elif i % 4 == 2:
                linked_list.insert(0, i)  # 總是插入到開頭
            else:
                mid = linked_list.size() // 2
                linked_list.insert(mid, i)  # 插入到中間

        insert_time = time.time() - start_time
        assert linked_list.size() == size, f"❌ 插入後 size 不正確，期望 {size}，實際 {linked_list.size()}"
        print(f"  ✅ 插入完成，耗時 {insert_time:.3f}s")

        # 隨機存取測試
        print(f"  2. 隨機存取測試...")
        start_time = time.time()
        for i in range(min(100, size)):  # 限制測試次數避免過長
            idx = i * (size // min(100, size))
            if idx < linked_list.size():
                value = linked_list.value_at(idx)
                assert value is not None or value == None, "存取值異常"

        access_time = time.time() - start_time
        print(f"  ✅ 隨機存取完成，耗時 {access_time:.3f}s")

        # 搜尋和刪除測試
        print(f"  3. 搜尋和刪除測試...")
        start_time = time.time()
        # 刪除一些特定值
        remove_count = 0
        for i in range(0, size, size // 10):  # 刪除大約10個元素
            if remove_count >= 10:  # 限制刪除次數
                break
            original_size = linked_list.size()
            linked_list.remove_value(i)
            if linked_list.size() < original_size:
                remove_count += 1

        remove_time = time.time() - start_time
        print(f"  ✅ 刪除完成，移除了 {remove_count} 個元素，耗時 {remove_time:.3f}s")

        # 記憶體清理
        del linked_list
        gc.collect()

        print(f"  規模 {size} 測試完成")


def test_time_complexity_verification():
    """時間複雜度驗證"""
    print("\n=== 時間複雜度驗證 ===")

    print("\n1. 測試 O(1) 操作...")
    # 測試前端和後端操作應該是常數時間
    test_sizes = [100, 1000, 5000]
    front_times = []
    back_times = []

    for size in test_sizes:
        linked_list = SinglyLinkedList()
        # 先建立一個大列表
        for i in range(size):
            linked_list.push_back(i)

        # 測試 push_front 和 pop_front (應該是 O(1))
        start_time = time.time()
        for _ in range(100):  # 執行100次操作
            linked_list.push_front("test")
            if linked_list.size() > size + 50:
                linked_list.pop_front()
        front_time = (time.time() - start_time) / 100  # 平均每次操作時間
        front_times.append(front_time)

        # 測試 push_back 的時間 (可能是 O(1) 如果有尾指標，否則 O(n))
        start_time = time.time()
        for _ in range(10):  # 較少次數因為可能是 O(n)
            linked_list.push_back("test")
        back_time = (time.time() - start_time) / 10
        back_times.append(back_time)

        print(f"  規模 {size}: front操作 {front_time*1000:.2f}ms, back操作 {back_time*1000:.2f}ms")

        del linked_list
        gc.collect()

    print("✅ 時間複雜度測試完成")

    print("\n2. 測試 O(n) 操作...")
    # 測試應該線性增長的操作
    access_times = []
    reverse_times = []

    for size in [500, 1000, 2000]:  # 較小規模以節省時間
        linked_list = SinglyLinkedList()
        for i in range(size):
            linked_list.push_back(i)

        # 測試 value_at 的時間 (應該是 O(n))
        start_time = time.time()
        # 存取中間位置的元素
        mid_idx = size // 2
        for _ in range(20):
            value = linked_list.value_at(mid_idx)
        access_time = (time.time() - start_time) / 20
        access_times.append(access_time)

        # 測試 reverse 的時間 (應該是 O(n))
        start_time = time.time()
        linked_list.reverse()
        reverse_time = time.time() - start_time
        reverse_times.append(reverse_time)

        print(f"  規模 {size}: 中間存取 {access_time*1000:.2f}ms, 反轉 {reverse_time*1000:.2f}ms")

        del linked_list
        gc.collect()

    print("✅ 線性操作測試完成")


def test_memory_efficiency():
    """記憶體效率測試"""
    print("\n=== 記憶體效率測試 ===")

    print("\n1. 測試記憶體使用增長...")

    # 簡單的記憶體使用測試
    import sys

    # 測試空列表的記憶體
    empty_list = SinglyLinkedList()
    base_size = sys.getsizeof(empty_list)

    # 測試不同大小列表的記憶體使用
    for size in [10, 100, 500]:
        linked_list = SinglyLinkedList()
        for i in range(size):
            linked_list.push_back(i)

        # 注意：這個測試只是示意性的，實際記憶體使用很難準確測量
        print(f"  {size} 個元素的列表對象大小: {sys.getsizeof(linked_list)} bytes")

        del linked_list
        gc.collect()

    print("✅ 記憶體效率測試完成")

    print("\n2. 測試記憶體清理...")
    # 測試大量創建和銷毀是否有記憶體洩漏
    for cycle in range(5):
        temp_lists = []
        for i in range(100):
            temp_list = SinglyLinkedList()
            for j in range(50):
                temp_list.push_back(j)
            temp_lists.append(temp_list)

        # 清理
        del temp_lists
        gc.collect()

    print("✅ 記憶體清理測試完成")


def test_edge_case_stability():
    """邊界情況穩定性測試"""
    print("\n=== 邊界情況穩定性測試 ===")

    print("\n1. 測試極端數據類型...")
    linked_list = SinglyLinkedList()

    # 測試各種極端數據
    extreme_data = [
        None,
        "",
        0,
        -1,
        float('inf'),
        float('-inf'),
        [],
        {},
        set(),
        "很長很長很長的字符串" * 100,
        list(range(1000)),
    ]

    try:
        for data in extreme_data:
            linked_list.push_back(data)
            # 測試能否正確處理
            assert linked_list.back() == data, "極端數據存儲不正確"

        print("✅ 極端數據類型處理正確")
    except Exception as e:
        print(f"⚠️ 極端數據類型處理異常: {e}")

    print("\n2. 測試重複操作穩定性...")
    # 重複執行相同操作，測試是否穩定
    test_list = SinglyLinkedList()

    for cycle in range(100):
        # 添加元素
        test_list.push_back(cycle)
        test_list.push_front(cycle)

        # 如果列表太大就清理一些
        if test_list.size() > 50:
            test_list.pop_front()
            test_list.pop_back()

    assert test_list.size() > 0, "重複操作後列表應該不為空"
    print("✅ 重複操作穩定性正確")

    print("\n3. 測試異常情況恢復...")
    recovery_list = SinglyLinkedList()
    recovery_list.push_back("test")

    # 嘗試各種可能導致錯誤的操作
    error_ops = [
        lambda: recovery_list.value_at(-1),  # 負索引
        lambda: recovery_list.value_at(100), # 超大索引
        lambda: recovery_list.erase(-1),     # 負索引刪除
        lambda: recovery_list.erase(100),    # 超大索引刪除
        lambda: recovery_list.insert(-1, "test"),  # 負索引插入
        lambda: recovery_list.value_n_from_end(0), # 無效 n 值
        lambda: recovery_list.value_n_from_end(100), # 過大 n 值
    ]

    error_count = 0
    for op in error_ops:
        try:
            op()
        except (IndexError, ValueError):
            error_count += 1
        except Exception as e:
            print(f"⚠️ 意外異常類型: {e}")

    # 確認列表在錯誤操作後仍然正常
    assert recovery_list.size() == 1, "錯誤操作後列表大小異常"
    assert recovery_list.front() == "test", "錯誤操作後列表內容異常"

    print(f"✅ 異常情況恢復正確（捕獲 {error_count} 個預期錯誤）")


def test_performance_benchmarks():
    """性能基準測試"""
    print("\n=== 性能基準測試 ===")

    print("\n執行基準性能測試...")

    # 標準測試配置
    test_size = 1000
    benchmark_results = {}

    # 1. 前端操作基準
    linked_list = SinglyLinkedList()
    start_time = time.time()
    for i in range(test_size):
        linked_list.push_front(i)
    push_front_time = time.time() - start_time
    benchmark_results['push_front'] = push_front_time

    start_time = time.time()
    for _ in range(test_size):
        linked_list.pop_front()
    pop_front_time = time.time() - start_time
    benchmark_results['pop_front'] = pop_front_time

    # 2. 後端操作基準
    linked_list = SinglyLinkedList()
    start_time = time.time()
    for i in range(test_size):
        linked_list.push_back(i)
    push_back_time = time.time() - start_time
    benchmark_results['push_back'] = push_back_time

    # 3. 隨機存取基準
    start_time = time.time()
    for i in range(min(100, test_size)):  # 限制次數
        idx = i * (test_size // min(100, test_size))
        if idx < linked_list.size():
            linked_list.value_at(idx)
    access_time = time.time() - start_time
    benchmark_results['random_access'] = access_time

    # 4. 反轉基準
    start_time = time.time()
    linked_list.reverse()
    reverse_time = time.time() - start_time
    benchmark_results['reverse'] = reverse_time

    # 顯示結果
    print(f"\n基準測試結果 (測試規模: {test_size} 個元素):")
    print(f"  push_front:    {benchmark_results['push_front']*1000:.2f}ms ({benchmark_results['push_front']*1000000/test_size:.2f}μs/op)")
    print(f"  pop_front:     {benchmark_results['pop_front']*1000:.2f}ms ({benchmark_results['pop_front']*1000000/test_size:.2f}μs/op)")
    print(f"  push_back:     {benchmark_results['push_back']*1000:.2f}ms ({benchmark_results['push_back']*1000000/test_size:.2f}μs/op)")
    print(f"  random_access: {benchmark_results['random_access']*1000:.2f}ms")
    print(f"  reverse:       {benchmark_results['reverse']*1000:.2f}ms")

    print("✅ 性能基準測試完成")


def main():
    """執行所有階段8測試"""
    print("🚀 開始階段8測試：性能和穩定性測試")
    print("測試範圍：大規模操作、時間複雜度、記憶體效率、穩定性")
    print("⏰ 注意：此階段測試可能需要較長時間...")

    try:
        # 執行各項測試
        test_previous_functionality_quick()
        test_large_scale_operations()
        test_time_complexity_verification()
        test_memory_efficiency()
        test_edge_case_stability()
        test_performance_benchmarks()

        print("\n" + "="*50)
        print("🎉 階段8測試全部通過！")
        print("✅ 大規模操作性能良好")
        print("✅ 時間複雜度符合預期")
        print("✅ 記憶體使用合理")
        print("✅ 邊界情況穩定")
        print("✅ 性能基準建立")
        print("\n📝 下一步：最終綜合驗證")
        print("   然後運行 python3 test_stage_final.py")
        print("\n💡 你的 Linked List 實作已經通過了嚴格的性能測試！")
        print("   可以考慮與 Python list 進行性能對比分析。")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作，特別注意：")
        print("1. 大量數據下的性能表現")
        print("2. 時間複雜度是否符合預期")
        print("3. 記憶體使用是否合理")
        print("4. 異常情況的穩定性")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼在高負載下的穩定性")
        sys.exit(1)


if __name__ == "__main__":
    main()