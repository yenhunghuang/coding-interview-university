#!/usr/bin/env python3
"""
階段5測試：前階段功能 + delete() + remove()

這個階段測試移除功能，涉及元素移位和查找操作。
運行方式：python3 test_stage5.py
"""

import sys
sys.path.append('.')

exec(open('dynamic_array.py').read())


def test_previous_functionality():
    """重新測試前階段功能"""
    print("=== 測試前階段功能 ===")

    arr = DynamicArray()

    # 測試基本功能流程
    test_data = [1, "hello", [1, 2], None, 42]
    for item in test_data:
        arr.push(item)

    # 測試 insert 和 prepend
    arr.insert(2, "inserted")
    arr.prepend("first")

    # 驗證基本功能依然正常
    assert arr.size() > 0
    assert not arr.is_empty()
    assert arr.at(0) == "first"

    print("✅ 前階段功能依然正確")


def test_delete_basic_functionality():
    """測試 delete() 基本功能"""
    print("\n=== 測試 delete() 基本功能 ===")

    arr = DynamicArray()

    # 建立測試數據
    test_data = ["A", "B", "C", "D", "E"]
    for item in test_data:
        arr.push(item)
    # 陣列現在是: ["A", "B", "C", "D", "E"]

    # 測試 1: 刪除中間元素
    print("\n1. 測試刪除中間元素...")
    arr.delete(2)  # 刪除 "C"
    # 陣列應該是: ["A", "B", "D", "E"]

    assert arr.size() == 4, "❌ 刪除後 size 不正確"
    assert arr.at(0) == "A", "❌ 位置 0 元素不正確"
    assert arr.at(1) == "B", "❌ 位置 1 元素不正確"
    assert arr.at(2) == "D", "❌ 刪除後元素沒有正確左移"
    assert arr.at(3) == "E", "❌ 位置 3 元素不正確"
    print("✅ 中間元素刪除正確")

    # 測試 2: 刪除第一個元素
    print("\n2. 測試刪除第一個元素...")
    arr.delete(0)  # 刪除 "A"
    # 陣列應該是: ["B", "D", "E"]

    assert arr.size() == 3, "❌ 刪除首元素後 size 不正確"
    assert arr.at(0) == "B", "❌ 刪除首元素後，第二個元素沒有成為第一個"
    assert arr.at(1) == "D", "❌ 位置 1 元素不正確"
    assert arr.at(2) == "E", "❌ 位置 2 元素不正確"
    print("✅ 首元素刪除正確")

    # 測試 3: 刪除最後一個元素
    print("\n3. 測試刪除最後一個元素...")
    arr.delete(arr.size() - 1)  # 刪除 "E"
    # 陣列應該是: ["B", "D"]

    assert arr.size() == 2, "❌ 刪除尾元素後 size 不正確"
    assert arr.at(0) == "B", "❌ 位置 0 元素不正確"
    assert arr.at(1) == "D", "❌ 位置 1 元素不正確"
    print("✅ 尾元素刪除正確")


def test_delete_error_handling():
    """測試 delete() 錯誤處理"""
    print("\n=== 測試 delete() 錯誤處理 ===")

    arr = DynamicArray()
    arr.push("test1")
    arr.push("test2")  # arr 現在是 ["test1", "test2"], size=2

    print("\n1. 測試無效索引...")
    invalid_indices = [-1, 2, 10, 100]

    for idx in invalid_indices:
        try:
            arr.delete(idx)
            print(f"❌ 無效索引 {idx} 應該拋出異常")
        except IndexError:
            print(f"✅ 無效索引 {idx} 正確拋出 IndexError")
        except Exception as e:
            print(f"⚠️ 無效索引 {idx} 拋出其他異常: {e}")

    # 測試空陣列刪除
    print("\n2. 測試空陣列刪除...")
    empty_arr = DynamicArray()

    try:
        empty_arr.delete(0)
        print("❌ 空陣列刪除應該拋出異常")
    except IndexError:
        print("✅ 空陣列刪除正確拋出 IndexError")
    except Exception as e:
        print(f"⚠️ 空陣列刪除拋出其他異常: {e}")


def test_remove_basic_functionality():
    """測試 remove() 基本功能"""
    print("\n=== 測試 remove() 基本功能 ===")

    arr = DynamicArray()

    # 測試 1: 移除存在的元素
    print("\n1. 測試移除存在的元素...")
    test_data = [10, "hello", [1, 2], 10, "world"]
    for item in test_data:
        arr.push(item)
    # 陣列: [10, "hello", [1, 2], 10, "world"]

    # 移除第一個出現的 10
    arr.remove(10)
    # 陣列應該是: ["hello", [1, 2], 10, "world"]

    assert arr.size() == 4, "❌ remove 後 size 不正確"
    assert arr.at(0) == "hello", "❌ remove 後第一個元素不正確"
    assert arr.at(1) == [1, 2], "❌ remove 後第二個元素不正確"
    assert arr.at(2) == 10, "❌ 第二個 10 應該還在"
    assert arr.at(3) == "world", "❌ remove 後最後元素不正確"
    print("✅ 移除存在元素正確")

    # 測試 2: 移除字符串
    print("\n2. 測試移除字符串...")
    arr.remove("hello")
    # 陣列應該是: [[1, 2], 10, "world"]

    assert arr.size() == 3, "❌ remove 字符串後 size 不正確"
    assert arr.at(0) == [1, 2], "❌ remove 後元素位置不正確"
    assert arr.at(1) == 10, "❌ remove 後元素位置不正確"
    assert arr.at(2) == "world", "❌ remove 後元素位置不正確"
    print("✅ 移除字符串正確")

    # 測試 3: 移除複雜對象
    print("\n3. 測試移除複雜對象...")
    arr.remove([1, 2])
    # 陣列應該是: [10, "world"]

    assert arr.size() == 2, "❌ remove 複雜對象後 size 不正確"
    assert arr.at(0) == 10, "❌ remove 後元素位置不正確"
    assert arr.at(1) == "world", "❌ remove 後元素位置不正確"
    print("✅ 移除複雜對象正確")


