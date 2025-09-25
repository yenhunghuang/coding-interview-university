#!/usr/bin/env python3
"""
階段8測試：前階段功能 + Python 魔術方法（可選進階功能）

這個階段測試 Python 特有的魔術方法，讓動態陣列更像內建的 list。
包括：__len__, __getitem__, __setitem__, __str__, __repr__, __iter__, __contains__
運行方式：python3 test_stage8.py
"""

import sys
sys.path.append('.')

exec(open('dynamic_array.py').read())


def test_previous_functionality():
    """重新測試前階段功能"""
    print("=== 測試前階段功能 ===")

    arr = DynamicArray()

    # 測試核心功能流程
    for i in range(10):
        arr.push(i)

    assert arr.size() == 10
    assert arr.find(5) == 5

    # 測試動態容量（如果從小容量開始）
    small_arr = DynamicArray(4)
    for i in range(8):  # 觸發擴容
        small_arr.push(i)
    assert small_arr.capacity() > 4

    print("✅ 前階段功能依然正確")


def test_len_magic_method():
    """測試 __len__ 魔術方法"""
    print("\n=== 測試 __len__ 魔術方法 ===")

    arr = DynamicArray()

    try:
        # 測試空陣列
        assert len(arr) == 0, "❌ 空陣列 len() 應該是 0"
        print("✅ 空陣列 len() 正確")

        # 測試有元素的陣列
        test_data = [1, 2, 3, 4, 5]
        for item in test_data:
            arr.push(item)

        assert len(arr) == 5, "❌ len() 與 size() 不一致"
        assert len(arr) == arr.size(), "❌ len() 應該與 size() 返回相同值"
        print("✅ len() 方法實作正確")

        # 測試動態變化
        arr.pop()
        assert len(arr) == 4, "❌ pop 後 len() 不正確"

        arr.delete(0)
        assert len(arr) == 3, "❌ delete 後 len() 不正確"

        arr.insert(1, "inserted")
        assert len(arr) == 4, "❌ insert 後 len() 不正確"

        print("✅ 動態操作後 len() 正確")

    except (TypeError, NotImplementedError):
        print("ℹ️ __len__ 方法尚未實作（這是可以接受的）")
    except Exception as e:
        print(f"⚠️ __len__ 方法實作有問題: {e}")


def test_getitem_magic_method():
    """測試 __getitem__ 魔術方法（支援 arr[index]）"""
    print("\n=== 測試 __getitem__ 魔術方法 ===")

    arr = DynamicArray()
    test_data = ["A", "B", "C", "D", "E"]
    for item in test_data:
        arr.push(item)

    try:
        # 測試正向索引
        assert arr[0] == "A", "❌ arr[0] 不正確"
        assert arr[2] == "C", "❌ arr[2] 不正確"
        assert arr[4] == "E", "❌ arr[4] 不正確"
        print("✅ 正向索引存取正確")

        # 測試負向索引（如果有實作）
        try:
            assert arr[-1] == "E", "❌ arr[-1] 應該是最後一個元素"
            assert arr[-2] == "D", "❌ arr[-2] 不正確"
            print("✅ 負向索引存取正確")
        except (IndexError, NotImplementedError):
            print("ℹ️ 負向索引未實作（這是可以接受的）")

        # 測試索引錯誤處理
        try:
            _ = arr[10]  # 超出範圍
            print("❌ 應該拋出 IndexError")
        except IndexError:
            print("✅ 無效索引正確拋出 IndexError")

        # 測試與 at() 方法的一致性
        for i in range(len(test_data)):
            assert arr[i] == arr.at(i), f"❌ arr[{i}] 與 arr.at({i}) 不一致"
        print("✅ 與 at() 方法一致")

    except (TypeError, NotImplementedError):
        print("ℹ️ __getitem__ 方法尚未實作（這是可以接受的）")
    except Exception as e:
        print(f"⚠️ __getitem__ 方法實作有問題: {e}")


