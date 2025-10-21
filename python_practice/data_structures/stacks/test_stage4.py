#!/usr/bin/env python3
"""
階段4測試：容量管理 - 有限容量堆疊

這個階段測試：
- 有容量限制的堆疊行為
- is_full() 方法
- 堆疊溢出處理
- 容量達到上限時的 push 行為

運行方式：python3 test_stage4.py

實作指引：
在 stack.py 中新增或完善以下方法：
    def is_full(self) -> bool     # 檢查是否已滿
    確保 push() 方法檢查容量限制
"""

import sys
sys.path.append('.')

exec(open('stack.py').read())

def test_is_full_functionality():
    """測試 is_full 功能"""
    print("=== 測試 is_full 功能 ===")

    # 測試 1: 無容量限制的堆疊
    print("\n1. 測試無容量限制的堆疊...")
    unlimited_stack = Stack()

    assert unlimited_stack.is_full() == False, f"❌ 無容量限制的堆疊 is_full() 應該始終是 False"

    # 推入一些元素後仍然不應該滿
    for i in range(100):
        unlimited_stack.push(i)

    assert unlimited_stack.is_full() == False, f"❌ 無容量限制的堆疊推入100個元素後 is_full() 仍應該是 False"
    print("✅ 無容量限制堆疊的 is_full 正確")

    # 測試 2: 有容量限制的空堆疊
    print("\n2. 測試有容量限制的空堆疊...")
    limited_stack = Stack(max_size=3)

    assert limited_stack.is_full() == False, f"❌ 空的有限堆疊 is_full() 應該是 False"
    print("✅ 有限堆疊空時 is_full 正確")

    # 測試 3: 逐步填滿有限堆疊
    print("\n3. 測試逐步填滿有限堆疊...")
    limited_stack.push("first")
    assert limited_stack.is_full() == False, f"❌ 推入1個元素後 is_full() 應該是 False"

    limited_stack.push("second")
    assert limited_stack.is_full() == False, f"❌ 推入2個元素後 is_full() 應該是 False"

    limited_stack.push("third")
    assert limited_stack.is_full() == True, f"❌ 推入3個元素後 is_full() 應該是 True"
    print("✅ 逐步填滿過程中 is_full 正確")


def test_capacity_enforcement():
    """測試容量限制執行"""
    print("\n=== 測試容量限制執行 ===")

    # 測試 1: 基本容量限制
    print("\n1. 測試基本容量限制...")
    stack = Stack(max_size=2)

    # 正常推入
    stack.push("first")
    stack.push("second")
    assert stack.size() == 2
    assert stack.is_full() == True

    # 嘗試超出容量
    try:
        stack.push("third")
        print("❌ 超出容量的 push() 應該拋出異常")
        return False
    except OverflowError as e:
        print(f"✅ 正確拋出 OverflowError: {e}")
    except Exception as e:
        print(f"⚠️ 拋出了其他類型的異常: {type(e).__name__}: {e}")

    # 確認堆疊狀態沒有改變
    assert stack.size() == 2, f"❌ 失敗的 push 不應該改變堆疊大小"
    assert stack.peek() == "second", f"❌ 失敗的 push 不應該改變堆疊內容"
    print("✅ 基本容量限制正確")

    # 測試 2: 最小容量 (1)
    print("\n2. 測試最小容量...")
    min_stack = Stack(max_size=1)

    min_stack.push("only")
    assert min_stack.is_full() == True

    try:
        min_stack.push("overflow")
        print("❌ 容量為1的堆疊推入第二個元素應該拋出異常")
        return False
    except OverflowError as e:
        print(f"✅ 正確拋出 OverflowError: {e}")

    print("✅ 最小容量限制正確")