def test_remove_not_found():
    """測試 remove() 元素不存在的情況"""
    print("\n=== 測試 remove() 元素不存在 ===")

    arr = DynamicArray()
    arr.push(1)
    arr.push(2)
    arr.push(3)

    # 測試移除不存在的元素
    print("\n1. 測試移除不存在的元素...")
    original_size = arr.size()

    # 移除不存在的元素應該不影響陣列
    arr.remove(99)  # 不存在的元素
    arr.remove("not_exist")  # 不存在的字符串

    assert arr.size() == original_size, "❌ 移除不存在元素後 size 改變了"
    assert arr.at(0) == 1, "❌ 移除不存在元素影響了現有元素"
    assert arr.at(1) == 2, "❌ 移除不存在元素影響了現有元素"
    assert arr.at(2) == 3, "❌ 移除不存在元素影響了現有元素"

    print("✅ 移除不存在元素處理正確")

    # 測試空陣列移除
    print("\n2. 測試空陣列移除...")
    empty_arr = DynamicArray()
    empty_arr.remove("anything")  # 應該不會出錯

    assert empty_arr.is_empty(), "❌ 空陣列移除後狀態改變"
    print("✅ 空陣列移除處理正確")


def test_delete_remove_integration():
    """測試 delete 和 remove 的整合"""
    print("\n=== 測試 delete 和 remove 整合 ===")

    arr = DynamicArray()

    # 建立測試數據
    test_data = ["X", 1, "Y", 2, "X", 3]
    for item in test_data:
        arr.push(item)
    # 陣列: ["X", 1, "Y", 2, "X", 3]

    print("\n1. 測試混合操作...")

    # 使用 remove 移除第一個 "X"
    arr.remove("X")  # 移除第一個 "X"
    # 陣列: [1, "Y", 2, "X", 3]

    # 使用 delete 刪除位置 1 的元素
    arr.delete(1)  # 刪除 "Y"
    # 陣列: [1, 2, "X", 3]

    # 再使用 remove 移除數字 2
    arr.remove(2)
    # 陣列: [1, "X", 3]

    # 驗證最終結果
    assert arr.size() == 3, "❌ 混合操作後 size 不正確"
    assert arr.at(0) == 1, "❌ 位置 0 元素不正確"
    assert arr.at(1) == "X", "❌ 位置 1 元素不正確"
    assert arr.at(2) == 3, "❌ 位置 2 元素不正確"

    print("✅ 混合操作正確")


def test_delete_remove_with_other_operations():
    """測試 delete/remove 與其他操作的整合"""
    print("\n=== 測試 delete/remove 與其他操作整合 ===")

    arr = DynamicArray()

    print("\n1. 測試 push → delete → push 循環...")

    # 建立初始狀態
    arr.push("A")
    arr.push("B")
    arr.push("C")  # [A, B, C]

    # 刪除中間元素
    arr.delete(1)  # [A, C]
    assert arr.size() == 2

    # 繼續 push
    arr.push("D")  # [A, C, D]
    assert arr.at(2) == "D"

    # 使用 remove
    arr.remove("A")  # [C, D]
    assert arr.size() == 2
    assert arr.at(0) == "C"

    # 使用 insert
    arr.insert(1, "E")  # [C, E, D]
    assert arr.size() == 3
    assert arr.at(1) == "E"

    # 最後驗證
    expected = ["C", "E", "D"]
    for i, expected_val in enumerate(expected):
        assert arr.at(i) == expected_val, f"❌ 位置 {i} 期望 {expected_val}，實際 {arr.at(i)}"

    print("✅ 與其他操作整合正確")


def main():
    """執行所有階段5測試"""
    print("🚀 開始階段5測試：前階段功能 + delete() + remove()")
    print("測試範圍：size(), capacity(), is_empty(), push(), at(), pop(), insert(), prepend(), delete(), remove()")

    try:
        # 執行各項測試
        test_previous_functionality()
        test_delete_basic_functionality()
        test_delete_error_handling()
        test_remove_basic_functionality()
        test_remove_not_found()
        test_delete_remove_integration()
        test_delete_remove_with_other_operations()

        print("\n" + "="*50)
        print("🎉 階段5測試全部通過！")
        print("✅ delete() 方法實作正確")
        print("✅ remove() 方法實作正確")
        print("✅ 元素移位和查找操作正確")
        print("✅ 與前階段功能整合正常")
        print("\n📝 下一步：實作 find() 方法")
        print("   然後運行 python3 test_stage6.py")
        print("\n💡 提示：delete/remove 操作涉及查找和移位，是比較重要的基礎操作！")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作，特別注意：")
        print("1. 元素移位邏輯是否正確")
        print("2. 查找邏輯是否正確")
        print("3. 邊界條件處理")
        print("4. size 更新是否正確")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法和實作邏輯")
        sys.exit(1)


if __name__ == "__main__":
    main()