def test_setitem_magic_method():
    """測試 __setitem__ 魔術方法（支援 arr[index] = value）"""
    print("\n=== 測試 __setitem__ 魔術方法 ===")

    arr = DynamicArray()
    test_data = [1, 2, 3, 4, 5]
    for item in test_data:
        arr.push(item)

    try:
        # 測試設置值
        arr[1] = "modified"
        assert arr[1] == "modified", "❌ arr[1] 設置後值不正確"
        assert arr[0] == 1, "❌ 設置 arr[1] 影響了其他元素"
        assert arr[2] == 3, "❌ 設置 arr[1] 影響了其他元素"
        print("✅ 索引設置值正確")

        # 測試設置不同類型的值
        arr[0] = [1, 2, 3]
        arr[2] = {"key": "value"}
        arr[3] = None

        assert arr[0] == [1, 2, 3], "❌ 設置列表值不正確"
        assert arr[2] == {"key": "value"}, "❌ 設置字典值不正確"
        assert arr[3] is None, "❌ 設置 None 值不正確"
        print("✅ 不同類型值設置正確")

        # 測試負向索引設置（如果有實作）
        try:
            arr[-1] = "last_modified"
            assert arr[-1] == "last_modified", "❌ 負向索引設置不正確"
            print("✅ 負向索引設置正確")
        except (IndexError, NotImplementedError):
            print("ℹ️ 負向索引設置未實作（這是可以接受的）")

        # 測試索引錯誤處理
        try:
            arr[10] = "should_fail"  # 超出範圍
            print("❌ 應該拋出 IndexError")
        except IndexError:
            print("✅ 無效索引設置正確拋出 IndexError")

        # 驗證 size 不變
        assert arr.size() == 5, "❌ __setitem__ 不應該改變陣列大小"
        print("✅ 設置值不改變陣列大小")

    except (TypeError, NotImplementedError):
        print("ℹ️ __setitem__ 方法尚未實作（這是可以接受的）")
    except Exception as e:
        print(f"⚠️ __setitem__ 方法實作有問題: {e}")


def test_str_and_repr_magic_methods():
    """測試 __str__ 和 __repr__ 魔術方法"""
    print("\n=== 測試 __str__ 和 __repr__ 魔術方法 ===")

    # 測試空陣列
    empty_arr = DynamicArray()
    try:
        empty_str = str(empty_arr)
        print(f"✅ 空陣列 str(): '{empty_str}'")
        assert isinstance(empty_str, str), "❌ str() 應該返回字符串"
    except (TypeError, NotImplementedError):
        print("ℹ️ __str__ 方法尚未實作（這是可以接受的）")

    # 測試有元素的陣列
    arr = DynamicArray()
    test_data = [1, "hello", [1, 2], None]
    for item in test_data:
        arr.push(item)

    try:
        arr_str = str(arr)
        print(f"✅ 陣列 str(): '{arr_str}'")

        # 基本驗證：字符串應該包含陣列的基本信息
        assert "1" in arr_str or "hello" in arr_str, "❌ str() 應該包含元素信息"

    except (TypeError, NotImplementedError):
        print("ℹ️ __str__ 方法尚未實作（這是可以接受的）")
    except Exception as e:
        print(f"⚠️ __str__ 方法實作有問題: {e}")

    # 測試 __repr__
    try:
        arr_repr = repr(arr)
        print(f"✅ 陣列 repr(): '{arr_repr}'")
        assert isinstance(arr_repr, str), "❌ repr() 應該返回字符串"
    except (TypeError, NotImplementedError):
        print("ℹ️ __repr__ 方法尚未實作（這是可以接受的）")
    except Exception as e:
        print(f"⚠️ __repr__ 方法實作有問題: {e}")


