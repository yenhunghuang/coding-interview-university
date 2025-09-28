#!/usr/bin/env python3
"""
階段4測試：隨機存取操作測試 - value_at(), insert(), erase()

這個階段測試列表的隨機存取操作，包括：
- value_at(index) - 根據索引獲取元素值
- insert(index, value) - 在指定位置插入元素
- erase(index) - 刪除指定位置的元素
- 各種邊界條件和錯誤處理

運行方式：python3 test_stage4.py

實作指引：
在 SinglyLinkedList 中新增這些方法：
- value_at(index) -> any：返回指定索引的值（0-based），越界拋出 IndexError
- insert(index, value) -> None：在指定索引插入新元素，原元素後移
- erase(index) -> None：刪除指定索引的元素，後續元素前移

時間複雜度：
- value_at(index): O(n) - 需要遍歷到指定位置
- insert(index, value): O(n) - 需要遍歷到指定位置
- erase(index): O(n) - 需要遍歷到指定位置

特別注意：
- 索引範圍：0 <= index < size() 對於 value_at 和 erase
- insert 允許 index = size()，表示在尾部插入
- 負數索引應拋出 IndexError
"""

import sys
sys.path.append('.')

exec(open('node.py').read())
exec(open('singly_linked_list.py').read())


def test_previous_functionality():
    """重新測試前階段功能（確保沒被破壞）"""
    print("=== 測試前階段功能 ===")

    linked_list = SinglyLinkedList()

    # 基礎方法
    assert linked_list.size() == 0
    assert linked_list.empty() == True

    # 前後端操作測試
    test_data = [1, 2, 3]
    for item in test_data:
        linked_list.push_back(item)

    assert linked_list.size() == 3
    assert linked_list.front() == 1
    assert linked_list.back() == 3

    for expected in reversed(test_data):
        assert linked_list.pop_back() == expected

    print("✅ 前階段功能依然正確")


def test_value_at_basic_functionality():
    """測試 value_at() 基本功能"""
    print("\n=== 測試 value_at() 基本功能 ===")

    linked_list = SinglyLinkedList()

    # 測試 1: 空列表 value_at 應該拋出異常
    print("\n1. 測試空列表 value_at()...")
    try:
        linked_list.value_at(0)
        print("❌ 空列表 value_at(0) 應該拋出 IndexError")
    except IndexError:
        print("✅ 空列表 value_at(0) 正確拋出 IndexError")
    except Exception as e:
        print(f"⚠️ 空列表 value_at(0) 拋出其他異常: {e}")

    # 測試 2: 單個元素列表
    print("\n2. 測試單個元素列表 value_at()...")
    linked_list.push_back("only_one")

    value = linked_list.value_at(0)
    assert value == "only_one", f"❌ value_at(0) 應該返回 'only_one'，實際返回 {value}"
    assert linked_list.size() == 1, "❌ value_at() 不應該改變列表大小"

    try:
        linked_list.value_at(1)
        print("❌ 單元素列表 value_at(1) 應該拋出 IndexError")
    except IndexError:
        print("✅ 單元素列表 value_at(1) 正確拋出 IndexError")

    print("✅ 單個元素列表 value_at() 正確")

    # 測試 3: 多個元素列表
    print("\n3. 測試多個元素列表 value_at()...")
    linked_list = SinglyLinkedList()
    test_data = ["zero", "one", "two", "three", "four"]

    for item in test_data:
        linked_list.push_back(item)

    # 測試所有有效索引
    for i, expected in enumerate(test_data):
        actual = linked_list.value_at(i)
        assert actual == expected, f"❌ value_at({i}) 應該返回 '{expected}'，實際返回 '{actual}'"

    assert linked_list.size() == len(test_data), "❌ value_at() 不應該改變列表大小"
    print("✅ 多個元素列表 value_at() 正確")


def test_value_at_error_handling():
    """測試 value_at() 錯誤處理"""
    print("\n=== 測試 value_at() 錯誤處理 ===")

    linked_list = SinglyLinkedList()
    for i in range(5):
        linked_list.push_back(i)  # [0, 1, 2, 3, 4]

    # 測試有效索引範圍：0, 1, 2, 3, 4
    valid_indices = [0, 1, 2, 3, 4]
    invalid_indices = [-1, -5, 5, 10, 100]

    print("\n1. 測試有效索引範圍...")
    for idx in valid_indices:
        try:
            value = linked_list.value_at(idx)
            assert value == idx, f"❌ value_at({idx}) 值不正確"
            print(f"✅ 索引 {idx} 有效，值為 {value}")
        except Exception as e:
            print(f"❌ 有效索引 {idx} 卻拋出異常: {e}")

    print("\n2. 測試無效索引...")
    for idx in invalid_indices:
        try:
            linked_list.value_at(idx)
            print(f"❌ 無效索引 {idx} 應該拋出異常")
        except IndexError:
            print(f"✅ 無效索引 {idx} 正確拋出 IndexError")
        except Exception as e:
            print(f"⚠️ 無效索引 {idx} 拋出其他異常: {e}")


