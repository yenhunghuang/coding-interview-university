#!/usr/bin/env python3
"""
階段2測試：基本操作 - push 和 peek/top 方法

這個階段測試：
- push() 方法：推入元素到堆疊頂部
- peek() 和 top() 方法：查看堆疊頂部元素但不移除
- 驗證 LIFO (後進先出) 的基本特性
- 確認 size() 的變化

運行方式：python3 test_stage2.py

實作指引：
在 stack.py 中新增以下方法：
    def push(self, item)      # 推入元素
    def peek(self) -> any     # 查看頂部元素
    def top(self) -> any      # peek() 的別名
"""

import sys
sys.path.append('.')

exec(open('stack.py').read())

def test_push_functionality():
    """測試 push 功能"""
    print("=== 測試 push 功能 ===")

    # 測試 1: 推入單個元素
    print("\n1. 測試推入單個元素...")
    stack = Stack()

    stack.push(42)
    assert stack.size() == 1, f"❌ push 後 size() 應該是 1，實際是 {stack.size()}"
    assert stack.is_empty() == False, f"❌ push 後 is_empty() 應該是 False，實際是 {stack.is_empty()}"
    print("✅ 推入單個元素正確")

    # 測試 2: 推入多個元素
    print("\n2. 測試推入多個元素...")
    stack.push("hello")
    stack.push([1, 2, 3])
    stack.push({"key": "value"})

    assert stack.size() == 4, f"❌ 推入4個元素後 size() 應該是 4，實際是 {stack.size()}"
    print("✅ 推入多個元素正確")

    # 測試 3: 推入 None 值
    print("\n3. 測試推入 None 值...")
    stack.push(None)
    assert stack.size() == 5, f"❌ 推入 None 後 size() 應該是 5，實際是 {stack.size()}"
    print("✅ 推入 None 值正確")


def test_peek_functionality():
    """測試 peek 功能"""
    print("\n=== 測試 peek 功能 ===")

    # 測試 1: peek 基本功能
    print("\n1. 測試 peek 基本功能...")
    stack = Stack()
    stack.push("first")
    stack.push("second")
    stack.push("third")

    # peek 應該返回最後推入的元素
    peeked = stack.peek()
    assert peeked == "third", f"❌ peek() 應該返回 'third'，實際返回 {peeked}"

    # peek 不應該改變堆疊大小
    assert stack.size() == 3, f"❌ peek 後 size() 應該還是 3，實際是 {stack.size()}"
    print("✅ peek 基本功能正確")

    # 測試 2: 連續 peek
    print("\n2. 測試連續 peek...")
    first_peek = stack.peek()
    second_peek = stack.peek()

    assert first_peek == second_peek == "third", f"❌ 連續 peek() 應該返回相同值"
    assert stack.size() == 3, f"❌ 連續 peek 後 size() 應該還是 3，實際是 {stack.size()}"
    print("✅ 連續 peek 正確")


def test_top_functionality():
    """測試 top 功能（應該和 peek 相同）"""
    print("\n=== 測試 top 功能 ===")

    stack = Stack()
    stack.push(100)
    stack.push(200)

    # top 和 peek 應該返回相同值
    peek_result = stack.peek()
    top_result = stack.top()

    assert peek_result == top_result == 200, f"❌ peek() 和 top() 應該返回相同值 200"
    assert stack.size() == 2, f"❌ top 後 size() 應該還是 2，實際是 {stack.size()}"
    print("✅ top 功能正確")


def test_lifo_behavior():
    """測試 LIFO (後進先出) 行為"""
    print("\n=== 測試 LIFO 行為 ===")

    stack = Stack()

    # 按順序推入
    items = ["first", "second", "third", "fourth"]
    for item in items:
        stack.push(item)

    # peek 應該看到最後推入的元素
    assert stack.peek() == "fourth", f"❌ 最後推入 'fourth'，peek() 應該看到它"

    # 繼續推入更多元素
    stack.push("fifth")
    assert stack.peek() == "fifth", f"❌ 最新推入 'fifth'，peek() 應該看到它"
    print("✅ LIFO 行為正確")


def test_empty_stack_peek():
    """測試空堆疊的 peek 操作"""
    print("\n=== 測試空堆疊 peek 操作 ===")

    stack = Stack()

    # 測試 1: 空堆疊 peek
    print("\n1. 測試空堆疊 peek...")
    try:
        stack.peek()
        print("❌ 空堆疊 peek() 應該拋出異常")
        return False
    except IndexError as e:
        print(f"✅ 正確拋出 IndexError: {e}")
    except Exception as e:
        print(f"⚠️ 拋出了其他類型的異常: {type(e).__name__}: {e}")

    # 測試 2: 空堆疊 top
    print("\n2. 測試空堆疊 top...")
    try:
        stack.top()
        print("❌ 空堆疊 top() 應該拋出異常")
        return False
    except IndexError as e:
        print(f"✅ 正確拋出 IndexError: {e}")
    except Exception as e:
        print(f"⚠️ 拋出了其他類型的異常: {type(e).__name__}: {e}")

    return True


def test_different_data_types():
    """測試不同數據類型"""
    print("\n=== 測試不同數據類型 ===")

    stack = Stack()

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
        stack.push(data)

    # 最後推入的應該是 None
    assert stack.peek() is None, f"❌ 最後推入 None，peek() 應該返回 None"
    assert stack.size() == len(test_data), f"❌ 推入 {len(test_data)} 個元素，size() 應該是 {len(test_data)}"
    print("✅ 不同數據類型處理正確")


def test_unimplemented_methods():
    """確認其他方法還沒實作"""
    print("\n=== 確認未實作方法 ===")

    stack = Stack()
    stack.push(1)  # 確保堆疊不為空

    # 測試還沒實作的方法
    unimplemented_tests = [
        ("pop", lambda: stack.pop()),
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
    print("🚀 開始階段2測試：基本操作")
    print("測試範圍：push(), peek(), top()")

    try:
        # 執行各項測試
        test_push_functionality()
        test_peek_functionality()
        test_top_functionality()
        test_lifo_behavior()
        test_empty_stack_peek()
        test_different_data_types()
        test_unimplemented_methods()

        print("\n" + "="*50)
        print("🎉 階段2測試全部通過！")
        print("✅ 基本操作 (push, peek, top) 實作正確")
        print("✅ LIFO 行為正確實現")
        print("\n📝 下一步：實作 pop() 方法")
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