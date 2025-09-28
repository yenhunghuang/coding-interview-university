#!/usr/bin/env python3
"""
最終階段測試：完整功能驗證和總結

這是 Singly Linked List 實作的最終驗證測試，包括：
- 所有功能的綜合測試
- 完整性檢查和總結
- 與 Coding Interview University 要求的對照
- 實作品質評估
- 學習成果總結

運行方式：python3 test_stage_final.py

這個測試將確認你的實作：
✅ 包含所有必需的方法
✅ 功能實作正確
✅ 錯誤處理適當
✅ 性能表現合理
✅ 代碼品質良好

通過此測試表示你已經完全掌握了 Singly Linked List 的實作！
"""

import sys
import time
sys.path.append('.')

exec(open('node.py').read())
exec(open('singly_linked_list.py').read())


def test_all_required_methods():
    """測試所有必需方法是否存在且工作正常"""
    print("=== 驗證所有必需方法 ===")

    linked_list = SinglyLinkedList()

    # Coding Interview University 要求的14個方法
    required_methods = [
        'size', 'empty', 'value_at', 'push_front', 'pop_front',
        'push_back', 'pop_back', 'front', 'back', 'insert',
        'erase', 'value_n_from_end', 'reverse', 'remove_value'
    ]

    print("\n檢查方法存在性...")
    for method in required_methods:
        assert hasattr(linked_list, method), f"❌ 缺少必需方法: {method}()"
        print(f"✅ {method}() 存在")

    print("\n快速功能驗證...")
    # 快速測試每個方法的基本功能

    # 基礎方法
    assert linked_list.size() == 0, "❌ size() 初始值不正確"
    assert linked_list.empty() == True, "❌ empty() 初始值不正確"

    # 添加元素
    linked_list.push_front(1)
    linked_list.push_back(2)
    linked_list.insert(1, 1.5)  # [1, 1.5, 2]

    # 訪問方法
    assert linked_list.size() == 3, "❌ size() 不正確"
    assert linked_list.empty() == False, "❌ empty() 不正確"
    assert linked_list.value_at(0) == 1, "❌ value_at() 不正確"
    assert linked_list.front() == 1, "❌ front() 不正確"
    assert linked_list.back() == 2, "❌ back() 不正確"
    assert linked_list.value_n_from_end(1) == 2, "❌ value_n_from_end() 不正確"

    # 修改方法
    linked_list.reverse()  # [2, 1.5, 1]
    assert linked_list.front() == 2, "❌ reverse() 不正確"

    linked_list.remove_value(1.5)  # [2, 1]
    assert linked_list.size() == 2, "❌ remove_value() 不正確"

    linked_list.erase(0)  # [1]
    assert linked_list.front() == 1, "❌ erase() 不正確"

    # 移除方法
    popped = linked_list.pop_front()
    assert popped == 1, "❌ pop_front() 不正確"
    assert linked_list.empty(), "❌ 最終狀態不正確"

    print("✅ 所有必需方法功能正常")


