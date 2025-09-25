#!/usr/bin/env python3
"""
階段3測試：基礎方法 + push() + at() + pop()

這個階段測試移除功能的加入。
運行方式：python3 test_stage3.py
"""

import sys
sys.path.append('.')

exec(open('dynamic_array.py').read())


def test_previous_functionality():
    """重新測試前階段功能（確保沒被破壞）"""
    print("=== 測試前階段功能 ===")

    arr = DynamicArray()

    # 基礎方法
    assert arr.size() == 0
    assert arr.capacity() == 16
    assert arr.is_empty() == True

    # push 和 at
    test_data = [1, "test", [1, 2], None]
    for item in test_data:
        arr.push(item)

    for i, expected in enumerate(test_data):
        assert arr.at(i) == expected

    print("✅ 前階段功能依然正確")


def test_pop_basic_functionality():
    """測試 pop() 基本功能"""
    print("\n=== 測試 pop() 基本功能 ===")

    arr = DynamicArray()

    # 測試 1: 單個元素 push 和 pop
    print("\n1. 測試單個元素 push 和 pop...")
    arr.push(42)

    assert arr.size() == 1, "❌ push 後 size 不正確"

    popped = arr.pop()
    assert popped == 42, f"❌ pop() 應該回傳 42，實際是 {popped}"
    assert arr.size() == 0, "❌ pop 後 size 應該是 0"
    assert arr.is_empty() == True, "❌ pop 後應該是空的"

    print("✅ 單個元素 push/pop 正確")

    # 測試 2: 多個元素的 LIFO 行為
    print("\n2. 測試多個元素的 LIFO (後進先出) 行為...")
    test_sequence = [10, "hello", [1, 2, 3], None, 99]

    # 按順序 push
    for item in test_sequence:
        arr.push(item)

    assert arr.size() == len(test_sequence), "❌ push 完後 size 不正確"

    # 按反順序 pop，應該得到相反的順序
    for expected in reversed(test_sequence):
        actual = arr.pop()
        assert actual == expected, f"❌ 期望 pop {expected}，實際得到 {actual}"

    assert arr.is_empty(), "❌ 全部 pop 完後應該是空的"
    print("✅ LIFO 行為正確")


def test_pop_error_handling():
    """測試 pop() 錯誤處理"""
    print("\n=== 測試 pop() 錯誤處理 ===")

    # 測試 1: 空陣列 pop
    print("\n1. 測試空陣列 pop...")
    empty_arr = DynamicArray()

    try:
        empty_arr.pop()
        print("❌ 空陣列 pop 應該拋出異常")
    except IndexError as e:
        print(f"✅ 空陣列 pop 正確拋出 IndexError: {e}")
    except Exception as e:
        print(f"⚠️ 空陣列 pop 拋出其他異常: {e}")

    # 測試 2: 多次 pop 到空
    print("\n2. 測試多次 pop 到空...")
    arr = DynamicArray()
    arr.push("only_one")

    # 第一次 pop 成功
    result = arr.pop()
    assert result == "only_one", "❌ 第一次 pop 結果不正確"

    # 第二次 pop 應該失敗
    try:
        arr.pop()
        print("❌ 第二次 pop 應該拋出異常")
    except IndexError:
        print("✅ 第二次 pop 正確拋出 IndexError")


def test_push_pop_cycles():
    """測試 push/pop 循環操作"""
    print("\n=== 測試 push/pop 循環操作 ===")

    arr = DynamicArray()

    print("\n1. 測試交替 push/pop...")

    # 交替操作測試
    arr.push(1)
    assert arr.size() == 1

    result = arr.pop()
    assert result == 1 and arr.size() == 0

    arr.push(2)
    arr.push(3)
    assert arr.size() == 2

    result = arr.pop()
    assert result == 3 and arr.size() == 1

    result = arr.pop()
    assert result == 2 and arr.size() == 0

    print("✅ 交替 push/pop 正確")

    print("\n2. 測試批量 push 然後批量 pop...")

    # 批量操作測試
    batch_data = list(range(20))  # [0, 1, 2, ..., 19]

    for item in batch_data:
        arr.push(item)

    assert arr.size() == 20, "❌ 批量 push 後 size 不正確"

    for expected in reversed(batch_data):
        actual = arr.pop()
        assert actual == expected, f"❌ 批量 pop 順序不正確"

    assert arr.is_empty(), "❌ 批量 pop 完後應該是空的"
    print("✅ 批量 push/pop 正確")


def test_pop_size_capacity_relationship():
    """測試 pop 後的 size 和 capacity 關係"""
    print("\n=== 測試 pop 後的 size/capacity 關係 ===")

    arr = DynamicArray()

    # 填充一些數據
    for i in range(10):
        arr.push(i)

    original_capacity = arr.capacity()

    print(f"\n1. 初始狀態: size={arr.size()}, capacity={arr.capacity()}")

    # pop 一些元素
    for _ in range(5):
        arr.pop()

    print(f"2. pop 5個後: size={arr.size()}, capacity={arr.capacity()}")

    # 在這個階段，capacity 可能還不會變化（動態縮容在後面實作）
    # 但 size 應該正確更新
    assert arr.size() == 5, "❌ pop 後 size 不正確"

    # pop 剩餘的所有元素
    while not arr.is_empty():
        arr.pop()

    print(f"3. 全部 pop 完: size={arr.size()}, capacity={arr.capacity()}")

    assert arr.size() == 0, "❌ 全部 pop 完後 size 應該是 0"
    assert arr.is_empty(), "❌ 全部 pop 完後應該是空的"

    print("✅ size/capacity 關係正確")


def test_pop_with_different_data_types():
    """測試不同資料類型的 pop"""
    print("\n=== 測試不同資料類型的 pop ===")

    arr = DynamicArray()

    # 不同類型的測試數據
    test_data = [
        42,                    # int
        3.14,                  # float
        "hello world",         # string
        [1, 2, 3, 4, 5],      # list
        {"key": "value"},      # dict
        (10, 20),             # tuple
        None,                  # None
        True,                  # boolean
    ]

    # push 所有數據
    for item in test_data:
        arr.push(item)

    # pop 並驗證（應該是反向順序）
    for expected in reversed(test_data):
        actual = arr.pop()
        assert actual == expected, f"❌ 不同資料類型 pop 失敗: 期望 {expected}, 得到 {actual}"

    assert arr.is_empty(), "❌ pop 完所有不同類型數據後應該是空的"
    print("✅ 不同資料類型 pop 正確")


def main():
    """執行所有階段3測試"""
    print("🚀 開始階段3測試：基礎方法 + push() + at() + pop()")
    print("測試範圍：size(), capacity(), is_empty(), push(), at(), pop()")

    try:
        # 執行各項測試
        test_previous_functionality()
        test_pop_basic_functionality()
        test_pop_error_handling()
        test_push_pop_cycles()
        test_pop_size_capacity_relationship()
        test_pop_with_different_data_types()

        print("\n" + "="*50)
        print("🎉 階段3測試全部通過！")
        print("✅ pop() 方法實作正確")
        print("✅ LIFO (後進先出) 行為正確")
        print("✅ 與前階段功能整合正常")
        print("\n📝 下一步：實作 insert() 和 prepend() 方法")
        print("   然後運行 python3 test_stage4.py")
        print("\n💡 提示：下個階段會開始涉及元素移位操作，比較複雜！")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作並修正後重新測試")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法和實作邏輯")
        sys.exit(1)


if __name__ == "__main__":
    main()