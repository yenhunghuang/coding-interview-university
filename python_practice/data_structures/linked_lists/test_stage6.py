#!/usr/bin/env python3
"""
階段6測試：數值操作測試 - remove_value()

這個階段測試基於數值的操作，包括：
- remove_value(value) - 移除第一個匹配的值
- 處理重複值的情況
- 處理不存在值的情況
- 與其他操作的整合測試

運行方式：python3 test_stage6.py

實作指引：
在 SinglyLinkedList 中新增這個方法：
- remove_value(value) -> None：移除第一個匹配的值，如果不存在則不做任何操作

實作提示：
- 需要遍歷列表找到第一個匹配的節點
- 找到後執行刪除操作（類似 erase，但基於值而非索引）
- 需要處理刪除頭節點的特殊情況
- 如果值不存在，靜默返回（不拋出異常）

時間複雜度：
- remove_value(): O(n) - 需要搜尋目標值

特別注意：
- 只移除第一個匹配的值
- 不存在的值不應該拋出異常
- 需要正確處理各種位置的刪除（頭、中、尾）
"""

import sys
sys.path.append('.')

exec(open('node.py').read())
exec(open('singly_linked_list.py').read())


def test_previous_functionality():
    """重新測試前階段功能（確保沒被破壞）"""
    print("=== 測試前階段功能 ===")

    linked_list = SinglyLinkedList()

    # 基礎功能測試
    test_data = [1, 2, 3, 4, 5]
    for item in test_data:
        linked_list.push_back(item)

    # 進階演算法測試
    assert linked_list.value_n_from_end(1) == 5
    assert linked_list.value_n_from_end(5) == 1

    linked_list.reverse()
    assert linked_list.front() == 5
    assert linked_list.back() == 1

    print("✅ 前階段功能依然正確")


def test_remove_value_basic_functionality():
    """測試 remove_value() 基本功能"""
    print("\n=== 測試 remove_value() 基本功能 ===")

    # 測試 1: 空列表移除
    print("\n1. 測試空列表移除...")
    empty_list = SinglyLinkedList()
    empty_list.remove_value("not_exist")  # 應該不拋出異常

    assert empty_list.size() == 0, "❌ 空列表移除後 size 應該還是 0"
    assert empty_list.empty() == True, "❌ 空列表移除後應該還是空的"
    print("✅ 空列表移除正確（無異常）")

    # 測試 2: 移除不存在的值
    print("\n2. 測試移除不存在的值...")
    linked_list = SinglyLinkedList()
    linked_list.push_back("a")
    linked_list.push_back("b")
    linked_list.push_back("c")

    original_size = linked_list.size()
    linked_list.remove_value("not_exist")  # 應該不拋出異常

    assert linked_list.size() == original_size, "❌ 移除不存在值後 size 不應該改變"
    assert linked_list.value_at(0) == "a", "❌ 移除不存在值後列表內容不應該改變"
    print("✅ 移除不存在值正確（無異常，無改變）")

    # 測試 3: 移除唯一元素
    print("\n3. 測試移除唯一元素...")
    single_list = SinglyLinkedList()
    single_list.push_back("only_one")

    single_list.remove_value("only_one")
    assert single_list.size() == 0, "❌ 移除唯一元素後 size 應該是 0"
    assert single_list.empty() == True, "❌ 移除唯一元素後列表應該為空"
    print("✅ 移除唯一元素正確")

    # 測試 4: 移除頭節點
    print("\n4. 測試移除頭節點...")
    linked_list = SinglyLinkedList()
    test_data = ["first", "second", "third"]
    for item in test_data:
        linked_list.push_back(item)

    linked_list.remove_value("first")  # 移除頭節點
    assert linked_list.size() == 2, "❌ 移除頭節點後 size 不正確"
    assert linked_list.front() == "second", "❌ 移除頭節點後新的頭節點不正確"
    assert linked_list.value_at(0) == "second", "❌ 移除頭節點後第一個元素不正確"
    assert linked_list.value_at(1) == "third", "❌ 移除頭節點後第二個元素不正確"
    print("✅ 移除頭節點正確")

    # 測試 5: 移除尾節點
    print("\n5. 測試移除尾節點...")
    linked_list = SinglyLinkedList()
    test_data = ["first", "second", "third"]
    for item in test_data:
        linked_list.push_back(item)

    linked_list.remove_value("third")  # 移除尾節點
    assert linked_list.size() == 2, "❌ 移除尾節點後 size 不正確"
    assert linked_list.back() == "second", "❌ 移除尾節點後新的尾節點不正確"
    assert linked_list.value_at(0) == "first", "❌ 移除尾節點後第一個元素不正確"
    assert linked_list.value_at(1) == "second", "❌ 移除尾節點後第二個元素不正確"
    print("✅ 移除尾節點正確")

    # 測試 6: 移除中間節點
    print("\n6. 測試移除中間節點...")
    linked_list = SinglyLinkedList()
    test_data = ["first", "second", "third", "fourth"]
    for item in test_data:
        linked_list.push_back(item)

    linked_list.remove_value("second")  # 移除中間節點
    assert linked_list.size() == 3, "❌ 移除中間節點後 size 不正確"
    assert linked_list.value_at(0) == "first", "❌ 移除中間節點後第一個元素不正確"
    assert linked_list.value_at(1) == "third", "❌ 移除中間節點後，後續元素沒有正確前移"
    assert linked_list.value_at(2) == "fourth", "❌ 移除中間節點後最後一個元素不正確"

    linked_list.remove_value("third")  # 再移除一個中間節點
    assert linked_list.size() == 2, "❌ 再次移除中間節點後 size 不正確"
    assert linked_list.value_at(0) == "first", "❌ 再次移除後第一個元素不正確"
    assert linked_list.value_at(1) == "fourth", "❌ 再次移除後第二個元素不正確"
    print("✅ 移除中間節點正確")


