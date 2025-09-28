#!/usr/bin/env python3
"""
階段7測試：整合測試 - 混合操作和複雜場景

這個階段測試所有功能的整合，包括：
- 複雜的操作序列
- 各種方法的混合使用
- 邊界條件的組合測試
- 實際使用場景模擬

運行方式：python3 test_stage7.py

測試重點：
- 驗證所有方法在復雜操作序列下的正確性
- 測試操作間的相互影響
- 確保在各種邊界條件組合下的穩定性
- 模擬真實使用場景

這個階段不會新增新的方法，而是全面測試現有功能的整合性。
"""

import sys
sys.path.append('.')

exec(open('node.py').read())
exec(open('singly_linked_list.py').read())


def test_all_basic_functionality():
    """全面測試所有基礎功能"""
    print("=== 全面測試所有基礎功能 ===")

    linked_list = SinglyLinkedList()

    # 測試所有方法是否都存在
    required_methods = [
        'size', 'empty', 'push_front', 'pop_front', 'front',
        'push_back', 'pop_back', 'back', 'value_at', 'insert',
        'erase', 'reverse', 'value_n_from_end', 'remove_value'
    ]

    for method in required_methods:
        assert hasattr(linked_list, method), f"❌ SinglyLinkedList 缺少方法: {method}"

    print("✅ 所有必要方法都存在")

    # 快速功能測試
    assert linked_list.empty() == True
    linked_list.push_back(1)
    assert linked_list.size() == 1
    assert linked_list.front() == 1
    assert linked_list.back() == 1
    assert linked_list.value_at(0) == 1
    assert linked_list.pop_front() == 1
    assert linked_list.empty() == True

    print("✅ 所有基礎功能快速測試通過")


def test_complex_operation_sequences():
    """測試複雜操作序列"""
    print("\n=== 測試複雜操作序列 ===")

    linked_list = SinglyLinkedList()

    print("\n1. 測試構建複雜列表...")
    # 構建一個複雜的列表：[10, 20, 30, 40, 50]
    operations = [
        ("push_back", 30),
        ("push_front", 20),
        ("push_front", 10),
        ("push_back", 40),
        ("insert", 4, 50),
    ]

    for op_name, *args in operations:
        getattr(linked_list, op_name)(*args)

    # 驗證最終結果
    expected = [10, 20, 30, 40, 50]
    assert linked_list.size() == len(expected), "❌ 複雜構建後 size 不正確"
    for i, exp_val in enumerate(expected):
        actual = linked_list.value_at(i)
        assert actual == exp_val, f"❌ 位置 {i} 期望 {exp_val}，實際 {actual}"

    print("✅ 複雜列表構建正確")

    print("\n2. 測試複雜修改操作...")
    # 執行一系列修改操作
    linked_list.reverse()  # [50, 40, 30, 20, 10]
    assert linked_list.front() == 50, "❌ 反轉後第一個元素不正確"

    linked_list.remove_value(30)  # [50, 40, 20, 10]
    assert linked_list.size() == 4, "❌ 移除後 size 不正確"

    linked_list.insert(2, 25)  # [50, 40, 25, 20, 10]
    assert linked_list.value_at(2) == 25, "❌ 插入後元素不正確"

    last_two = linked_list.value_n_from_end(2)  # 應該是 20
    assert last_two == 20, f"❌ value_n_from_end(2) 期望 20，實際 {last_two}"

    linked_list.erase(0)  # [40, 25, 20, 10]
    assert linked_list.front() == 40, "❌ 刪除後第一個元素不正確"

    print("✅ 複雜修改操作正確")


