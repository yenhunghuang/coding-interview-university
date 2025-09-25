#!/usr/bin/env python3
"""
階段4測試：前階段功能 + insert() + prepend()

這個階段測試插入功能，涉及元素移位操作。
運行方式：python3 test_stage4.py
"""

import sys
sys.path.append('.')

exec(open('dynamic_array.py').read())

def test_previous_functionality():
    """重新測試前階段功能"""
    print("=== 測試前階段功能 ===")

    arr = DynamicArray()

    # 測試 push, at, pop 的基本流程
    test_data = [1, 2, 3]
    for item in test_data:
        arr.push(item)

    assert arr.size() == 3
    assert arr.at(1) == 2

    popped = arr.pop()
    assert popped == 3 and arr.size() == 2

    print("✅ 前階段功能依然正確")


def test_insert_basic_functionality():
    """測試 insert() 基本功能"""
    print("\n=== 測試 insert() 基本功能 ===")

    arr = DynamicArray()

    # 測試 1: 空陣列插入
    print("\n1. 測試空陣列插入...")
    arr.insert(0, "first")

    assert arr.size() == 1, "❌ 插入後 size 不正確"
    assert arr.at(0) == "first", "❌ 插入元素不正確"
    print("✅ 空陣列插入正確")

    # 測試 2: 尾端插入
    print("\n2. 測試尾端插入...")
    arr.insert(1, "last")  # 在位置 1（尾端）插入

    assert arr.size() == 2, "❌ 尾端插入後 size 不正確"
    assert arr.at(0) == "first", "❌ 原有元素被影響"
    assert arr.at(1) == "last", "❌ 尾端插入元素不正確"
    print("✅ 尾端插入正確")

    # 測試 3: 中間插入（這是關鍵測試）
    print("\n3. 測試中間插入...")
    arr.insert(1, "middle")  # 在位置 1 插入，原來位置 1 的元素應該向右移

    assert arr.size() == 3, "❌ 中間插入後 size 不正確"
    assert arr.at(0) == "first", "❌ 位置 0 元素被影響"
    assert arr.at(1) == "middle", "❌ 中間插入元素不正確"
    assert arr.at(2) == "last", "❌ 原位置 1 的元素沒有正確右移"
    print("✅ 中間插入正確")

    # 測試 4: 開頭插入
    print("\n4. 測試開頭插入...")
    arr.insert(0, "new_first")  # 在位置 0 插入，所有元素都應該右移

    assert arr.size() == 4, "❌ 開頭插入後 size 不正確"
    assert arr.at(0) == "new_first", "❌ 開頭插入元素不正確"
    assert arr.at(1) == "first", "❌ 原開頭元素沒有正確右移"
    assert arr.at(2) == "middle", "❌ 中間元素沒有正確右移"
    assert arr.at(3) == "last", "❌ 尾端元素沒有正確右移"
    print("✅ 開頭插入正確")


def test_insert_error_handling():
    """測試 insert() 錯誤處理"""
    print("\n=== 測試 insert() 錯誤處理 ===")

    arr = DynamicArray()
    arr.push(1)
    arr.push(2)  # arr 現在是 [1, 2], size=2

    # 測試有效的索引範圍：0, 1, 2（可以在尾端插入）
    valid_indices = [0, 1, 2]
    invalid_indices = [-1, 3, 10, 100]

    print("\n1. 測試有效索引範圍...")
    # 這裡不實際插入，只是確認不會拋出異常
    for idx in [0, 2]:  # 測試開頭和尾端
        try:
            temp_arr = DynamicArray()
            temp_arr.push(1)
            temp_arr.push(2)
            temp_arr.insert(idx, f"test_{idx}")
            print(f"✅ 索引 {idx} 有效")
        except Exception as e:
            print(f"❌ 有效索引 {idx} 卻拋出異常: {e}")

    print("\n2. 測試無效索引...")
    for idx in invalid_indices:
        try:
            arr.insert(idx, "should_fail")
            print(f"❌ 無效索引 {idx} 應該拋出異常")
        except IndexError:
            print(f"✅ 無效索引 {idx} 正確拋出 IndexError")
        except Exception as e:
            print(f"⚠️ 無效索引 {idx} 拋出其他異常: {e}")


