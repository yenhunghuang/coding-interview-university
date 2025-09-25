#!/usr/bin/env python3
"""
階段7測試：前階段功能 + 動態容量管理

這個階段測試自動擴容和縮容功能，是動態陣列的核心特性。
運行方式：python3 test_stage7.py
"""

import sys
sys.path.append('.')

exec(open('dynamic_array.py').read())


def test_previous_functionality():
    """重新測試前階段功能"""
    print("=== 測試前階段功能 ===")

    arr = DynamicArray()

    # 測試核心功能流程
    test_data = [1, 2, 3, 4, 5]
    for item in test_data:
        arr.push(item)

    assert arr.size() == 5
    assert arr.find(3) == 2

    arr.insert(2, "inserted")
    assert arr.at(2) == "inserted"

    arr.remove(1)
    assert arr.find(1) == -1

    print("✅ 前階段功能依然正確")


def test_automatic_expansion():
    """測試自動擴容功能"""
    print("\n=== 測試自動擴容功能 ===")

    # 測試 1: 從小容量開始，觀察擴容過程
    print("\n1. 測試擴容觸發...")
    arr = DynamicArray(4)  # 初始容量為 4
    assert arr.capacity() == 4, "❌ 初始容量設置不正確"

    # 填滿初始容量
    for i in range(4):
        arr.push(f"item_{i}")
        print(f"   推入 item_{i}: size={arr.size()}, capacity={arr.capacity()}")

    assert arr.size() == 4, "❌ 填滿後 size 不正確"
    assert arr.capacity() == 4, "❌ 填滿後容量不應該變化"

    # 推入第5個元素，應該觸發擴容
    print(f"\n   推入第5個元素前: size={arr.size()}, capacity={arr.capacity()}")
    arr.push("trigger_expansion")
    print(f"   推入第5個元素後: size={arr.size()}, capacity={arr.capacity()}")

    assert arr.size() == 5, "❌ 擴容後 size 不正確"
    new_capacity = arr.capacity()
    assert new_capacity > 4, f"❌ 擴容後容量應該大於4，實際是 {new_capacity}"

    # 驗證擴容倍率（通常是 2 倍）
    expected_capacity = 4 * 2  # 通常是2倍擴容
    if new_capacity == expected_capacity:
        print(f"✅ 標準2倍擴容: 4 -> {new_capacity}")
    else:
        print(f"ℹ️ 非標準擴容策略: 4 -> {new_capacity}")

    # 驗證所有數據都還在
    for i in range(4):
        assert arr.at(i) == f"item_{i}", f"❌ 擴容後元素 {i} 遺失"
    assert arr.at(4) == "trigger_expansion", "❌ 觸發擴容的元素遺失"

    print("✅ 自動擴容功能正確")


def test_multiple_expansions():
    """測試多次擴容"""
    print("\n=== 測試多次擴容 ===")

    arr = DynamicArray(2)  # 從很小的容量開始
    capacity_history = [arr.capacity()]

    print(f"\n1. 初始容量: {arr.capacity()}")

    # 推入足夠多的元素觸發多次擴容
    target_size = 32  # 這應該會觸發多次擴容
    for i in range(target_size):
        old_capacity = arr.capacity()
        arr.push(f"data_{i}")
        new_capacity = arr.capacity()

        if new_capacity > old_capacity:
            print(f"   擴容發生: {old_capacity} -> {new_capacity} (在推入第 {i+1} 個元素時)")
            capacity_history.append(new_capacity)

    print(f"\n2. 最終狀態: size={arr.size()}, capacity={arr.capacity()}")
    print(f"   容量變化歷史: {capacity_history}")

    # 驗證最終狀態
    assert arr.size() == target_size, f"❌ 最終 size 應該是 {target_size}"
    assert arr.capacity() >= target_size, "❌ 最終容量應該足以容納所有元素"

    # 驗證所有數據完整性
    for i in range(target_size):
        assert arr.at(i) == f"data_{i}", f"❌ 多次擴容後元素 {i} 遺失或變化"

    # 驗證至少發生了多次擴容
    assert len(capacity_history) >= 3, f"❌ 應該發生多次擴容，實際歷史: {capacity_history}"

    print("✅ 多次擴容功能正確")