def test_iter_magic_method():
    """測試 __iter__ 魔術方法（支援 for 迴圈）"""
    print("\n=== 測試 __iter__ 魔術方法 ===")

    arr = DynamicArray()
    test_data = ["apple", "banana", "cherry", "date"]
    for item in test_data:
        arr.push(item)

    try:
        # 測試 for 迴圈
        collected_items = []
        for item in arr:
            collected_items.append(item)

        assert collected_items == test_data, "❌ 迭代結果與原始數據不符"
        print("✅ for 迴圈迭代正確")

        # 測試多次迭代
        second_iteration = list(arr)
        assert second_iteration == test_data, "❌ 第二次迭代結果不正確"
        print("✅ 多次迭代正確")

        # 測試空陣列迭代
        empty_arr = DynamicArray()
        empty_list = list(empty_arr)
        assert empty_list == [], "❌ 空陣列迭代應該得到空列表"
        print("✅ 空陣列迭代正確")

        # 測試與內建函數的配合
        arr_list = list(arr)
        assert arr_list == test_data, "❌ list() 轉換不正確"

        arr_tuple = tuple(arr)
        assert arr_tuple == tuple(test_data), "❌ tuple() 轉換不正確"

        print("✅ 與內建函數配合正確")

    except (TypeError, NotImplementedError):
        print("ℹ️ __iter__ 方法尚未實作（這是可以接受的）")
    except Exception as e:
        print(f"⚠️ __iter__ 方法實作有問題: {e}")


def test_contains_magic_method():
    """測試 __contains__ 魔術方法（支援 in 操作符）"""
    print("\n=== 測試 __contains__ 魔術方法 ===")

    arr = DynamicArray()
    test_data = [10, "hello", [1, 2], None, True]
    for item in test_data:
        arr.push(item)

    try:
        # 測試存在的元素
        assert 10 in arr, "❌ 10 應該在陣列中"
        assert "hello" in arr, "❌ 'hello' 應該在陣列中"
        assert [1, 2] in arr, "❌ [1, 2] 應該在陣列中"
        assert None in arr, "❌ None 應該在陣列中"
        assert True in arr, "❌ True 應該在陣列中"
        print("✅ 存在元素檢測正確")

        # 測試不存在的元素
        assert 99 not in arr, "❌ 99 不應該在陣列中"
        assert "world" not in arr, "❌ 'world' 不應該在陣列中"
        assert [3, 4] not in arr, "❌ [3, 4] 不應該在陣列中"
        assert False not in arr, "❌ False 不應該在陣列中"
        print("✅ 不存在元素檢測正確")

        # 測試空陣列
        empty_arr = DynamicArray()
        assert "anything" not in empty_arr, "❌ 空陣列不應該包含任何元素"
        print("✅ 空陣列檢測正確")

        # 測試與 find() 方法的一致性
        for item in test_data:
            contains_result = item in arr
            find_result = arr.find(item) != -1
            assert contains_result == find_result, f"❌ '{item}' 的 in 和 find() 結果不一致"

        print("✅ 與 find() 方法一致")

    except (TypeError, NotImplementedError):
        print("ℹ️ __contains__ 方法尚未實作（這是可以接受的）")
    except Exception as e:
        print(f"⚠️ __contains__ 方法實作有問題: {e}")


def test_magic_methods_integration():
    """測試魔術方法的整合使用"""
    print("\n=== 測試魔術方法整合使用 ===")

    arr = DynamicArray()

    try:
        # 建立測試數據
        for i in range(5):
            arr.push(f"item_{i}")

        print("\n1. 測試組合使用...")

        # 使用 len() 獲取長度，然後用 [] 存取
        if hasattr(arr, '__len__'):
            for i in range(len(arr)):
                if hasattr(arr, '__getitem__'):
                    item = arr[i]
                    print(f"   arr[{i}] = {item}")

        # 使用 in 檢查，然後用 [] 修改
        if hasattr(arr, '__contains__') and hasattr(arr, '__setitem__'):
            if "item_2" in arr:
                arr[2] = "modified_item_2"
                print("   找到 item_2 並修改為 modified_item_2")

        # 使用 for 迴圈遍歷
        if hasattr(arr, '__iter__'):
            print("   使用 for 迴圈遍歷:")
            for i, item in enumerate(arr):
                print(f"      [{i}]: {item}")

        # 測試與 Python 內建功能的整合
        if hasattr(arr, '__iter__'):
            # 轉換為內建類型
            as_list = list(arr)
            as_tuple = tuple(arr)
            print(f"   轉換為 list: {as_list}")
            print(f"   轉換為 tuple: {as_tuple}")

        # 測試與 str() 的整合
        if hasattr(arr, '__str__'):
            print(f"   字符串表示: {str(arr)}")

        print("✅ 魔術方法整合使用正常")

    except Exception as e:
        print(f"⚠️ 魔術方法整合使用有問題: {e}")


