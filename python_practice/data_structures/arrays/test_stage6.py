#!/usr/bin/env python3
"""
階段6測試：前階段功能 + find()

這個階段測試查找功能，用於定位元素位置。
運行方式：python3 test_stage6.py
"""

import sys
sys.path.append('.')

exec(open('dynamic_array.py').read())


def test_previous_functionality():
    """重新測試前階段功能"""
    print("=== 測試前階段功能 ===")

    arr = DynamicArray()

    # 測試基本操作流程
    arr.push(1)
    arr.push(2)
    arr.push(3)

    assert arr.size() == 3
    assert arr.at(1) == 2

    arr.delete(1)  # 刪除中間元素
    assert arr.size() == 2
    assert arr.at(1) == 3

    arr.remove(1)  # 移除值為1的元素
    assert arr.size() == 1
    assert arr.at(0) == 3

    print("✅ 前階段功能依然正確")


def test_find_basic_functionality():
    """測試 find() 基本功能"""
    print("\n=== 測試 find() 基本功能 ===")

    arr = DynamicArray()

    # 測試 1: 空陣列查找
    print("\n1. 測試空陣列查找...")
    result = arr.find("anything")
    assert result == -1, f"❌ 空陣列查找應該回傳 -1，實際是 {result}"
    print("✅ 空陣列查找正確")

    # 測試 2: 查找存在的元素
    print("\n2. 測試查找存在的元素...")
    test_data = [10, "hello", [1, 2], None, True, 3.14]
    for item in test_data:
        arr.push(item)

    # 測試各種類型的查找
    assert arr.find(10) == 0, "❌ 查找整數失敗"
    assert arr.find("hello") == 1, "❌ 查找字符串失敗"
    assert arr.find([1, 2]) == 2, "❌ 查找列表失敗"
    assert arr.find(None) == 3, "❌ 查找 None 失敗"
    assert arr.find(True) == 4, "❌ 查找布爾值失敗"
    assert arr.find(3.14) == 5, "❌ 查找浮點數失敗"

    print("✅ 查找存在元素正確")

    # 測試 3: 查找不存在的元素
    print("\n3. 測試查找不存在的元素...")
    not_exist_items = [99, "not_exist", [3, 4], False, 2.71]

    for item in not_exist_items:
        result = arr.find(item)
        assert result == -1, f"❌ 查找不存在元素 {item} 應該回傳 -1，實際是 {result}"

    print("✅ 查找不存在元素正確")


def test_find_duplicate_elements():
    """測試 find() 處理重複元素"""
    print("\n=== 測試 find() 處理重複元素 ===")

    arr = DynamicArray()

    # 測試重複元素
    print("\n1. 測試重複元素查找...")
    test_sequence = ["A", "B", "A", "C", "A", "B"]
    for item in test_sequence:
        arr.push(item)
    # 陣列: ["A", "B", "A", "C", "A", "B"]

    # find() 應該回傳第一個匹配的位置
    assert arr.find("A") == 0, "❌ 應該回傳第一個 'A' 的位置 0"
    assert arr.find("B") == 1, "❌ 應該回傳第一個 'B' 的位置 1"
    assert arr.find("C") == 3, "❌ 應該回傳 'C' 的位置 3"

    print("✅ 重複元素查找正確（回傳第一個匹配）")

    # 測試數字重複
    print("\n2. 測試數字重複查找...")
    num_arr = DynamicArray()
    num_sequence = [1, 2, 1, 3, 1, 2, 4]
    for num in num_sequence:
        num_arr.push(num)
    # 陣列: [1, 2, 1, 3, 1, 2, 4]

    assert num_arr.find(1) == 0, "❌ 應該回傳第一個 1 的位置 0"
    assert num_arr.find(2) == 1, "❌ 應該回傳第一個 2 的位置 1"
    assert num_arr.find(3) == 3, "❌ 應該回傳 3 的位置 3"
    assert num_arr.find(4) == 6, "❌ 應該回傳 4 的位置 6"

    print("✅ 數字重複查找正確")


