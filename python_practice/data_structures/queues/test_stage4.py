#!/usr/bin/env python3
"""
階段4測試：完整 FIFO 行為驗證

這個階段測試：
- 複雜的 FIFO 場景
- 大量數據的佇列操作
- 邊界條件測試
- 容量限制下的完整行為

運行方式：python3 test_stage4.py

實作指引：
確保所有之前實作的方法都正確運作
"""

import sys
sys.path.append('.')

exec(open('queue.py').read())

def test_large_scale_operations():
    """測試大規模操作"""
    print("=== 測試大規模操作 ===")

    queue = Queue()

    # 測試 1: 入隊大量數據
    print("\n1. 測試入隊 1000 個元素...")
    n = 1000
    for i in range(n):
        queue.enqueue(i)

    assert queue.size() == n, f"❌ 入隊 {n} 個元素後，size() 應該是 {n}"
    print(f"✅ 成功入隊 {n} 個元素")

    # 測試 2: 驗證 FIFO 順序
    print("\n2. 驗證 FIFO 順序...")
    for i in range(n):
        dequeued = queue.dequeue()
        assert dequeued == i, f"❌ 第 {i} 個出隊應該是 {i}，實際是 {dequeued}"

    assert queue.is_empty() == True, "❌ 全部出隊後應該是空的"
    print(f"✅ FIFO 順序完全正確")


def test_queue_with_capacity():
    """測試有容量限制的佇列完整行為"""
    print("\n=== 測試有容量限制的佇列 ===")

    capacity = 5
    queue = Queue(max_size=capacity)

    # 填滿佇列
    print(f"\n1. 填滿容量為 {capacity} 的佇列...")
    for i in range(capacity):
        queue.enqueue(i)

    assert queue.is_full() == True, "❌ 填滿後 is_full() 應該是 True"
    assert queue.size() == capacity, f"❌ size() 應該是 {capacity}"
    print("✅ 佇列已滿")

    # 出隊一個
    print("\n2. 出隊一個元素後再入隊...")
    dequeued = queue.dequeue()
    assert dequeued == 0, f"❌ 應該出隊 0，實際是 {dequeued}"
    assert queue.is_full() == False, "❌ 出隊後 is_full() 應該是 False"

    # 現在應該可以再入隊一個
    queue.enqueue(capacity)  # 入隊新元素
    assert queue.is_full() == True, "❌ 再次填滿後 is_full() 應該是 True"
    print("✅ 容量管理正確")

    # 驗證最終順序
    print("\n3. 驗證最終順序...")
    expected = list(range(1, capacity + 1))  # [1, 2, 3, 4, 5]
    for exp in expected:
        assert queue.dequeue() == exp, f"❌ 應該出隊 {exp}"

    print("✅ 容量限制下的 FIFO 正確")


def test_alternating_operations():
    """測試交替操作"""
    print("\n=== 測試交替操作 ===")

    queue = Queue()

    # 交替入隊和出隊
    print("\n1. 交替入隊和出隊...")
    operations = [
        ('enqueue', 1),
        ('enqueue', 2),
        ('dequeue', 1),   # 應該得到 1
        ('enqueue', 3),
        ('enqueue', 4),
        ('dequeue', 2),   # 應該得到 2
        ('dequeue', 3),   # 應該得到 3
        ('enqueue', 5),
        ('dequeue', 4),   # 應該得到 4
        ('dequeue', 5),   # 應該得到 5
    ]

    for op, value in operations:
        if op == 'enqueue':
            queue.enqueue(value)
        else:  # dequeue
            result = queue.dequeue()
            assert result == value, f"❌ 出隊應該得到 {value}，實際是 {result}"

    assert queue.is_empty() == True, "❌ 最後應該是空的"
    print("✅ 交替操作正確")


def test_refill_after_empty():
    """測試清空後重新填充"""
    print("\n=== 測試清空後重新填充 ===")

    queue = Queue(max_size=3)

    # 第一輪：填充和清空
    print("\n1. 第一輪填充和清空...")
    for i in range(3):
        queue.enqueue(i)

    for i in range(3):
        assert queue.dequeue() == i

    assert queue.is_empty() == True, "❌ 應該是空的"

    # 第二輪：重新填充
    print("\n2. 第二輪重新填充...")
    for i in range(10, 13):
        queue.enqueue(i)

    assert queue.size() == 3, "❌ size 應該是 3"
    assert queue.is_full() == True, "❌ 應該是滿的"

    # 驗證第二輪數據
    for i in range(10, 13):
        assert queue.dequeue() == i, f"❌ 應該出隊 {i}"

    print("✅ 重新填充正確")