def test_expansion_with_different_operations():
    """測試不同操作觸發的擴容"""
    print("\n=== 測試不同操作觸發的擴容 ===")

    # 測試 1: push 操作觸發擴容
    print("\n1. 測試 push 觸發擴容...")
    push_arr = DynamicArray(3)
    for i in range(4):  # 超出容量
        push_arr.push(f"push_{i}")

    assert push_arr.capacity() > 3, "❌ push 操作應該觸發擴容"
    print("✅ push 擴容正確")

    # 測試 2: insert 操作觸發擴容
    print("\n2. 測試 insert 觸發擴容...")
    insert_arr = DynamicArray(3)
    for i in range(3):  # 填滿
        insert_arr.push(i)

    old_capacity = insert_arr.capacity()
    insert_arr.insert(1, "inserted")  # 應該觸發擴容
    new_capacity = insert_arr.capacity()

    assert new_capacity > old_capacity, "❌ insert 操作應該觸發擴容"
    assert insert_arr.at(1) == "inserted", "❌ insert 後元素位置不正確"
    print("✅ insert 擴容正確")

    # 測試 3: prepend 操作觸發擴容
    print("\n3. 測試 prepend 觸發擴容...")
    prepend_arr = DynamicArray(3)
    for i in range(3):  # 填滿
        prepend_arr.push(i)

    old_capacity = prepend_arr.capacity()
    prepend_arr.prepend("prepended")  # 應該觸發擴容
    new_capacity = prepend_arr.capacity()

    assert new_capacity > old_capacity, "❌ prepend 操作應該觸發擴容"
    assert prepend_arr.at(0) == "prepended", "❌ prepend 後元素位置不正確"
    print("✅ prepend 擴容正確")


def test_contraction_if_implemented():
    """測試縮容功能（如果實作了的話）"""
    print("\n=== 測試縮容功能（如果有實作） ===")

    # 建立一個較大的陣列然後移除大部分元素
    arr = DynamicArray(4)

    # 先觸發擴容
    for i in range(16):  # 足以觸發多次擴容
        arr.push(i)

    expanded_capacity = arr.capacity()
    print(f"\n1. 擴容後狀態: size={arr.size()}, capacity={expanded_capacity}")

    # 移除大部分元素
    while arr.size() > 2:
        arr.pop()

    final_capacity = arr.capacity()
    print(f"2. 移除後狀態: size={arr.size()}, capacity={final_capacity}")

    if final_capacity < expanded_capacity:
        print(f"✅ 實作了縮容功能: {expanded_capacity} -> {final_capacity}")

        # 如果有縮容，驗證數據完整性
        remaining_data = [arr.at(i) for i in range(arr.size())]
        expected_data = [0, 1]  # 剩下的前兩個元素
        assert remaining_data == expected_data, "❌ 縮容後數據不正確"
        print("✅ 縮容後數據完整性正確")

    elif final_capacity == expanded_capacity:
        print("ℹ️ 未實作縮容功能或縮容條件未滿足（這是可以接受的）")

    else:
        print("⚠️ 意外的容量變化行為")

    print("✅ 縮容測試完成")


def test_capacity_efficiency():
    """測試容量使用效率"""
    print("\n=== 測試容量使用效率 ===")

    arr = DynamicArray(8)

    print("\n1. 測試容量使用率...")

    # 記錄不同大小時的容量使用情況
    size_capacity_pairs = []

    for target_size in [5, 10, 15, 20, 25]:
        while arr.size() < target_size:
            arr.push(f"item_{arr.size()}")

        capacity = arr.capacity()
        utilization = arr.size() / capacity
        size_capacity_pairs.append((arr.size(), capacity, utilization))
        print(f"   size: {arr.size()}, capacity: {capacity}, 使用率: {utilization:.2%}")

    # 驗證容量使用的合理性
    for size, capacity, utilization in size_capacity_pairs:
        assert capacity >= size, f"❌ 容量 {capacity} 小於實際大小 {size}"
        assert utilization >= 0.25, f"❌ 使用率過低 {utilization:.2%}，可能浪費過多記憶體"

    print("✅ 容量使用效率合理")


