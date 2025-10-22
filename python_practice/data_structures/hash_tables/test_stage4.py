"""
測試階段 4: 刪除操作 (Remove Operations)

學習目標：
1. 理解如何從雜湊表中刪除鍵值對
2. 處理刪除鏈結串列中不同位置的節點
3. 正確維護大小計數
4. 處理刪除不存在的鍵

測試重點：
- 刪除單一元素
- 刪除鏈結串列頭部、中間、尾部的節點
- 刪除後的查找操作
- 刪除不存在的鍵的錯誤處理
"""

import unittest
from hash_table import HashTable


class CollisionHashTable(HashTable):
    """強制碰撞的雜湊表，用於測試鏈結串列操作"""

    def _hash(self, key):
        return 0


class TestStage4(unittest.TestCase):
    """階段 4：刪除操作測試"""

    def setUp(self):
        """每個測試前的設置"""
        self.ht = HashTable()

    def test_01_remove_single_item(self):
        """測試刪除單一元素"""
        self.ht.put("key", "value")
        self.assertEqual(self.ht.size(), 1)

        self.ht.remove("key")

        self.assertEqual(self.ht.size(), 0,
                         "刪除後大小應該是 0")
        self.assertTrue(self.ht.is_empty(),
                       "刪除唯一元素後應該是空的")

    def test_02_remove_and_verify_not_found(self):
        """測試刪除後無法找到該鍵"""
        self.ht.put("key", "value")
        self.ht.remove("key")

        # 刪除後查找應該拋出 KeyError
        with self.assertRaises(KeyError):
            self.ht.get("key")

        # contains 應該回傳 False
        self.assertFalse(self.ht.contains("key"))

    def test_03_remove_from_multiple_items(self):
        """測試從多個元素中刪除一個"""
        self.ht.put("a", 1)
        self.ht.put("b", 2)
        self.ht.put("c", 3)

        self.ht.remove("b")

        self.assertEqual(self.ht.size(), 2)
        self.assertTrue(self.ht.contains("a"))
        self.assertFalse(self.ht.contains("b"))
        self.assertTrue(self.ht.contains("c"))

    def test_04_remove_nonexistent_key(self):
        """測試刪除不存在的鍵"""
        self.ht.put("key", "value")

        # 刪除不存在的鍵應該拋出 KeyError
        with self.assertRaises(KeyError):
            self.ht.remove("nonexistent")

    def test_05_remove_from_empty_table(self):
        """測試從空雜湊表刪除"""
        with self.assertRaises(KeyError):
            self.ht.remove("anything")

    def test_06_remove_head_of_collision_chain(self):
        """測試刪除碰撞鏈的頭節點"""
        collision_ht = CollisionHashTable(capacity=10)

        # 插入三個會碰撞的鍵
        collision_ht.put("first", 1)
        collision_ht.put("second", 2)
        collision_ht.put("third", 3)

        # 刪除第一個插入的（可能是鏈尾）
        # 注意：由於是頭插法，最後插入的會在頭部
        collision_ht.remove("third")

        self.assertEqual(collision_ht.size(), 2)
        self.assertFalse(collision_ht.contains("third"))
        self.assertTrue(collision_ht.contains("first"))
        self.assertTrue(collision_ht.contains("second"))

    def test_07_remove_middle_of_collision_chain(self):
        """測試刪除碰撞鏈的中間節點"""
        collision_ht = CollisionHashTable(capacity=10)

        collision_ht.put("a", 1)
        collision_ht.put("b", 2)
        collision_ht.put("c", 3)

        # 刪除中間的
        collision_ht.remove("b")

        self.assertEqual(collision_ht.size(), 2)
        self.assertTrue(collision_ht.contains("a"))
        self.assertFalse(collision_ht.contains("b"))
        self.assertTrue(collision_ht.contains("c"))

        # 確保其他元素的值正確
        self.assertEqual(collision_ht.get("a"), 1)
        self.assertEqual(collision_ht.get("c"), 3)

    def test_08_remove_tail_of_collision_chain(self):
        """測試刪除碰撞鏈的尾節點"""
        collision_ht = CollisionHashTable(capacity=10)

        collision_ht.put("a", 1)
        collision_ht.put("b", 2)
        collision_ht.put("c", 3)

        # 刪除第一個插入的（可能是鏈尾）
        collision_ht.remove("a")

        self.assertEqual(collision_ht.size(), 2)
        self.assertFalse(collision_ht.contains("a"))
        self.assertTrue(collision_ht.contains("b"))
        self.assertTrue(collision_ht.contains("c"))

    def test_09_remove_all_items_one_by_one(self):
        """測試逐一刪除所有元素"""
        items = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]

        # 插入所有元素
        for key, value in items:
            self.ht.put(key, value)

        self.assertEqual(self.ht.size(), 5)

        # 逐一刪除
        for key, _ in items:
            self.ht.remove(key)

        self.assertEqual(self.ht.size(), 0)
        self.assertTrue(self.ht.is_empty())

    def test_10_remove_and_reinsert(self):
        """測試刪除後重新插入"""
        self.ht.put("key", "value1")
        self.ht.remove("key")

        # 重新插入相同的鍵
        self.ht.put("key", "value2")

        self.assertEqual(self.ht.size(), 1)
        self.assertEqual(self.ht.get("key"), "value2")

    def test_11_remove_with_collision_stress(self):
        """測試碰撞情況下的刪除壓力測試"""
        collision_ht = CollisionHashTable(capacity=10)

        # 插入大量元素
        n = 50
        for i in range(n):
            collision_ht.put(f"key{i}", i)

        # 刪除一半的元素
        for i in range(0, n, 2):
            collision_ht.remove(f"key{i}")

        # 驗證大小
        self.assertEqual(collision_ht.size(), n // 2)

        # 驗證刪除的元素不存在
        for i in range(0, n, 2):
            self.assertFalse(collision_ht.contains(f"key{i}"))

        # 驗證保留的元素存在且值正確
        for i in range(1, n, 2):
            self.assertTrue(collision_ht.contains(f"key{i}"))
            self.assertEqual(collision_ht.get(f"key{i}"), i)

    def test_12_remove_pattern(self):
        """測試特定的刪除模式"""
        # 插入
        for i in range(10):
            self.ht.put(f"key{i}", i)

        # 刪除偶數索引
        for i in range(0, 10, 2):
            self.ht.remove(f"key{i}")

        # 驗證
        self.assertEqual(self.ht.size(), 5)
        for i in range(10):
            if i % 2 == 0:
                self.assertFalse(self.ht.contains(f"key{i}"))
            else:
                self.assertTrue(self.ht.contains(f"key{i}"))

    def test_13_remove_and_size_consistency(self):
        """測試刪除操作與大小計數的一致性"""
        # 插入 20 個元素
        for i in range(20):
            self.ht.put(i, i * 10)

        self.assertEqual(self.ht.size(), 20)

        # 刪除 5 個元素
        for i in range(5):
            self.ht.remove(i)

        self.assertEqual(self.ht.size(), 15)

        # 再刪除 10 個元素
        for i in range(5, 15):
            self.ht.remove(i)

        self.assertEqual(self.ht.size(), 5)

    def test_14_remove_after_update(self):
        """測試更新後刪除"""
        self.ht.put("key", "value1")
        self.ht.put("key", "value2")  # 更新
        self.ht.put("key", "value3")  # 再次更新

        self.assertEqual(self.ht.size(), 1)

        self.ht.remove("key")

        self.assertEqual(self.ht.size(), 0)
        self.assertFalse(self.ht.contains("key"))

    def test_15_remove_does_not_affect_other_buckets(self):
        """測試刪除不影響其他桶"""
        # 使用較大的容量，確保元素分散在不同的桶
        large_ht = HashTable(capacity=100)

        # 插入多個元素
        for i in range(20):
            large_ht.put(f"key{i}", i)

        # 刪除一個元素
        large_ht.remove("key5")

        # 確保其他元素不受影響
        for i in range(20):
            if i == 5:
                self.assertFalse(large_ht.contains(f"key{i}"))
            else:
                self.assertTrue(large_ht.contains(f"key{i}"))
                self.assertEqual(large_ht.get(f"key{i}"), i)


def run_tests():
    """執行所有測試"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage4)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print("🎉 恭喜！階段 4 的所有測試都通過了！")
        print("\n你已經掌握了：")
        print("✓ remove 方法的實作")
        print("✓ 刪除鏈結串列中不同位置的節點")
        print("✓ 正確維護大小計數")
        print("✓ 刪除操作的錯誤處理")
        print("\n準備好進入階段 5：動態調整大小")
    else:
        print("❌ 還有一些測試沒有通過，請檢查你的實作。")
        print(f"\n通過：{result.testsRun - len(result.failures) - len(result.errors)}/{result.testsRun}")
    print("=" * 70)

    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