def test_boundary_conditions():
    """測試邊界條件"""
    print("\n=== 測試邊界條件 ===")

    # 測試 1: 容量為 1 的佇列
    print("\n1. 測試容量為 1 的佇列...")
    queue = Queue(max_size=1)

    queue.enqueue("only")
    assert queue.is_full() == True, "❌ 應該是滿的"
    assert queue.front() == "only", "❌ front 應該返回 'only'"
    assert queue.dequeue() == "only", "❌ dequeue 應該返回 'only'"
    assert queue.is_empty() == True, "❌ 應該是空的"
    print("✅ 容量為 1 的佇列正確")

    # 測試 2: 入隊出隊單個元素
    print("\n2. 測試入隊出隊單個元素...")
    queue2 = Queue()
    queue2.enqueue(42)
    assert queue2.size() == 1, "❌ size 應該是 1"
    assert queue2.dequeue() == 42, "❌ 應該出隊 42"
    assert queue2.size() == 0, "❌ size 應該是 0"
    print("✅ 單個元素操作正確")

    # 測試 3: 重複相同值
    print("\n3. 測試入隊相同值...")
    queue3 = Queue()
    same_value = "same"
    for _ in range(5):
        queue3.enqueue(same_value)

    for _ in range(5):
        assert queue3.dequeue() == same_value, f"❌ 應該出隊 '{same_value}'"

    print("✅ 相同值處理正確")


def test_stress_operations():
    """測試壓力操作"""
    print("\n=== 測試壓力操作 ===")

    queue = Queue()

    # 模擬實際使用場景：持續入隊和出隊
    print("\n1. 模擬持續的入隊出隊操作...")
    total_operations = 100

    for i in range(total_operations):
        # 入隊
        queue.enqueue(f"item_{i}")

        # 每 3 個入隊後出隊 1 個（除了前 5 個）
        if i > 5 and i % 3 == 0:
            queue.dequeue()

    # 驗證佇列不為空且大小合理
    expected_size = total_operations - (total_operations // 3 - 1)
    assert queue.size() == expected_size, f"❌ size 應該約為 {expected_size}"
    print(f"✅ 壓力測試通過，最終 size = {queue.size()}")


def test_front_without_dequeue():
    """測試多次 front 不影響佇列"""
    print("\n=== 測試多次 front 操作 ===")

    queue = Queue()
    test_items = [1, 2, 3, 4, 5]

    for item in test_items:
        queue.enqueue(item)

    # 多次調用 front
    print("\n1. 多次調用 front...")
    for _ in range(10):
        front_item = queue.front()
        assert front_item == 1, "❌ front 應該始終返回第一個元素"

    # 確認佇列未改變
    assert queue.size() == len(test_items), "❌ size 不應該改變"

    # 驗證完整順序
    for expected in test_items:
        assert queue.dequeue() == expected, f"❌ 應該出隊 {expected}"

    print("✅ front 操作不影響佇列")


def main():
    """執行所有階段4測試"""
    print("🚀 開始階段4測試：完整 FIFO 行為驗證")
    print("測試範圍：複雜場景、邊界條件、大規模操作")

    try:
        # 執行各項測試
        test_large_scale_operations()
        test_queue_with_capacity()
        test_alternating_operations()
        test_refill_after_empty()
        test_boundary_conditions()
        test_stress_operations()
        test_front_without_dequeue()

        print("\n" + "="*50)
        print("🎉 階段4測試全部通過！")
        print("✅ 完整 FIFO 行為驗證正確")
        print("✅ 邊界條件處理正確")
        print("✅ 大規模操作性能良好")
        print("\n📝 下一步：實作輔助功能（clear, __str__ 等）")
        print("   然後運行 python3 test_stage5.py")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作並修正後重新測試")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法")
        sys.exit(1)


if __name__ == "__main__":
    main()