def test_python_list_like_behavior():
    """測試類似 Python list 的行為"""
    print("\n=== 測試類似 Python list 的行為 ===")

    arr = DynamicArray()
    python_list = []

    # 並行操作測試
    test_operations = [
        ("push", "hello"),
        ("push", 42),
        ("push", [1, 2, 3]),
        ("push", None),
    ]

    print("\n1. 並行操作比較...")
    for operation, value in test_operations:
        if operation == "push":
            arr.push(value)
            python_list.append(value)

    # 比較基本屬性
    try:
        if hasattr(arr, '__len__'):
            assert len(arr) == len(python_list), "❌ 長度與 Python list 不一致"
            print("✅ 長度與 Python list 一致")

        # 比較元素存取
        if hasattr(arr, '__getitem__'):
            for i in range(len(python_list)):
                assert arr[i] == python_list[i], f"❌ 位置 {i} 元素與 Python list 不一致"
            print("✅ 元素存取與 Python list 一致")

        # 比較包含關係
        if hasattr(arr, '__contains__'):
            for item in python_list:
                assert item in arr, f"❌ {item} 在 Python list 中但不在 DynamicArray 中"
            print("✅ 包含關係與 Python list 一致")

        # 比較迭代行為
        if hasattr(arr, '__iter__'):
            arr_items = list(arr)
            assert arr_items == python_list, "❌ 迭代結果與 Python list 不一致"
            print("✅ 迭代行為與 Python list 一致")

    except Exception as e:
        print(f"⚠️ 與 Python list 比較時出現問題: {e}")

    print("✅ Python list 行為比較完成")


def main():
    """執行所有階段8測試"""
    print("🚀 開始階段8測試：前階段功能 + Python 魔術方法")
    print("測試範圍：所有前階段功能 + __len__, __getitem__, __setitem__, __str__, __repr__, __iter__, __contains__")
    print("\n💡 注意：魔術方法是可選功能，未實作不會影響基本功能")

    try:
        # 執行各項測試
        test_previous_functionality()
        test_len_magic_method()
        test_getitem_magic_method()
        test_setitem_magic_method()
        test_str_and_repr_magic_methods()
        test_iter_magic_method()
        test_contains_magic_method()
        test_magic_methods_integration()
        test_python_list_like_behavior()

        print("\n" + "="*60)
        print("🎉 階段8測試全部完成！")
        print("✅ 所有前階段功能正常")
        print("✅ Python 魔術方法測試完成")
        print("✅ 與 Python 內建 list 行為比較完成")
        print("\n🎊 恭喜！你已經完成了完整的動態陣列實作！")
        print("\n📚 學習成果總結：")
        print("   ✅ 基礎方法：size(), capacity(), is_empty()")
        print("   ✅ 核心操作：push(), at(), pop()")
        print("   ✅ 插入操作：insert(), prepend()")
        print("   ✅ 刪除操作：delete(), remove()")
        print("   ✅ 查找功能：find()")
        print("   ✅ 動態容量：自動擴容/縮容")
        print("   ✅ Python 整合：魔術方法")
        print("\n🚀 下一步建議：")
        print("   1. 研究時間複雜度分析")
        print("   2. 學習下一個數據結構（鏈表）")
        print("   3. 解決 LeetCode 陣列相關題目")
        print("   4. 比較不同程式語言的陣列實作")
        print("\n💡 核心概念掌握：")
        print("   - 攤還分析：push/pop 平均 O(1)")
        print("   - 空間換時間：預分配記憶體提高效率")
        print("   - 動態擴容：平衡記憶體使用和性能")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法")
        sys.exit(1)


if __name__ == "__main__":
    main()