def test_remove_value_with_duplicates():
    """測試有重複值的 remove_value()"""
    print("\n=== 測試重複值的 remove_value() ===")

    # 測試 1: 移除第一個重複值
    print("\n1. 測試移除第一個重複值...")
    linked_list = SinglyLinkedList()
    test_data = ["a", "b", "a", "c", "a"]  # 'a' 出現在位置 0, 2, 4
    for item in test_data:
        linked_list.push_back(item)

    # 移除第一個 'a' (位置 0)
    linked_list.remove_value("a")
    assert linked_list.size() == 4, "❌ 移除第一個重複值後 size 不正確"

    # 檢查剩餘元素: ["b", "a", "c", "a"]
    expected_remaining = ["b", "a", "c", "a"]
    for i, expected in enumerate(expected_remaining):
        actual = linked_list.value_at(i)
        assert actual == expected, f"❌ 移除第一個重複值後位置 {i} 期望 {expected}，實際 {actual}"
    print("✅ 移除第一個重複值正確")

    # 測試 2: 再次移除（現在第一個 'a' 在位置 1）
    print("\n2. 測試再次移除重複值...")
    linked_list.remove_value("a")
    assert linked_list.size() == 3, "❌ 再次移除重複值後 size 不正確"

    # 檢查剩餘元素: ["b", "c", "a"]
    expected_remaining = ["b", "c", "a"]
    for i, expected in enumerate(expected_remaining):
        actual = linked_list.value_at(i)
        assert actual == expected, f"❌ 再次移除重複值後位置 {i} 期望 {expected}，實際 {actual}"
    print("✅ 再次移除重複值正確")

    # 測試 3: 移除最後一個重複值
    print("\n3. 測試移除最後一個重複值...")
    linked_list.remove_value("a")  # 移除最後一個 'a'
    assert linked_list.size() == 2, "❌ 移除最後一個重複值後 size 不正確"

    # 檢查剩餘元素: ["b", "c"]
    expected_remaining = ["b", "c"]
    for i, expected in enumerate(expected_remaining):
        actual = linked_list.value_at(i)
        assert actual == expected, f"❌ 移除最後一個重複值後位置 {i} 期望 {expected}，實際 {actual}"
    print("✅ 移除最後一個重複值正確")

    # 測試 4: 再次嘗試移除已不存在的值
    print("\n4. 測試移除已不存在的值...")
    original_size = linked_list.size()
    linked_list.remove_value("a")  # 'a' 已經不存在了

    assert linked_list.size() == original_size, "❌ 移除不存在值後 size 不應該改變"
    assert linked_list.value_at(0) == "b", "❌ 移除不存在值後列表內容不應該改變"
    assert linked_list.value_at(1) == "c", "❌ 移除不存在值後列表內容不應該改變"
    print("✅ 移除已不存在值正確（無變化）")