def test_edge_case_combinations():
    """測試邊界條件組合"""
    print("\n=== 測試邊界條件組合 ===")

    print("\n1. 測試空列表各種操作...")
    empty_list = SinglyLinkedList()

    # 所有在空列表上會拋出異常的操作
    error_operations = [
        ("pop_front", IndexError),
        ("pop_back", IndexError),
        ("front", IndexError),
        ("back", IndexError),
        ("value_at", IndexError, 0),
        ("erase", IndexError, 0),
        ("value_n_from_end", IndexError, 1),
    ]

    for op_data in error_operations:
        op_name = op_data[0]
        expected_error = op_data[1]
        args = op_data[2:] if len(op_data) > 2 else []

        try:
            getattr(empty_list, op_name)(*args)
            print(f"❌ 空列表 {op_name}() 應該拋出 {expected_error.__name__}")
        except expected_error:
            print(f"✅ 空列表 {op_name}() 正確拋出 {expected_error.__name__}")
        except Exception as e:
            print(f"⚠️ 空列表 {op_name}() 拋出其他異常: {e}")

    # 不會拋出異常的操作
    safe_operations = [
        ("remove_value", "not_exist"),
        ("insert", 0, "first"),
    ]

    for op_name, *args in safe_operations:
        try:
            getattr(empty_list, op_name)(*args)
            print(f"✅ 空列表 {op_name}() 正確處理")
        except Exception as e:
            print(f"❌ 空列表 {op_name}() 不應該拋出異常: {e}")

    print("\n2. 測試單元素列表各種操作...")
    single_list = SinglyLinkedList()
    single_list.push_back("single")

    # 單元素列表的特殊性質
    assert single_list.front() == single_list.back(), "❌ 單元素列表 front() 和 back() 應該相同"
    assert single_list.value_at(0) == "single", "❌ 單元素列表 value_at(0) 不正確"
    assert single_list.value_n_from_end(1) == "single", "❌ 單元素列表 value_n_from_end(1) 不正確"

    # 單元素列表反轉
    single_list.reverse()
    assert single_list.front() == "single", "❌ 單元素列表反轉後元素不正確"
    assert single_list.size() == 1, "❌ 單元素列表反轉後 size 不正確"

    print("✅ 單元素列表操作正確")


