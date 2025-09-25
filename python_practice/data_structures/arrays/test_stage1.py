#!/usr/bin/env python3
"""
階段1測試：基礎方法 (size, capacity, is_empty)

這個階段只測試最基本的三個方法。
運行方式：python3 test_stage1.py
"""
import sys
sys.path.append('.')

exec(open('dynamic_array.py').read())

def test_basic_methods():
    """測試基礎方法功能"""
    print("=== 測試基礎方法 ===")

    # 測試 1: 預設初始化
    print("\n1. 測試預設初始化...")
    arr = DynamicArray()

    assert arr.size() == 0, f"❌ size() 應該是 0，實際是 {arr.size()}"
    assert arr.capacity() == 16, f"❌ capacity() 應該是 16，實際是 {arr.capacity()}"
    assert arr.is_empty() == True, f"❌ is_empty() 應該是 True，實際是 {arr.is_empty()}"
    print("✅ 預設初始化正確")

    # 測試 2: 自訂容量初始化
    print("\n2. 測試自訂容量初始化...")
    arr32 = DynamicArray(32)

    assert arr32.size() == 0, f"❌ size() 應該是 0，實際是 {arr32.size()}"
    assert arr32.capacity() == 32, f"❌ capacity() 應該是 32，實際是 {arr32.capacity()}"
    assert arr32.is_empty() == True, f"❌ is_empty() 應該是 True，實際是 {arr32.is_empty()}"
    print("✅ 自訂容量初始化正確")

    # 測試 3: 小容量初始化
    print("\n3. 測試小容量初始化...")
    arr1 = DynamicArray(1)

    assert arr1.size() == 0, f"❌ size() 應該是 0，實際是 {arr1.size()}"
    assert arr1.capacity() == 1, f"❌ capacity() 應該是 1，實際是 {arr1.capacity()}"
    assert arr1.is_empty() == True, f"❌ is_empty() 應該是 True，實際是 {arr1.is_empty()}"
    print("✅ 小容量初始化正確")


def test_error_handling():
    """測試錯誤處理"""
    print("\n=== 測試錯誤處理 ===")

    # 測試 1: 無效容量 0
    print("\n1. 測試無效容量 0...")
    try:
        arr = DynamicArray(0)
        print("❌ 應該拋出 ValueError")
        return False
    except ValueError as e:
        print(f"✅ 正確拋出 ValueError: {e}")

    # 測試 2: 無效容量 -1
    print("\n2. 測試無效容量 -1...")
    try:
        arr = DynamicArray(-1)
        print("❌ 應該拋出 ValueError")
        return False
    except ValueError as e:
        print(f"✅ 正確拋出 ValueError: {e}")

    return True


def test_unimplemented_methods():
    """確認其他方法還沒實作"""
    print("\n=== 確認未實作方法 ===")

    arr = DynamicArray()

    # 測試幾個還沒實作的方法
    unimplemented_tests = [
        ("push", lambda: arr.push(1)),
        ("at", lambda: arr.at(0)),
        ("pop", lambda: arr.pop()),
        ("find", lambda: arr.find(1)),
    ]

    for method_name, test_func in unimplemented_tests:
        try:
            test_func()
            print(f"❌ {method_name}() 應該還沒實作")
        except NotImplementedError:
            print(f"✅ {method_name}() 正確顯示未實作")
        except Exception as e:
            print(f"⚠️ {method_name}() 拋出其他異常: {e}")


def main():
    """執行所有階段1測試"""
    print("🚀 開始階段1測試：基礎方法")
    print("測試範圍：size(), capacity(), is_empty()")

    try:
        # 執行各項測試
        test_basic_methods()
        test_error_handling()
        test_unimplemented_methods()

        print("\n" + "="*50)
        print("🎉 階段1測試全部通過！")
        print("✅ 基礎方法 (size, capacity, is_empty) 實作正確")
        print("\n📝 下一步：實作 push() 和 at() 方法")
        print("   然後運行 python3 test_stage2.py")

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