def test_prepend_functionality():
    """測試 prepend() 功能"""
    print("\n=== 測試 prepend() 功能 ===")

    arr = DynamicArray()

    # 測試 1: 空陣列 prepend
    print("\n1. 測試空陣列 prepend...")
    arr.prepend("first")

    assert arr.size() == 1, "❌ prepend 後 size 不正確"
    assert arr.at(0) == "first", "❌ prepend 元素不正確"
    print("✅ 空陣列 prepend 正確")

    # 測試 2: 非空陣列 prepend
    print("\n2. 測試非空陣列 prepend...")
    arr.prepend("new_first")

    assert arr.size() == 2, "❌ prepend 後 size 不正確"
    assert arr.at(0) == "new_first", "❌ 新的第一個元素不正確"
    assert arr.at(1) == "first", "❌ 原第一個元素沒有正確移位"
    print("✅ 非空陣列 prepend 正確")

    # 測試 3: 多次 prepend
    print("\n3. 測試多次 prepend...")
    for i in range(5):
        arr.prepend(f"item_{i}")

    # 陣列現在應該是: ["item_4", "item_3", "item_2", "item_1", "item_0", "new_first", "first"]
    assert arr.size() == 7, "❌ 多次 prepend 後 size 不正確"
    assert arr.at(0) == "item_4", "❌ 最後 prepend 的元素應該在最前面"
    assert arr.at(5) == "new_first", "❌ 原有元素位置不正確"
    assert arr.at(6) == "first", "❌ 最初元素位置不正確"
    print("✅ 多次 prepend 正確")


def test_insert_prepend_integration():
    """測試 insert 和 prepend 的整合"""
    print("\n=== 測試 insert 和 prepend 整合 ===")

    arr = DynamicArray()

    # 建立一個測試序列
    arr.push("A")
    arr.push("B")
    arr.push("C")
    # 陣列: ["A", "B", "C"]

    print("\n1. 測試混合操作...")

    # 在中間插入
    arr.insert(1, "X")  # ["A", "X", "B", "C"]
    assert arr.at(1) == "X", "❌ 中間插入不正確"

    # 在開頭插入 (使用 prepend)
    arr.prepend("Y")  # ["Y", "A", "X", "B", "C"]
    assert arr.at(0) == "Y", "❌ prepend 不正確"

    # 在尾端插入
    arr.insert(arr.size(), "Z")  # ["Y", "A", "X", "B", "C", "Z"]
    assert arr.at(arr.size() - 1) == "Z", "❌ 尾端插入不正確"

    # 驗證最終狀態
    expected = ["Y", "A", "X", "B", "C", "Z"]
    assert arr.size() == len(expected), "❌ 最終 size 不正確"

    for i, expected_val in enumerate(expected):
        actual_val = arr.at(i)
        assert actual_val == expected_val, f"❌ 位置 {i} 期望 {expected_val}，實際 {actual_val}"

    print("✅ 混合操作正確")


def test_insert_with_existing_operations():
    """測試 insert 與現有操作（push, pop）的整合"""
    print("\n=== 測試 insert 與現有操作整合 ===")

    arr = DynamicArray()

    print("\n1. 測試 insert + push + pop 混合...")

    # 建立初始狀態
    arr.push(1)
    arr.push(2)
    arr.push(3)  # [1, 2, 3]

    # 插入元素
    arr.insert(1, "inserted")  # [1, "inserted", 2, 3]

    # 驗證插入結果
    assert arr.at(1) == "inserted", "❌ 插入後元素不正確"
    assert arr.at(2) == 2, "❌ 插入後原元素位置不正確"

    # 繼續 push
    arr.push("end")  # [1, "inserted", 2, 3, "end"]

    # pop 應該得到最後 push 的元素
    popped = arr.pop()
    assert popped == "end", "❌ pop 結果不正確"

    # 再 pop 應該得到 3
    popped = arr.pop()
    assert popped == 3, "❌ 第二次 pop 結果不正確"

    # 驗證剩餘元素
    assert arr.size() == 3, "❌ 操作後 size 不正確"
    assert arr.at(0) == 1, "❌ 位置 0 元素不正確"
    assert arr.at(1) == "inserted", "❌ 位置 1 元素不正確"
    assert arr.at(2) == 2, "❌ 位置 2 元素不正確"

    print("✅ 與現有操作整合正確")


def main():
    """執行所有階段4測試"""
    print("🚀 開始階段4測試：前階段功能 + insert() + prepend()")
    print("測試範圍：size(), capacity(), is_empty(), push(), at(), pop(), insert(), prepend()")

    try:
        # 執行各項測試
        test_previous_functionality()
        test_insert_basic_functionality()
        test_insert_error_handling()
        test_prepend_functionality()
        test_insert_prepend_integration()
        test_insert_with_existing_operations()

        print("\n" + "="*50)
        print("🎉 階段4測試全部通過！")
        print("✅ insert() 方法實作正確")
        print("✅ prepend() 方法實作正確")
        print("✅ 元素移位操作正確")
        print("✅ 與前階段功能整合正常")
        print("\n📝 下一步：實作 delete() 和 remove() 方法")
        print("   然後運行 python3 test_stage5.py")
        print("\n💡 提示：insert/prepend 是比較複雜的操作，通過這階段表示你已經掌握了元素移位的核心概念！")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作，特別注意：")
        print("1. 元素移位邏輯是否正確")
        print("2. 邊界條件處理")
        print("3. size 更新是否正確")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法和實作邏輯")
        sys.exit(1)


if __name__ == "__main__":
    main()