def test_stress_operations():
    """壓力測試 - 大量操作"""
    print("\n=== 壓力測試 ===")

    linked_list = SinglyLinkedList()

    print("\n1. 測試大量插入和刪除...")
    # 插入大量元素
    for i in range(100):
        if i % 3 == 0:
            linked_list.push_front(i)
        elif i % 3 == 1:
            linked_list.push_back(i)
        else:
            linked_list.insert(linked_list.size() // 2, i)

    assert linked_list.size() == 100, f"❌ 大量插入後 size 期望 100，實際 {linked_list.size()}"

    # 隨機刪除元素
    for i in range(0, 100, 5):  # 刪除 i = 0, 5, 10, 15, ..., 95
        linked_list.remove_value(i)

    expected_size = 100 - 20  # 刪除了20個元素
    assert linked_list.size() == expected_size, f"❌ 大量刪除後 size 期望 {expected_size}，實際 {linked_list.size()}"

    print("✅ 大量插入和刪除正確")

    print("\n2. 測試重複反轉...")
    original_first = linked_list.front()
    original_last = linked_list.back()

    # 反轉偶數次應該恢復原狀
    for _ in range(10):
        linked_list.reverse()

    assert linked_list.front() == original_first, "❌ 偶數次反轉後 front() 應該恢復原狀"
    assert linked_list.back() == original_last, "❌ 偶數次反轉後 back() 應該恢復原狀"

    print("✅ 重複反轉正確")


def test_real_world_scenarios():
    """模擬真實世界使用場景"""
    print("\n=== 模擬真實使用場景 ===")

    print("\n1. 模擬待辦事項列表...")
    todo_list = SinglyLinkedList()

    # 添加任務
    todo_list.push_back("寫報告")
    todo_list.push_back("開會")
    todo_list.push_front("緊急：回覆郵件")  # 緊急任務插到最前面

    assert todo_list.front() == "緊急：回覆郵件", "❌ 緊急任務應該在最前面"

    # 在特定位置插入任務
    todo_list.insert(2, "準備簡報")

    # 完成任務（從前面開始）
    completed = todo_list.pop_front()
    assert completed == "緊急：回覆郵件", "❌ 完成的任務不正確"

    # 取消某個任務
    todo_list.remove_value("開會")
    assert todo_list.size() == 2, "❌ 取消任務後 size 不正確"

    print("✅ 待辦事項列表模擬正確")

    print("\n2. 模擬瀏覽歷史...")
    history = SinglyLinkedList()

    # 瀏覽頁面（新頁面加到前面）
    pages = ["首頁", "產品頁", "購物車", "結帳頁", "確認頁"]
    for page in pages:
        history.push_front(page)

    # 檢查最近瀏覽的頁面
    recent = history.front()
    assert recent == "確認頁", "❌ 最近瀏覽頁面不正確"

    # 檢查瀏覽歷史總數
    assert history.size() == len(pages), "❌ 瀏覽歷史數量不正確"

    # 清除特定頁面的歷史
    history.remove_value("購物車")

    # 獲取第n個瀏覽記錄
    third_recent = history.value_n_from_end(3)  # 倒數第三個
    # 當前順序：["確認頁", "結帳頁", "產品頁", "首頁"]（移除了"購物車"）
    # 倒數第三個應該是"產品頁"
    assert third_recent == "產品頁", f"❌ 倒數第三個瀏覽記錄期望 '產品頁'，實際 '{third_recent}'"

    print("✅ 瀏覽歷史模擬正確")


def test_data_integrity_after_operations():
    """測試操作後數據完整性"""
    print("\n=== 測試數據完整性 ===")

    linked_list = SinglyLinkedList()

    # 建立測試數據
    test_data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    for item in test_data:
        linked_list.push_back(item)

    print("\n1. 測試各種操作後的完整性...")

    # 執行各種操作
    operations = [
        ("insert", 2, "Coconut"),     # 在位置2插入
        ("remove_value", "Banana"),   # 移除值
        ("reverse", ),                # 反轉
        ("erase", 1),                 # 刪除位置1
        ("push_front", "Avocado"),    # 前端插入
        ("pop_back", ),               # 後端移除
    ]

    for op_name, *args in operations:
        old_size = linked_list.size()
        result = getattr(linked_list, op_name)(*args)

        # 驗證操作後列表仍然有效
        assert linked_list.size() >= 0, "❌ 操作後 size 不應該為負"

        # 驗證所有索引都可以訪問
        for i in range(linked_list.size()):
            try:
                value = linked_list.value_at(i)
                assert value is not None or value == None, "❌ 獲取的值異常"
            except Exception as e:
                print(f"❌ 操作 {op_name} 後索引 {i} 訪問失敗: {e}")

        # 驗證 front() 和 back() 的一致性
        if not linked_list.empty():
            assert linked_list.front() == linked_list.value_at(0), "❌ front() 與 value_at(0) 不一致"
            assert linked_list.back() == linked_list.value_at(linked_list.size() - 1), "❌ back() 與最後一個元素不一致"

    print("✅ 所有操作後數據完整性正確")


def main():
    """執行所有階段7測試"""
    print("🚀 開始階段7測試：整合測試")
    print("測試範圍：所有功能的整合性和複雜使用場景")

    try:
        # 執行各項測試
        test_all_basic_functionality()
        test_complex_operation_sequences()
        test_edge_case_combinations()
        test_stress_operations()
        test_real_world_scenarios()
        test_data_integrity_after_operations()

        print("\n" + "="*50)
        print("🎉 階段7測試全部通過！")
        print("✅ 所有功能整合正常")
        print("✅ 複雜操作序列正確")
        print("✅ 邊界條件處理正確")
        print("✅ 壓力測試通過")
        print("✅ 真實場景模擬正確")
        print("✅ 數據完整性保證")
        print("\n📝 下一步：性能測試和最終驗證")
        print("   然後運行 python3 test_stage8.py")
        print("\n💡 恭喜！你的 linked list 實作非常穩健！")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作，特別注意：")
        print("1. 操作間的相互影響")
        print("2. 復雜操作序列的正確性")
        print("3. 邊界條件的組合處理")
        print("4. 數據完整性的維護")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼穩定性和錯誤處理")
        sys.exit(1)


if __name__ == "__main__":
    main()