def test_find_with_complex_objects():
    """測試 find() 處理複雜對象"""
    print("\n=== 測試 find() 處理複雜對象 ===")

    arr = DynamicArray()

    # 測試各種複雜對象
    print("\n1. 測試複雜對象查找...")

    # 列表對象
    list_obj1 = [1, 2, 3]
    list_obj2 = [4, 5, 6]
    list_obj3 = [1, 2, 3]  # 與 list_obj1 內容相同但是不同對象

    # 字典對象
    dict_obj1 = {"key": "value", "num": 42}
    dict_obj2 = {"name": "test", "active": True}

    # 元組對象
    tuple_obj = (10, 20, 30)

    # 加入陣列
    complex_objects = [list_obj1, dict_obj1, list_obj2, tuple_obj, dict_obj2]
    for obj in complex_objects:
        arr.push(obj)

    # 測試查找相同引用的對象
    assert arr.find(list_obj1) == 0, "❌ 查找 list_obj1 失敗"
    assert arr.find(dict_obj1) == 1, "❌ 查找 dict_obj1 失敗"
    assert arr.find(list_obj2) == 2, "❌ 查找 list_obj2 失敗"
    assert arr.find(tuple_obj) == 3, "❌ 查找 tuple_obj 失敗"
    assert arr.find(dict_obj2) == 4, "❌ 查找 dict_obj2 失敗"

    # 測試查找內容相同但引用不同的對象（這個行為取決於Python的==比較）
    result = arr.find(list_obj3)
    if result == 0:
        print("✅ find() 使用值比較（內容相等即認為找到）")
    elif result == -1:
        print("✅ find() 使用引用比較（需要是同一個對象）")
    else:
        print(f"⚠️ 意外的查找結果: {result}")

    print("✅ 複雜對象查找測試完成")


def test_find_edge_cases():
    """測試 find() 邊界情況"""
    print("\n=== 測試 find() 邊界情況 ===")

    # 測試 1: 單元素陣列
    print("\n1. 測試單元素陣列...")
    single_arr = DynamicArray()
    single_arr.push("only_one")

    assert single_arr.find("only_one") == 0, "❌ 單元素查找失敗"
    assert single_arr.find("not_exist") == -1, "❌ 單元素陣列查找不存在元素失敗"
    print("✅ 單元素陣列查找正確")

    # 測試 2: 特殊值查找
    print("\n2. 測試特殊值查找...")
    special_arr = DynamicArray()
    special_values = [0, "", False, None, [], {}]
    for val in special_values:
        special_arr.push(val)

    assert special_arr.find(0) == 0, "❌ 查找數字 0 失敗"
    assert special_arr.find("") == 1, "❌ 查找空字符串失敗"
    assert special_arr.find(False) == 2, "❌ 查找 False 失敗"
    assert special_arr.find(None) == 3, "❌ 查找 None 失敗"

    # 注意：[] 和 {} 的查找行為取決於 Python 的比較邏輯
    empty_list_result = special_arr.find([])
    empty_dict_result = special_arr.find({})

    print(f"✅ 特殊值查找測試完成（空列表結果: {empty_list_result}, 空字典結果: {empty_dict_result}）")


