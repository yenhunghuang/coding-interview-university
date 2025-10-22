#!/usr/bin/env python3
"""
階段5測試：輔助功能和字串表示

這個階段測試：
- clear() 方法：清空佇列
- __str__() 方法：字串表示
- __repr__() 方法：詳細表示
- max_size 屬性：獲取最大容量
- 邊界情況和錯誤處理

運行方式：python3 test_stage5.py

實作指引：
在 queue.py 中新增以下方法：
    def clear(self)           # 清空佇列
    def __str__(self) -> str  # 字串表示
    def __repr__(self) -> str # 詳細表示
    @property max_size        # 容量屬性
"""

import sys
sys.path.append('.')

exec(open('queue.py').read())

def test_clear_functionality():
    """測試 clear 功能"""
    print("=== 測試 clear 功能 ===")

    # 測試 1: 清空有元素的佇列
    print("\n1. 測試清空有元素的佇列...")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.size() == 3, "❌ 清空前 size 應該是 3"

    queue.clear()

    assert queue.size() == 0, "❌ 清空後 size 應該是 0"
    assert queue.is_empty() == True, "❌ 清空後 is_empty() 應該是 True"
    print("✅ 清空有元素的佇列正確")

    # 測試 2: 清空空佇列
    print("\n2. 測試清空空佇列...")
    queue2 = Queue()
    queue2.clear()

    assert queue2.size() == 0, "❌ 清空空佇列後 size 應該是 0"
    assert queue2.is_empty() == True, "❌ 清空空佇列後 is_empty() 應該是 True"
    print("✅ 清空空佇列正確")

    # 測試 3: 清空後重新使用
    print("\n3. 測試清空後重新使用...")
    queue3 = Queue()
    queue3.enqueue(1)
    queue3.enqueue(2)
    queue3.clear()

    # 清空後應該可以正常使用
    queue3.enqueue(10)
    queue3.enqueue(20)

    assert queue3.size() == 2, "❌ 清空後重新入隊，size 應該是 2"
    assert queue3.dequeue() == 10, "❌ 應該出隊 10"
    assert queue3.dequeue() == 20, "❌ 應該出隊 20"
    print("✅ 清空後重新使用正確")

    # 測試 4: 有容量限制的佇列清空
    print("\n4. 測試有容量限制的佇列清空...")
    queue4 = Queue(max_size=3)
    queue4.enqueue(1)
    queue4.enqueue(2)
    queue4.enqueue(3)

    assert queue4.is_full() == True, "❌ 清空前應該是滿的"

    queue4.clear()

    assert queue4.is_empty() == True, "❌ 清空後應該是空的"
    assert queue4.is_full() == False, "❌ 清空後 is_full() 應該是 False"

    # 清空後容量限制應該還在
    queue4.enqueue(1)
    queue4.enqueue(2)
    queue4.enqueue(3)
    assert queue4.is_full() == True, "❌ 重新填滿後應該又是滿的"
    print("✅ 有容量限制的佇列清空正確")


def test_str_representation():
    """測試字串表示"""
    print("\n=== 測試字串表示 ===")

    # 測試 1: 空佇列
    print("\n1. 測試空佇列的字串表示...")
    queue = Queue()
    str_repr = str(queue)

    assert "Queue" in str_repr, "❌ 字串表示應該包含 'Queue'"
    assert "[]" in str_repr or "empty" in str_repr.lower(), "❌ 應該表示為空"
    print(f"✅ 空佇列: {str_repr}")

    # 測試 2: 有元素的佇列
    print("\n2. 測試有元素的佇列字串表示...")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    str_repr = str(queue)
    assert "Queue" in str_repr, "❌ 字串表示應該包含 'Queue'"
    # 應該能看出前端和尾部
    assert "front" in str_repr.lower() or "rear" in str_repr.lower(), "❌ 應該標示前端或尾部"
    print(f"✅ 有元素: {str_repr}")

    # 測試 3: 單個元素
    print("\n3. 測試單個元素的字串表示...")
    queue2 = Queue()
    queue2.enqueue("single")

    str_repr = str(queue2)
    assert "Queue" in str_repr, "❌ 字串表示應該包含 'Queue'"
    assert "single" in str_repr, "❌ 應該顯示元素內容"
    print(f"✅ 單個元素: {str_repr}")


def test_repr_representation():
    """測試詳細表示"""
    print("\n=== 測試詳細表示 ===")

    # 測試 1: 無容量限制的佇列
    print("\n1. 測試無容量限制的佇列...")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)

    repr_str = repr(queue)
    assert "Queue" in repr_str, "❌ repr 應該包含 'Queue'"
    assert "size" in repr_str.lower() or "2" in repr_str, "❌ 應該顯示大小信息"
    print(f"✅ 無容量限制: {repr_str}")

    # 測試 2: 有容量限制的佇列
    print("\n2. 測試有容量限制的佇列...")
    queue2 = Queue(max_size=5)
    queue2.enqueue(1)

    repr_str = repr(queue2)
    assert "Queue" in repr_str, "❌ repr 應該包含 'Queue'"
    assert "5" in repr_str or "max" in repr_str.lower(), "❌ 應該顯示最大容量"
    print(f"✅ 有容量限制: {repr_str}")


