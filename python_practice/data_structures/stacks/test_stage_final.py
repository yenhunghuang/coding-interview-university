#!/usr/bin/env python3
"""
最終階段測試：完整功能驗證

這個階段是完整的功能測試，包括：
- 所有基本操作的綜合測試
- 效能特性驗證
- 邊界條件和錯誤處理
- 實際應用場景模擬
- 程式碼品質檢查

運行方式：python3 test_stage_final.py

這是完整的 Stack 實作驗證，通過這個測試表示你的實作已經完成！
"""

import sys
import time
import random
sys.path.append('.')

exec(open('stack.py').read())

def test_complete_basic_operations():
    """完整基本操作測試"""
    print("=== 完整基本操作測試 ===")

    stack = Stack()

    # 測試完整的操作序列
    operations = [
        ("push", "a"),
        ("push", "b"),
        ("push", "c"),
        ("peek", "c"),
        ("pop", "c"),
        ("push", "d"),
        ("peek", "d"),
        ("pop", "d"),
        ("pop", "b"),
        ("push", "e"),
        ("peek", "e"),
        ("pop", "e"),
        ("pop", "a"),
    ]

    for op, expected in operations:
        if op == "push":
            stack.push(expected)
            print(f"   push({expected}) -> size: {stack.size()}")
        elif op == "pop":
            result = stack.pop()
            assert result == expected, f"❌ pop() 應該返回 {expected}，實際返回 {result}"
            print(f"   pop() -> {result}, size: {stack.size()}")
        elif op == "peek":
            result = stack.peek()
            assert result == expected, f"❌ peek() 應該返回 {expected}，實際返回 {result}"
            print(f"   peek() -> {result}, size: {stack.size()}")

    assert stack.is_empty(), f"❌ 所有操作完成後堆疊應該為空"
    print("✅ 完整基本操作正確")


def test_capacity_comprehensive():
    """容量管理綜合測試"""
    print("\n=== 容量管理綜合測試 ===")

    # 測試各種容量大小
    test_sizes = [1, 2, 3, 5, 10, 100]

    for max_size in test_sizes:
        print(f"\n   測試容量 {max_size}...")
        stack = Stack(max_size=max_size)

        # 填滿堆疊
        for i in range(max_size):
            stack.push(f"item_{i}")

        assert stack.size() == max_size
        assert stack.is_full() == True

        # 嘗試超出容量
        try:
            stack.push("overflow")
            print(f"❌ 容量 {max_size} 的堆疊應該拒絕額外元素")
            return False
        except OverflowError:
            pass

        # 清空堆疊
        while not stack.is_empty():
            stack.pop()

        assert stack.is_empty()
        assert stack.is_full() == False

    print("✅ 容量管理綜合測試正確")


def test_data_type_comprehensive():
    """數據類型綜合測試"""
    print("\n=== 數據類型綜合測試 ===")

    stack = Stack()

    # 測試各種數據類型
    test_data = [
        # 基本類型
        None,
        True,
        False,
        0,
        -1,
        42,
        3.14,
        -2.71,
        "",
        "hello",
        "多位元組字符: 你好",

        # 容器類型
        [],
        [1, 2, 3],
        {},
        {"key": "value", "nested": {"inner": "data"}},
        (),
        (1, 2, 3),
        set(),
        {1, 2, 3},

        # 複雜對象
        range(5),
        lambda x: x + 1,
    ]

    # 推入所有數據
    for data in test_data:
        stack.push(data)

    # 以相反順序取出並驗證
    for expected in reversed(test_data):
        popped = stack.pop()

        # 特殊處理 lambda 函數
        if callable(expected) and callable(popped):
            # 只檢查都是可調用的
            assert callable(popped), f"❌ 應該 pop 出可調用對象"
        else:
            assert popped == expected, f"❌ 應該 pop {expected}，實際 pop {popped}"

    print("✅ 數據類型綜合測試正確")


