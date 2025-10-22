"""
測試階段 1: 初始化和雜湊函數測試

學習目標：
1. 理解雜湊表的初始化參數
2. 理解雜湊函數的作用
3. 驗證初始狀態的正確性

測試重點：
- 建構函數正確初始化所有屬性
- 雜湊函數回傳有效的索引範圍
- 初始狀態為空
"""

import unittest
from hash_table import HashTable


class TestStage1(unittest.TestCase):
    """階段 1：初始化和雜湊函數測試"""

    def test_01_default_initialization(self):
        """測試預設初始化"""
        ht = HashTable()

        # 驗證預設容量
        self.assertEqual(ht.get_capacity(), 16,
                         "預設容量應該是 16")

        # 驗證初始大小為 0
        self.assertEqual(ht.size(), 0,
                         "初始大小應該是 0")

        # 驗證初始狀態為空
        self.assertTrue(ht.is_empty(),
                        "新建立的雜湊表應該是空的")

    def test_02_custom_initialization(self):
        """測試自訂容量初始化"""
        ht = HashTable(capacity=32)

        self.assertEqual(ht.get_capacity(), 32,
                         "應該使用自訂的容量")
        self.assertEqual(ht.size(), 0,
                         "初始大小應該是 0")

    def test_03_custom_load_factor(self):
        """測試自訂負載因子"""
        ht = HashTable(capacity=16, load_factor=0.8)

        # 負載因子會在擴容時使用，這裡先驗證初始狀態
        self.assertEqual(ht.get_load_factor(), 0.0,
                         "空的雜湊表負載因子應該是 0")

    def test_04_hash_function_returns_valid_index(self):
        """測試雜湊函數回傳有效索引"""
        ht = HashTable(capacity=10)

        # 測試多個不同的鍵
        keys = ["apple", "banana", "cherry", "date", "elderberry",
                "fig", "grape", "honeydew", 123, 456, 7.89]

        for key in keys:
            index = ht._hash(key)

            # 驗證索引在有效範圍內
            self.assertGreaterEqual(index, 0,
                                    f"雜湊索引不能是負數：key={key}, index={index}")
            self.assertLess(index, ht.get_capacity(),
                           f"雜湊索引必須小於容量：key={key}, index={index}")

    def test_05_hash_function_consistency(self):
        """測試雜湊函數的一致性"""
        ht = HashTable(capacity=16)

        key = "test_key"

        # 同一個鍵多次雜湊應該得到相同的索引
        index1 = ht._hash(key)
        index2 = ht._hash(key)
        index3 = ht._hash(key)

        self.assertEqual(index1, index2,
                         "相同的鍵應該產生相同的雜湊索引")
        self.assertEqual(index2, index3,
                         "相同的鍵應該產生相同的雜湊索引")

    def test_06_different_keys_may_have_different_hashes(self):
        """測試不同的鍵通常會產生不同的雜湊值"""
        ht = HashTable(capacity=100)

        # 使用較大的容量來減少碰撞機會
        keys = [f"key{i}" for i in range(20)]
        hashes = [ht._hash(key) for key in keys]

        # 至少應該有一些不同的雜湊值（不要求全部不同，因為可能有碰撞）
        unique_hashes = len(set(hashes))
        self.assertGreater(unique_hashes, 1,
                          "不同的鍵應該產生多個不同的雜湊值")

    def test_07_is_empty_on_new_table(self):
        """測試新建立的雜湊表是否為空"""
        ht = HashTable()

        self.assertTrue(ht.is_empty(),
                        "新建立的雜湊表應該是空的")
        self.assertEqual(ht.size(), 0,
                         "新建立的雜湊表大小應該是 0")

    def test_08_initial_load_factor(self):
        """測試初始負載因子"""
        ht = HashTable(capacity=16)

        self.assertEqual(ht.get_load_factor(), 0.0,
                         "空的雜湊表負載因子應該是 0.0")

    def test_09_str_representation_empty(self):
        """測試空雜湊表的字串表示"""
        ht = HashTable()

        str_repr = str(ht)
        self.assertEqual(str_repr, "{}",
                         "空雜湊表的字串表示應該是 '{}'")

    def test_10_repr_representation(self):
        """測試雜湊表的 repr 表示"""
        ht = HashTable(capacity=16)

        repr_str = repr(ht)
        self.assertIn("HashTable", repr_str,
                      "repr 應該包含 'HashTable'")
        self.assertIn("size=0", repr_str,
                      "repr 應該包含初始大小")
        self.assertIn("capacity=16", repr_str,
                      "repr 應該包含容量")


def run_tests():
    """執行所有測試"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStage1)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print("🎉 恭喜！階段 1 的所有測試都通過了！")
        print("\n你已經掌握了：")
        print("✓ 雜湊表的初始化")
        print("✓ 雜湊函數的實作")
        print("✓ 基本屬性的存取")
        print("\n準備好進入階段 2：基本的 put/get 操作")
    else:
        print("❌ 還有一些測試沒有通過，請檢查你的實作。")
        print(f"\n通過：{result.testsRun - len(result.failures) - len(result.errors)}/{result.testsRun}")
    print("=" * 70)

    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