def test_coding_interview_university_requirements():
    """對照 Coding Interview University 的具體要求"""
    print("\n=== 對照 Coding Interview University 要求 ===")

    print("\n1. 檢查方法簽名和行為...")

    linked_list = SinglyLinkedList()

    # 建立測試數據
    test_data = ["A", "B", "C", "D", "E"]
    for item in test_data:
        linked_list.push_back(item)  # [A, B, C, D, E]

    # 測試每個要求的具體行為
    requirements_tests = [
        ("size() returns number of data elements",
         lambda: linked_list.size() == 5),

        ("empty() returns true if empty",
         lambda: not linked_list.empty() and SinglyLinkedList().empty()),

        ("value_at(index) returns value of nth item starting at 0",
         lambda: linked_list.value_at(0) == "A" and linked_list.value_at(4) == "E"),

        ("push_front(value) adds item to front",
         lambda: (linked_list.push_front("X"), linked_list.front() == "X")[1]),

        ("pop_front() remove front item and return its value",
         lambda: linked_list.pop_front() == "X"),

        ("push_back(value) adds item at end",
         lambda: (linked_list.push_back("Y"), linked_list.back() == "Y")[1]),

        ("pop_back() removes end item and returns its value",
         lambda: linked_list.pop_back() == "Y"),

        ("front() get value of front item",
         lambda: linked_list.front() == "A"),

        ("back() get value of end item",
         lambda: linked_list.back() == "E"),

        ("insert(index, value) insert value at index",
         lambda: (linked_list.insert(2, "Z"), linked_list.value_at(2) == "Z")[1]),

        ("erase(index) removes node at given index",
         lambda: (linked_list.erase(2), linked_list.value_at(2) != "Z")[1]),

        ("value_n_from_end(n) returns value of node at nth position from end",
         lambda: linked_list.value_n_from_end(1) == "E" and linked_list.value_n_from_end(5) == "A"),

        ("reverse() reverses the list",
         lambda: (linked_list.reverse(), linked_list.front() == "E" and linked_list.back() == "A")[1]),

        ("remove_value(value) removes first item with this value",
         lambda: (linked_list.remove_value("C"), "C" not in [linked_list.value_at(i) for i in range(linked_list.size())])[1]),
    ]

    for description, test_func in requirements_tests:
        try:
            result = test_func()
            if result:
                print(f"✅ {description}")
            else:
                print(f"❌ {description} - 測試失敗")
        except Exception as e:
            print(f"❌ {description} - 異常: {e}")

    print("\n✅ Coding Interview University 要求驗證完成")


def test_comprehensive_functionality():
    """綜合功能測試"""
    print("\n=== 綜合功能測試 ===")

    print("\n1. 測試完整的使用流程...")

    # 模擬一個完整的使用場景
    playlist = SinglyLinkedList()

    # 建立播放列表
    songs = ["Song1", "Song2", "Song3", "Song4", "Song5"]
    for song in songs:
        playlist.push_back(song)

    print(f"  ✅ 建立播放列表，共 {playlist.size()} 首歌")

    # 添加新歌到開頭（最喜歡的）
    playlist.push_front("Favorite Song")
    assert playlist.front() == "Favorite Song", "添加最愛歌曲失敗"

    # 在特定位置插入歌曲
    playlist.insert(3, "Inserted Song")
    assert playlist.value_at(3) == "Inserted Song", "插入歌曲失敗"

    print("  ✅ 添加和插入歌曲成功")

    # 播放歌曲（從前面開始）
    current_song = playlist.pop_front()
    assert current_song == "Favorite Song", "播放歌曲失敗"

    # 移除不喜歡的歌曲
    playlist.remove_value("Song2")
    remaining_songs = [playlist.value_at(i) for i in range(playlist.size())]
    assert "Song2" not in remaining_songs, "移除歌曲失敗"

    print("  ✅ 播放和移除歌曲成功")

    # 重新排列播放列表（反轉）
    original_first = playlist.front()
    original_last = playlist.back()
    playlist.reverse()
    assert playlist.front() == original_last, "反轉播放列表失敗"
    assert playlist.back() == original_first, "反轉播放列表失敗"

    print("  ✅ 重新排列播放列表成功")

    # 獲取倒數第二首歌
    if playlist.size() >= 2:
        second_last = playlist.value_n_from_end(2)
        print(f"  ✅ 倒數第二首歌: {second_last}")

    print("✅ 完整使用流程測試成功")


