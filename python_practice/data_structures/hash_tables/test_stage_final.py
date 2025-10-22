"""
最終測試階段: 完整整合測試 (Final Integration Tests)

學習目標：
1. 驗證雜湊表在各種複雜場景下的穩定性
2. 測試極端情況和邊界條件
3. 性能和壓力測試
4. 實際應用場景模擬

測試重點：
- 大規模資料操作
- 混合操作序列
- 極端情況處理
- 實際應用場景
"""

import unittest
import random
import string
from hash_table import HashTable


class TestStageFinal(unittest.TestCase):
    """最終階段：完整整合測試"""

    def test_01_large_scale_operations(self):
        """測試大規模操作"""
        ht = HashTable()
        n = 1000

        # 插入 1000 個元素
        for i in range(n):
            ht.put(f"key{i}", i * 2)

        # 驗證大小
        self.assertEqual(ht.size(), n)

        # 隨機查詢
        for _ in range(100):
            i = random.randint(0, n - 1)
            self.assertEqual(ht.get(f"key{i}"), i * 2)

        # 刪除一半
        for i in range(0, n, 2):
            ht.remove(f"key{i}")

        self.assertEqual(ht.size(), n // 2)

    def test_02_random_operations_sequence(self):
        """測試隨機操作序列"""
        ht = HashTable()
        reference = {}  # Python 字典作為參考

        operations = ['put', 'get', 'remove', 'contains']
        keys = [f"key{i}" for i in range(50)]

        for _ in range(500):
            op = random.choice(operations)
            key = random.choice(keys)

            if op == 'put':
                value = random.randint(1, 1000)
                ht.put(key, value)
                reference[key] = value

            elif op == 'get':
                if key in reference:
                    self.assertEqual(ht.get(key), reference[key])
                else:
                    with self.assertRaises(KeyError):
                        ht.get(key)

            elif op == 'remove':
                if key in reference:
                    ht.remove(key)
                    del reference[key]
                else:
                    with self.assertRaises(KeyError):
                        ht.remove(key)

            elif op == 'contains':
                self.assertEqual(ht.contains(key), key in reference)

        # 最終狀態應該一致
        self.assertEqual(ht.size(), len(reference))

    def test_03_stress_test_with_collisions(self):
        """碰撞壓力測試"""
        # 使用小容量增加碰撞
        ht = HashTable(capacity=16)

        # 插入大量元素
        n = 500
        for i in range(n):
            ht.put(f"item_{i}", i)

        # 驗證所有元素
        for i in range(n):
            self.assertEqual(ht.get(f"item_{i}"), i)

        self.assertEqual(ht.size(), n)

    def test_04_dictionary_implementation(self):
        """字典實作測試"""
        word_freq = HashTable()

        text = """
        Python is a high-level programming language.
        Python is widely used for web development.
        Programming is fun and Python makes it easier.
        """

        # 統計單詞頻率
        words = text.lower().split()
        for word in words:
            word = word.strip('.,')
            if word:
                if word_freq.contains(word):
                    count = word_freq.get(word)
                    word_freq.put(word, count + 1)
                else:
                    word_freq.put(word, 1)

        # 驗證特定單詞的頻率
        self.assertEqual(word_freq.get("python"), 3)
        self.assertEqual(word_freq.get("is"), 3)
        self.assertGreater(word_freq.size(), 0)

    def test_05_cache_implementation(self):
        """快取實作測試"""
        cache = HashTable()
        MAX_SIZE = 100

        def get_from_cache(key):
            """從快取獲取數據"""
            if cache.contains(key):
                return cache.get(key)
            return None

        def put_in_cache(key, value):
            """放入快取"""
            if cache.size() >= MAX_SIZE:
                # 簡單策略：清空重新開始
                cache.clear()
            cache.put(key, value)

        # 模擬快取使用
        for i in range(150):
            key = f"data_{i % 50}"  # 重複使用一些鍵
            value = get_from_cache(key)

            if value is None:
                # 快取未命中，計算並存入
                value = i * i
                put_in_cache(key, value)

        # 快取應該不超過最大大小
        self.assertLessEqual(cache.size(), MAX_SIZE)

    def test_06_user_session_management(self):
        """用戶會話管理測試"""
        sessions = HashTable()

        # 建立多個用戶會話
        for i in range(100):
            session_id = f"session_{i}"
            user_data = {
                "user_id": f"user_{i}",
                "login_time": f"2025-01-{(i % 28) + 1}",
                "ip": f"192.168.1.{i % 255}"
            }
            sessions.put(session_id, user_data)

        # 驗證會話
        self.assertEqual(sessions.size(), 100)

        # 查詢特定會話
        session_data = sessions.get("session_50")
        self.assertEqual(session_data["user_id"], "user_50")

        # 登出（刪除會話）
        for i in range(10):
            sessions.remove(f"session_{i}")

        self.assertEqual(sessions.size(), 90)

    def test_07_configuration_manager(self):
        """配置管理器測試"""
        config = HashTable()

        # 載入配置
        config.put("database.host", "localhost")
        config.put("database.port", 5432)
        config.put("database.name", "myapp")
        config.put("cache.enabled", True)
        config.put("cache.ttl", 3600)
        config.put("api.timeout", 30)
        config.put("api.retries", 3)

        # 讀取配置
        self.assertEqual(config.get("database.host"), "localhost")
        self.assertEqual(config.get("cache.enabled"), True)

        # 更新配置
        config.put("api.timeout", 60)
        self.assertEqual(config.get("api.timeout"), 60)

        # 獲取所有配置鍵
        keys = config.keys()
        self.assertEqual(len(keys), 7)

    def test_08_phone_book(self):
        """電話簿測試"""
        phone_book = HashTable()

        # 新增聯絡人
        contacts = {
            "Alice": "0912-345-678",
            "Bob": "0923-456-789",
            "Charlie": "0934-567-890",
            "David": "0945-678-901",
            "Eve": "0956-789-012"
        }

        for name, phone in contacts.items():
            phone_book.put(name, phone)

        # 查詢
        self.assertEqual(phone_book.get("Alice"), "0912-345-678")

        # 更新
        phone_book.put("Alice", "0911-111-111")
        self.assertEqual(phone_book.get("Alice"), "0911-111-111")

        # 刪除
        phone_book.remove("Bob")
        self.assertFalse(phone_book.contains("Bob"))

        # 列出所有聯絡人
        names = phone_book.keys()
        self.assertEqual(len(names), 4)

    def test_09_symbol_table(self):
        """符號表測試（編譯器應用）"""
        symbol_table = HashTable()

        # 變數聲明
        symbol_table.put("x", {"type": "int", "value": 10})
        symbol_table.put("y", {"type": "float", "value": 3.14})
        symbol_table.put("name", {"type": "string", "value": "Alice"})

        # 查找變數
        x_info = symbol_table.get("x")
        self.assertEqual(x_info["type"], "int")
        self.assertEqual(x_info["value"], 10)

        # 變數賦值（更新）
        symbol_table.put("x", {"type": "int", "value": 20})
        self.assertEqual(symbol_table.get("x")["value"], 20)

        # 檢查變數是否存在
        self.assertTrue(symbol_table.contains("y"))
        self.assertFalse(symbol_table.contains("z"))

    def test_10_extreme_load_factor(self):
        """極端負載因子測試"""
        # 高負載因子
        ht_high = HashTable(capacity=10, load_factor=0.95)
        for i in range(20):
            ht_high.put(f"key{i}", i)

        self.assertEqual(ht_high.size(), 20)
        for i in range(20):
            self.assertEqual(ht_high.get(f"key{i}"), i)

        # 低負載因子
        ht_low = HashTable(capacity=10, load_factor=0.3)
        for i in range(20):
            ht_low.put(f"key{i}", i)

        self.assertEqual(ht_low.size(), 20)
        for i in range(20):
            self.assertEqual(ht_low.get(f"key{i}"), i)

    def test_11_string_key_operations(self):
        """字串鍵操作測試"""
        ht = HashTable()

        # 使用各種字串作為鍵
        test_strings = [
            "",  # 空字串
            " ",  # 空白
            "a",  # 單字元
            "Hello, World!",  # 包含標點
            "你好世界",  # 中文
            "🎉🎊",  # emoji
            "a" * 100,  # 長字串
            "key\nwith\nnewlines",  # 包含換行
            "key\twith\ttabs",  # 包含 tab
        ]

        for i, key in enumerate(test_strings):
            ht.put(key, i)

        # 驗證
        for i, key in enumerate(test_strings):
            self.assertEqual(ht.get(key), i)

    def test_12_mixed_type_keys(self):
        """混合類型鍵測試"""
        ht = HashTable()

        # 不同類型的鍵
        ht.put("string", 1)
        ht.put(42, 2)
        ht.put(3.14, 3)
        ht.put((1, 2, 3), 4)
        ht.put(True, 5)

        self.assertEqual(ht.size(), 5)
        self.assertEqual(ht.get("string"), 1)
        self.assertEqual(ht.get(42), 2)
        self.assertEqual(ht.get(3.14), 3)
        self.assertEqual(ht.get((1, 2, 3)), 4)
        self.assertEqual(ht.get(True), 5)

    def test_13_complex_values(self):
        """複雜值類型測試"""
        ht = HashTable()

        # 各種複雜的值
        ht.put("list", [1, 2, 3, 4, 5])
        ht.put("dict", {"nested": {"key": "value"}})
        ht.put("tuple", (1, 2, 3))
        ht.put("set", {1, 2, 3})
        ht.put("none", None)

        self.assertEqual(ht.get("list"), [1, 2, 3, 4, 5])
        self.assertEqual(ht.get("dict"), {"nested": {"key": "value"}})
        self.assertEqual(ht.get("tuple"), (1, 2, 3))
        self.assertEqual(ht.get("set"), {1, 2, 3})
        self.assertIsNone(ht.get("none"))

    def test_14_performance_consistency(self):
        """性能一致性測試"""
        ht = HashTable()

        # 插入大量元素後，操作時間應該保持穩定
        n = 10000

        # 插入
        for i in range(n):
            ht.put(f"key{i}", i)

        # 隨機訪問應該很快（雖然我們不測量時間，但驗證正確性）
        for _ in range(1000):
            i = random.randint(0, n - 1)
            value = ht.get(f"key{i}")
            self.assertEqual(value, i)

    def test_15_complete_lifecycle(self):
        """完整生命週期測試"""
        ht = HashTable(capacity=8, load_factor=0.75)

        # 階段 1: 初始化
        self.assertTrue(ht.is_empty())
        self.assertEqual(ht.get_capacity(), 8)

        # 階段 2: 填充
        for i in range(20):
            ht.put(f"key{i}", i)

        self.assertEqual(ht.size(), 20)
        self.assertGreater(ht.get_capacity(), 8)  # 應該已經擴容

        # 階段 3: 混合操作
        for i in range(5):
            ht.remove(f"key{i}")

        for i in range(10, 15):
            ht.put(f"key{i}", i * 2)  # 更新

        # 階段 4: 驗證
        self.assertEqual(ht.size(), 15)
        for i in range(5):
            self.assertFalse(ht.contains(f"key{i}"))

        for i in range(10, 15):
            self.assertEqual(ht.get(f"key{i}"), i * 2)

        # 階段 5: 清空
        ht.clear()
        self.assertTrue(ht.is_empty())

        # 階段 6: 重新使用
        ht.put("new_key", "new_value")
        self.assertEqual(ht.size(), 1)
        self.assertEqual(ht.get("new_key"), "new_value")


def run_tests():
    """執行所有測試"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStageFinal)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print("🎉🎊 恭喜！你已經完成了所有測試！ 🎊🎉")
        print("\n你已經完全掌握了雜湊表資料結構：")
        print("✓ 雜湊函數設計")
        print("✓ 碰撞處理（分離鏈結法）")
        print("✓ 動態調整大小")
        print("✓ 完整的字典操作")
        print("✓ 實際應用場景")
        print("✓ 極端情況處理")
        print("\n你現在可以：")
        print("• 實作自己的雜湊表")
        print("• 理解 Python dict 的底層原理")
        print("• 解決相關的面試問題")
        print("• 在專案中正確使用雜湊表")
        print("\n建議下一步：")
        print("• 閱讀 HASH_TABLE_LEARNING_GUIDE.md 深入學習")
        print("• 嘗試實作開放定址法")
        print("• 研究更進階的雜湊函數")
        print("• 解決 LeetCode 上的雜湊表相關題目")
    else:
        print("❌ 還有一些測試沒有通過，請檢查你的實作。")
        print(f"\n通過：{result.testsRun - len(result.failures) - len(result.errors)}/{result.testsRun}")
    print("=" * 70)

    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
