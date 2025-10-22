"""
測試階段 3: 碰撞處理 (Collision Handling)

學習目標：
1. 理解雜湊碰撞的概念
2. 理解分離鏈結法如何處理碰撞
3. 驗證碰撞情況下的正確行為

測試重點：
- 多個鍵映射到同一個桶時的處理
- 碰撞情況下的插入、查找、更新操作
- 確保鏈結串列正確維護
"""

import unittest
from hash_table import HashTable


class CollisionHashTable(HashTable):
    """
    特製的雜湊表，用於測試碰撞處理
    強制所有鍵雜湊到相同的索引，以測試分離鏈結法
    """

    def _hash(self, key):
        """強制所有鍵雜湊到索引 0"""
        return 0


class TestStage3(unittest.TestCase):
    """階段 3：碰撞處理測試"""

    def setUp(self):
        """每個測試前的設置"""
        self.ht = HashTable()
        self.collision_ht = CollisionHashTable(capacity=10)

    def test_01_forced_collision_insertion(self):
        """測試強制碰撞情況下的插入"""
        # 所有鍵都會雜湊到同一個桶
        self.collision_ht.put("key1", "value1")
        self.collision_ht.put("key2", "value2")
        self.collision_ht.put("key3", "value3")

        self.assertEqual(self.collision_ht.size(), 3,
                         "即使碰撞，也應該正確儲存所有鍵值對")

    def test_02_forced_collision_retrieval(self):
        """測試強制碰撞情況下的查找"""
        self.collision_ht.put("key1", "value1")
        self.collision_ht.put("key2", "value2")
        self.collision_ht.put("key3", "value3")

        # 每個鍵都應該回傳正確的值
        self.assertEqual(self.collision_ht.get("key1"), "value1")
        self.assertEqual(self.collision_ht.get("key2"), "value2")
        self.assertEqual(self.collision_ht.get("key3"), "value3")

    def test_03_forced_collision_update(self):
        """測試強制碰撞情況下的更新"""
        self.collision_ht.put("key1", "value1")
        self.collision_ht.put("key2", "value2")
        self.collision_ht.put("key3", "value3")

        # 更新中間的鍵
        self.collision_ht.put("key2", "new_value2")

        self.assertEqual(self.collision_ht.get("key2"), "new_value2",
                         "應該正確更新碰撞鏈中的值")
        self.assertEqual(self.collision_ht.size(), 3,
                         "更新不應該改變大小")

        # 確保其他鍵沒有受影響
        self.assertEqual(self.collision_ht.get("key1"), "value1")
        self.assertEqual(self.collision_ht.get("key3"), "value3")

    def test_04_collision_with_same_hash(self):
        """測試實際碰撞情況"""
        # 使用小容量增加碰撞機會
        small_ht = HashTable(capacity=4)

        # 插入多個鍵，增加碰撞機會
        keys = [f"key{i}" for i in range(10)]
        for i, key in enumerate(keys):
            small_ht.put(key, i)

        # 驗證所有鍵值對都正確儲存
        self.assertEqual(small_ht.size(), 10)
        for i, key in enumerate(keys):
            self.assertEqual(small_ht.get(key), i,
                           f"鍵 {key} 應該回傳正確的值")

    def test_05_collision_chain_order(self):
        """測試碰撞鏈的順序不影響結果"""
        self.collision_ht.put("a", 1)
        self.collision_ht.put("b", 2)
        self.collision_ht.put("c", 3)

        # 無論插入順序如何，都應該能正確查找
        self.assertEqual(self.collision_ht.get("c"), 3)
        self.assertEqual(self.collision_ht.get("a"), 1)
        self.assertEqual(self.collision_ht.get("b"), 2)

    def test_06_contains_with_collision(self):
        """測試碰撞情況下的 contains 方法"""
        self.collision_ht.put("key1", "value1")
        self.collision_ht.put("key2", "value2")
        self.collision_ht.put("key3", "value3")

        self.assertTrue(self.collision_ht.contains("key1"))
        self.assertTrue(self.collision_ht.contains("key2"))
        self.assertTrue(self.collision_ht.contains("key3"))
        self.assertFalse(self.collision_ht.contains("key4"))

    def test_07_many_collisions(self):
        """測試大量碰撞"""
        # 所有鍵都雜湊到同一個桶
        n = 50
        for i in range(n):
            self.collision_ht.put(f"key{i}", i)

        # 驗證大小
        self.assertEqual(self.collision_ht.size(), n)

        # 驗證所有值都正確
        for i in range(n):
            self.assertEqual(self.collision_ht.get(f"key{i}"), i)

    def test_08_collision_with_duplicate_updates(self):
        """測試碰撞鏈中的重複更新"""
        self.collision_ht.put("a", 1)
        self.collision_ht.put("b", 2)
        self.collision_ht.put("c", 3)

        # 多次更新同一個鍵
        self.collision_ht.put("b", 20)
        self.collision_ht.put("b", 200)
        self.collision_ht.put("b", 2000)

        self.assertEqual(self.collision_ht.get("b"), 2000)
        self.assertEqual(self.collision_ht.size(), 3,
                         "重複更新不應該增加大小")

    def test_09_natural_collisions(self):
        """測試自然發生的碰撞（使用標準雜湊表）"""
        # 插入足夠多的元素，在小容量下必然會有碰撞
        small_ht = HashTable(capacity=8)

        # 插入 20 個元素，必然會有碰撞
        for i in range(20):
            small_ht.put(f"item_{i}", i * 10)

        # 驗證所有元素都能正確查找
        for i in range(20):
            self.assertEqual(small_ht.get(f"item_{i}"), i * 10)

        self.assertEqual(small_ht.size(), 20)

    def test_10_collision_with_none_values(self):
        """測試碰撞情況下的 None 值"""
        self.collision_ht.put("a", None)
        self.collision_ht.put("b", "value")
        self.collision_ht.put("c", None)

        self.assertIsNone(self.collision_ht.get("a"))
        self.assertEqual(self.collision_ht.get("b"), "value")
        self.assertIsNone(self.collision_ht.get("c"))

    def test_11_collision_error_handling(self):
        """測試碰撞情況下的錯誤處理"""
        self.collision_ht.put("key1", "value1")
        self.collision_ht.put("key2", "value2")

        # 查找不存在的鍵應該拋出 KeyError
        with self.assertRaises(KeyError):
            self.collision_ht.get("key3")

        # 即使桶不為空
        with self.assertRaises(KeyError):
            self.collision_ht.get("nonexistent")

    def test_12_collision_stress_test(self):
        """碰撞壓力測試"""
        # 在單一桶中插入大量元素
        n = 100
        for i in range(n):
            self.collision_ht.put(i, i * i)

        # 驗證所有元素
        for i in range(n):
            self.assertEqual(self.collision_ht.get(i), i * i)

        # 驗證大小
        self.assertEqual(self.collision_ht.size(), n)

        # 驗證 contains
        for i in range(n):
            self.assertTrue(self.collision_ht.contains(i))


def run_tests():
    """執行所有測試"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage3)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print("🎉 恭喜！階段 3 的所有測試都通過了！")
        print("\n你已經掌握了：")
        print("✓ 雜湊碰撞的概念")
        print("✓ 分離鏈結法的實作")
        print("✓ 碰撞情況下的正確操作")
        print("✓ 鏈結串列的維護")
        print("\n準備好進入階段 4：刪除操作")
    else:
        print("❌ 還有一些測試沒有通過，請檢查你的實作。")
        print(f"\n通過：{result.testsRun - len(result.failures) - len(result.errors)}/{result.testsRun}")
    print("=" * 70)

    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
