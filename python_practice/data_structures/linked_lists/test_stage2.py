#!/usr/bin/env python3
"""
階段2測試：前端操作測試 - push_front(), pop_front(), front()

這個階段測試列表前端的操作，包括：
- push_front(value) - 在列表前端插入元素
- pop_front() - 移除並返回前端元素
- front() - 獲取前端元素值（不移除）
- 與 size(), empty() 的整合測試

運行方式：python3 test_stage2.py

實作指引：
在 SinglyLinkedList 中新增這些方法：
- push_front(value) -> None：在頭部插入新節點
- pop_front() -> any：移除頭節點並返回其值，空列表應拋出 IndexError
- front() -> any：返回頭節點的值，空列表應拋出 IndexError

時間複雜度要求：
- push_front(): O(1)
- pop_front(): O(1)
- front(): O(1)
"""

import sys
sys.path.append('.')

exec(open('node.py').read())
exec(open('singly_linked_list.py').read())


def test_previous_functionality():
    """重新測試前階段功能（確保沒被破壞）"""
    print("=== 測試前階段功能 ===")

    linked_list = SinglyLinkedList()

    # 基礎方法測試
    assert linked_list.size() == 0
    assert linked_list.empty() == True

    print("✅ 前階段功能依然正確")


def test_push_front_basic_functionality():
    """測試 push_front() 基本功能"""
    print("\n=== 測試 push_front() 基本功能 ===")

    linked_list = SinglyLinkedList()

    # 測試 1: 空列表插入第一個元素
    print("\n1. 測試空列表插入第一個元素...")
    linked_list.push_front("first")

    assert linked_list.size() == 1, f"❌ push_front 後 size 應該是 1，實際是 {linked_list.size()}"
    assert linked_list.empty() == False, f"❌ push_front 後 empty() 應該是 False"
    print("✅ 空列表插入第一個元素正確")

    # 測試 2: 連續插入多個元素（LIFO 行為）
    print("\n2. 測試連續插入多個元素...")
    linked_list.push_front("second")
    linked_list.push_front("third")

    assert linked_list.size() == 3, f"❌ 插入3個元素後 size 應該是 3，實際是 {linked_list.size()}"
    assert linked_list.empty() == False, f"❌ 插入元素後 empty() 應該是 False"
    print("✅ 連續插入正確")

    # 測試 3: 不同數據類型插入
    print("\n3. 測試不同數據類型插入...")
    test_list = SinglyLinkedList()
    test_data = [42, 3.14, "hello", [1, 2, 3], {"key": "value"}, None, True]

    for item in test_data:
        test_list.push_front(item)

    assert test_list.size() == len(test_data), f"❌ 插入 {len(test_data)} 個元素後 size 不正確"
    print("✅ 不同數據類型插入正確")


def test_front_functionality():
    """測試 front() 功能"""
    print("\n=== 測試 front() 功能 ===")

    # 測試 1: 空列表 front 應該拋出異常
    print("\n1. 測試空列表 front()...")
    empty_list = SinglyLinkedList()

    try:
        empty_list.front()
        print("❌ 空列表 front() 應該拋出 IndexError")
    except IndexError:
        print("✅ 空列表 front() 正確拋出 IndexError")
    except Exception as e:
        print(f"⚠️ 空列表 front() 拋出其他異常: {e}")

    # 測試 2: 單個元素列表
    print("\n2. 測試單個元素列表 front()...")
    single_list = SinglyLinkedList()
    single_list.push_front("only_one")

    front_value = single_list.front()
    assert front_value == "only_one", f"❌ front() 應該返回 'only_one'，實際返回 {front_value}"
    assert single_list.size() == 1, "❌ front() 不應該改變列表大小"
    print("✅ 單個元素列表 front() 正確")

    # 測試 3: 多個元素列表（LIFO 驗證）
    print("\n3. 測試多個元素列表 front()...")
    multi_list = SinglyLinkedList()
    test_sequence = ["first", "second", "third", "fourth"]

    # 按順序插入，最後插入的應該在前面
    for item in test_sequence:
        multi_list.push_front(item)

    # 最後插入的 "fourth" 應該在最前面
    front_value = multi_list.front()
    assert front_value == "fourth", f"❌ front() 應該返回 'fourth'，實際返回 {front_value}"
    assert multi_list.size() == 4, "❌ front() 不應該改變列表大小"
    print("✅ 多個元素列表 front() 正確")