def test_remove_value_different_types():
    """測試不同數據類型的 remove_value()"""
    print("\n=== 測試不同數據類型的 remove_value() ===")

    linked_list = SinglyLinkedList()

    # 添加不同類型的數據
    test_data = [42, 3.14, "hello", [1, 2, 3], {"key": "value"}, None, True, False]
    for item in test_data:
        linked_list.push_back(item)

    original_size = linked_list.size()

    # 測試移除整數
    linked_list.remove_value(42)
    assert linked_list.size() == original_size - 1, "❌ 移除整數後 size 不正確"

    # 測試移除浮點數
    linked_list.remove_value(3.14)
    assert linked_list.size() == original_size - 2, "❌ 移除浮點數後 size 不正確"

    # 測試移除字符串
    linked_list.remove_value("hello")
    assert linked_list.size() == original_size - 3, "❌ 移除字符串後 size 不正確"

    # 測試移除列表
    linked_list.remove_value([1, 2, 3])
    assert linked_list.size() == original_size - 4, "❌ 移除列表後 size 不正確"

    # 測試移除字典
    linked_list.remove_value({"key": "value"})
    assert linked_list.size() == original_size - 5, "❌ 移除字典後 size 不正確"

    # 測試移除 None
    linked_list.remove_value(None)
    assert linked_list.size() == original_size - 6, "❌ 移除 None 後 size 不正確"

    # 測試移除布爾值
    linked_list.remove_value(True)
    assert linked_list.size() == original_size - 7, "❌ 移除 True 後 size 不正確"

    linked_list.remove_value(False)
    assert linked_list.size() == original_size - 8, "❌ 移除 False 後 size 不正確"

    # 現在列表應該是空的
    assert linked_list.empty(), "❌ 移除所有元素後列表應該為空"

    print("✅ 不同數據類型 remove_value() 正確")


def test_remove_value_integration():
    """測試 remove_value() 與其他操作的整合"""
    print("\n=== 測試 remove_value() 與其他操作整合 ===")

    linked_list = SinglyLinkedList()

    # 建立測試數據
    linked_list.push_back("A")
    linked_list.push_front("B")  # ["B", "A"]
    linked_list.insert(1, "C")   # ["B", "C", "A"]
    linked_list.push_back("D")   # ["B", "C", "A", "D"]

    print("\n1. 測試 remove_value 與插入操作混合...")

    # 移除中間的元素
    linked_list.remove_value("C")  # ["B", "A", "D"]
    assert linked_list.size() == 3, "❌ 移除後 size 不正確"
    assert linked_list.value_at(1) == "A", "❌ 移除後元素位置不正確"

    # 再插入一個元素
    linked_list.insert(2, "E")  # ["B", "A", "E", "D"]
    assert linked_list.size() == 4, "❌ 插入後 size 不正確"

    # 移除頭元素
    linked_list.remove_value("B")  # ["A", "E", "D"]
    assert linked_list.front() == "A", "❌ 移除頭元素後 front() 不正確"

    print("✅ remove_value 與插入操作混合正確")

    print("\n2. 測試 remove_value 與反轉操作混合...")

    # 當前: ["A", "E", "D"]
    linked_list.reverse()  # ["D", "E", "A"]

    # 移除中間元素
    linked_list.remove_value("E")  # ["D", "A"]
    assert linked_list.size() == 2, "❌ 反轉後移除，size 不正確"
    assert linked_list.value_at(0) == "D", "❌ 反轉後移除，第一個元素不正確"
    assert linked_list.value_at(1) == "A", "❌ 反轉後移除，第二個元素不正確"

    print("✅ remove_value 與反轉操作混合正確")

    print("\n3. 測試 remove_value 與 value_n_from_end 混合...")

    # 當前: ["D", "A"]
    linked_list.push_back("F")  # ["D", "A", "F"]

    # 使用 value_n_from_end 獲取值，然後移除
    last_value = linked_list.value_n_from_end(1)  # "F"
    linked_list.remove_value(last_value)  # ["D", "A"]

    assert linked_list.size() == 2, "❌ value_n_from_end 與 remove_value 混合後 size 不正確"
    assert linked_list.back() == "A", "❌ value_n_from_end 與 remove_value 混合後 back() 不正確"

    print("✅ remove_value 與 value_n_from_end 混合正確")


def main():
    """執行所有階段6測試"""
    print("🚀 開始階段6測試：數值操作測試")
    print("測試範圍：前階段功能 + remove_value()")

    try:
        # 執行各項測試
        test_previous_functionality()
        test_remove_value_basic_functionality()
        test_remove_value_with_duplicates()
        test_remove_value_different_types()
        test_remove_value_integration()

        print("\n" + "="*50)
        print("🎉 階段6測試全部通過！")
        print("✅ remove_value() 方法實作正確")
        print("✅ 重複值處理正確")
        print("✅ 不同數據類型處理正確")
        print("✅ 與前階段功能整合正常")
        print("\n📝 下一步：整合測試和邊界情況測試")
        print("   然後運行 python3 test_stage7.py")
        print("\n💡 提示：")
        print("   - remove_value() 只移除第一個匹配的值")
        print("   - 不存在的值不應拋出異常")
        print("   - 需要處理頭、中、尾三種刪除情況")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作，特別注意：")
        print("1. remove_value() 只移除第一個匹配的元素")
        print("2. 不存在的值應該靜默返回，不拋出異常")
        print("3. 需要正確處理刪除頭節點的情況")
        print("4. 刪除後要正確更新節點連接")
        print("5. 不同數據類型的比較要正確")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法和實作邏輯")
        sys.exit(1)


if __name__ == "__main__":
    main()