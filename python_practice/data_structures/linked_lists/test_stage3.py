#!/usr/bin/env python3
"""
階段3測試：後端操作測試 - push_back(), pop_back(), back()

這個階段測試列表後端的操作，包括：
- push_back(value) - 在列表後端插入元素
- pop_back() - 移除並返回後端元素
- back() - 獲取後端元素值（不移除）
- 前端和後端操作的混合測試

運行方式：python3 test_stage3.py

實作指引：
在 SinglyLinkedList 中新增這些方法：
- push_back(value) -> None：在尾部插入新節點
- pop_back() -> any：移除尾節點並返回其值，空列表應拋出 IndexError
- back() -> any：返回尾節點的值，空列表應拋出 IndexError

時間複雜度考慮：
- 無尾指標：push_back() O(n), pop_back() O(n), back() O(n)
- 有尾指標：push_back() O(1), pop_back() O(n), back() O(1)
- pop_back() 在單鏈表中很難做到 O(1)，因為需要找到倒數第二個節點

建議：考慮添加 tail 指標來優化部分操作
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

    # 前端操作
    test_data = [1, "test", [1, 2], None]
    for item in test_data:
        linked_list.push_front(item)

    for expected in reversed(test_data):
        assert linked_list.pop_front() == expected

    print("✅ 前階段功能依然正確")


def test_push_back_basic_functionality():
    """測試 push_back() 基本功能"""
    print("\n=== 測試 push_back() 基本功能 ===")

    linked_list = SinglyLinkedList()

    # 測試 1: 空列表插入第一個元素
    print("\n1. 測試空列表插入第一個元素...")
    linked_list.push_back("first")

    assert linked_list.size() == 1, f"❌ push_back 後 size 應該是 1，實際是 {linked_list.size()}"
    assert linked_list.empty() == False, f"❌ push_back 後 empty() 應該是 False"
    print("✅ 空列表插入第一個元素正確")

    # 測試 2: 連續插入多個元素（FIFO 行為）
    print("\n2. 測試連續插入多個元素...")
    linked_list.push_back("second")
    linked_list.push_back("third")

    assert linked_list.size() == 3, f"❌ 插入3個元素後 size 應該是 3，實際是 {linked_list.size()}"
    assert linked_list.empty() == False, f"❌ 插入元素後 empty() 應該是 False"
    print("✅ 連續插入正確")

    # 測試 3: 不同數據類型插入
    print("\n3. 測試不同數據類型插入...")
    test_list = SinglyLinkedList()
    test_data = [42, 3.14, "hello", [1, 2, 3], {"key": "value"}, None, True]

    for item in test_data:
        test_list.push_back(item)

    assert test_list.size() == len(test_data), f"❌ 插入 {len(test_data)} 個元素後 size 不正確"
    print("✅ 不同數據類型插入正確")


def test_back_functionality():
    """測試 back() 功能"""
    print("\n=== 測試 back() 功能 ===")

    # 測試 1: 空列表 back 應該拋出異常
    print("\n1. 測試空列表 back()...")
    empty_list = SinglyLinkedList()

    try:
        empty_list.back()
        print("❌ 空列表 back() 應該拋出 IndexError")
    except IndexError:
        print("✅ 空列表 back() 正確拋出 IndexError")
    except Exception as e:
        print(f"⚠️ 空列表 back() 拋出其他異常: {e}")

    # 測試 2: 單個元素列表
    print("\n2. 測試單個元素列表 back()...")
    single_list = SinglyLinkedList()
    single_list.push_back("only_one")

    back_value = single_list.back()
    assert back_value == "only_one", f"❌ back() 應該返回 'only_one'，實際返回 {back_value}"
    assert single_list.size() == 1, "❌ back() 不應該改變列表大小"
    print("✅ 單個元素列表 back() 正確")

    # 測試 3: 多個元素列表（FIFO 驗證）
    print("\n3. 測試多個元素列表 back()...")
    multi_list = SinglyLinkedList()
    test_sequence = ["first", "second", "third", "fourth"]

    # 按順序插入，最後插入的應該在後面
    for item in test_sequence:
        multi_list.push_back(item)

    # 最後插入的 "fourth" 應該在最後面
    back_value = multi_list.back()
    assert back_value == "fourth", f"❌ back() 應該返回 'fourth'，實際返回 {back_value}"
    assert multi_list.size() == 4, "❌ back() 不應該改變列表大小"
    print("✅ 多個元素列表 back() 正確")


def test_pop_back_functionality():
    """測試 pop_back() 功能"""
    print("\n=== 測試 pop_back() 功能 ===")

    # 測試 1: 空列表 pop 應該拋出異常
    print("\n1. 測試空列表 pop_back()...")
    empty_list = SinglyLinkedList()

    try:
        empty_list.pop_back()
        print("❌ 空列表 pop_back() 應該拋出 IndexError")
    except IndexError:
        print("✅ 空列表 pop_back() 正確拋出 IndexError")
    except Exception as e:
        print(f"⚠️ 空列表 pop_back() 拋出其他異常: {e}")

    # 測試 2: 單個元素 pop
    print("\n2. 測試單個元素 pop_back()...")
    single_list = SinglyLinkedList()
    single_list.push_back("only_one")

    popped_value = single_list.pop_back()
    assert popped_value == "only_one", f"❌ pop_back() 應該返回 'only_one'，實際返回 {popped_value}"
    assert single_list.size() == 0, "❌ pop_back() 後 size 應該是 0"
    assert single_list.empty() == True, "❌ pop_back() 後列表應該為空"
    print("✅ 單個元素 pop_back() 正確")

    # 測試 3: 多個元素的 FIFO 行為（反向）
    print("\n3. 測試多個元素的 FIFO (先進後出) 行為...")
    multi_list = SinglyLinkedList()
    test_sequence = ["first", "second", "third", "fourth"]

    # 按順序插入
    for item in test_sequence:
        multi_list.push_back(item)

    assert multi_list.size() == len(test_sequence), "❌ 插入後 size 不正確"

    # 按反順序 pop，應該得到反順序
    for expected in reversed(test_sequence):
        actual = multi_list.pop_back()
        assert actual == expected, f"❌ 期望 pop {expected}，實際得到 {actual}"

    assert multi_list.empty(), "❌ 全部 pop 完後應該是空的"
    print("✅ FIFO 行為正確")


def test_push_pop_back_integration():
    """測試 push_back 和 pop_back 的整合"""
    print("\n=== 測試 push_back 和 pop_back 整合 ===")

    linked_list = SinglyLinkedList()

    print("\n1. 測試交替 push_back/pop_back...")

    # 交替操作測試
    linked_list.push_back(1)
    assert linked_list.size() == 1

    result = linked_list.pop_back()
    assert result == 1 and linked_list.size() == 0

    linked_list.push_back(2)
    linked_list.push_back(3)
    assert linked_list.size() == 2

    result = linked_list.pop_back()
    assert result == 3 and linked_list.size() == 1

    result = linked_list.pop_back()
    assert result == 2 and linked_list.size() == 0

    print("✅ 交替 push_back/pop_back 正確")

    print("\n2. 測試批量 push_back 然後批量 pop_back...")

    # 批量操作測試
    batch_data = list(range(20))  # [0, 1, 2, ..., 19]

    for item in batch_data:
        linked_list.push_back(item)

    assert linked_list.size() == 20, "❌ 批量 push_back 後 size 不正確"

    for expected in reversed(batch_data):
        actual = linked_list.pop_back()
        assert actual == expected, f"❌ 批量 pop_back 順序不正確"

    assert linked_list.empty(), "❌ 批量 pop_back 完後應該是空的"
    print("✅ 批量 push_back/pop_back 正確")


def test_front_back_mixed_operations():
    """測試前端和後端混合操作"""
    print("\n=== 測試前端和後端混合操作 ===")

    linked_list = SinglyLinkedList()

    # 測試 1: push_front 和 push_back 混合
    print("\n1. 測試 push_front 和 push_back 混合...")
    linked_list.push_front("front1")  # ["front1"]
    linked_list.push_back("back1")    # ["front1", "back1"]
    linked_list.push_front("front2")  # ["front2", "front1", "back1"]
    linked_list.push_back("back2")    # ["front2", "front1", "back1", "back2"]

    assert linked_list.size() == 4, "❌ 混合插入後 size 不正確"
    assert linked_list.front() == "front2", "❌ front() 值不正確"
    assert linked_list.back() == "back2", "❌ back() 值不正確"
    print("✅ push_front 和 push_back 混合正確")

    # 測試 2: pop_front 和 pop_back 混合
    print("\n2. 測試 pop_front 和 pop_back 混合...")
    # 當前狀態: ["front2", "front1", "back1", "back2"]

    front_popped = linked_list.pop_front()  # 移除 "front2"
    assert front_popped == "front2", f"❌ pop_front() 應該返回 'front2'，實際返回 {front_popped}"

    back_popped = linked_list.pop_back()    # 移除 "back2"
    assert back_popped == "back2", f"❌ pop_back() 應該返回 'back2'，實際返回 {back_popped}"

    assert linked_list.size() == 2, "❌ 混合 pop 後 size 不正確"
    assert linked_list.front() == "front1", "❌ 剩餘的 front() 值不正確"
    assert linked_list.back() == "back1", "❌ 剩餘的 back() 值不正確"
    print("✅ pop_front 和 pop_back 混合正確")

    # 測試 3: 完全清空
    print("\n3. 測試完全清空...")
    linked_list.pop_front()  # 移除 "front1"
    linked_list.pop_back()   # 移除 "back1"

    assert linked_list.empty(), "❌ 全部移除後應該為空"
    assert linked_list.size() == 0, "❌ 全部移除後 size 應該是 0"
    print("✅ 完全清空正確")


def test_single_element_operations():
    """測試單元素列表的各種操作"""
    print("\n=== 測試單元素列表操作 ===")

    # front() 和 back() 在單元素列表中應該返回相同值
    single_list = SinglyLinkedList()
    single_list.push_front("single")

    assert single_list.front() == "single", "❌ 單元素列表 front() 不正確"
    assert single_list.back() == "single", "❌ 單元素列表 back() 不正確"
    assert single_list.front() == single_list.back(), "❌ 單元素列表 front() 和 back() 應該相同"

    print("✅ 單元素列表操作正確")


def main():
    """執行所有階段3測試"""
    print("🚀 開始階段3測試：後端操作測試")
    print("測試範圍：size(), empty(), push_front(), pop_front(), front(), push_back(), pop_back(), back()")

    try:
        # 執行各項測試
        test_previous_functionality()
        test_push_back_basic_functionality()
        test_back_functionality()
        test_pop_back_functionality()
        test_push_pop_back_integration()
        test_front_back_mixed_operations()
        test_single_element_operations()

        print("\n" + "="*50)
        print("🎉 階段3測試全部通過！")
        print("✅ push_back() 方法實作正確")
        print("✅ pop_back() 方法實作正確")
        print("✅ back() 方法實作正確")
        print("✅ 前端和後端操作混合正確")
        print("✅ 與前階段功能整合正常")
        print("\n📝 下一步：實作 value_at(), insert(), erase() 方法")
        print("   然後運行 python3 test_stage4.py")
        print("\n💡 提示：")
        print("   - value_at(index) 需要遍歷到指定位置")
        print("   - insert(index, value) 需要處理邊界情況")
        print("   - erase(index) 需要重新連接節點")
        print("   - 考慮 index 邊界檢查和異常處理")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作，特別注意：")
        print("1. push_back() 應該將新節點連接到列表尾部")
        print("2. pop_back() 需要找到倒數第二個節點來更新連接")
        print("3. back() 需要遍歷到最後一個節點")
        print("4. 空列表操作應該拋出 IndexError")
        print("5. 單元素列表中 front() 和 back() 應該返回相同值")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法和實作邏輯")
        sys.exit(1)


if __name__ == "__main__":
    main()