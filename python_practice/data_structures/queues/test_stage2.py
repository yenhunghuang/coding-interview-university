#!/usr/bin/env python3
"""
階段2測試：入隊操作 - enqueue 和 is_full 方法

這個階段測試：
- enqueue() 方法：將元素加入佇列尾部
- is_full() 方法：檢查佇列是否已滿
- 驗證容量限制
- 確認 size() 的變化

運行方式：python3 test_stage2.py

實作指引：
在 queue.py 中新增以下方法：
    def enqueue(self, item)   # 入隊操作
    def is_full(self) -> bool # 檢查是否已滿
"""

import sys
sys.path.append('.')

exec(open('queue.py').read())

def test_enqueue_functionality():
    """測試 enqueue 功能"""
    print("=== 測試 enqueue 功能 ===")

    # 測試 1: 入隊單個元素
    print("\n1. 測試入隊單個元素...")
    queue = Queue()

    queue.enqueue(42)
    assert queue.size() == 1, f"❌ enqueue 後 size() 應該是 1，實際是 {queue.size()}"
    assert queue.is_empty() == False, f"❌ enqueue 後 is_empty() 應該是 False，實際是 {queue.is_empty()}"
    print("✅ 入隊單個元素正確")

    # 測試 2: 入隊多個元素
    print("\n2. 測試入隊多個元素...")
    queue.enqueue("hello")
    queue.enqueue([1, 2, 3])
    queue.enqueue({"key": "value"})

    assert queue.size() == 4, f"❌ 入隊4個元素後 size() 應該是 4，實際是 {queue.size()}"
    print("✅ 入隊多個元素正確")

    # 測試 3: 入隊 None 值
    print("\n3. 測試入隊 None 值...")
    queue.enqueue(None)
    assert queue.size() == 5, f"❌ 入隊 None 後 size() 應該是 5，實際是 {queue.size()}"
    print("✅ 入隊 None 值正確")


def test_is_full_functionality():
    """測試 is_full 功能"""
    print("\n=== 測試 is_full 功能 ===")

    # 測試 1: 無容量限制的佇列
    print("\n1. 測試無容量限制的佇列...")
    queue_unlimited = Queue()

    assert queue_unlimited.is_full() == False, "❌ 無容量限制的佇列 is_full() 應該始終是 False"
    queue_unlimited.enqueue(1)
    queue_unlimited.enqueue(2)
    queue_unlimited.enqueue(3)
    assert queue_unlimited.is_full() == False, "❌ 無容量限制的佇列 is_full() 應該始終是 False"
    print("✅ 無容量限制的佇列 is_full() 正確")

    # 測試 2: 有容量限制的佇列
    print("\n2. 測試有容量限制的佇列...")
    queue_limited = Queue(max_size=3)

    assert queue_limited.is_full() == False, "❌ 空佇列 is_full() 應該是 False"

    queue_limited.enqueue(1)
    assert queue_limited.is_full() == False, "❌ 未滿佇列 is_full() 應該是 False"

    queue_limited.enqueue(2)
    assert queue_limited.is_full() == False, "❌ 未滿佇列 is_full() 應該是 False"

    queue_limited.enqueue(3)
    assert queue_limited.is_full() == True, "❌ 已滿佇列 is_full() 應該是 True"
    print("✅ 有容量限制的佇列 is_full() 正確")


def test_capacity_overflow():
    """測試容量溢出處理"""
    print("\n=== 測試容量溢出處理 ===")

    queue = Queue(max_size=2)

    # 填滿佇列
    queue.enqueue("first")
    queue.enqueue("second")

    # 測試溢出
    print("\n1. 測試佇列滿時繼續入隊...")
    try:
        queue.enqueue("third")
        print("❌ 應該拋出 OverflowError")
        return False
    except OverflowError as e:
        print(f"✅ 正確拋出 OverflowError: {e}")

    # 確認佇列狀態未改變
    assert queue.size() == 2, "❌ 溢出後佇列大小不應改變"
    assert queue.is_full() == True, "❌ 溢出後佇列應該還是滿的"
    print("✅ 溢出處理正確，佇列狀態保持不變")

    return True


def test_different_data_types():
    """測試不同數據類型"""
    print("\n=== 測試不同數據類型 ===")

    queue = Queue()

    # 測試不同類型的數據
    test_data = [
        42,                    # 整數
        3.14,                 # 浮點數
        "hello",              # 字串
        [1, 2, 3],           # 列表
        {"a": 1},            # 字典
        (1, 2),              # 元組
        True,                # 布林值
        None                 # None
    ]

    for data in test_data:
        queue.enqueue(data)

    assert queue.size() == len(test_data), f"❌ 入隊 {len(test_data)} 個元素，size() 應該是 {len(test_data)}"
    print("✅ 不同數據類型處理正確")


def test_sequential_operations():
    """測試連續操作"""
    print("\n=== 測試連續操作 ===")

    queue = Queue(max_size=5)

    # 連續入隊
    for i in range(5):
        queue.enqueue(i)
        expected_size = i + 1
        assert queue.size() == expected_size, f"❌ 第 {i+1} 次入隊後，size() 應該是 {expected_size}"

    assert queue.is_full() == True, "❌ 填滿後 is_full() 應該是 True"
    print("✅ 連續入隊操作正確")


def test_unimplemented_methods():
    """確認其他方法還沒實作"""
    print("\n=== 確認未實作方法 ===")

    queue = Queue()
    queue.enqueue(1)  # 確保佇列不為空

    # 測試還沒實作的方法
    unimplemented_tests = [
        ("dequeue", lambda: queue.dequeue()),
        ("front", lambda: queue.front()),
    ]

    for method_name, test_func in unimplemented_tests:
        try:
            test_func()
            print(f"❌ {method_name}() 應該還沒實作")
        except NotImplementedError:
            print(f"✅ {method_name}() 正確顯示未實作")
        except Exception as e:
            print(f"⚠️ {method_name}() 拋出其他異常: {e}")


def main():
    """執行所有階段2測試"""
    print("🚀 開始階段2測試：入隊操作")
    print("測試範圍：enqueue(), is_full()")

    try:
        # 執行各項測試
        test_enqueue_functionality()
        test_is_full_functionality()
        test_capacity_overflow()
        test_different_data_types()
        test_sequential_operations()
        test_unimplemented_methods()

        print("\n" + "="*50)
        print("🎉 階段2測試全部通過！")
        print("✅ 入隊操作 (enqueue, is_full) 實作正確")
        print("✅ 容量限制處理正確")
        print("\n📝 下一步：實作 dequeue() 和 front() 方法")
        print("   然後運行 python3 test_stage3.py")

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