def test_expansion_preserves_functionality():
    """測試擴容不影響其他功能"""
    print("\n=== 測試擴容不影響其他功能 ===")

    arr = DynamicArray(4)

    # 建立初始數據
    initial_data = ["A", "B", "C", "D"]
    for item in initial_data:
        arr.push(item)

    print("\n1. 觸發擴容前測試所有功能...")
    assert arr.find("B") == 1, "❌ 擴容前 find 功能異常"
    assert arr.at(2) == "C", "❌ 擴容前 at 功能異常"

    # 觸發擴容
    arr.push("E")  # 觸發擴容

    print("2. 觸發擴容後測試所有功能...")

    # 測試 find 功能
    assert arr.find("A") == 0, "❌ 擴容後 find 功能異常"
    assert arr.find("E") == 4, "❌ 擴容後新元素 find 異常"

    # 測試 at 功能
    for i, expected in enumerate(["A", "B", "C", "D", "E"]):
        assert arr.at(i) == expected, f"❌ 擴容後 at({i}) 異常"

    # 測試 insert 功能
    arr.insert(2, "inserted")
    assert arr.at(2) == "inserted", "❌ 擴容後 insert 功能異常"
    assert arr.at(3) == "C", "❌ 擴容後 insert 影響了其他元素"

    # 測試 delete 功能
    arr.delete(0)  # 刪除 "A"
    assert arr.at(0) == "B", "❌ 擴容後 delete 功能異常"

    # 測試 remove 功能
    arr.remove("inserted")
    assert arr.find("inserted") == -1, "❌ 擴容後 remove 功能異常"

    # 測試 pop 功能
    last_item = arr.pop()
    assert last_item == "E", "❌ 擴容後 pop 功能異常"

    print("✅ 擴容後所有功能依然正常")


def test_expansion_stress():
    """測試擴容的穩定性"""
    print("\n=== 測試擴容穩定性 ===")

    arr = DynamicArray(1)  # 從最小容量開始

    print("\n1. 大量數據測試...")
    target_size = 1000

    # 快速推入大量數據
    for i in range(target_size):
        arr.push(i)

        # 每100個檢查一次完整性
        if (i + 1) % 100 == 0:
            assert arr.size() == i + 1, f"❌ 第 {i+1} 個元素後 size 不正確"
            assert arr.at(i) == i, f"❌ 第 {i+1} 個元素值不正確"

    # 最終驗證
    assert arr.size() == target_size, f"❌ 最終 size 不正確"
    final_capacity = arr.capacity()
    assert final_capacity >= target_size, f"❌ 最終容量不足: {final_capacity} < {target_size}"

    # 隨機檢查一些位置
    import random
    check_positions = random.sample(range(target_size), min(20, target_size))
    for pos in check_positions:
        assert arr.at(pos) == pos, f"❌ 位置 {pos} 的值不正確"

    print(f"✅ 大量數據測試通過 (最終容量: {final_capacity})")


def main():
    """執行所有階段7測試"""
    print("🚀 開始階段7測試：前階段功能 + 動態容量管理")
    print("測試範圍：所有前階段功能 + 自動擴容/縮容")

    try:
        # 執行各項測試
        test_previous_functionality()
        test_automatic_expansion()
        test_multiple_expansions()
        test_expansion_with_different_operations()
        test_contraction_if_implemented()
        test_capacity_efficiency()
        test_expansion_preserves_functionality()
        test_expansion_stress()

        print("\n" + "="*60)
        print("🎉 階段7測試全部通過！")
        print("✅ 自動擴容功能實作正確")
        print("✅ 多次擴容處理正常")
        print("✅ 不同操作觸發擴容正確")
        print("✅ 縮容功能測試完成（如果有實作）")
        print("✅ 容量使用效率合理")
        print("✅ 擴容不影響其他功能")
        print("✅ 大量數據處理穩定")
        print("\n📝 下一步：實作 Python 魔術方法（可選）")
        print("   然後運行 python3 test_stage8.py")
        print("\n🎊 恭喜！動態容量管理是動態陣列最核心的功能，你已經掌握了！")
        print("\n💡 關鍵概念回顧：")
        print("   - 擴容通常使用2倍策略平衡時間和空間複雜度")
        print("   - 縮容條件通常比較嚴格，避免頻繁的擴縮")
        print("   - 攤還時間複雜度：push/pop 操作平均 O(1)")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作，特別注意：")
        print("1. 擴容觸發條件是否正確")
        print("2. 擴容倍率是否合理")
        print("3. 擴容後數據複製是否正確")
        print("4. 擴容後 capacity() 更新是否正確")
        print("5. 各種操作觸發擴容的處理")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法和實作邏輯")
        sys.exit(1)


if __name__ == "__main__":
    main()