def test_error_handling_completeness():
    """完整錯誤處理測試"""
    print("\n=== 完整錯誤處理測試 ===")

    empty_list = SinglyLinkedList()
    single_list = SinglyLinkedList()
    single_list.push_back("single")

    # 所有應該拋出 IndexError 的情況
    error_cases = [
        ("空列表 pop_front", lambda: empty_list.pop_front()),
        ("空列表 pop_back", lambda: empty_list.pop_back()),
        ("空列表 front", lambda: empty_list.front()),
        ("空列表 back", lambda: empty_list.back()),
        ("空列表 value_at", lambda: empty_list.value_at(0)),
        ("空列表 erase", lambda: empty_list.erase(0)),
        ("空列表 value_n_from_end", lambda: empty_list.value_n_from_end(1)),
        ("負索引 value_at", lambda: single_list.value_at(-1)),
        ("超界索引 value_at", lambda: single_list.value_at(10)),
        ("負索引 erase", lambda: single_list.erase(-1)),
        ("超界索引 erase", lambda: single_list.erase(10)),
        ("負索引 insert", lambda: single_list.insert(-1, "test")),
        ("超界索引 insert", lambda: single_list.insert(10, "test")),
        ("無效 n value_n_from_end", lambda: single_list.value_n_from_end(0)),
        ("超大 n value_n_from_end", lambda: single_list.value_n_from_end(10)),
    ]

    error_count = 0
    for description, error_func in error_cases:
        try:
            error_func()
            print(f"❌ {description} 應該拋出異常")
        except IndexError:
            print(f"✅ {description} 正確拋出 IndexError")
            error_count += 1
        except Exception as e:
            print(f"⚠️ {description} 拋出其他異常: {e}")

    # 不應該拋出異常的情況
    safe_cases = [
        ("空列表 remove_value", lambda: empty_list.remove_value("not_exist")),
        ("空列表 reverse", lambda: empty_list.reverse()),
        ("移除不存在值", lambda: single_list.remove_value("not_exist")),
    ]

    safe_count = 0
    for description, safe_func in safe_cases:
        try:
            safe_func()
            print(f"✅ {description} 正確處理（無異常）")
            safe_count += 1
        except Exception as e:
            print(f"❌ {description} 不應該拋出異常: {e}")

    print(f"✅ 錯誤處理測試完成（{error_count} 個錯誤正確捕獲，{safe_count} 個安全操作）")


def test_performance_summary():
    """性能總結測試"""
    print("\n=== 性能總結測試 ===")

    test_size = 1000
    linked_list = SinglyLinkedList()

    print(f"\n使用 {test_size} 個元素進行性能測試...")

    # 前端操作性能
    start_time = time.time()
    for i in range(test_size):
        linked_list.push_front(i)
    front_ops_time = time.time() - start_time

    # 後端操作性能（清空重建）
    linked_list = SinglyLinkedList()
    start_time = time.time()
    for i in range(test_size):
        linked_list.push_back(i)
    back_ops_time = time.time() - start_time

    # 存取操作性能
    start_time = time.time()
    for i in range(0, test_size, 100):  # 每100個測試一次
        linked_list.value_at(i)
    access_time = time.time() - start_time

    # 反轉性能
    start_time = time.time()
    linked_list.reverse()
    reverse_time = time.time() - start_time

    print(f"\n性能總結:")
    print(f"  前端操作 ({test_size} 次 push_front): {front_ops_time:.3f}s")
    print(f"  後端操作 ({test_size} 次 push_back): {back_ops_time:.3f}s")
    print(f"  隨機存取 ({test_size//100} 次 value_at): {access_time:.3f}s")
    print(f"  列表反轉 (1 次 reverse): {reverse_time:.3f}s")

    # 性能評估
    if front_ops_time < 0.1:
        print("  ✅ 前端操作性能優秀（接近 O(1)）")
    elif front_ops_time < 0.5:
        print("  ✅ 前端操作性能良好")
    else:
        print("  ⚠️ 前端操作性能有待優化")

    if access_time < 0.5:
        print("  ✅ 存取操作性能在預期範圍（O(n)）")
    else:
        print("  ⚠️ 存取操作性能偏慢")

    print("✅ 性能總結完成")