def test_full_stack_operations():
    """測試滿堆疊的其他操作"""
    print("\n=== 測試滿堆疊的其他操作 ===")

    stack = Stack(max_size=3)

    # 填滿堆疊
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.is_full() == True

    # 測試 1: 滿堆疊的 peek 操作
    print("\n1. 測試滿堆疊的 peek 操作...")
    peeked = stack.peek()
    assert peeked == 3, f"❌ 滿堆疊 peek() 應該返回 3，實際返回 {peeked}"
    assert stack.is_full() == True, f"❌ peek 後堆疊應該仍然是滿的"
    print("✅ 滿堆疊 peek 操作正確")

    # 測試 2: 滿堆疊的 pop 操作
    print("\n2. 測試滿堆疊的 pop 操作...")
    popped = stack.pop()
    assert popped == 3, f"❌ pop() 應該返回 3，實際返回 {popped}"
    assert stack.is_full() == False, f"❌ pop 後堆疊應該不再是滿的"
    assert stack.size() == 2, f"❌ pop 後 size() 應該是 2，實際是 {stack.size()}"
    print("✅ 滿堆疊 pop 操作正確")

    # 測試 3: pop 後可以再次 push
    print("\n3. 測試 pop 後可以再次 push...")
    stack.push("new")
    assert stack.is_full() == True, f"❌ 重新推入後應該再次是滿的"
    assert stack.peek() == "new", f"❌ 新推入的元素應該在頂部"
    print("✅ pop 後再次 push 正確")


def test_capacity_edge_cases():
    """測試容量邊界情況"""
    print("\n=== 測試容量邊界情況 ===")

    # 測試 1: 反覆填滿和清空
    print("\n1. 測試反覆填滿和清空...")
    stack = Stack(max_size=2)

    for cycle in range(3):
        # 填滿
        stack.push(f"cycle_{cycle}_1")
        stack.push(f"cycle_{cycle}_2")
        assert stack.is_full() == True

        # 清空
        stack.pop()
        stack.pop()
        assert stack.is_empty() == True
        assert stack.is_full() == False

    print("✅ 反覆填滿和清空正確")

    # 測試 2: 部分填充狀態
    print("\n2. 測試部分填充狀態...")
    stack = Stack(max_size=5)

    for i in range(3):
        stack.push(i)

    assert stack.size() == 3
    assert stack.is_full() == False
    assert stack.is_empty() == False

    # 還可以推入更多
    stack.push("more")
    assert stack.is_full() == False

    stack.push("last")
    assert stack.is_full() == True

    print("✅ 部分填充狀態正確")


def test_mixed_capacity_operations():
    """測試混合容量操作"""
    print("\n=== 測試混合容量操作 ===")

    stack = Stack(max_size=4)

    # 複雜操作序列
    stack.push("a")
    stack.push("b")
    assert stack.is_full() == False

    stack.pop()
    stack.push("c")
    stack.push("d")
    stack.push("e")
    assert stack.is_full() == True

    # 嘗試超出容量
    try:
        stack.push("overflow")
        print("❌ 應該拋出 OverflowError")
        return False
    except OverflowError:
        pass

    # 驗證最終狀態
    assert stack.size() == 4
    assert stack.peek() == "e"

    # 清空並重新開始
    while not stack.is_empty():
        stack.pop()

    assert stack.is_full() == False
    assert stack.is_empty() == True

    print("✅ 混合容量操作正確")


def test_capacity_with_different_data_types():
    """測試容量限制與不同數據類型"""
    print("\n=== 測試容量限制與不同數據類型 ===")

    stack = Stack(max_size=3)

    # 推入不同類型的數據
    test_data = [
        {"type": "dict"},
        [1, 2, 3],
        None
    ]

    for data in test_data:
        stack.push(data)

    assert stack.is_full() == True

    # 嘗試推入更多
    try:
        stack.push("overflow")
        print("❌ 應該拋出 OverflowError")
        return False
    except OverflowError:
        pass

    # 驗證可以正確 pop
    popped = stack.pop()
    assert popped is None

    assert stack.is_full() == False

    print("✅ 容量限制與不同數據類型正確")


def main():
    """執行所有階段4測試"""
    print("🚀 開始階段4測試：容量管理")
    print("測試範圍：is_full(), 容量限制, 溢出處理")

    try:
        # 執行各項測試
        test_is_full_functionality()
        test_capacity_enforcement()
        test_full_stack_operations()
        test_capacity_edge_cases()
        test_mixed_capacity_operations()
        test_capacity_with_different_data_types()

        print("\n" + "="*50)
        print("🎉 階段4測試全部通過！")
        print("✅ 容量管理 (is_full, 溢出處理) 實作正確")
        print("✅ 有限和無限容量堆疊都正常工作")
        print("\n📝 下一步：實作 clear() 和字串表示方法")
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