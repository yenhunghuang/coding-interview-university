#!/usr/bin/env python3
"""
最終測試：完整集成測試和實際應用驗證

這個階段測試：
- 所有功能的綜合驗證
- 實際應用場景測試
- 效能測試
- 應用函數測試（hot_potato, generate_binary_numbers 等）

運行方式：python3 test_stage_final.py

實作指引：
確保所有 Queue 方法都已正確實作
選擇性實作應用函數（hot_potato, generate_binary_numbers, level_order_traversal）
"""

import sys
sys.path.append('.')

exec(open('queue.py').read())

def test_all_methods_comprehensive():
    """綜合測試所有方法"""
    print("=== 綜合測試所有方法 ===")

    # 創建有容量限制的佇列
    queue = Queue(max_size=10)

    # 初始狀態
    assert queue.is_empty() == True, "❌ 初始應該是空的"
    assert queue.size() == 0, "❌ 初始 size 應該是 0"
    assert queue.is_full() == False, "❌ 初始不應該是滿的"
    assert queue.max_size == 10, "❌ max_size 應該是 10"
    print("✅ 初始狀態正確")

    # 入隊操作
    print("\n測試入隊...")
    for i in range(10):
        queue.enqueue(i)
        assert queue.size() == i + 1, f"❌ 第 {i+1} 次入隊後 size 應該是 {i+1}"

    assert queue.is_full() == True, "❌ 填滿後應該是滿的"
    assert queue.is_empty() == False, "❌ 有元素時不應該是空的"
    print("✅ 入隊操作正確")

    # front 操作
    print("\n測試 front...")
    assert queue.front() == 0, "❌ front 應該返回 0"
    assert queue.size() == 10, "❌ front 不應該改變 size"
    print("✅ front 操作正確")

    # 出隊操作
    print("\n測試出隊...")
    for i in range(10):
        assert queue.front() == i, f"❌ front 應該返回 {i}"
        dequeued = queue.dequeue()
        assert dequeued == i, f"❌ dequeue 應該返回 {i}"
        assert queue.size() == 9 - i, f"❌ 第 {i+1} 次出隊後 size 應該是 {9-i}"

    assert queue.is_empty() == True, "❌ 全部出隊後應該是空的"
    print("✅ 出隊操作正確")

    # 字串表示
    print("\n測試字串表示...")
    str_repr = str(queue)
    assert "Queue" in str_repr, "❌ str 應該包含 'Queue'"
    repr_str = repr(queue)
    assert "Queue" in repr_str, "❌ repr 應該包含 'Queue'"
    print(f"✅ str: {str_repr}")
    print(f"✅ repr: {repr_str}")

    # 清空操作
    print("\n測試清空...")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.clear()
    assert queue.is_empty() == True, "❌ 清空後應該是空的"
    assert queue.size() == 0, "❌ 清空後 size 應該是 0"
    print("✅ 清空操作正確")

    print("\n🎉 所有方法綜合測試通過！")


def test_real_world_scenarios():
    """測試實際應用場景"""
    print("\n=== 測試實際應用場景 ===")

    # 場景 1: 打印機佇列
    print("\n場景 1: 打印機佇列模擬")
    printer_queue = Queue(max_size=5)

    print("  添加打印任務...")
    jobs = ["doc1.pdf", "photo.jpg", "report.docx", "slides.pptx"]
    for job in jobs:
        printer_queue.enqueue(job)
        print(f"    已加入佇列: {job}")

    print(f"  當前佇列: {printer_queue}")
    print(f"  待處理任務數: {printer_queue.size()}")

    print("  開始打印...")
    while not printer_queue.is_empty():
        current_job = printer_queue.dequeue()
        print(f"    正在打印: {current_job}")

    print("  ✅ 所有任務已完成")

    # 場景 2: 客服系統
    print("\n場景 2: 客服系統排隊")
    customer_queue = Queue()

    customers = [
        ("Alice", "技術支援"),
        ("Bob", "帳單問題"),
        ("Carol", "產品諮詢"),
        ("David", "退換貨"),
    ]

    print("  客戶加入隊列...")
    for name, issue in customers:
        customer_queue.enqueue((name, issue))
        print(f"    {name} 排隊中 - 問題: {issue}")

    print(f"\n  前方等待人數: {customer_queue.size()}")
    print(f"  下一位客戶: {customer_queue.front()[0]}")

    print("\n  開始服務...")
    served_count = 0
    while not customer_queue.is_empty():
        name, issue = customer_queue.dequeue()
        served_count += 1
        print(f"    服務第 {served_count} 位: {name} - {issue}")
        print(f"      剩餘等待: {customer_queue.size()} 人")

    print("  ✅ 所有客戶已服務完畢")

    # 場景 3: 消息佇列
    print("\n場景 3: 消息佇列處理")
    message_queue = Queue(max_size=10)

    print("  接收消息...")
    messages = [
        {"id": 1, "type": "email", "content": "Welcome!"},
        {"id": 2, "type": "sms", "content": "Verification code: 1234"},
        {"id": 3, "type": "push", "content": "New update available"},
    ]

    for msg in messages:
        message_queue.enqueue(msg)
        print(f"    收到消息 #{msg['id']}: {msg['type']}")

    print("\n  處理消息...")
    while not message_queue.is_empty():
        msg = message_queue.dequeue()
        print(f"    處理消息 #{msg['id']}: {msg['content']}")

    print("  ✅ 所有消息已處理")


