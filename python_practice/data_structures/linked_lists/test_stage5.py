#!/usr/bin/env python3
"""
階段5測試：進階演算法測試 - reverse(), value_n_from_end()

這個階段測試演算法性較強的操作，包括：
- reverse() - 反轉整個列表
- value_n_from_end(n) - 獲取從尾端數第n個元素的值
- 各種邊界條件和演算法正確性驗證

運行方式：python3 test_stage5.py

實作指引：
在 SinglyLinkedList 中新增這些方法：
- reverse() -> None：原地反轉列表，改變節點連接順序
- value_n_from_end(n) -> any：返回從尾端數第n個元素（1-based），越界拋出 IndexError

演算法提示：
- reverse(): 需要三個指標（prev, current, next）來重新連接節點
- value_n_from_end(): 可以用雙指標技巧或先計算長度再定位

時間複雜度：
- reverse(): O(n) - 需要遍歷一次重新連接
- value_n_from_end(): O(n) - 無論用哪種方法都需要遍歷

特別注意：
- reverse() 會改變列表結構，需要更新頭尾指標
- value_n_from_end() 使用1-based計數（n=1表示最後一個元素）
"""

import sys
sys.path.append('.')

exec(open('node.py').read())
exec(open('singly_linked_list.py').read())


def test_previous_functionality():
    """重新測試前階段功能（確保沒被破壞）"""
    print("=== 測試前階段功能 ===")

    linked_list = SinglyLinkedList()

    # 基礎方法和核心操作測試
    test_data = [1, 2, 3]
    for item in test_data:
        linked_list.push_back(item)

    assert linked_list.size() == 3
    assert linked_list.value_at(1) == 2

    # 插入和刪除測試
    linked_list.insert(1, "inserted")
    assert linked_list.value_at(1) == "inserted"
    assert linked_list.size() == 4

    linked_list.erase(1)
    assert linked_list.value_at(1) == 2
    assert linked_list.size() == 3

    print("✅ 前階段功能依然正確")


def test_reverse_basic_functionality():
    """測試 reverse() 基本功能"""
    print("\n=== 測試 reverse() 基本功能 ===")

    # 測試 1: 空列表反轉
    print("\n1. 測試空列表反轉...")
    empty_list = SinglyLinkedList()
    empty_list.reverse()

    assert empty_list.size() == 0, "❌ 空列表反轉後 size 應該還是 0"
    assert empty_list.empty() == True, "❌ 空列表反轉後應該還是空的"
    print("✅ 空列表反轉正確")

    # 測試 2: 單個元素列表反轉
    print("\n2. 測試單個元素列表反轉...")
    single_list = SinglyLinkedList()
    single_list.push_back("single")

    single_list.reverse()
    assert single_list.size() == 1, "❌ 單元素列表反轉後 size 不正確"
    assert single_list.value_at(0) == "single", "❌ 單元素列表反轉後元素不正確"
    assert single_list.front() == "single", "❌ 單元素列表反轉後 front() 不正確"
    assert single_list.back() == "single", "❌ 單元素列表反轉後 back() 不正確"
    print("✅ 單個元素列表反轉正確")

    # 測試 3: 兩個元素列表反轉
    print("\n3. 測試兩個元素列表反轉...")
    two_list = SinglyLinkedList()
    two_list.push_back("first")
    two_list.push_back("second")

    # 反轉前: ["first", "second"]
    two_list.reverse()
    # 反轉後: ["second", "first"]

    assert two_list.size() == 2, "❌ 兩元素列表反轉後 size 不正確"
    assert two_list.value_at(0) == "second", "❌ 反轉後第一個元素不正確"
    assert two_list.value_at(1) == "first", "❌ 反轉後第二個元素不正確"
    assert two_list.front() == "second", "❌ 反轉後 front() 不正確"
    assert two_list.back() == "first", "❌ 反轉後 back() 不正確"
    print("✅ 兩個元素列表反轉正確")

    # 測試 4: 多個元素列表反轉
    print("\n4. 測試多個元素列表反轉...")
    multi_list = SinglyLinkedList()
    original_data = ["A", "B", "C", "D", "E"]

    for item in original_data:
        multi_list.push_back(item)

    # 反轉前: ["A", "B", "C", "D", "E"]
    multi_list.reverse()
    # 反轉後: ["E", "D", "C", "B", "A"]

    expected_reversed = list(reversed(original_data))
    assert multi_list.size() == len(expected_reversed), "❌ 多元素列表反轉後 size 不正確"

    for i, expected in enumerate(expected_reversed):
        actual = multi_list.value_at(i)
        assert actual == expected, f"❌ 反轉後位置 {i} 期望 {expected}，實際 {actual}"

    assert multi_list.front() == "E", "❌ 反轉後 front() 不正確"
    assert multi_list.back() == "A", "❌ 反轉後 back() 不正確"
    print("✅ 多個元素列表反轉正確")


