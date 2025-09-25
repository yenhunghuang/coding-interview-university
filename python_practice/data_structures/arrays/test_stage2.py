#!/usr/bin/env python3
"""
階段2測試：基礎方法 + push() + at()

這個階段測試基礎方法加上新增和存取功能。
運行方式：python3 test_stage2.py
"""

import sys
sys.path.append('.')

exec(open('dynamic_array.py').read())


def test_basic_methods():
    """重新測試基礎方法（確保沒被破壞）"""
    print("=== 測試基礎方法 ===")

    arr = DynamicArray()
    assert arr.size() == 0, f"❌ size() 應該是 0"
    assert arr.capacity() == 16, f"❌ capacity() 應該是 16"
    assert arr.is_empty() == True, f"❌ is_empty() 應該是 True"
    print("✅ 基礎方法依然正確")


def test_push_functionality():
    """測試 push() 方法"""
    print("\n=== 測試 push() 方法 ===")

    arr = DynamicArray()

    # 測試 1: 單個元素
    print("\n1. 測試新增單個元素...")
    arr.push(42)

    assert arr.size() == 1, f"❌ push後 size() 應該是 1，實際是 {arr.size()}"
    assert arr.is_empty() == False, f"❌ push後 is_empty() 應該是 False"
    print("✅ 單個元素新增正確")

    # 測試 2: 多個元素
    print("\n2. 測試新增多個元素...")
    arr.push("hello")
    arr.push([1, 2, 3])
    arr.push(None)

    assert arr.size() == 4, f"❌ push後 size() 應該是 4，實際是 {arr.size()}"
    print("✅ 多個元素新增正確")

    # 測試 3: 容量管理（不超過初始容量）
    print("\n3. 測試容量變化...")
    initial_capacity = arr.capacity()

    # 新增更多元素，但不超過初始容量
    for i in range(12):  # 總共會有 4 + 12 = 16 個元素
        arr.push(f"item_{i}")

    assert arr.size() == 16, f"❌ size() 應該是 16，實際是 {arr.size()}"
    assert arr.capacity() == initial_capacity, f"❌ 容量不應該變化"
    print("✅ 在容量範圍內新增正確")


def test_at_functionality():
    """測試 at() 方法"""
    print("\n=== 測試 at() 方法 ===")

    arr = DynamicArray()

    # 先加入一些測試數據
    test_data = [10, "test", [1, 2], None, 42]
    for item in test_data:
        arr.push(item)

    # 測試 1: 正常索引存取
    print("\n1. 測試正常索引存取...")
    for i in range(len(test_data)):
        result = arr.at(i)
        expected = test_data[i]
        assert result == expected, f"❌ at({i}) 應該是 {expected}，實際是 {result}"
    print("✅ 正常索引存取正確")

    # 測試 2: 邊界索引
    print("\n2. 測試邊界索引...")

    # 測試第一個和最後一個索引
    assert arr.at(0) == test_data[0], f"❌ at(0) 不正確"
    assert arr.at(arr.size() - 1) == test_data[-1], f"❌ at(size-1) 不正確"
    print("✅ 邊界索引存取正確")

    # 測試 3: 無效索引
    print("\n3. 測試無效索引...")

    invalid_indices = [-1, arr.size(), arr.size() + 10, 100]

    for idx in invalid_indices:
        try:
            result = arr.at(idx)
            print(f"❌ at({idx}) 應該拋出 IndexError")
        except IndexError:
            print(f"✅ at({idx}) 正確拋出 IndexError")
        except Exception as e:
            print(f"⚠️ at({idx}) 拋出其他異常: {e}")

    # 測試 4: 空陣列存取
    print("\n4. 測試空陣列存取...")
    empty_arr = DynamicArray()

    try:
        empty_arr.at(0)
        print("❌ 空陣列的 at(0) 應該拋出 IndexError")
    except IndexError:
        print("✅ 空陣列存取正確拋出 IndexError")


def test_push_at_integration():
    """測試 push 和 at 的整合"""
    print("\n=== 測試 push 和 at 整合 ===")

    arr = DynamicArray()

    # 測試：交替使用 push 和 at
    print("\n1. 測試交替使用 push 和 at...")

    arr.push(1)
    assert arr.at(0) == 1, "❌ 第一次 push 後 at(0) 不正確"

    arr.push(2)
    assert arr.at(0) == 1 and arr.at(1) == 2, "❌ 第二次 push 後存取不正確"

    arr.push(3)
    assert arr.at(2) == 3, "❌ 第三次 push 後存取不正確"

    print("✅ push 和 at 整合正常")

    # 測試：大量數據
    print("\n2. 測試大量數據...")
    large_arr = DynamicArray()

    # 新增 100 個元素
    for i in range(100):
        large_arr.push(i * i)  # 平方數

    # 隨機檢查幾個位置
    test_positions = [0, 10, 50, 99]
    for pos in test_positions:
        expected = pos * pos
        actual = large_arr.at(pos)
        assert actual == expected, f"❌ 位置 {pos} 的值不正確"

    print("✅ 大量數據處理正確")


def test_edge_cases():
    """測試邊界情況"""
    print("\n=== 測試邊界情況 ===")

    # 測試 1: 最小容量陣列
    print("\n1. 測試最小容量陣列...")
    small_arr = DynamicArray(1)

    small_arr.push("only_one")
    assert small_arr.size() == 1
    assert small_arr.at(0) == "only_one"
    print("✅ 最小容量陣列正常")

    # 測試 2: 不同資料類型
    print("\n2. 測試不同資料類型...")
    mixed_arr = DynamicArray()

    mixed_data = [42, "string", [1, 2, 3], {"key": "value"}, None, True, 3.14]

    for item in mixed_data:
        mixed_arr.push(item)

    for i, expected in enumerate(mixed_data):
        actual = mixed_arr.at(i)
        assert actual == expected, f"❌ 混合資料類型位置 {i} 不正確"

    print("✅ 不同資料類型處理正確")


def main():
    """執行所有階段2測試"""
    print("🚀 開始階段2測試：基礎方法 + push() + at()")
    print("測試範圍：size(), capacity(), is_empty(), push(), at()")

    try:
        # 執行各項測試
        test_basic_methods()
        test_push_functionality()
        test_at_functionality()
        test_push_at_integration()
        test_edge_cases()

        print("\n" + "="*50)
        print("🎉 階段2測試全部通過！")
        print("✅ push() 和 at() 方法實作正確")
        print("✅ 與基礎方法整合正常")
        print("\n📝 下一步：實作 pop() 方法")
        print("   然後運行 python3 test_stage3.py")

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