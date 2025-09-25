#!/usr/bin/env python3
"""
最終階段測試：完整功能測試

這個腳本測試所有功能，包括動態容量管理。
運行方式：python3 test_stage_final.py
"""

import sys
sys.path.append('.')

exec(open('dynamic_array.py').read())


def test_all_basic_operations():
    """測試所有基本操作"""
    print("=== 測試所有基本操作 ===")

    arr = DynamicArray()

    # 測試空陣列
    assert arr.size() == 0
    assert arr.capacity() >= 16  # 至少是16
    assert arr.is_empty() == True

    # 測試 push 和 at
    test_data = [1, "hello", [1, 2], None, 42]
    for item in test_data:
        arr.push(item)

    for i, expected in enumerate(test_data):
        assert arr.at(i) == expected

    # 測試 find
    assert arr.find(1) == 0
    assert arr.find("hello") == 1
    assert arr.find("not_exist") == -1

    # 測試 insert
    arr.insert(2, "inserted")
    assert arr.at(2) == "inserted"
    assert arr.at(3) == [1, 2]  # 原來位置2的元素移到位置3

    # 測試 prepend
    arr.prepend("first")
    assert arr.at(0) == "first"
    assert arr.at(1) == 1  # 原來的第一個元素

    # 測試 pop
    original_size = arr.size()
    last_item = arr.at(arr.size() - 1)
    popped = arr.pop()
    assert popped == last_item
    assert arr.size() == original_size - 1

    # 測試 delete
    arr.delete(0)  # 刪除第一個元素
    assert arr.at(0) == 1  # 原來的第二個元素變成第一個

    # 測試 remove
    arr.remove(1)  # 移除值為1的元素
    assert arr.find(1) == -1  # 應該找不到了

    print("✅ 所有基本操作正確")


def test_dynamic_capacity():
    """測試動態容量管理"""
    print("\n=== 測試動態容量管理 ===")

    # 從小容量開始測試擴容
    arr = DynamicArray(4)
    assert arr.capacity() == 4

    # 填滿初始容量
    for i in range(4):
        arr.push(i)

    assert arr.size() == 4
    assert arr.capacity() == 4

    # 新增第5個元素，應該觸發擴容
    arr.push("trigger_expand")
    assert arr.size() == 5

    # 容量應該擴大（通常是2倍）
    new_capacity = arr.capacity()
    assert new_capacity > 4, f"容量應該擴大，但還是 {new_capacity}"

    print(f"✅ 擴容測試通過: {4} -> {new_capacity}")

    # 測試縮容（如果實作了的話）
    # 移除大部分元素
    while arr.size() > 2:
        arr.pop()

    # 某些實作可能會在使用率很低時縮容
    final_capacity = arr.capacity()
    print(f"✅ 縮容測試: 最終容量 {final_capacity} (size: {arr.size()})")


def test_edge_cases():
    """測試邊界情況"""
    print("\n=== 測試邊界情況 ===")

    # 測試最小容量
    arr = DynamicArray(1)
    arr.push("only")
    assert arr.size() == 1
    assert arr.at(0) == "only"

    popped = arr.pop()
    assert popped == "only"
    assert arr.is_empty()

    # 測試錯誤處理
    try:
        DynamicArray(0)
        assert False, "應該拋出異常"
    except ValueError:
        pass

    try:
        arr.at(0)  # 空陣列存取
        assert False, "應該拋出異常"
    except IndexError:
        pass

    try:
        arr.pop()  # 空陣列 pop
        assert False, "應該拋出異常"
    except IndexError:
        pass

    print("✅ 邊界情況處理正確")


def test_large_data():
    """測試大量數據"""
    print("\n=== 測試大量數據 ===")

    arr = DynamicArray()

    # 新增1000個元素
    for i in range(1000):
        arr.push(i * i)

    assert arr.size() == 1000

    # 隨機檢查一些位置
    test_positions = [0, 100, 500, 999]
    for pos in test_positions:
        expected = pos * pos
        actual = arr.at(pos)
        assert actual == expected, f"位置 {pos} 的值不正確"

    # 移除所有元素
    while not arr.is_empty():
        arr.pop()

    assert arr.size() == 0
    assert arr.is_empty()

    print("✅ 大量數據處理正確")


def test_python_integration():
    """測試Python整合功能（如果實作了魔術方法）"""
    print("\n=== 測試Python整合 ===")

    arr = DynamicArray()
    arr.push(1)
    arr.push(2)
    arr.push(3)

    # 測試 __len__ (如果實作了)
    try:
        assert len(arr) == 3, "len() 不正確"
        print("✅ len() 支援正確")
    except (TypeError, NotImplementedError):
        print("ℹ️ len() 尚未實作")

    # 測試 __getitem__ (如果實作了)
    try:
        assert arr[1] == 2, "arr[index] 不正確"
        print("✅ arr[index] 支援正確")
    except (TypeError, NotImplementedError):
        print("ℹ️ arr[index] 尚未實作")

    # 測試 __setitem__ (如果實作了)
    try:
        arr[1] = "changed"
        assert arr[1] == "changed", "arr[index] = value 不正確"
        print("✅ arr[index] = value 支援正確")
    except (TypeError, NotImplementedError):
        print("ℹ️ arr[index] = value 尚未實作")

    # 測試 __str__ (如果實作了)
    try:
        str_repr = str(arr)
        assert "1" in str_repr or "changed" in str_repr, "str() 結果異常"
        print(f"✅ str() 支援正確: {str_repr}")
    except (TypeError, NotImplementedError):
        print("ℹ️ str() 尚未實作")


def main():
    """執行完整測試"""
    print("🚀 開始完整功能測試")
    print("測試所有 DynamicArray 功能")

    try:
        test_all_basic_operations()
        test_dynamic_capacity()
        test_edge_cases()
        test_large_data()
        test_python_integration()

        print("\n" + "="*60)
        print("🎉 完整功能測試全部通過！")
        print("✅ DynamicArray 實作完成且正確")
        print("✅ 所有基本操作正常")
        print("✅ 動態容量管理正常")
        print("✅ 邊界情況處理正確")
        print("✅ 大量數據處理正常")
        print("\n🎊 恭喜！你已經成功實作了一個完整的動態陣列！")
        print("\n📚 接下來可以：")
        print("1. 學習下一個數據結構（Linked Lists）")
        print("2. 解決 LeetCode 陣列相關題目")
        print("3. 比較你的實作與 Python list 的差異")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查對應功能的實作")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼")
        sys.exit(1)


if __name__ == "__main__":
    main()