def test_reverse_twice():
    """測試連續兩次反轉（應該恢復原狀）"""
    print("\n=== 測試連續兩次反轉 ===")

    linked_list = SinglyLinkedList()
    original_data = [1, 2, 3, 4, 5]

    for item in original_data:
        linked_list.push_back(item)

    # 記錄原始狀態
    original_values = [linked_list.value_at(i) for i in range(linked_list.size())]

    # 反轉兩次
    linked_list.reverse()
    linked_list.reverse()

    # 應該恢復原狀
    assert linked_list.size() == len(original_data), "❌ 兩次反轉後 size 不正確"

    for i, expected in enumerate(original_data):
        actual = linked_list.value_at(i)
        assert actual == expected, f"❌ 兩次反轉後位置 {i} 期望 {expected}，實際 {actual}"

    print("✅ 連續兩次反轉正確恢復原狀")


def test_value_n_from_end_basic_functionality():
    """測試 value_n_from_end() 基本功能"""
    print("\n=== 測試 value_n_from_end() 基本功能 ===")

    # 測試 1: 空列表
    print("\n1. 測試空列表...")
    empty_list = SinglyLinkedList()

    try:
        empty_list.value_n_from_end(1)
        print("❌ 空列表 value_n_from_end(1) 應該拋出 IndexError")
    except IndexError:
        print("✅ 空列表 value_n_from_end(1) 正確拋出 IndexError")
    except Exception as e:
        print(f"⚠️ 空列表 value_n_from_end(1) 拋出其他異常: {e}")

    # 測試 2: 單個元素列表
    print("\n2. 測試單個元素列表...")
    single_list = SinglyLinkedList()
    single_list.push_back("only_one")

    # n=1 應該返回最後一個（也是唯一一個）元素
    value = single_list.value_n_from_end(1)
    assert value == "only_one", f"❌ value_n_from_end(1) 應該返回 'only_one'，實際返回 {value}"
    assert single_list.size() == 1, "❌ value_n_from_end() 不應該改變列表大小"

    # n=2 應該拋出異常
    try:
        single_list.value_n_from_end(2)
        print("❌ 單元素列表 value_n_from_end(2) 應該拋出 IndexError")
    except IndexError:
        print("✅ 單元素列表 value_n_from_end(2) 正確拋出 IndexError")

    print("✅ 單個元素列表 value_n_from_end() 正確")

    # 測試 3: 多個元素列表
    print("\n3. 測試多個元素列表...")
    multi_list = SinglyLinkedList()
    test_data = ["first", "second", "third", "fourth", "fifth"]  # 索引: 0, 1, 2, 3, 4

    for item in test_data:
        multi_list.push_back(item)

    # 測試從尾端數的各個位置
    # n=1: 最後一個元素 (index 4) -> "fifth"
    # n=2: 倒數第二個元素 (index 3) -> "fourth"
    # n=3: 倒數第三個元素 (index 2) -> "third"
    # n=4: 倒數第四個元素 (index 1) -> "second"
    # n=5: 倒數第五個元素 (index 0) -> "first"

    test_cases = [
        (1, "fifth"),   # 最後一個
        (2, "fourth"),  # 倒數第二個
        (3, "third"),   # 倒數第三個
        (4, "second"),  # 倒數第四個
        (5, "first"),   # 倒數第五個（第一個）
    ]

    for n, expected in test_cases:
        actual = multi_list.value_n_from_end(n)
        assert actual == expected, f"❌ value_n_from_end({n}) 期望 '{expected}'，實際 '{actual}'"
        print(f"✅ value_n_from_end({n}) = '{actual}' 正確")

    assert multi_list.size() == len(test_data), "❌ value_n_from_end() 不應該改變列表大小"
    print("✅ 多個元素列表 value_n_from_end() 正確")


def test_value_n_from_end_error_handling():
    """測試 value_n_from_end() 錯誤處理"""
    print("\n=== 測試 value_n_from_end() 錯誤處理 ===")

    linked_list = SinglyLinkedList()
    for i in range(5):
        linked_list.push_back(i)  # [0, 1, 2, 3, 4]

    # 有效的 n 值：1, 2, 3, 4, 5
    # 無效的 n 值：0, -1, 6, 10, 100

    valid_n_values = [1, 2, 3, 4, 5]
    invalid_n_values = [0, -1, 6, 10, 100]

    print("\n1. 測試有效 n 值...")
    for n in valid_n_values:
        try:
            value = linked_list.value_n_from_end(n)
            print(f"✅ n={n} 有效，值為 {value}")
        except Exception as e:
            print(f"❌ 有效 n 值 {n} 卻拋出異常: {e}")

    print("\n2. 測試無效 n 值...")
    for n in invalid_n_values:
        try:
            linked_list.value_n_from_end(n)
            print(f"❌ 無效 n 值 {n} 應該拋出異常")
        except IndexError:
            print(f"✅ 無效 n 值 {n} 正確拋出 IndexError")
        except Exception as e:
            print(f"⚠️ 無效 n 值 {n} 拋出其他異常: {e}")