def test_performance():
    """測試效能"""
    print("\n=== 測試效能 ===")

    import time

    # 大規模操作測試
    n = 10000
    queue = Queue()

    print(f"\n測試 {n} 次入隊操作...")
    start_time = time.time()
    for i in range(n):
        queue.enqueue(i)
    enqueue_time = time.time() - start_time
    print(f"  完成時間: {enqueue_time:.4f} 秒")
    print(f"  平均每次: {(enqueue_time/n)*1000000:.2f} 微秒")

    print(f"\n測試 {n} 次出隊操作...")
    start_time = time.time()
    for i in range(n):
        queue.dequeue()
    dequeue_time = time.time() - start_time
    print(f"  完成時間: {dequeue_time:.4f} 秒")
    print(f"  平均每次: {(dequeue_time/n)*1000000:.2f} 微秒")

    # 混合操作測試
    print(f"\n測試 {n} 次混合操作...")
    queue2 = Queue()
    start_time = time.time()
    for i in range(n):
        queue2.enqueue(i)
        if i % 2 == 0 and not queue2.is_empty():
            queue2.dequeue()
    mixed_time = time.time() - start_time
    print(f"  完成時間: {mixed_time:.4f} 秒")
    print(f"  平均每次: {(mixed_time/n)*1000000:.2f} 微秒")

    print("\n✅ 效能測試完成")


def test_hot_potato_if_implemented():
    """測試燙手山芋遊戲（如果已實作）"""
    print("\n=== 測試燙手山芋遊戲 ===")

    try:
        # 測試 1: 基本遊戲
        print("\n1. 測試基本遊戲...")
        names = ["Alice", "Bob", "Carol", "David", "Eve"]
        winner = hot_potato(names, 7)

        assert winner in names, f"❌ 獲勝者 {winner} 不在參與者名單中"
        print(f"  參與者: {names}")
        print(f"  傳遞次數: 7")
        print(f"  ✅ 獲勝者: {winner}")

        # 測試 2: 不同參數
        print("\n2. 測試不同參數...")
        names2 = ["A", "B", "C"]
        winner2 = hot_potato(names2, 5)
        assert winner2 in names2, f"❌ 獲勝者 {winner2} 不在參與者名單中"
        print(f"  ✅ 獲勝者: {winner2}")

        print("\n✅ 燙手山芋遊戲測試通過")

    except NotImplementedError:
        print("  ⚠️ hot_potato 函數尚未實作")
        print("  這是選擇性的進階練習")
    except Exception as e:
        print(f"  ❌ 測試失敗: {e}")