def test_insert_basic_functionality():
    """測試 insert() 基本功能"""
    print("\n=== 測試 insert() 基本功能 ===")

    # 測試 1: 空列表插入
    print("\n1. 測試空列表插入...")
    linked_list = SinglyLinkedList()
    linked_list.insert(0, "first")

    assert linked_list.size() == 1, "❌ 插入後 size 不正確"
    assert linked_list.value_at(0) == "first", "❌ 插入元素不正確"
    print("✅ 空列表插入正確")

    # 測試 2: 尾端插入
    print("\n2. 測試尾端插入...")
    linked_list.insert(1, "last")  # 在位置 1（尾端）插入

    assert linked_list.size() == 2, "❌ 尾端插入後 size 不正確"
    assert linked_list.value_at(0) == "first", "❌ 原有元素被影響"
    assert linked_list.value_at(1) == "last", "❌ 尾端插入元素不正確"
    print("✅ 尾端插入正確")

    # 測試 3: 中間插入（這是關鍵測試）
    print("\n3. 測試中間插入...")
    linked_list.insert(1, "middle")  # 在位置 1 插入，原來位置 1 的元素應該向右移

    assert linked_list.size() == 3, "❌ 中間插入後 size 不正確"
    assert linked_list.value_at(0) == "first", "❌ 位置 0 元素被影響"
    assert linked_list.value_at(1) == "middle", "❌ 中間插入元素不正確"
    assert linked_list.value_at(2) == "last", "❌ 原位置 1 的元素沒有正確右移"
    print("✅ 中間插入正確")

    # 測試 4: 開頭插入
    print("\n4. 測試開頭插入...")
    linked_list.insert(0, "new_first")  # 在位置 0 插入，所有元素都應該右移

    assert linked_list.size() == 4, "❌ 開頭插入後 size 不正確"
    assert linked_list.value_at(0) == "new_first", "❌ 開頭插入元素不正確"
    assert linked_list.value_at(1) == "first", "❌ 原開頭元素沒有正確右移"
    assert linked_list.value_at(2) == "middle", "❌ 中間元素沒有正確右移"
    assert linked_list.value_at(3) == "last", "❌ 尾端元素沒有正確右移"
    print("✅ 開頭插入正確")


def test_insert_error_handling():
    """測試 insert() 錯誤處理"""
    print("\n=== 測試 insert() 錯誤處理 ===")

    linked_list = SinglyLinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)  # 列表現在是 [1, 2], size=2

    # 測試有效的索引範圍：0, 1, 2（可以在尾端插入）
    valid_indices = [0, 1, 2]
    invalid_indices = [-1, 3, 10, 100]

    print("\n1. 測試有效索引範圍...")
    # 這裡不實際插入，只是確認不會拋出異常
    for idx in [0, 2]:  # 測試開頭和尾端
        try:
            temp_list = SinglyLinkedList()
            temp_list.push_back(1)
            temp_list.push_back(2)
            temp_list.insert(idx, f"test_{idx}")
            print(f"✅ 索引 {idx} 有效")
        except Exception as e:
            print(f"❌ 有效索引 {idx} 卻拋出異常: {e}")

    print("\n2. 測試無效索引...")
    for idx in invalid_indices:
        try:
            linked_list.insert(idx, "should_fail")
            print(f"❌ 無效索引 {idx} 應該拋出異常")
        except IndexError:
            print(f"✅ 無效索引 {idx} 正確拋出 IndexError")
        except Exception as e:
            print(f"⚠️ 無效索引 {idx} 拋出其他異常: {e}")


def test_erase_basic_functionality():
    """測試 erase() 基本功能"""
    print("\n=== 測試 erase() 基本功能 ===")

    # 測試 1: 單個元素列表刪除
    print("\n1. 測試單個元素列表刪除...")
    linked_list = SinglyLinkedList()
    linked_list.push_back("only_one")

    linked_list.erase(0)
    assert linked_list.size() == 0, "❌ 刪除後 size 應該是 0"
    assert linked_list.empty() == True, "❌ 刪除後列表應該為空"
    print("✅ 單個元素列表刪除正確")

    # 測試 2: 多個元素列表刪除開頭
    print("\n2. 測試刪除開頭元素...")
    linked_list = SinglyLinkedList()
    test_data = ["first", "second", "third", "fourth"]
    for item in test_data:
        linked_list.push_back(item)

    linked_list.erase(0)  # 刪除 "first"
    assert linked_list.size() == 3, "❌ 刪除開頭後 size 不正確"
    assert linked_list.value_at(0) == "second", "❌ 刪除開頭後第一個元素不正確"
    assert linked_list.value_at(1) == "third", "❌ 後續元素沒有正確前移"
    print("✅ 刪除開頭元素正確")

    # 測試 3: 刪除中間元素
    print("\n3. 測試刪除中間元素...")
    linked_list.erase(1)  # 刪除 "third"（現在在位置1）
    assert linked_list.size() == 2, "❌ 刪除中間元素後 size 不正確"
    assert linked_list.value_at(0) == "second", "❌ 前面元素被影響"
    assert linked_list.value_at(1) == "fourth", "❌ 後面元素沒有正確前移"
    print("✅ 刪除中間元素正確")

    # 測試 4: 刪除尾端元素
    print("\n4. 測試刪除尾端元素...")
    linked_list.erase(1)  # 刪除 "fourth"（現在在位置1，是最後一個）
    assert linked_list.size() == 1, "❌ 刪除尾端後 size 不正確"
    assert linked_list.value_at(0) == "second", "❌ 剩餘元素不正確"
    print("✅ 刪除尾端元素正確")


