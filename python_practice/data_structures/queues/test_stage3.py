#!/usr/bin/env python3
"""
階段3測試：出隊操作 - dequeue 和 front 方法

這個階段測試：
- dequeue() 方法：移除並返回佇列前端元素
- front() 方法：查看佇列前端元素但不移除
- 驗證 FIFO (先進先出) 的基本特性
- 空佇列的錯誤處理

運行方式：python3 test_stage3.py

實作指引：
在 queue.py 中新增以下方法：
    def dequeue(self) -> any  # 出隊操作
    def front(self) -> any    # 查看前端元素
"""

import sys
sys.path.append('.')

exec(open('queue.py').read())

def test_dequeue_functionality():
    """測試 dequeue 功能"""
    print("=== 測試 dequeue 功能 ===")

    # 測試 1: 基本出隊
    print("\n1. 測試基本出隊...")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    result = queue.dequeue()
    assert result == 1, f"❌ 第一個出隊應該是 1，實際是 {result}"
    assert queue.size() == 2, f"❌ 出隊後 size() 應該是 2，實際是 {queue.size()}"
    print("✅ 基本出隊正確")

    # 測試 2: 連續出隊
    print("\n2. 測試連續出隊...")
    result2 = queue.dequeue()
    assert result2 == 2, f"❌ 第二個出隊應該是 2，實際是 {result2}"

    result3 = queue.dequeue()
    assert result3 == 3, f"❌ 第三個出隊應該是 3，實際是 {result3}"

    assert queue.size() == 0, f"❌ 全部出隊後 size() 應該是 0，實際是 {queue.size()}"
    assert queue.is_empty() == True, f"❌ 全部出隊後 is_empty() 應該是 True"
    print("✅ 連續出隊正確")


def test_front_functionality():
    """測試 front 功能"""
    print("\n=== 測試 front 功能 ===")

    # 測試 1: front 基本功能
    print("\n1. 測試 front 基本功能...")
    queue = Queue()
    queue.enqueue("first")
    queue.enqueue("second")
    queue.enqueue("third")

    # front 應該返回第一個入隊的元素
    front_item = queue.front()
    assert front_item == "first", f"❌ front() 應該返回 'first'，實際返回 {front_item}"

    # front 不應該改變佇列大小
    assert queue.size() == 3, f"❌ front 後 size() 應該還是 3，實際是 {queue.size()}"
    print("✅ front 基本功能正確")

    # 測試 2: 連續 front
    print("\n2. 測試連續 front...")
    first_front = queue.front()
    second_front = queue.front()

    assert first_front == second_front == "first", f"❌ 連續 front() 應該返回相同值"
    assert queue.size() == 3, f"❌ 連續 front 後 size() 應該還是 3，實際是 {queue.size()}"
    print("✅ 連續 front 正確")


def test_fifo_behavior():
    """測試 FIFO (先進先出) 行為"""
    print("\n=== 測試 FIFO 行為 ===")

    queue = Queue()

    # 按順序入隊
    items = ["first", "second", "third", "fourth", "fifth"]
    for item in items:
        queue.enqueue(item)

    print("\n驗證出隊順序...")
    # 出隊順序應該與入隊順序相同（FIFO）
    for expected_item in items:
        # 先檢查 front
        front_item = queue.front()
        assert front_item == expected_item, f"❌ front() 應該是 {expected_item}，實際是 {front_item}"

        # 再出隊
        dequeued_item = queue.dequeue()
        assert dequeued_item == expected_item, f"❌ dequeue() 應該是 {expected_item}，實際是 {dequeued_item}"

    assert queue.is_empty() == True, "❌ 全部出隊後佇列應該是空的"
    print("✅ FIFO 行為完全正確")


def test_mixed_operations():
    """測試混合操作（入隊和出隊交替）"""
    print("\n=== 測試混合操作 ===")

    queue = Queue()

    # 入隊 3 個
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # 出隊 1 個
    assert queue.dequeue() == 1, "❌ 應該出隊 1"
    assert queue.size() == 2, "❌ size 應該是 2"

    # 再入隊 2 個
    queue.enqueue(4)
    queue.enqueue(5)
    assert queue.size() == 4, "❌ size 應該是 4"

    # 驗證順序：應該是 2, 3, 4, 5
    expected = [2, 3, 4, 5]
    for exp in expected:
        assert queue.dequeue() == exp, f"❌ 應該出隊 {exp}"

    assert queue.is_empty() == True, "❌ 最後應該是空的"
    print("✅ 混合操作正確")


def test_empty_queue_operations():
    """測試空佇列的操作"""
    print("\n=== 測試空佇列操作 ===")

    queue = Queue()

    # 測試 1: 空佇列 dequeue
    print("\n1. 測試空佇列 dequeue...")
    try:
        queue.dequeue()
        print("❌ 空佇列 dequeue() 應該拋出異常")
        return False
    except IndexError as e:
        print(f"✅ 正確拋出 IndexError: {e}")
    except Exception as e:
        print(f"⚠️ 拋出了其他類型的異常: {type(e).__name__}: {e}")

    # 測試 2: 空佇列 front
    print("\n2. 測試空佇列 front...")
    try:
        queue.front()
        print("❌ 空佇列 front() 應該拋出異常")
        return False
    except IndexError as e:
        print(f"✅ 正確拋出 IndexError: {e}")
    except Exception as e:
        print(f"⚠️ 拋出了其他類型的異常: {type(e).__name__}: {e}")

    # 測試 3: 出隊到空後再操作
    print("\n3. 測試出隊到空後再操作...")
    queue.enqueue(1)
    queue.dequeue()

    try:
        queue.dequeue()
        print("❌ 空佇列 dequeue() 應該拋出異常")
        return False
    except IndexError as e:
        print(f"✅ 正確拋出 IndexError: {e}")

    return True


def test_different_data_types():
    """測試不同數據類型的 FIFO"""
    print("\n=== 測試不同數據類型的 FIFO ===")

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

    # 驗證出隊順序與入隊順序相同
    for expected_data in test_data:
        dequeued = queue.dequeue()
        assert dequeued == expected_data, f"❌ 應該出隊 {expected_data}，實際是 {dequeued}"

    print("✅ 不同數據類型的 FIFO 正確")


def test_unimplemented_methods():
    """確認其他方法還沒實作"""
    print("\n=== 確認未實作方法 ===")

    queue = Queue()
    queue.enqueue(1)

    # 測試還沒實作的方法
    unimplemented_tests = [
        ("clear", lambda: queue.clear()),
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
    """執行所有階段3測試"""
    print("🚀 開始階段3測試：出隊操作")
    print("測試範圍：dequeue(), front()")

    try:
        # 執行各項測試
        test_dequeue_functionality()
        test_front_functionality()
        test_fifo_behavior()
        test_mixed_operations()
        test_empty_queue_operations()
        test_different_data_types()
        test_unimplemented_methods()

        print("\n" + "="*50)
        print("🎉 階段3測試全部通過！")
        print("✅ 出隊操作 (dequeue, front) 實作正確")
        print("✅ FIFO 行為完全正確")
        print("✅ 錯誤處理正確")
        print("\n📝 下一步：進行完整 FIFO 行為驗證")
        print("   然後運行 python3 test_stage4.py")

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