def test_find_with_dynamic_operations():
    """測試 find() 與動態操作的整合"""
    print("\n=== 測試 find() 與動態操作整合 ===")

    arr = DynamicArray()

    print("\n1. 測試查找 → 刪除 → 再查找...")

    # 建立初始數據
    initial_data = ["X", "Y", "Z", "X", "W"]
    for item in initial_data:
        arr.push(item)
    # 陣列: ["X", "Y", "Z", "X", "W"]

    # 查找第一個 "X"
    pos1 = arr.find("X")
    assert pos1 == 0, f"❌ 第一次查找 'X' 應該在位置 0，實際是 {pos1}"

    # 刪除第一個 "X"
    arr.delete(0)
    # 陣列現在是: ["Y", "Z", "X", "W"]

    # 再次查找 "X"，應該找到原來第二個 "X"，現在在位置 2
    pos2 = arr.find("X")
    assert pos2 == 2, f"❌ 刪除後查找 'X' 應該在位置 2，實際是 {pos2}"

    print("✅ 查找與刪除操作整合正確")

    print("\n2. 測試查找 → 插入 → 再查找...")

    # 在位置 1 插入新元素
    arr.insert(1, "NEW")
    # 陣列現在是: ["Y", "NEW", "Z", "X", "W"]

    # 查找各元素的新位置
    assert arr.find("Y") == 0, "❌ 插入後 'Y' 位置錯誤"
    assert arr.find("NEW") == 1, "❌ 插入的 'NEW' 位置錯誤"
    assert arr.find("Z") == 2, "❌ 插入後 'Z' 位置錯誤"
    assert arr.find("X") == 3, "❌ 插入後 'X' 位置錯誤"
    assert arr.find("W") == 4, "❌ 插入後 'W' 位置錯誤"

    print("✅ 查找與插入操作整合正確")


def test_find_performance_pattern():
    """測試 find() 基本性能模式"""
    print("\n=== 測試 find() 基本性能模式 ===")

    arr = DynamicArray()

    # 建立較大的測試數據
    print("\n1. 測試較大數據集...")
    for i in range(100):
        arr.push(i)

    # 查找存在的元素（不同位置）
    assert arr.find(0) == 0, "❌ 查找第一個元素失敗"
    assert arr.find(50) == 50, "❌ 查找中間元素失敗"
    assert arr.find(99) == 99, "❌ 查找最後元素失敗"

    # 查找不存在的元素
    assert arr.find(100) == -1, "❌ 查找不存在元素失敗"
    assert arr.find(-1) == -1, "❌ 查找負數失敗"

    print("✅ 較大數據集查找正確")

    print("\n2. 測試查找與 remove 的配合...")

    # 使用 find 定位然後用 remove 移除
    target_value = 25
    pos_before_remove = arr.find(target_value)
    assert pos_before_remove == 25, "❌ remove 前定位失敗"

    arr.remove(target_value)
    pos_after_remove = arr.find(target_value)
    assert pos_after_remove == -1, "❌ remove 後應該找不到元素"

    print("✅ find 與 remove 配合正確")


def main():
    """執行所有階段6測試"""
    print("🚀 開始階段6測試：前階段功能 + find()")
    print("測試範圍：size(), capacity(), is_empty(), push(), at(), pop(), insert(), prepend(), delete(), remove(), find()")

    try:
        # 執行各項測試
        test_previous_functionality()
        test_find_basic_functionality()
        test_find_duplicate_elements()
        test_find_with_complex_objects()
        test_find_edge_cases()
        test_find_with_dynamic_operations()
        test_find_performance_pattern()

        print("\n" + "="*50)
        print("🎉 階段6測試全部通過！")
        print("✅ find() 方法實作正確")
        print("✅ 各種數據類型查找正確")
        print("✅ 重複元素處理正確")
        print("✅ 與其他操作整合正常")
        print("\n📝 下一步：實作動態容量管理")
        print("   然後運行 python3 test_stage7.py")
        print("\n💡 提示：find() 是線性搜索，複雜度是 O(n)。")
        print("   在實際應用中，如果需要頻繁查找，可以考慮使用雜湊表等更高效的數據結構。")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作，特別注意：")
        print("1. 查找邏輯是否正確")
        print("2. 是否正確處理空陣列")
        print("3. 是否正確處理不存在的元素")
        print("4. 重複元素是否回傳第一個匹配位置")
        print("5. 不同數據類型的比較是否正確")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法和實作邏輯")
        sys.exit(1)


if __name__ == "__main__":
    main()