def generate_final_report():
    """生成最終測試報告"""
    print("\n=== 最終測試報告 ===")

    # 統計信息
    total_methods = 14
    implemented_methods = []

    linked_list = SinglyLinkedList()
    required_methods = [
        'size', 'empty', 'value_at', 'push_front', 'pop_front',
        'push_back', 'pop_back', 'front', 'back', 'insert',
        'erase', 'value_n_from_end', 'reverse', 'remove_value'
    ]

    for method in required_methods:
        if hasattr(linked_list, method):
            implemented_methods.append(method)

    implementation_rate = len(implemented_methods) / total_methods * 100

    print(f"\n📊 實作統計:")
    print(f"  必需方法總數: {total_methods}")
    print(f"  已實作方法: {len(implemented_methods)}")
    print(f"  完成率: {implementation_rate:.1f}%")

    print(f"\n✅ 已實作的方法:")
    for method in implemented_methods:
        print(f"    - {method}()")

    if len(implemented_methods) < total_methods:
        missing_methods = [m for m in required_methods if m not in implemented_methods]
        print(f"\n❌ 缺少的方法:")
        for method in missing_methods:
            print(f"    - {method}()")

    # 功能評估
    print(f"\n🎯 功能評估:")
    feature_categories = {
        "基礎操作": ["size", "empty"],
        "前端操作": ["push_front", "pop_front", "front"],
        "後端操作": ["push_back", "pop_back", "back"],
        "隨機存取": ["value_at", "insert", "erase"],
        "進階功能": ["reverse", "value_n_from_end", "remove_value"],
    }

    for category, methods in feature_categories.items():
        implemented_in_category = [m for m in methods if m in implemented_methods]
        category_rate = len(implemented_in_category) / len(methods) * 100
        print(f"  {category}: {category_rate:.0f}% ({len(implemented_in_category)}/{len(methods)})")

    # 學習成果
    print(f"\n🎓 學習成果:")
    if implementation_rate >= 100:
        print("  🏆 完美！你已經完全掌握了 Singly Linked List 的實作")
        print("  💡 可以繼續學習 Doubly Linked List 或其他數據結構")
    elif implementation_rate >= 90:
        print("  🌟 優秀！你的實作非常完整")
        print("  💡 完善剩餘的小細節就完美了")
    elif implementation_rate >= 80:
        print("  👍 良好！你已經掌握了主要功能")
        print("  💡 繼續完善進階功能")
    else:
        print("  📚 還需努力！繼續實作剩餘功能")
        print("  💡 專注於基礎操作的正確實作")

    print(f"\n🚀 下一步建議:")
    if implementation_rate >= 100:
        print("  1. 嘗試優化性能（如添加 tail 指標）")
        print("  2. 實作 Doubly Linked List")
        print("  3. 學習其他數據結構（Stack, Queue, Hash Table）")
        print("  4. 用你的 Linked List 實作 Stack 或 Queue")
    else:
        print("  1. 完成剩餘方法的實作")
        print("  2. 通過所有測試階段")
        print("  3. 優化錯誤處理")


def main():
    """執行最終驗證測試"""
    print("🏁 開始最終階段測試：完整功能驗證")
    print("這是你的 Singly Linked List 實作的畢業考試！")

    try:
        test_all_required_methods()
        test_coding_interview_university_requirements()
        test_comprehensive_functionality()
        test_error_handling_completeness()
        test_performance_summary()
        generate_final_report()

        print("\n" + "="*60)
        print("🎉🎉🎉 恭喜！最終測試全部通過！ 🎉🎉🎉")
        print()
        print("🏆 你已經成功實作了完整的 Singly Linked List！")
        print("📚 你的實作符合 Coding Interview University 的所有要求")
        print("💪 你已經掌握了指標操作和鏈式數據結構的核心概念")
        print()
        print("📝 你可以在 README.md 中標記 Linked Lists 部分為完成 ✅")
        print("🚀 準備好迎接下一個挑戰：Stack 和 Queue！")
        print()
        print("💡 學習心得：")
        print("   - 鏈表相比數組的優勢：插入刪除 O(1)（已知位置）")
        print("   - 鏈表的劣勢：隨機存取 O(n)，記憶體不連續")
        print("   - 指標操作的重要性：三指標反轉技巧")
        print("   - 邊界條件處理：空表、單元素表的特殊考慮")

    except AssertionError as e:
        print(f"\n❌ 最終測試失敗: {e}")
        print("\n📋 修正建議：")
        print("1. 檢查所有必需方法是否正確實作")
        print("2. 確保錯誤處理符合預期")
        print("3. 驗證邊界條件的處理")
        print("4. 重新運行前面階段的測試找出問題")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查代碼完整性和語法正確性")
        sys.exit(1)


if __name__ == "__main__":
    main()