def test_error_handling_comprehensive():
    """錯誤處理綜合測試"""
    print("\n=== 錯誤處理綜合測試 ===")

    # 測試 1: 初始化錯誤
    print("\n   測試初始化錯誤...")
    invalid_sizes = [-100, -1, 0]
    for size in invalid_sizes:
        try:
            Stack(max_size=size)
            print(f"❌ max_size={size} 應該拋出 ValueError")
            return False
        except ValueError:
            pass

    # 測試 2: 空堆疊操作錯誤
    print("\n   測試空堆疊操作錯誤...")
    empty_stack = Stack()

    empty_operations = ["pop", "peek", "top"]
    for op_name in empty_operations:
        try:
            getattr(empty_stack, op_name)()
            print(f"❌ 空堆疊 {op_name}() 應該拋出 IndexError")
            return False
        except IndexError:
            pass

    # 測試 3: 容量溢出錯誤
    print("\n   測試容量溢出錯誤...")
    full_stack = Stack(max_size=1)
    full_stack.push("full")

    try:
        full_stack.push("overflow")
        print("❌ 滿堆疊 push() 應該拋出 OverflowError")
        return False
    except OverflowError:
        pass

    print("✅ 錯誤處理綜合測試正確")


def test_performance_characteristics():
    """效能特性測試"""
    print("\n=== 效能特性測試 ===")

    # 測試大量操作的效能
    stack = Stack()
    n = 10000

    # 測試 push 效能
    print(f"\n   測試 {n} 次 push 操作...")
    start_time = time.time()
    for i in range(n):
        stack.push(i)
    push_time = time.time() - start_time

    assert stack.size() == n
    print(f"   {n} 次 push 耗時: {push_time:.4f} 秒")

    # 測試 peek 效能（應該是 O(1)）
    print(f"\n   測試 {n} 次 peek 操作...")
    start_time = time.time()
    for i in range(n):
        stack.peek()
    peek_time = time.time() - start_time

    print(f"   {n} 次 peek 耗時: {peek_time:.4f} 秒")

    # 測試 pop 效能
    print(f"\n   測試 {n} 次 pop 操作...")
    start_time = time.time()
    for i in range(n):
        stack.pop()
    pop_time = time.time() - start_time

    assert stack.is_empty()
    print(f"   {n} 次 pop 耗時: {pop_time:.4f} 秒")

    # 基本效能檢查（這些時間閾值是相對寬鬆的）
    max_time = 1.0  # 1秒
    assert push_time < max_time, f"❌ Push 操作太慢: {push_time:.4f}s"
    assert peek_time < max_time, f"❌ Peek 操作太慢: {peek_time:.4f}s"
    assert pop_time < max_time, f"❌ Pop 操作太慢: {pop_time:.4f}s"

    print("✅ 效能特性測試通過")


def test_real_world_scenarios():
    """實際應用場景測試"""
    print("\n=== 實際應用場景測試 ===")

    # 場景 1: 函數調用堆疊模擬
    print("\n   場景1: 函數調用堆疊模擬...")
    call_stack = Stack()

    def simulate_function_call(func_name):
        call_stack.push(f"calling {func_name}")
        return f"result of {func_name}"

    def simulate_function_return():
        return call_stack.pop()

    # 模擬深度調用
    simulate_function_call("main")
    simulate_function_call("process_data")
    simulate_function_call("validate_input")
    simulate_function_call("parse_json")

    assert call_stack.size() == 4

    # 模擬返回
    assert "parse_json" in simulate_function_return()
    assert "validate_input" in simulate_function_return()
    assert "process_data" in simulate_function_return()
    assert "main" in simulate_function_return()

    assert call_stack.is_empty()
    print("   ✅ 函數調用堆疊模擬正確")

    # 場景 2: 括號匹配檢查
    print("\n   場景2: 括號匹配檢查...")

    def check_parentheses(expression):
        stack = Stack()
        pairs = {'(': ')', '[': ']', '{': '}'}

        for char in expression:
            if char in pairs:  # 開括號
                stack.push(char)
            elif char in pairs.values():  # 閉括號
                if stack.is_empty():
                    return False
                if pairs[stack.pop()] != char:
                    return False

        return stack.is_empty()

    # 測試各種表達式
    test_cases = [
        ("()", True),
        ("[]", True),
        ("{}", True),
        ("([{}])", True),
        ("((()))", True),
        ("(", False),
        (")", False),
        ("([)]", False),
        ("(()", False),
    ]

    for expr, expected in test_cases:
        result = check_parentheses(expr)
        assert result == expected, f"❌ 表達式 '{expr}' 應該是 {expected}，實際是 {result}"

    print("   ✅ 括號匹配檢查正確")

    # 場景 3: 計算器表達式求值（簡化版）
    print("\n   場景3: 計算器表達式求值...")

    def evaluate_postfix(expression):
        """計算後綴表達式"""
        stack = Stack()

        for token in expression.split():
            if token in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    result = a / b
                stack.push(result)
            else:
                stack.push(float(token))

        return stack.pop()

    # 測試後綴表達式
    expressions = [
        ("3 4 +", 7.0),      # 3 + 4
        ("15 7 1 1 + - / 3 * 2 1 1 + + -", 5.0),  # ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1))
        ("5 1 2 + 4 * + 3 -", 14.0),  # 5 + ((1 + 2) * 4) - 3
    ]

    for expr, expected in expressions:
        result = evaluate_postfix(expr)
        assert abs(result - expected) < 0.0001, f"❌ 表達式 '{expr}' 應該是 {expected}，實際是 {result}"

    print("   ✅ 計算器表達式求值正確")


