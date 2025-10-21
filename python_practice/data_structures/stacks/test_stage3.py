#!/usr/bin/env python3
"""
階段3測試：移除操作 - pop 方法

這個階段測試：
- pop() 方法：移除並返回堆疊頂部元素
- 完整的 LIFO (後進先出) 行為驗證
- 空堆疊的 pop 錯誤處理
- push 和 pop 的組合操作

運行方式：python3 test_stage3.py

實作指引：
在 stack.py 中新增以下方法：
    def pop(self) -> any      # 移除並返回頂部元素
"""

import sys
sys.path.append('.')

exec(open('stack.py').read())

def test_pop_basic_functionality():
    """測試 pop 基本功能"""
    print("=== 測試 pop 基本功能 ===")

    # 測試 1: 單個元素的 pop
    print("\n1. 測試單個元素的 pop...")
    stack = Stack()
    stack.push(42)

    popped = stack.pop()
    assert popped == 42, f"❌ pop() 應該返回 42，實際返回 {popped}"
    assert stack.size() == 0, f"❌ pop 後 size() 應該是 0，實際是 {stack.size()}"
    assert stack.is_empty() == True, f"❌ pop 後 is_empty() 應該是 True"
    print("✅ 單個元素 pop 正確")

    # 測試 2: 多個元素的 pop
    print("\n2. 測試多個元素的 pop...")
    stack.push("first")
    stack.push("second")
    stack.push("third")

    # 按 LIFO 順序 pop
    third = stack.pop()
    assert third == "third", f"❌ 第一次 pop() 應該返回 'third'，實際返回 {third}"
    assert stack.size() == 2, f"❌ 第一次 pop 後 size() 應該是 2，實際是 {stack.size()}"

    second = stack.pop()
    assert second == "second", f"❌ 第二次 pop() 應該返回 'second'，實際返回 {second}"
    assert stack.size() == 1, f"❌ 第二次 pop 後 size() 應該是 1，實際是 {stack.size()}"

    first = stack.pop()
    assert first == "first", f"❌ 第三次 pop() 應該返回 'first'，實際返回 {first}"
    assert stack.size() == 0, f"❌ 第三次 pop 後 size() 應該是 0，實際是 {stack.size()}"
    assert stack.is_empty() == True, f"❌ 全部 pop 後應該為空"
    print("✅ 多個元素 pop 正確")


def test_lifo_behavior_complete():
    """測試完整的 LIFO 行為"""
    print("\n=== 測試完整 LIFO 行為 ===")

    stack = Stack()

    # 推入一系列元素
    items = [1, "two", [3], {"four": 4}, None, True, 3.14]

    for item in items:
        stack.push(item)

    # 應該以相反順序 pop 出來
    for expected_item in reversed(items):
        popped_item = stack.pop()
        assert popped_item == expected_item, f"❌ pop() 應該返回 {expected_item}，實際返回 {popped_item}"

    assert stack.is_empty(), f"❌ 全部 pop 後堆疊應該為空"
    print("✅ 完整 LIFO 行為正確")


def test_empty_stack_pop():
    """測試空堆疊的 pop 操作"""
    print("\n=== 測試空堆疊 pop 操作 ===")

    # 測試 1: 空堆疊 pop
    print("\n1. 測試空堆疊 pop...")
    stack = Stack()

    try:
        stack.pop()
        print("❌ 空堆疊 pop() 應該拋出異常")
        return False
    except IndexError as e:
        print(f"✅ 正確拋出 IndexError: {e}")
    except Exception as e:
        print(f"⚠️ 拋出了其他類型的異常: {type(e).__name__}: {e}")

    # 測試 2: pop 到空後再 pop
    print("\n2. 測試 pop 到空後再 pop...")
    stack.push("test")
    stack.pop()  # 現在堆疊應該為空

    try:
        stack.pop()
        print("❌ 再次 pop() 應該拋出異常")
        return False
    except IndexError as e:
        print(f"✅ 正確拋出 IndexError: {e}")
    except Exception as e:
        print(f"⚠️ 拋出了其他類型的異常: {type(e).__name__}: {e}")

    return True


def test_pop_and_peek_consistency():
    """測試 pop 和 peek 的一致性"""
    print("\n=== 測試 pop 和 peek 一致性 ===")

    stack = Stack()
    stack.push("alpha")
    stack.push("beta")
    stack.push("gamma")

    # peek 應該看到即將被 pop 的元素
    peeked = stack.peek()
    popped = stack.pop()
    assert peeked == popped, f"❌ peek() 和 pop() 應該返回相同值，peek: {peeked}, pop: {popped}"

    # 再次測試
    peeked2 = stack.peek()
    popped2 = stack.pop()
    assert peeked2 == popped2, f"❌ 第二次 peek() 和 pop() 應該返回相同值"

    print("✅ pop 和 peek 一致性正確")


def test_mixed_operations():
    """測試混合操作序列"""
    print("\n=== 測試混合操作序列 ===")

    stack = Stack()

    # 複雜的操作序列
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.peek() == 1

    stack.push(3)
    stack.push(4)
    assert stack.size() == 3  # 1, 3, 4

    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 1
    assert stack.is_empty()

    # 空後再操作
    stack.push("restart")
    assert stack.peek() == "restart"
    assert stack.pop() == "restart"

    print("✅ 混合操作序列正確")


def test_pop_different_data_types():
    """測試 pop 不同數據類型"""
    print("\n=== 測試 pop 不同數據類型 ===")

    stack = Stack()

    # 推入不同類型
    test_data = [
        None,
        False,
        0,
        "",
        [],
        {},
        3.14,
        "hello",
        [1, 2, 3],
        {"key": "value"}
    ]

    for data in test_data:
        stack.push(data)

    # 以相反順序 pop 並驗證
    for expected in reversed(test_data):
        popped = stack.pop()
        if expected != expected:  # NaN 檢查
            assert popped != popped, f"❌ 應該 pop NaN"
        else:
            assert popped == expected, f"❌ 應該 pop {expected}，實際 pop {popped}"

    print("✅ 不同數據類型 pop 正確")


def test_stack_state_after_operations():
    """測試操作後堆疊狀態"""
    print("\n=== 測試操作後堆疊狀態 ===")

    stack = Stack()

    # 初始狀態
    assert stack.is_empty()
    assert stack.size() == 0

    # 推入一個元素
    stack.push("test")
    assert not stack.is_empty()
    assert stack.size() == 1

    # pop 後狀態
    stack.pop()
    assert stack.is_empty()
    assert stack.size() == 0

    # 重複操作
    for i in range(3):
        stack.push(f"item_{i}")

    assert stack.size() == 3
    assert not stack.is_empty()

    for i in range(3):
        stack.pop()

    assert stack.size() == 0
    assert stack.is_empty()

    print("✅ 操作後堆疊狀態正確")


def main():
    """執行所有階段3測試"""
    print("🚀 開始階段3測試：移除操作")
    print("測試範圍：pop()")

    try:
        # 執行各項測試
        test_pop_basic_functionality()
        test_lifo_behavior_complete()
        test_empty_stack_pop()
        test_pop_and_peek_consistency()
        test_mixed_operations()
        test_pop_different_data_types()
        test_stack_state_after_operations()

        print("\n" + "="*50)
        print("🎉 階段3測試全部通過！")
        print("✅ 移除操作 (pop) 實作正確")
        print("✅ 完整 LIFO 行為驗證通過")
        print("✅ 錯誤處理正確")
        print("\n📝 下一步：實作容量限制和 is_full() 方法")
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