"""
測試階段 5: 動態調整大小 (Dynamic Resizing)

學習目標：
1. 理解負載因子的概念
2. 理解何時需要擴容
3. 理解重新雜湊 (rehashing) 的過程
4. 驗證擴容後的正確性

測試重點：
- 超過負載因子閾值時自動擴容
- 擴容後所有元素仍可正確訪問
- 擴容後的容量正確加倍
- 擴容不影響已存在的鍵值對
"""

import unittest
from hash_table import HashTable


class TestStage5(unittest.TestCase):
    """階段 5：動態調整大小測試"""

    def test_01_initial_capacity(self):
        """測試初始容量"""
        ht = HashTable(capacity=16)
        self.assertEqual(ht.get_capacity(), 16)

    def test_02_load_factor_calculation(self):
        """測試負載因子計算"""
        ht = HashTable(capacity=10)

        self.assertEqual(ht.get_load_factor(), 0.0,
                         "空雜湊表的負載因子應該是 0")

        ht.put("a", 1)
        self.assertAlmostEqual(ht.get_load_factor(), 0.1,
                              places=2)

        ht.put("b", 2)
        self.assertAlmostEqual(ht.get_load_factor(), 0.2,
                              places=2)

        for i in range(3, 8):
            ht.put(f"key{i}", i)

        # 7 個元素，容量 10，負載因子 = 0.7
        self.assertAlmostEqual(ht.get_load_factor(), 0.7,
                              places=2)

    def test_03_resize_triggered_by_load_factor(self):
        """測試負載因子觸發擴容"""
        # 使用小容量和標準負載因子
        ht = HashTable(capacity=4, load_factor=0.75)

        initial_capacity = ht.get_capacity()
        self.assertEqual(initial_capacity, 4)

        # 插入元素直到觸發擴容
        # 4 * 0.75 = 3，所以插入第 4 個元素時應該擴容
        ht.put("a", 1)
        ht.put("b", 2)
        ht.put("c", 3)

        # 此時還沒擴容
        self.assertEqual(ht.get_capacity(), 4)

        # 插入第 4 個元素，應該觸發擴容
        ht.put("d", 4)

        # 容量應該加倍
        self.assertEqual(ht.get_capacity(), 8,
                         "超過負載因子後應該擴容到 8")

    def test_04_data_preserved_after_resize(self):
        """測試擴容後資料完整性"""
        ht = HashTable(capacity=4, load_factor=0.75)

        # 插入資料
        data = {f"key{i}": i * 10 for i in range(10)}
        for key, value in data.items():
            ht.put(key, value)

        # 容量應該已經擴容（可能多次）
        self.assertGreater(ht.get_capacity(), 4,
                          "插入 10 個元素後應該已經擴容")

        # 驗證所有資料都還在
        for key, value in data.items():
            self.assertEqual(ht.get(key), value,
                           f"擴容後鍵 {key} 的值應該保持不變")

        # 驗證大小
        self.assertEqual(ht.size(), len(data))

    def test_05_multiple_resizes(self):
        """測試多次擴容"""
        ht = HashTable(capacity=2, load_factor=0.75)

        # 記錄容量變化
        capacities = [ht.get_capacity()]

        # 插入足夠多的元素以觸發多次擴容
        for i in range(20):
            ht.put(f"key{i}", i)
            current_capacity = ht.get_capacity()
            if current_capacity != capacities[-1]:
                capacities.append(current_capacity)

        # 應該發生多次擴容
        self.assertGreater(len(capacities), 1,
                          "應該發生多次擴容")

        # 每次擴容都應該是加倍
        for i in range(1, len(capacities)):
            self.assertEqual(capacities[i], capacities[i - 1] * 2,
                           f"擴容應該是加倍: {capacities[i-1]} -> {capacities[i]}")

        # 驗證所有資料完整性
        for i in range(20):
            self.assertEqual(ht.get(f"key{i}"), i)

    def test_06_resize_with_custom_load_factor(self):
        """測試自訂負載因子的擴容"""
        # 使用較低的負載因子，會更早擴容
        ht = HashTable(capacity=10, load_factor=0.5)

        # 10 * 0.5 = 5，插入第 6 個元素時應該擴容
        for i in range(5):
            ht.put(f"key{i}", i)

        self.assertEqual(ht.get_capacity(), 10,
                         "還沒超過負載因子")

        ht.put("key5", 5)

        self.assertEqual(ht.get_capacity(), 20,
                         "超過負載因子後應該擴容")

    def test_07_size_unchanged_after_resize(self):
        """測試擴容不改變元素數量"""
        ht = HashTable(capacity=4, load_factor=0.75)

        for i in range(10):
            ht.put(f"key{i}", i)

        # 大小應該是插入的元素數量，不受擴容影響
        self.assertEqual(ht.size(), 10,
                         "擴容不應該改變元素數量")

    def test_08_contains_after_resize(self):
        """測試擴容後 contains 方法"""
        ht = HashTable(capacity=4, load_factor=0.75)

        keys = [f"key{i}" for i in range(10)]
        for key in keys:
            ht.put(key, key)

        # 驗證所有鍵都存在
        for key in keys:
            self.assertTrue(ht.contains(key),
                          f"擴容後鍵 {key} 應該仍然存在")

    def test_09_remove_after_resize(self):
        """測試擴容後的刪除操作"""
        ht = HashTable(capacity=4, load_factor=0.75)

        # 插入足夠多的元素以觸發擴容
        for i in range(10):
            ht.put(f"key{i}", i)

        # 確保已經擴容
        self.assertGreater(ht.get_capacity(), 4)

        # 刪除一些元素
        ht.remove("key0")
        ht.remove("key5")

        self.assertEqual(ht.size(), 8)
        self.assertFalse(ht.contains("key0"))
        self.assertFalse(ht.contains("key5"))

        # 其他元素應該仍然存在
        for i in [1, 2, 3, 4, 6, 7, 8, 9]:
            self.assertTrue(ht.contains(f"key{i}"))

    def test_10_update_after_resize(self):
        """測試擴容後的更新操作"""
        ht = HashTable(capacity=4, load_factor=0.75)

        # 觸發擴容
        for i in range(10):
            ht.put(f"key{i}", i)

        # 更新一些值
        ht.put("key0", 100)
        ht.put("key5", 500)

        self.assertEqual(ht.get("key0"), 100)
        self.assertEqual(ht.get("key5"), 500)
        self.assertEqual(ht.size(), 10,
                         "更新不應該改變大小")

    def test_11_resize_stress_test(self):
        """擴容壓力測試"""
        ht = HashTable(capacity=2, load_factor=0.75)

        n = 1000
        # 插入大量元素
        for i in range(n):
            ht.put(f"key{i}", i * i)

        # 驗證容量已經大幅增加
        self.assertGreater(ht.get_capacity(), 100)

        # 驗證所有元素都正確
        for i in range(n):
            self.assertEqual(ht.get(f"key{i}"), i * i)

        self.assertEqual(ht.size(), n)

    def test_12_load_factor_after_resize(self):
        """測試擴容後的負載因子"""
        ht = HashTable(capacity=4, load_factor=0.75)

        # 插入元素直到擴容
        for i in range(4):
            ht.put(f"key{i}", i)

        # 擴容後負載因子應該降低
        self.assertLess(ht.get_load_factor(), 0.75,
                       "擴容後負載因子應該降低")

    def test_13_keys_and_values_after_resize(self):
        """測試擴容後的 keys 和 values 方法"""
        ht = HashTable(capacity=4, load_factor=0.75)

        data = {f"key{i}": i * 10 for i in range(10)}
        for key, value in data.items():
            ht.put(key, value)

        keys = ht.keys()
        values = ht.values()

        self.assertEqual(len(keys), 10)
        self.assertEqual(len(values), 10)

        # 驗證所有鍵都在
        for key in data.keys():
            self.assertIn(key, keys)

        # 驗證所有值都在
        for value in data.values():
            self.assertIn(value, values)

    def test_14_clear_after_resize(self):
        """測試擴容後的清空操作"""
        ht = HashTable(capacity=4, load_factor=0.75)

        # 觸發擴容
        for i in range(10):
            ht.put(f"key{i}", i)

        old_capacity = ht.get_capacity()

        # 清空
        ht.clear()

        # 容量不變，但大小為 0
        self.assertEqual(ht.get_capacity(), old_capacity,
                         "清空不應該改變容量")
        self.assertEqual(ht.size(), 0)
        self.assertTrue(ht.is_empty())

    def test_15_progressive_resize(self):
        """測試漸進式擴容"""
        ht = HashTable(capacity=2, load_factor=0.75)

        capacities = []
        sizes = []

        # 逐個插入元素，記錄容量變化
        for i in range(50):
            ht.put(f"key{i}", i)
            capacities.append(ht.get_capacity())
            sizes.append(ht.size())

        # 容量應該階梯式增長
        unique_capacities = sorted(set(capacities))
        self.assertGreater(len(unique_capacities), 1,
                          "應該發生多次擴容")

        # 大小應該線性增長
        for i, size in enumerate(sizes):
            self.assertEqual(size, i + 1,
                           "大小應該等於插入的元素數量")


def run_tests():
    """執行所有測試"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage5)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print("🎉 恭喜！階段 5 的所有測試都通過了！")
        print("\n你已經掌握了：")
        print("✓ 負載因子的計算")
        print("✓ 自動擴容機制")
        print("✓ 重新雜湊過程")
        print("✓ 擴容後的資料完整性")
        print("\n準備好進入階段 6：進階操作")
    else:
        print("❌ 還有一些測試沒有通過，請檢查你的實作。")
        print(f"\n通過：{result.testsRun - len(result.failures) - len(result.errors)}/{result.testsRun}")
    print("=" * 70)

    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