def test_max_size_property():
    """測試 max_size 屬性"""
    print("\n=== 測試 max_size 屬性 ===")

    # 測試 1: 無容量限制
    print("\n1. 測試無容量限制的佇列...")
    queue = Queue()
    assert queue.max_size is None, "❌ 無容量限制時 max_size 應該是 None"
    print("✅ 無容量限制 max_size 正確")

    # 測試 2: 有容量限制
    print("\n2. 測試有容量限制的佇列...")
    queue2 = Queue(max_size=10)
    assert queue2.max_size == 10, f"❌ max_size 應該是 10，實際是 {queue2.max_size}"
    print("✅ 有容量限制 max_size 正確")

    # 測試 3: 操作後 max_size 不變
    print("\n3. 測試操作後 max_size 不變...")
    queue2.enqueue(1)
    queue2.enqueue(2)
    queue2.dequeue()

    assert queue2.max_size == 10, "❌ 操作後 max_size 不應該改變"
    print("✅ max_size 保持不變")


def test_edge_cases():
    """測試邊界情況"""
    print("\n=== 測試邊界情況 ===")

    # 測試 1: None 值處理
    print("\n1. 測試 None 值處理...")
    queue = Queue()
    queue.enqueue(None)
    queue.enqueue(0)
    queue.enqueue(False)
    queue.enqueue("")

    assert queue.dequeue() is None, "❌ 應該出隊 None"
    assert queue.dequeue() == 0, "❌ 應該出隊 0"
    assert queue.dequeue() == False, "❌ 應該出隊 False"
    assert queue.dequeue() == "", "❌ 應該出隊空字串"
    print("✅ 特殊值處理正確")

    # 測試 2: 大物件處理
    print("\n2. 測試大物件處理...")
    queue2 = Queue()
    large_list = list(range(1000))
    large_dict = {i: f"value_{i}" for i in range(100)}

    queue2.enqueue(large_list)
    queue2.enqueue(large_dict)

    assert queue2.dequeue() == large_list, "❌ 應該正確出隊大列表"
    assert queue2.dequeue() == large_dict, "❌ 應該正確出隊大字典"
    print("✅ 大物件處理正確")


def test_complete_workflow():
    """測試完整工作流程"""
    print("\n=== 測試完整工作流程 ===")

    print("\n模擬實際使用場景...")
    queue = Queue(max_size=5)

    # 場景：任務佇列
    tasks = ["task1", "task2", "task3", "task4", "task5"]

    # 添加任務
    print("1. 添加所有任務...")
    for task in tasks:
        queue.enqueue(task)

    print(f"   當前佇列: {queue}")
    assert queue.is_full() == True, "❌ 應該是滿的"

    # 處理一些任務
    print("2. 處理前3個任務...")
    for i in range(3):
        processed = queue.dequeue()
        print(f"   處理: {processed}")
        assert processed == tasks[i], f"❌ 應該處理 {tasks[i]}"

    # 添加新任務
    print("3. 添加新任務...")
    queue.enqueue("task6")
    queue.enqueue("task7")

    assert queue.is_full() == True, "❌ 又應該是滿的"

    # 檢查狀態
    print(f"4. 當前狀態: {queue}")
    print(f"   size: {queue.size()}, is_full: {queue.is_full()}")

    # 清空並驗證
    remaining = []
    while not queue.is_empty():
        remaining.append(queue.dequeue())

    expected_remaining = ["task4", "task5", "task6", "task7"]
    assert remaining == expected_remaining, f"❌ 剩餘任務應該是 {expected_remaining}"

    print("✅ 完整工作流程正確")


def test_immutability_of_configuration():
    """測試配置的不可變性"""
    print("\n=== 測試配置的不可變性 ===")

    queue = Queue(max_size=5)

    # max_size 應該是只讀的（通過 property）
    print("\n1. 測試 max_size 是只讀的...")
    original_max_size = queue.max_size

    try:
        queue.max_size = 10
        # 如果可以設置，檢查是否真的改變了
        if queue.max_size == 10:
            print("⚠️ max_size 可以被修改（這可能不是期望的行為）")
        else:
            print("✅ max_size 無法修改（setter 無效）")
    except AttributeError:
        print("✅ max_size 是只讀的（無 setter）")

    # 確保原始容量限制仍然有效
    for i in range(5):
        queue.enqueue(i)

    try:
        queue.enqueue(5)
        print("❌ 容量限制失效了")
    except OverflowError:
        print("✅ 容量限制仍然有效")


def main():
    """執行所有階段5測試"""
    print("🚀 開始階段5測試：輔助功能和邊界情況")
    print("測試範圍：clear(), __str__(), __repr__(), max_size")

    try:
        # 執行各項測試
        test_clear_functionality()
        test_str_representation()
        test_repr_representation()
        test_max_size_property()
        test_edge_cases()
        test_complete_workflow()
        test_immutability_of_configuration()

        print("\n" + "="*50)
        print("🎉 階段5測試全部通過！")
        print("✅ 輔助功能實作正確")
        print("✅ 字串表示清晰易讀")
        print("✅ 邊界情況處理良好")
        print("\n📝 下一步：運行最終綜合測試")
        print("   然後運行 python3 test_stage_final.py")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作並修正後重新測試")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法")
        sys.exit(1)


if __name__ == "__main__":
    main()