def test_reverse_and_value_n_from_end_integration():
    """測試 reverse() 和 value_n_from_end() 的整合"""
    print("\n=== 測試 reverse() 和 value_n_from_end() 整合 ===")

    linked_list = SinglyLinkedList()
    original_data = ["A", "B", "C", "D", "E"]

    for item in original_data:
        linked_list.push_back(item)

    # 測試反轉前的 value_n_from_end
    print("\n1. 測試反轉前...")
    assert linked_list.value_n_from_end(1) == "E", "❌ 反轉前倒數第1個應該是 'E'"
    assert linked_list.value_n_from_end(5) == "A", "❌ 反轉前倒數第5個應該是 'A'"

    # 反轉列表
    linked_list.reverse()

    # 測試反轉後的 value_n_from_end
    print("\n2. 測試反轉後...")
    # 反轉後: ["E", "D", "C", "B", "A"]
    assert linked_list.value_n_from_end(1) == "A", "❌ 反轉後倒數第1個應該是 'A'"
    assert linked_list.value_n_from_end(2) == "B", "❌ 反轉後倒數第2個應該是 'B'"
    assert linked_list.value_n_from_end(5) == "E", "❌ 反轉後倒數第5個應該是 'E'"

    print("✅ reverse() 和 value_n_from_end() 整合正確")


def test_operations_after_reverse():
    """測試反轉後其他操作是否正常"""
    print("\n=== 測試反轉後其他操作 ===")

    linked_list = SinglyLinkedList()
    for i in range(5):
        linked_list.push_back(i)  # [0, 1, 2, 3, 4]

    linked_list.reverse()  # [4, 3, 2, 1, 0]

    # 測試反轉後的各種操作
    print("\n1. 測試反轉後的基本操作...")
    assert linked_list.size() == 5, "❌ 反轉後 size 不正確"
    assert linked_list.front() == 4, "❌ 反轉後 front() 不正確"
    assert linked_list.back() == 0, "❌ 反轉後 back() 不正確"

    print("\n2. 測試反轉後的 value_at...")
    expected_values = [4, 3, 2, 1, 0]
    for i, expected in enumerate(expected_values):
        actual = linked_list.value_at(i)
        assert actual == expected, f"❌ 反轉後 value_at({i}) 期望 {expected}，實際 {actual}"

    print("\n3. 測試反轉後的插入刪除...")
    linked_list.insert(2, "inserted")  # [4, 3, "inserted", 2, 1, 0]
    assert linked_list.value_at(2) == "inserted", "❌ 反轉後插入不正確"

    linked_list.erase(2)  # [4, 3, 2, 1, 0]
    assert linked_list.value_at(2) == 2, "❌ 反轉後刪除不正確"

    print("✅ 反轉後其他操作正常")


def main():
    """執行所有階段5測試"""
    print("🚀 開始階段5測試：進階演算法測試")
    print("測試範圍：前階段功能 + reverse(), value_n_from_end()")

    try:
        # 執行各項測試
        test_previous_functionality()
        test_reverse_basic_functionality()
        test_reverse_twice()
        test_value_n_from_end_basic_functionality()
        test_value_n_from_end_error_handling()
        test_reverse_and_value_n_from_end_integration()
        test_operations_after_reverse()

        print("\n" + "="*50)
        print("🎉 階段5測試全部通過！")
        print("✅ reverse() 方法實作正確")
        print("✅ value_n_from_end() 方法實作正確")
        print("✅ 演算法邏輯正確")
        print("✅ 與前階段功能整合正常")
        print("\n📝 下一步：實作 remove_value() 方法")
        print("   然後運行 python3 test_stage6.py")
        print("\n💡 提示：")
        print("   - reverse() 是經典的鏈表操作，掌握三指標技巧")
        print("   - value_n_from_end() 展示了鏈表的靈活性")
        print("   - remove_value() 需要搜尋和刪除的結合")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作，特別注意：")
        print("1. reverse() 需要正確處理三個指標（prev, current, next）")
        print("2. reverse() 後要更新頭尾指標")
        print("3. value_n_from_end() 使用1-based計數")
        print("4. value_n_from_end() 需要正確計算位置")
        print("5. 邊界條件：空列表、單元素列表")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法和演算法邏輯")
        sys.exit(1)


if __name__ == "__main__":
    main()