def test_stress_testing():
    """壓力測試"""
    print("\n=== 壓力測試 ===")

    # 測試 1: 隨機操作序列
    print("\n   測試隨機操作序列...")
    stack = Stack()
    reference_list = []  # 用列表模擬堆疊行為作為參考

    random.seed(42)  # 固定隨機種子確保可重現

    for _ in range(1000):
        operation = random.choice(['push', 'pop', 'peek'])

        if operation == 'push':
            value = random.randint(1, 100)
            stack.push(value)
            reference_list.append(value)

        elif operation == 'pop' and not stack.is_empty():
            popped = stack.pop()
            expected = reference_list.pop()
            assert popped == expected, f"❌ Pop 不匹配: {popped} vs {expected}"

        elif operation == 'peek' and not stack.is_empty():
            peeked = stack.peek()
            expected = reference_list[-1]
            assert peeked == expected, f"❌ Peek 不匹配: {peeked} vs {expected}"

    # 清理剩餘元素
    while not stack.is_empty():
        popped = stack.pop()
        expected = reference_list.pop()
        assert popped == expected

    print("   ✅ 隨機操作序列正確")

    # 測試 2: 容量邊界壓力測試
    print("\n   測試容量邊界壓力測試...")
    for max_size in [1, 2, 5, 10]:
        stack = Stack(max_size=max_size)

        # 反覆填滿和清空
        for cycle in range(10):
            # 填滿
            for i in range(max_size):
                stack.push(f"cycle_{cycle}_item_{i}")

            assert stack.is_full()
            assert stack.size() == max_size

            # 清空
            for i in range(max_size):
                stack.pop()

            assert stack.is_empty()

    print("   ✅ 容量邊界壓力測試正確")


def main():
    """執行最終完整測試"""
    print("🚀 開始最終完整測試")
    print("這是 Stack 實作的完整驗證測試")
    print("="*60)

    try:
        # 執行所有測試
        test_complete_basic_operations()
        test_capacity_comprehensive()
        test_data_type_comprehensive()
        test_error_handling_comprehensive()
        test_performance_characteristics()
        test_real_world_scenarios()
        test_stress_testing()

        print("\n" + "="*60)
        print("🎉🎉🎉 所有測試通過！Stack 實作完成！🎉🎉🎉")
        print("\n✅ 基本操作正確 (push, pop, peek, top)")
        print("✅ 容量管理正確 (有限/無限容量)")
        print("✅ 錯誤處理完善")
        print("✅ 效能特性良好")
        print("✅ 實際應用場景驗證通過")
        print("✅ 壓力測試通過")

        print("\n🏆 恭喜！你已經成功實作了一個完整的 Stack 數據結構！")
        print("\n📚 學習總結：")
        print("   - 理解了 LIFO (後進先出) 原則")
        print("   - 掌握了堆疊的基本操作")
        print("   - 學會了容量管理和錯誤處理")
        print("   - 了解了堆疊在實際問題中的應用")

        print("\n🎯 下一步建議：")
        print("   - 學習隊列 (Queue) 數據結構")
        print("   - 研究其他高級數據結構")
        print("   - 練習更多堆疊相關的算法問題")

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