def test_binary_numbers_if_implemented():
    """測試二進位數字生成（如果已實作）"""
    print("\n=== 測試二進位數字生成 ===")

    try:
        # 測試 1: 生成 1-5
        print("\n1. 測試生成 1-5 的二進位...")
        result = generate_binary_numbers(5)
        expected = ['1', '10', '11', '100', '101']

        assert result == expected, f"❌ 預期 {expected}，實際 {result}"
        print(f"  ✅ 結果: {result}")

        # 測試 2: 生成 1-10
        print("\n2. 測試生成 1-10 的二進位...")
        result2 = generate_binary_numbers(10)
        expected2 = ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010']

        assert result2 == expected2, f"❌ 預期 {expected2}，實際 {result2}"
        print(f"  ✅ 結果: {result2}")

        # 測試 3: 邊界情況
        print("\n3. 測試邊界情況...")
        result3 = generate_binary_numbers(1)
        assert result3 == ['1'], f"❌ 生成 1 個應該是 ['1']"
        print(f"  ✅ 生成 1 個: {result3}")

        print("\n✅ 二進位數字生成測試通過")

    except NotImplementedError:
        print("  ⚠️ generate_binary_numbers 函數尚未實作")
        print("  這是選擇性的進階練習")
    except Exception as e:
        print(f"  ❌ 測試失敗: {e}")


def test_error_handling_comprehensive():
    """綜合錯誤處理測試"""
    print("\n=== 綜合錯誤處理測試 ===")

    # 測試所有可能的錯誤情況
    errors_caught = 0

    # 1. 無效初始化
    print("\n1. 測試無效初始化...")
    for invalid_size in [0, -1, -100]:
        try:
            Queue(max_size=invalid_size)
            print(f"  ❌ max_size={invalid_size} 應該拋出異常")
        except ValueError:
            errors_caught += 1
            print(f"  ✅ max_size={invalid_size} 正確拋出 ValueError")

    # 2. 空佇列操作
    print("\n2. 測試空佇列操作...")
    empty_queue = Queue()

    try:
        empty_queue.dequeue()
        print("  ❌ 空佇列 dequeue 應該拋出異常")
    except IndexError:
        errors_caught += 1
        print("  ✅ 空佇列 dequeue 正確拋出 IndexError")

    try:
        empty_queue.front()
        print("  ❌ 空佇列 front 應該拋出異常")
    except IndexError:
        errors_caught += 1
        print("  ✅ 空佇列 front 正確拋出 IndexError")

    # 3. 溢出
    print("\n3. 測試溢出...")
    full_queue = Queue(max_size=2)
    full_queue.enqueue(1)
    full_queue.enqueue(2)

    try:
        full_queue.enqueue(3)
        print("  ❌ 滿佇列 enqueue 應該拋出異常")
    except OverflowError:
        errors_caught += 1
        print("  ✅ 滿佇列 enqueue 正確拋出 OverflowError")

    print(f"\n✅ 捕獲 {errors_caught} 個預期錯誤")


def main():
    """執行所有最終測試"""
    print("=" * 60)
    print("🎯 開始最終綜合測試")
    print("=" * 60)

    try:
        # 核心功能測試
        test_all_methods_comprehensive()
        test_real_world_scenarios()
        test_error_handling_comprehensive()

        # 效能測試
        test_performance()

        # 應用函數測試（選擇性）
        print("\n" + "=" * 60)
        print("🌟 進階應用函數測試（選擇性）")
        print("=" * 60)
        test_hot_potato_if_implemented()
        test_binary_numbers_if_implemented()

        # 最終總結
        print("\n" + "=" * 60)
        print("🎊 恭喜！所有測試通過！")
        print("=" * 60)
        print("\n✅ Queue 數據結構實作完成")
        print("✅ 所有核心方法運作正常")
        print("✅ FIFO 行為正確無誤")
        print("✅ 錯誤處理完善")
        print("✅ 效能表現良好")
        print("✅ 實際應用場景驗證通過")

        print("\n📚 學習成果：")
        print("   ✓ 理解 FIFO (先進先出) 原則")
        print("   ✓ 掌握佇列的基本操作")
        print("   ✓ 了解容量管理和錯誤處理")
        print("   ✓ 能應用佇列解決實際問題")

        print("\n🚀 下一步建議：")
        print("   1. 實作進階應用函數（如果還沒完成）")
        print("   2. 嘗試用鏈表實作 Queue")
        print("   3. 實作 Circular Queue（循環佇列）")
        print("   4. 學習 Deque（雙端佇列）")
        print("   5. 使用 Queue 解決 LeetCode 問題")

        print("\n🎓 相關主題推薦：")
        print("   • Priority Queue（優先佇列）")
        print("   • Breadth-First Search（廣度優先搜尋）")
        print("   • Level-Order Traversal（層序遍歷）")
        print("   • Task Scheduling（任務調度）")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作並修正後重新測試")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
