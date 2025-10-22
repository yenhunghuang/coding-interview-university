#!/usr/bin/env python3
"""
階段1測試：基礎結構測試 - Queue 初始化和基本查詢方法

這個階段測試最基本的結構建立，包括：
- Queue 類別的初始化
- size() 和 is_empty() 基本方法
- 容量限制的初始化（如果有的話）
- 錯誤處理驗證

運行方式：python3 test_stage1.py

實作指引：
你需要創建 queue.py 文件，包含 Queue 類別

預期方法簽名：
class Queue:
    def __init__(self, max_size=None)
    def size(self) -> int
    def is_empty(self) -> bool
"""

import sys
sys.path.append('.')

exec(open('queue.py').read())

def test_basic_initialization():
    """測試基本初始化"""
    print("=== 測試基本初始化 ===")

    # 測試 1: 預設初始化（無容量限制）
    print("\n1. 測試預設初始化...")
    queue = Queue()

    assert queue.size() == 0, f"❌ size() 應該是 0，實際是 {queue.size()}"
    assert queue.is_empty() == True, f"❌ is_empty() 應該是 True，實際是 {queue.is_empty()}"
    print("✅ 預設初始化正確")

    # 測試 2: 有容量限制的初始化
    print("\n2. 測試有容量限制的初始化...")
    queue_limited = Queue(max_size=10)

    assert queue_limited.size() == 0, f"❌ size() 應該是 0，實際是 {queue_limited.size()}"
    assert queue_limited.is_empty() == True, f"❌ is_empty() 應該是 True，實際是 {queue_limited.is_empty()}"
    print("✅ 有容量限制的初始化正確")

    # 測試 3: 最小容量限制
    print("\n3. 測試最小容量限制...")
    queue_min = Queue(max_size=1)

    assert queue_min.size() == 0, f"❌ size() 應該是 0，實際是 {queue_min.size()}"
    assert queue_min.is_empty() == True, f"❌ is_empty() 應該是 True，實際是 {queue_min.is_empty()}"
    print("✅ 最小容量限制初始化正確")


def test_error_handling():
    """測試錯誤處理"""
    print("\n=== 測試錯誤處理 ===")

    # 測試 1: 無效容量 0
    print("\n1. 測試無效容量 0...")
    try:
        queue = Queue(max_size=0)
        print("❌ 應該拋出 ValueError")
        return False
    except ValueError as e:
        print(f"✅ 正確拋出 ValueError: {e}")

    # 測試 2: 無效容量 -1
    print("\n2. 測試無效容量 -1...")
    try:
        queue = Queue(max_size=-1)
        print("❌ 應該拋出 ValueError")
        return False
    except ValueError as e:
        print(f"✅ 正確拋出 ValueError: {e}")

    return True


def test_unimplemented_methods():
    """確認其他方法還沒實作"""
    print("\n=== 確認未實作方法 ===")

    queue = Queue()

    # 測試幾個還沒實作的方法
    unimplemented_tests = [
        ("enqueue", lambda: queue.enqueue(1)),
        ("dequeue", lambda: queue.dequeue()),
        ("front", lambda: queue.front()),
        ("is_full", lambda: queue.is_full()),
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
    """執行所有階段1測試"""
    print("🚀 開始階段1測試：基礎結構")
    print("測試範圍：__init__(), size(), is_empty()")

    try:
        # 執行各項測試
        test_basic_initialization()
        test_error_handling()
        test_unimplemented_methods()

        print("\n" + "="*50)
        print("🎉 階段1測試全部通過！")
        print("✅ 基礎結構 (初始化, size, is_empty) 實作正確")
        print("\n📝 下一步：實作 enqueue() 和 is_full() 方法")
        print("   然後運行 python3 test_stage2.py")

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
