"""
測試階段 2: 基本的 put 和 get 操作

學習目標：
1. 理解如何插入鍵值對
2. 理解如何查找鍵值對
3. 理解更新現有鍵的值
4. 處理鍵不存在的情況

測試重點：
- put 方法正確插入新的鍵值對
- get 方法正確回傳對應的值
- 更新現有鍵的值
- 查找不存在的鍵會拋出 KeyError
"""

import unittest
from hash_table import HashTable


class TestStage2(unittest.TestCase):
    """階段 2：基本的 put/get 操作測試"""

    def setUp(self):
        """每個測試前的設置"""
        self.ht = HashTable()

    def test_01_put_single_item(self):
        """測試插入單一鍵值對"""
        self.ht.put("name", "Alice")

        self.assertEqual(self.ht.size(), 1,
                         "插入一個鍵值對後，大小應該是 1")
        self.assertFalse(self.ht.is_empty(),
                        "插入後雜湊表不應該是空的")

    def test_02_get_existing_item(self):
        """測試取得存在的鍵"""
        self.ht.put("name", "Alice")

        value = self.ht.get("name")
        self.assertEqual(value, "Alice",
                         "應該回傳正確的值")

    def test_03_put_multiple_items(self):
        """測試插入多個鍵值對"""
        self.ht.put("name", "Alice")
        self.ht.put("age", 25)
        self.ht.put("city", "Taipei")

        self.assertEqual(self.ht.size(), 3,
                         "插入三個鍵值對後，大小應該是 3")

    def test_04_get_multiple_items(self):
        """測試取得多個鍵值對"""
        self.ht.put("name", "Alice")
        self.ht.put("age", 25)
        self.ht.put("city", "Taipei")

        self.assertEqual(self.ht.get("name"), "Alice")
        self.assertEqual(self.ht.get("age"), 25)
        self.assertEqual(self.ht.get("city"), "Taipei")

    def test_05_update_existing_key(self):
        """測試更新現有鍵的值"""
        self.ht.put("name", "Alice")
        self.assertEqual(self.ht.get("name"), "Alice")

        # 更新值
        self.ht.put("name", "Bob")
        self.assertEqual(self.ht.get("name"), "Bob",
                         "更新後應該回傳新的值")

        # 大小不應該改變
        self.assertEqual(self.ht.size(), 1,
                         "更新現有鍵不應該增加大小")

    def test_06_get_nonexistent_key(self):
        """測試取得不存在的鍵"""
        self.ht.put("name", "Alice")

        # 查找不存在的鍵應該拋出 KeyError
        with self.assertRaises(KeyError):
            self.ht.get("age")

    def test_07_get_from_empty_table(self):
        """測試從空雜湊表取得值"""
        # 空雜湊表查找任何鍵都應該拋出 KeyError
        with self.assertRaises(KeyError):
            self.ht.get("anything")

    def test_08_put_different_data_types(self):
        """測試插入不同資料型別"""
        # 字串鍵
        self.ht.put("string_key", "value")

        # 整數鍵
        self.ht.put(123, "number_key")

        # 元組鍵（不可變）
        self.ht.put((1, 2), "tuple_key")

        self.assertEqual(self.ht.get("string_key"), "value")
        self.assertEqual(self.ht.get(123), "number_key")
        self.assertEqual(self.ht.get((1, 2)), "tuple_key")

    def test_09_put_with_none_value(self):
        """測試插入 None 作為值"""
        self.ht.put("key", None)

        self.assertEqual(self.ht.size(), 1,
                         "None 也是有效的值")
        self.assertIsNone(self.ht.get("key"),
                         "應該能夠儲存和取得 None 值")

    def test_10_contains_method(self):
        """測試 contains 方法"""
        self.ht.put("name", "Alice")
        self.ht.put("age", 25)

        # 存在的鍵
        self.assertTrue(self.ht.contains("name"),
                       "contains 應該對存在的鍵回傳 True")
        self.assertTrue(self.ht.contains("age"),
                       "contains 應該對存在的鍵回傳 True")

        # 不存在的鍵
        self.assertFalse(self.ht.contains("city"),
                        "contains 應該對不存在的鍵回傳 False")

    def test_11_put_and_get_sequence(self):
        """測試插入和查找的序列操作"""
        # 插入
        self.ht.put("a", 1)
        self.assertEqual(self.ht.get("a"), 1)

        self.ht.put("b", 2)
        self.assertEqual(self.ht.get("b"), 2)
        self.assertEqual(self.ht.get("a"), 1)  # 確保 a 還在

        self.ht.put("c", 3)
        self.assertEqual(self.ht.get("c"), 3)
        self.assertEqual(self.ht.get("b"), 2)  # 確保 b 還在
        self.assertEqual(self.ht.get("a"), 1)  # 確保 a 還在

    def test_12_overwrite_with_different_type(self):
        """測試用不同型別的值覆寫"""
        self.ht.put("key", "string")
        self.assertEqual(self.ht.get("key"), "string")

        self.ht.put("key", 123)
        self.assertEqual(self.ht.get("key"), 123)

        self.ht.put("key", [1, 2, 3])
        self.assertEqual(self.ht.get("key"), [1, 2, 3])

    def test_13_size_tracking(self):
        """測試大小追蹤的正確性"""
        self.assertEqual(self.ht.size(), 0)

        self.ht.put("a", 1)
        self.assertEqual(self.ht.size(), 1)

        self.ht.put("b", 2)
        self.assertEqual(self.ht.size(), 2)

        # 更新不應該改變大小
        self.ht.put("a", 10)
        self.assertEqual(self.ht.size(), 2)

        self.ht.put("c", 3)
        self.assertEqual(self.ht.size(), 3)


def run_tests():
    """執行所有測試"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage2)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print("🎉 恭喜！階段 2 的所有測試都通過了！")
        print("\n你已經掌握了：")
        print("✓ put 方法的實作")
        print("✓ get 方法的實作")
        print("✓ 更新現有鍵的值")
        print("✓ 例外處理")
        print("\n準備好進入階段 3：碰撞處理")
    else:
        print("❌ 還有一些測試沒有通過，請檢查你的實作。")
        print(f"\n通過：{result.testsRun - len(result.failures) - len(result.errors)}/{result.testsRun}")
    print("=" * 70)

    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
