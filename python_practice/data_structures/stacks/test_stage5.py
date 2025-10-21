#!/usr/bin/env python3
"""
階段5測試：輔助功能 - clear 和字串表示

這個階段測試：
- clear() 方法：清空堆疊
- __str__() 方法：字串表示
- __repr__() 方法：詳細表示（選擇性）
- 清空後的狀態恢復

運行方式：python3 test_stage5.py

實作指引：
在 stack.py 中新增以下方法：
    def clear(self)           # 清空堆疊
    def __str__(self) -> str  # 字串表示
    def __repr__(self) -> str # 詳細表示（選擇性）
"""

import sys
sys.path.append('.')

exec(open('stack.py').read())

def test_clear_functionality():
    """測試 clear 功能"""
    print("=== 測試 clear 功能 ===")

    # 測試 1: 清空有元素的堆疊
    print("\n1. 測試清空有元素的堆疊...")
    stack = Stack()

    # 推入一些元素
    for i in range(5):
        stack.push(f"item_{i}")

    assert stack.size() == 5, f"❌ 推入5個元素後 size() 應該是 5"
    assert stack.is_empty() == False, f"❌ 有元素時 is_empty() 應該是 False"

    # 清空
    stack.clear()

    assert stack.size() == 0, f"❌ clear() 後 size() 應該是 0，實際是 {stack.size()}"
    assert stack.is_empty() == True, f"❌ clear() 後 is_empty() 應該是 True"
    print("✅ 清空有元素的堆疊正確")

    # 測試 2: 清空空堆疊
    print("\n2. 測試清空空堆疊...")
    empty_stack = Stack()
    empty_stack.clear()

    assert empty_stack.size() == 0, f"❌ 清空空堆疊後 size() 應該是 0"
    assert empty_stack.is_empty() == True, f"❌ 清空空堆疊後 is_empty() 應該是 True"
    print("✅ 清空空堆疊正確")

    # 測試 3: 有容量限制的堆疊清空
    print("\n3. 測試有容量限制的堆疊清空...")
    limited_stack = Stack(max_size=3)

    # 填滿堆疊
    limited_stack.push("a")
    limited_stack.push("b")
    limited_stack.push("c")
    assert limited_stack.is_full() == True

    # 清空
    limited_stack.clear()

    assert limited_stack.size() == 0
    assert limited_stack.is_empty() == True
    assert limited_stack.is_full() == False
    print("✅ 有容量限制的堆疊清空正確")


def test_clear_and_reuse():
    """測試清空後重新使用"""
    print("\n=== 測試清空後重新使用 ===")

    stack = Stack()

    # 第一輪使用
    stack.push("first_round_1")
    stack.push("first_round_2")
    assert stack.size() == 2

    # 清空
    stack.clear()

    # 第二輪使用
    stack.push("second_round_1")
    stack.push("second_round_2")
    stack.push("second_round_3")

    assert stack.size() == 3
    assert stack.peek() == "second_round_3"

    # 驗證可以正常操作
    popped = stack.pop()
    assert popped == "second_round_3"
    assert stack.size() == 2

    print("✅ 清空後重新使用正確")


def test_string_representation():
    """測試字串表示"""
    print("\n=== 測試字串表示 ===")

    # 測試 1: 空堆疊的字串表示
    print("\n1. 測試空堆疊的字串表示...")
    empty_stack = Stack()

    str_repr = str(empty_stack)
    # 空堆疊應該有某種表示方式
    assert isinstance(str_repr, str), f"❌ str() 應該返回字串"
    assert len(str_repr) > 0, f"❌ str() 不應該返回空字串"
    print(f"✅ 空堆疊字串表示: {str_repr}")

    # 測試 2: 有元素的堆疊字串表示
    print("\n2. 測試有元素的堆疊字串表示...")
    stack = Stack()
    stack.push("bottom")
    stack.push("middle")
    stack.push("top")

    str_repr = str(stack)
    assert isinstance(str_repr, str), f"❌ str() 應該返回字串"

    # 字串表示應該包含元素信息（具體格式可以很靈活）
    # 這裡只檢查是否為非空字串
    assert len(str_repr) > 0, f"❌ 有元素時 str() 不應該返回空字串"
    print(f"✅ 有元素堆疊字串表示: {str_repr}")

    # 測試 3: 不同數據類型的字串表示
    print("\n3. 測試不同數據類型的字串表示...")
    mixed_stack = Stack()
    mixed_stack.push(42)
    mixed_stack.push("hello")
    mixed_stack.push([1, 2, 3])
    mixed_stack.push(None)

    str_repr = str(mixed_stack)
    assert isinstance(str_repr, str), f"❌ 混合類型 str() 應該返回字串"
    assert len(str_repr) > 0, f"❌ 混合類型 str() 不應該返回空字串"
    print(f"✅ 混合類型堆疊字串表示: {str_repr}")


