"""
測試階段 6: 進階操作 (Advanced Operations)

學習目標：
1. 實作和使用 keys()、values() 方法
2. 實作 clear() 方法
3. 測試字串表示方法
4. 綜合運用所有基本操作

測試重點：
- keys() 回傳所有鍵
- values() 回傳所有值
- clear() 清空雜湊表
- 字串表示的正確性
- 複雜場景的綜合測試
"""

import unittest
from hash_table import HashTable


class TestStage6(unittest.TestCase):
    """階段 6：進階操作測試"""

    def setUp(self):
        """每個測試前的設置"""
        self.ht = HashTable()

    def test_01_keys_empty_table(self):
        """測試空雜湊表的 keys"""
        keys = self.ht.keys()
        self.assertEqual(keys, [],
                         "空雜湊表應該回傳空列表")

    def test_02_keys_single_item(self):
        """測試單一元素的 keys"""
        self.ht.put("key", "value")
        keys = self.ht.keys()

        self.assertEqual(len(keys), 1)
        self.assertIn("key", keys)

    def test_03_keys_multiple_items(self):
        """測試多個元素的 keys"""
        data = {"a": 1, "b": 2, "c": 3, "d": 4}
        for key, value in data.items():
            self.ht.put(key, value)

        keys = self.ht.keys()

        self.assertEqual(len(keys), 4)
        for key in data.keys():
            self.assertIn(key, keys,
                         f"keys() 應該包含鍵 {key}")

    def test_04_values_empty_table(self):
        """測試空雜湊表的 values"""
        values = self.ht.values()
        self.assertEqual(values, [],
                         "空雜湊表應該回傳空列表")

    def test_05_values_single_item(self):
        """測試單一元素的 values"""
        self.ht.put("key", "value")
        values = self.ht.values()

        self.assertEqual(len(values), 1)
        self.assertIn("value", values)

    def test_06_values_multiple_items(self):
        """測試多個元素的 values"""
        data = {"a": 1, "b": 2, "c": 3, "d": 4}
        for key, value in data.items():
            self.ht.put(key, value)

        values = self.ht.values()

        self.assertEqual(len(values), 4)
        for value in data.values():
            self.assertIn(value, values,
                         f"values() 應該包含值 {value}")

    def test_07_keys_values_correspondence(self):
        """測試 keys 和 values 的對應關係"""
        data = {"apple": 100, "banana": 200, "cherry": 300}
        for key, value in data.items():
            self.ht.put(key, value)

        keys = self.ht.keys()
        values = self.ht.values()

        # 數量應該相同
        self.assertEqual(len(keys), len(values))

        # 每個鍵對應的值應該在 values 中
        for key in keys:
            value = self.ht.get(key)
            self.assertIn(value, values)

    def test_08_clear_empty_table(self):
        """測試清空空雜湊表"""
        self.ht.clear()

        self.assertTrue(self.ht.is_empty())
        self.assertEqual(self.ht.size(), 0)

    def test_09_clear_non_empty_table(self):
        """測試清空非空雜湊表"""
        for i in range(10):
            self.ht.put(f"key{i}", i)

        self.assertEqual(self.ht.size(), 10)

        self.ht.clear()

        self.assertTrue(self.ht.is_empty())
        self.assertEqual(self.ht.size(), 0)
        self.assertEqual(self.ht.keys(), [])
        self.assertEqual(self.ht.values(), [])

    def test_10_clear_and_reuse(self):
        """測試清空後重新使用"""
        # 第一輪
        self.ht.put("a", 1)
        self.ht.put("b", 2)
        self.ht.clear()

        # 第二輪
        self.ht.put("c", 3)
        self.ht.put("d", 4)

        self.assertEqual(self.ht.size(), 2)
        self.assertTrue(self.ht.contains("c"))
        self.assertTrue(self.ht.contains("d"))
        self.assertFalse(self.ht.contains("a"))
        self.assertFalse(self.ht.contains("b"))

    def test_11_str_representation_with_items(self):
        """測試非空雜湊表的字串表示"""
        self.ht.put("name", "Alice")
        self.ht.put("age", 25)

        str_repr = str(self.ht)

        # 應該包含鍵值對
        self.assertIn("name", str_repr)
        self.assertIn("Alice", str_repr)
        self.assertIn("age", str_repr)
        self.assertIn("25", str_repr)

    def test_12_keys_after_remove(self):
        """測試刪除後的 keys"""
        self.ht.put("a", 1)
        self.ht.put("b", 2)
        self.ht.put("c", 3)

        self.ht.remove("b")

        keys = self.ht.keys()
        self.assertEqual(len(keys), 2)
        self.assertIn("a", keys)
        self.assertNotIn("b", keys)
        self.assertIn("c", keys)

    def test_13_values_after_update(self):
        """測試更新後的 values"""
        self.ht.put("a", 1)
        self.ht.put("b", 2)
        self.ht.put("a", 10)  # 更新

        values = self.ht.values()
        self.assertEqual(len(values), 2)
        self.assertIn(10, values)
        self.assertIn(2, values)
        self.assertNotIn(1, values,
                        "舊值應該被替換")

    def test_14_iteration_pattern(self):
        """測試迭代模式"""
        data = {"apple": 100, "banana": 200, "cherry": 300}
        for key, value in data.items():
            self.ht.put(key, value)

        # 使用 keys() 迭代
        retrieved_data = {}
        for key in self.ht.keys():
            retrieved_data[key] = self.ht.get(key)

        self.assertEqual(retrieved_data, data,
                        "應該能正確迭代所有鍵值對")

    def test_15_keys_values_with_duplicates_values(self):
        """測試值有重複的情況"""
        self.ht.put("a", 100)
        self.ht.put("b", 100)  # 相同的值
        self.ht.put("c", 200)

        keys = self.ht.keys()
        values = self.ht.values()

        self.assertEqual(len(keys), 3,
                        "鍵應該是唯一的")
        self.assertEqual(len(values), 3,
                        "即使值重複，也應該回傳所有值")

        # 應該有兩個 100
        self.assertEqual(values.count(100), 2)
        self.assertEqual(values.count(200), 1)

    def test_16_complex_workflow(self):
        """測試複雜的工作流程"""
        # 插入
        self.ht.put("user1", {"name": "Alice", "age": 25})
        self.ht.put("user2", {"name": "Bob", "age": 30})
        self.ht.put("user3", {"name": "Charlie", "age": 35})

        # 查詢
        user1 = self.ht.get("user1")
        self.assertEqual(user1["name"], "Alice")

        # 更新
        self.ht.put("user1", {"name": "Alice", "age": 26})

        # 刪除
        self.ht.remove("user2")

        # 檢查狀態
        self.assertEqual(self.ht.size(), 2)
        self.assertTrue(self.ht.contains("user1"))
        self.assertFalse(self.ht.contains("user2"))
        self.assertTrue(self.ht.contains("user3"))

        # 獲取所有鍵
        keys = self.ht.keys()
        self.assertEqual(len(keys), 2)
        self.assertIn("user1", keys)
        self.assertIn("user3", keys)

    def test_17_keys_with_different_types(self):
        """測試不同類型的鍵"""
        self.ht.put("string", 1)
        self.ht.put(123, 2)
        self.ht.put((1, 2), 3)

        keys = self.ht.keys()
        self.assertEqual(len(keys), 3)
        self.assertIn("string", keys)
        self.assertIn(123, keys)
        self.assertIn((1, 2), keys)

    def test_18_values_with_none(self):
        """測試包含 None 的值"""
        self.ht.put("a", None)
        self.ht.put("b", 100)
        self.ht.put("c", None)

        values = self.ht.values()
        self.assertEqual(len(values), 3)
        self.assertEqual(values.count(None), 2)
        self.assertEqual(values.count(100), 1)

    def test_19_keys_values_after_resize(self):
        """測試擴容後的 keys 和 values"""
        # 插入足夠多的元素以觸發擴容
        for i in range(20):
            self.ht.put(f"key{i}", i * 10)

        keys = self.ht.keys()
        values = self.ht.values()

        self.assertEqual(len(keys), 20)
        self.assertEqual(len(values), 20)

        # 驗證所有鍵值對都正確
        for i in range(20):
            self.assertIn(f"key{i}", keys)
            self.assertIn(i * 10, values)

    def test_20_comprehensive_operations(self):
        """綜合操作測試"""
        # 建立學生成績系統
        students = {
            "S001": {"name": "Alice", "score": 85},
            "S002": {"name": "Bob", "score": 92},
            "S003": {"name": "Charlie", "score": 78},
            "S004": {"name": "David", "score": 88},
            "S005": {"name": "Eve", "score": 95}
        }

        # 插入所有學生
        for student_id, info in students.items():
            self.ht.put(student_id, info)

        # 更新一個學生的成績
        self.ht.put("S001", {"name": "Alice", "score": 90})

        # 刪除一個學生
        self.ht.remove("S003")

        # 檢查
        self.assertEqual(self.ht.size(), 4)

        # 獲取所有學生 ID
        student_ids = self.ht.keys()
        self.assertEqual(len(student_ids), 4)
        self.assertIn("S001", student_ids)
        self.assertNotIn("S003", student_ids)

        # 計算平均分（從 values 中提取）
        scores = [info["score"] for info in self.ht.values()]
        avg_score = sum(scores) / len(scores)
        self.assertGreater(avg_score, 0)

        # 清空後重新開始
        self.ht.clear()
        self.assertTrue(self.ht.is_empty())


def run_tests():
    """執行所有測試"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage6)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print("🎉 恭喜！階段 6 的所有測試都通過了！")
        print("\n你已經掌握了：")
        print("✓ keys() 和 values() 方法")
        print("✓ clear() 方法")
        print("✓ 字串表示")
        print("✓ 複雜場景的綜合運用")
        print("\n準備好進入最終階段：完整整合測試")
    else:
        print("❌ 還有一些測試沒有通過，請檢查你的實作。")
        print(f"\n通過：{result.testsRun - len(result.failures) - len(result.errors)}/{result.testsRun}")
    print("=" * 70)

    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
