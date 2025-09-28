#!/usr/bin/env python3
"""
階段1測試：基礎結構測試 - Node類別和SinglyLinkedList初始化

這個階段測試最基本的結構建立，包括：
- Node 類別的基本功能
- SinglyLinkedList 的初始化
- size() 和 empty() 基本方法
- 錯誤處理驗證

運行方式：python3 test_stage1.py

實作指引：
你需要創建兩個文件：
1. node.py - 包含 Node 類別
2. singly_linked_list.py - 包含 SinglyLinkedList 類別

預期方法簽名：
class Node:
    def __init__(self, data, next_node=None)

class SinglyLinkedList:
    def __init__(self)
    def size(self) -> int
    def empty(self) -> bool
"""

import sys
sys.path.append('.')

# 嘗試導入你的實作
try:
    exec(open('node.py').read())
    exec(open('singly_linked_list.py').read())
except FileNotFoundError as e:
    print(f"❌ 找不到實作文件: {e}")
    print("\n請創建以下文件：")
    print("1. node.py - Node 類別實作")
    print("2. singly_linked_list.py - SinglyLinkedList 類別實作")
    sys.exit(1)


def test_node_basic_functionality():
    """測試 Node 類別基本功能"""
    print("=== 測試 Node 類別基本功能 ===")

    # 測試 1: 基本 Node 創建
    print("\n1. 測試基本 Node 創建...")
    try:
        node = Node(42)
        assert hasattr(node, 'data'), "❌ Node 應該有 data 屬性"
        assert hasattr(node, 'next'), "❌ Node 應該有 next 屬性"
        assert node.data == 42, f"❌ node.data 應該是 42，實際是 {node.data}"
        assert node.next is None, f"❌ node.next 應該是 None，實際是 {node.next}"
        print("✅ 基本 Node 創建正確")
    except Exception as e:
        print(f"❌ Node 創建失敗: {e}")
        return False

    # 測試 2: Node 鏈接
    print("\n2. 測試 Node 鏈接...")
    try:
        node1 = Node("first")
        node2 = Node("second")
        node1.next = node2

        assert node1.next == node2, "❌ node1.next 應該指向 node2"
        assert node1.data == "first", "❌ node1.data 不正確"
        assert node2.data == "second", "❌ node2.data 不正確"
        assert node2.next is None, "❌ node2.next 應該是 None"
        print("✅ Node 鏈接正確")
    except Exception as e:
        print(f"❌ Node 鏈接失敗: {e}")
        return False

    # 測試 3: 不同數據類型的 Node
    print("\n3. 測試不同數據類型的 Node...")
    try:
        test_data = [1, "hello", [1, 2, 3], {"key": "value"}, None, True]
        for data in test_data:
            node = Node(data)
            assert node.data == data, f"❌ Node 數據不匹配: 期望 {data}，得到 {node.data}"
        print("✅ 不同數據類型 Node 創建正確")
    except Exception as e:
        print(f"❌ 不同數據類型 Node 創建失敗: {e}")
        return False

    return True


def test_linked_list_initialization():
    """測試 SinglyLinkedList 初始化"""
    print("\n=== 測試 SinglyLinkedList 初始化 ===")

    # 測試 1: 基本初始化
    print("\n1. 測試基本初始化...")
    try:
        linked_list = SinglyLinkedList()
        assert hasattr(linked_list, 'size'), "❌ SinglyLinkedList 應該有 size() 方法"
        assert hasattr(linked_list, 'empty'), "❌ SinglyLinkedList 應該有 empty() 方法"
        print("✅ SinglyLinkedList 基本初始化正確")
    except Exception as e:
        print(f"❌ SinglyLinkedList 初始化失敗: {e}")
        return False

    return True


def test_basic_methods():
    """測試基本方法 size() 和 empty()"""
    print("\n=== 測試基本方法 ===")

    linked_list = SinglyLinkedList()

    # 測試 1: 空列表的 size 和 empty
    print("\n1. 測試空列表狀態...")
    try:
        size = linked_list.size()
        is_empty = linked_list.empty()

        assert isinstance(size, int), f"❌ size() 應該返回 int，實際返回 {type(size)}"
        assert size == 0, f"❌ 空列表 size() 應該是 0，實際是 {size}"

        assert isinstance(is_empty, bool), f"❌ empty() 應該返回 bool，實際返回 {type(is_empty)}"
        assert is_empty == True, f"❌ 空列表 empty() 應該是 True，實際是 {is_empty}"

        print("✅ 空列表狀態正確")
    except Exception as e:
        print(f"❌ 空列表狀態測試失敗: {e}")
        return False

    return True


def test_unimplemented_methods():
    """確認其他方法還沒實作"""
    print("\n=== 確認未實作方法 ===")

    linked_list = SinglyLinkedList()

    # 測試還沒實作的方法，應該拋出 NotImplementedError
    unimplemented_tests = [
        ("push_front", lambda: linked_list.push_front(1)),
        ("pop_front", lambda: linked_list.pop_front()),
        ("push_back", lambda: linked_list.push_back(1)),
        ("front", lambda: linked_list.front()),
        ("back", lambda: linked_list.back()),
        ("value_at", lambda: linked_list.value_at(0)),
    ]

    for method_name, test_func in unimplemented_tests:
        try:
            test_func()
            print(f"❌ {method_name}() 應該還沒實作")
        except NotImplementedError:
            print(f"✅ {method_name}() 正確顯示未實作")
        except AttributeError:
            print(f"⚠️ {method_name}() 方法不存在（這是正常的）")
        except Exception as e:
            print(f"⚠️ {method_name}() 拋出其他異常: {e}")


def main():
    """執行所有階段1測試"""
    print("🚀 開始階段1測試：基礎結構測試")
    print("測試範圍：Node 類別，SinglyLinkedList 初始化，size(), empty()")

    try:
        # 執行各項測試
        if not test_node_basic_functionality():
            raise AssertionError("Node 類別測試失敗")

        if not test_linked_list_initialization():
            raise AssertionError("SinglyLinkedList 初始化測試失敗")

        if not test_basic_methods():
            raise AssertionError("基本方法測試失敗")

        test_unimplemented_methods()

        print("\n" + "="*50)
        print("🎉 階段1測試全部通過！")
        print("✅ Node 類別實作正確")
        print("✅ SinglyLinkedList 基本結構正確")
        print("✅ size() 和 empty() 方法實作正確")
        print("\n📝 下一步：實作 push_front() 和 pop_front() 方法")
        print("   然後運行 python3 test_stage2.py")
        print("\n💡 提示：")
        print("   - push_front() 在列表開頭插入元素")
        print("   - pop_front() 移除並返回開頭元素")
        print("   - 注意處理空列表的 pop 操作異常")

    except AssertionError as e:
        print(f"\n❌ 測試失敗: {e}")
        print("請檢查你的實作並修正後重新測試")
        print("\n實作提示：")
        print("1. Node 類別需要 data 和 next 屬性")
        print("2. SinglyLinkedList 需要追蹤頭節點")
        print("3. size() 返回當前元素數量")
        print("4. empty() 返回是否為空列表")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ 執行錯誤: {e}")
        print("請檢查你的程式碼語法和實作邏輯")
        sys.exit(1)


if __name__ == "__main__":
    main()