def test_erase_error_handling():
    """測試 erase() 錯誤處理"""
    print("\n=== 測試 erase() 錯誤處理 ===")

    # 測試 1: 空列表 erase
    print("\n1. 測試空列表 erase()...")
    empty_list = SinglyLinkedList()

    try:
        empty_list.erase(0)
        print("❌ 空列表 erase(0) 應該拋出 IndexError")
    except IndexError:
        print("✅ 空列表 erase(0) 正確拋出 IndexError")
    except Exception as e:
        print(f"⚠️ 空列表 erase(0) 拋出其他異常: {e}")

    # 測試 2: 無效索引
    print("\n2. 測試無效索引...")
    linked_list = SinglyLinkedList()
    for i in range(3):
        linked_list.push_back(i)  # [0, 1, 2]

    valid_indices = [0, 1, 2]
    invalid_indices = [-1, 3, 10, 100]

    for idx in invalid_indices:
        try:
            temp_list = SinglyLinkedList()
            for i in range(3):
                temp_list.push_back(i)
            temp_list.erase(idx)
            print(f"❌ 無效索引 {idx} 應該拋出異常")
        except IndexError:
            print(f"✅ 無效索引 {idx} 正確拋出 IndexError")
        except Exception as e:
            print(f"⚠️ 無效索引 {idx} 拋出其他異常: {e}")


def test_insert_erase_integration():
    """測試 insert 和 erase 的整合"""
    print("\n=== 測試 insert 和 erase 整合 ===")

    linked_list = SinglyLinkedList()

    # 建立一個測試序列
    linked_list.push_back("A")
    linked_list.push_back("B")
    linked_list.push_back("C")
    # 列表: ["A", "B", "C"]

    print("\n1. 測試混合操作...")

    # 在中間插入
    linked_list.insert(1, "X")  # ["A", "X", "B", "C"]
    assert linked_list.value_at(1) == "X", "❌ 中間插入不正確"

    # 刪除開頭
    linked_list.erase(0)  # ["X", "B", "C"]
    assert linked_list.value_at(0) == "X", "❌ 刪除開頭後第一個元素不正確"

    # 在尾端插入
    linked_list.insert(linked_list.size(), "Z")  # ["X", "B", "C", "Z"]
    assert linked_list.value_at(linked_list.size() - 1) == "Z", "❌ 尾端插入不正確"

    # 驗證最終狀態
    expected = ["X", "B", "C", "Z"]
    assert linked_list.size() == len(expected), "❌ 最終 size 不正確"

    for i, expected_val in enumerate(expected):
        actual_val = linked_list.value_at(i)
        assert actual_val == expected_val, f"❌ 位置 {i} 期望 {expected_val}，實際 {actual_val}"

    print("✅ 混合操作正確")


def main():
    """執行所有階段4測試"""
    print("🚀 開始階段4測試：隨機存取操作測試")
    print("測試範圍：前階段功能 + value_at(), insert(), erase()")

    try:
        # 執行各項測試
        test_previous_functionality()
        test_value_at_basic_functionality()
        test_value_at_error_handling()
        test_insert_basic_functionality()
        test_insert_error_handling()
        test_erase_basic_functionality()
        test_erase_error_handling()
        test_insert_erase_integration()

        print("\n" + "="*50)
        print("🎉 階段4測試全部通過！")
        print("✅ value_at() 方法實作正確")
        print("✅ insert() 方法實作正確")
        print("✅ erase() 方法實作正確")
        print("✅ 元素移位操作正確")
        print("✅ 與前階段功能整合正常")
        print("\n📝 下一步：實作進階方法 reverse() 和 value_n_from_end()")
        print("   然後運行 python3 test_stage5.py")
        print("\n💡 提示：")
        print("   - reverse() 需要重新連接所有節點的指標")
        print("   - value_n_from_end() 可以用兩次遍歷或雙指標技巧")
        print("   - 這些是演算法性較強的操作！")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作，特別注意：")
        print("1. value_at() 需要正確遍歷到指定位置")
        print("2. insert() 需要在正確位置插入並保持連接")
        print("3. erase() 需要正確移除節點並重新連接")
        print("4. 索引邊界檢查和異常處理")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法和實作邏輯")
        sys.exit(1)


if __name__ == "__main__":
    main()