def test_pop_front_functionality():
    """測試 pop_front() 功能"""
    print("\n=== 測試 pop_front() 功能 ===")

    # 測試 1: 空列表 pop 應該拋出異常
    print("\n1. 測試空列表 pop_front()...")
    empty_list = SinglyLinkedList()

    try:
        empty_list.pop_front()
        print("❌ 空列表 pop_front() 應該拋出 IndexError")
    except IndexError:
        print("✅ 空列表 pop_front() 正確拋出 IndexError")
    except Exception as e:
        print(f"⚠️ 空列表 pop_front() 拋出其他異常: {e}")

    # 測試 2: 單個元素 pop
    print("\n2. 測試單個元素 pop_front()...")
    single_list = SinglyLinkedList()
    single_list.push_front("only_one")

    popped_value = single_list.pop_front()
    assert popped_value == "only_one", f"❌ pop_front() 應該返回 'only_one'，實際返回 {popped_value}"
    assert single_list.size() == 0, "❌ pop_front() 後 size 應該是 0"
    assert single_list.empty() == True, "❌ pop_front() 後列表應該為空"
    print("✅ 單個元素 pop_front() 正確")

    # 測試 3: 多個元素的 LIFO 行為
    print("\n3. 測試多個元素的 LIFO (後進先出) 行為...")
    multi_list = SinglyLinkedList()
    test_sequence = ["first", "second", "third", "fourth"]

    # 按順序插入
    for item in test_sequence:
        multi_list.push_front(item)

    assert multi_list.size() == len(test_sequence), "❌ 插入後 size 不正確"

    # 按反順序 pop，應該得到相反的順序
    for expected in reversed(test_sequence):
        actual = multi_list.pop_front()
        assert actual == expected, f"❌ 期望 pop {expected}，實際得到 {actual}"

    assert multi_list.empty(), "❌ 全部 pop 完後應該是空的"
    print("✅ LIFO 行為正確")


def test_push_pop_integration():
    """測試 push_front 和 pop_front 的整合"""
    print("\n=== 測試 push_front 和 pop_front 整合 ===")

    linked_list = SinglyLinkedList()

    print("\n1. 測試交替 push_front/pop_front...")

    # 交替操作測試
    linked_list.push_front(1)
    assert linked_list.size() == 1

    result = linked_list.pop_front()
    assert result == 1 and linked_list.size() == 0

    linked_list.push_front(2)
    linked_list.push_front(3)
    assert linked_list.size() == 2

    result = linked_list.pop_front()
    assert result == 3 and linked_list.size() == 1

    result = linked_list.pop_front()
    assert result == 2 and linked_list.size() == 0

    print("✅ 交替 push_front/pop_front 正確")

    print("\n2. 測試批量 push_front 然後批量 pop_front...")

    # 批量操作測試
    batch_data = list(range(20))  # [0, 1, 2, ..., 19]

    for item in batch_data:
        linked_list.push_front(item)

    assert linked_list.size() == 20, "❌ 批量 push_front 後 size 不正確"

    for expected in reversed(batch_data):
        actual = linked_list.pop_front()
        assert actual == expected, f"❌ 批量 pop_front 順序不正確"

    assert linked_list.empty(), "❌ 批量 pop_front 完後應該是空的"
    print("✅ 批量 push_front/pop_front 正確")


def test_front_after_operations():
    """測試各種操作後的 front() 行為"""
    print("\n=== 測試操作後的 front() 行為 ===")

    linked_list = SinglyLinkedList()

    # 測試 push 後 front
    linked_list.push_front("a")
    assert linked_list.front() == "a"

    linked_list.push_front("b")
    assert linked_list.front() == "b"  # 最新插入的在前面

    # 測試 pop 後 front
    popped = linked_list.pop_front()
    assert popped == "b"
    assert linked_list.front() == "a"  # 現在 "a" 在前面

    linked_list.push_front("c")
    assert linked_list.front() == "c"

    print("✅ 操作後的 front() 行為正確")


def main():
    """執行所有階段2測試"""
    print("🚀 開始階段2測試：前端操作測試")
    print("測試範圍：size(), empty(), push_front(), pop_front(), front()")

    try:
        # 執行各項測試
        test_previous_functionality()
        test_push_front_basic_functionality()
        test_front_functionality()
        test_pop_front_functionality()
        test_push_pop_integration()
        test_front_after_operations()

        print("\n" + "="*50)
        print("🎉 階段2測試全部通過！")
        print("✅ push_front() 方法實作正確")
        print("✅ pop_front() 方法實作正確")
        print("✅ front() 方法實作正確")
        print("✅ LIFO (後進先出) 行為正確")
        print("✅ 與前階段功能整合正常")
        print("\n📝 下一步：實作 push_back(), pop_back(), back() 方法")
        print("   然後運行 python3 test_stage3.py")
        print("\n💡 提示：")
        print("   - push_back() 需要遍歷到尾部或使用尾指標")
        print("   - pop_back() 需要找到倒數第二個節點")
        print("   - 考慮使用 tail 指標優化後端操作到 O(1)")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作，特別注意：")
        print("1. push_front() 應該將新節點設為新的頭節點")
        print("2. pop_front() 應該更新頭指標並返回原頭節點的值")
        print("3. front() 只返回值，不修改列表結構")
        print("4. 空列表操作應該拋出 IndexError")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法和實作邏輯")
        sys.exit(1)


if __name__ == "__main__":
    main()