def test_repr_if_implemented():
    """測試 repr 表示（如果實作）"""
    print("\n=== 測試 repr 表示（如果實作）===")

    stack = Stack()
    stack.push(1)
    stack.push(2)

    # 檢查是否實作了 __repr__
    try:
        repr_str = repr(stack)
        assert isinstance(repr_str, str), f"❌ repr() 應該返回字串"
        print(f"✅ repr 表示: {repr_str}")

        # 可選：檢查 repr 是否更詳細
        str_str = str(stack)
        print(f"   str 表示:  {str_str}")

    except Exception as e:
        print(f"⚠️ repr() 可能未實作或有問題: {e}")


def test_string_after_operations():
    """測試各種操作後的字串表示"""
    print("\n=== 測試各種操作後的字串表示 ===")

    stack = Stack(max_size=3)

    # 測試 1: 推入過程中的字串表示
    print("\n1. 測試推入過程中的字串表示...")

    print(f"   空堆疊: {str(stack)}")

    stack.push("first")
    print(f"   推入1個: {str(stack)}")

    stack.push("second")
    print(f"   推入2個: {str(stack)}")

    stack.push("third")
    print(f"   推入3個: {str(stack)}")

    # 測試 2: pop 過程中的字串表示
    print("\n2. 測試 pop 過程中的字串表示...")

    stack.pop()
    print(f"   pop 1個: {str(stack)}")

    stack.pop()
    print(f"   pop 2個: {str(stack)}")

    stack.pop()
    print(f"   pop 3個: {str(stack)}")

    # 測試 3: 清空後的字串表示
    print("\n3. 測試清空後的字串表示...")
    stack.push("test")
    stack.clear()
    print(f"   清空後: {str(stack)}")

    print("✅ 各種操作後的字串表示都正常")


def test_clear_edge_cases():
    """測試清空的邊界情況"""
    print("\n=== 測試清空的邊界情況 ===")

    # 測試 1: 多次清空
    print("\n1. 測試多次清空...")
    stack = Stack()
    stack.push("test")

    # 第一次清空
    stack.clear()
    assert stack.is_empty()

    # 再次清空
    stack.clear()
    assert stack.is_empty()

    # 第三次清空
    stack.clear()
    assert stack.is_empty()
    print("✅ 多次清空正確")

    # 測試 2: 清空後錯誤操作
    print("\n2. 測試清空後錯誤操作...")
    stack.clear()

    # 嘗試從空堆疊 pop
    try:
        stack.pop()
        print("❌ 清空後 pop() 應該拋出異常")
        return False
    except IndexError:
        print("✅ 清空後 pop() 正確拋出異常")

    # 嘗試從空堆疊 peek
    try:
        stack.peek()
        print("❌ 清空後 peek() 應該拋出異常")
        return False
    except IndexError:
        print("✅ 清空後 peek() 正確拋出異常")

    return True


def main():
    """執行所有階段5測試"""
    print("🚀 開始階段5測試：輔助功能")
    print("測試範圍：clear(), __str__(), __repr__()")

    try:
        # 執行各項測試
        test_clear_functionality()
        test_clear_and_reuse()
        test_string_representation()
        test_repr_if_implemented()
        test_string_after_operations()
        test_clear_edge_cases()

        print("\n" + "="*50)
        print("🎉 階段5測試全部通過！")
        print("✅ 輔助功能 (clear, 字串表示) 實作正確")
        print("✅ 清空功能完整且可重複使用")
        print("\n📝 下一步：實作進階功能（複製、相等比較等）")
        print("   然後運行 python3 test_stage6.py")

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