"""
Dynamic Array 測試案例

測試涵蓋：
- 基礎功能測試
- 邊界條件測試
- 容量管理測試
- 錯誤處理測試
"""

import pytest
import sys
from pathlib import Path

# 加入上層目錄以便 import
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from data_structures.arrays.dynamic_array import DynamicArray


class TestDynamicArray:
    """DynamicArray 完整測試套件"""

    def test_initialization(self):
        """測試陣列初始化"""
        # 預設初始化
        arr = DynamicArray()
        assert arr.size() == 0
        assert arr.capacity() == 16
        assert arr.is_empty() is True

        # 自訂初始容量
        arr = DynamicArray(32)
        assert arr.size() == 0
        assert arr.capacity() == 32
        assert arr.is_empty() is True

        # 錯誤的初始容量
        with pytest.raises(ValueError):
            DynamicArray(0)

        with pytest.raises(ValueError):
            DynamicArray(-1)

    def test_push_and_at(self):
        """測試 push 和 at 方法"""
        arr = DynamicArray()

        # 新增元素
        arr.push(1)
        arr.push(2)
        arr.push(3)

        assert arr.size() == 3
        assert arr.is_empty() is False
        assert arr.at(0) == 1
        assert arr.at(1) == 2
        assert arr.at(2) == 3

    def test_at_bounds_checking(self):
        """測試 at 方法的邊界檢查"""
        arr = DynamicArray()
        arr.push(1)

        # 有效索引
        assert arr.at(0) == 1

        # 無效索引
        with pytest.raises(IndexError):
            arr.at(-1)

        with pytest.raises(IndexError):
            arr.at(1)

        with pytest.raises(IndexError):
            arr.at(100)

    def test_pop(self):
        """測試 pop 方法"""
        arr = DynamicArray()

        # 從空陣列 pop
        with pytest.raises(IndexError):
            arr.pop()

        # 正常 pop
        arr.push(1)
        arr.push(2)
        arr.push(3)

        assert arr.pop() == 3
        assert arr.size() == 2
        assert arr.at(1) == 2

        assert arr.pop() == 2
        assert arr.size() == 1

        assert arr.pop() == 1
        assert arr.size() == 0
        assert arr.is_empty() is True

    def test_insert(self):
        """測試 insert 方法"""
        arr = DynamicArray()

        # 在空陣列插入
        arr.insert(0, 1)
        assert arr.size() == 1
        assert arr.at(0) == 1

        # 在中間插入
        arr.push(3)
        arr.insert(1, 2)  # [1, 2, 3]
        assert arr.size() == 3
        assert arr.at(0) == 1
        assert arr.at(1) == 2
        assert arr.at(2) == 3

        # 在開頭插入
        arr.insert(0, 0)  # [0, 1, 2, 3]
        assert arr.size() == 4
        assert arr.at(0) == 0

        # 在尾端插入
        arr.insert(4, 4)  # [0, 1, 2, 3, 4]
        assert arr.size() == 5
        assert arr.at(4) == 4

        # 錯誤的插入位置
        with pytest.raises(IndexError):
            arr.insert(-1, 100)

        with pytest.raises(IndexError):
            arr.insert(10, 100)

    def test_prepend(self):
        """測試 prepend 方法"""
        arr = DynamicArray()

        arr.prepend(3)
        arr.prepend(2)
        arr.prepend(1)

        assert arr.size() == 3
        assert arr.at(0) == 1
        assert arr.at(1) == 2
        assert arr.at(2) == 3

    def test_delete(self):
        """測試 delete 方法"""
        arr = DynamicArray()
        for i in range(5):
            arr.push(i)  # [0, 1, 2, 3, 4]

        # 刪除中間元素
        arr.delete(2)  # [0, 1, 3, 4]
        assert arr.size() == 4
        assert arr.at(2) == 3

        # 刪除開頭元素
        arr.delete(0)  # [1, 3, 4]
        assert arr.size() == 3
        assert arr.at(0) == 1

        # 刪除尾端元素
        arr.delete(2)  # [1, 3]
        assert arr.size() == 2
        assert arr.at(1) == 3

        # 錯誤的刪除位置
        with pytest.raises(IndexError):
            arr.delete(-1)

        with pytest.raises(IndexError):
            arr.delete(5)

    def test_remove(self):
        """測試 remove 方法"""
        arr = DynamicArray()
        arr.push(1)
        arr.push(2)
        arr.push(3)
        arr.push(2)  # [1, 2, 3, 2]

        # 移除存在的元素（移除第一個）
        arr.remove(2)  # [1, 3, 2]
        assert arr.size() == 3
        assert arr.at(1) == 3

        # 移除不存在的元素
        with pytest.raises(ValueError):
            arr.remove(100)

    def test_find(self):
        """測試 find 方法"""
        arr = DynamicArray()
        arr.push(1)
        arr.push(2)
        arr.push(3)
        arr.push(2)

        # 找到第一個匹配的索引
        assert arr.find(2) == 1
        assert arr.find(3) == 2
        assert arr.find(1) == 0

        # 找不到元素
        assert arr.find(100) == -1

    def test_automatic_resizing(self):
        """測試自動調整容量"""
        arr = DynamicArray(4)  # 小容量測試擴容

        # 測試擴容
        for i in range(5):
            arr.push(i)

        assert arr.size() == 5
        assert arr.capacity() == 8  # 4 * 2

        # 繼續新增觸發再次擴容
        for i in range(5, 9):
            arr.push(i)

        assert arr.size() == 9
        assert arr.capacity() == 16  # 8 * 2

    def test_automatic_shrinking(self):
        """測試自動縮容"""
        arr = DynamicArray()

        # 填滿陣列觸發擴容
        for i in range(17):  # 超過初始容量 16
            arr.push(i)

        assert arr.capacity() == 32  # 擴容到 32

        # 移除元素觸發縮容
        while arr.size() > 8:  # 32 / 4 = 8
            arr.pop()

        # 下一次 pop 應該觸發縮容
        arr.pop()
        assert arr.capacity() == 16  # 32 / 2 = 16

        # 測試最小容量限制
        while arr.size() > 4:
            arr.pop()

        arr.pop()
        assert arr.capacity() >= 16  # 最小容量 16

    def test_magic_methods(self):
        """測試魔術方法"""
        arr = DynamicArray()
        arr.push(1)
        arr.push(2)
        arr.push(3)

        # __len__
        assert len(arr) == 3

        # __getitem__
        assert arr[0] == 1
        assert arr[1] == 2
        assert arr[2] == 3

        # __setitem__
        arr[1] = 10
        assert arr[1] == 10

        # 索引錯誤
        with pytest.raises(IndexError):
            _ = arr[10]

        with pytest.raises(IndexError):
            arr[10] = 100

        # __str__
        empty_arr = DynamicArray()
        assert str(empty_arr) == "[]"
        assert str(arr) == "[1, 10, 3]"

        # __repr__
        repr_str = repr(arr)
        assert "DynamicArray" in repr_str
        assert "size=3" in repr_str
        assert "capacity=" in repr_str

    def test_edge_cases(self):
        """測試邊界條件"""
        arr = DynamicArray(1)  # 最小容量

        # 單一元素操作
        arr.push(42)
        assert arr.size() == 1
        assert arr.capacity() == 1
        assert arr.at(0) == 42

        # 觸發擴容
        arr.push(43)
        assert arr.size() == 2
        assert arr.capacity() == 2

        # 清空陣列
        arr.pop()
        arr.pop()
        assert arr.is_empty() is True

    def test_data_types(self):
        """測試不同資料類型"""
        arr = DynamicArray()

        # 整數
        arr.push(42)
        assert arr.at(0) == 42

        # 字串
        arr.push("hello")
        assert arr.at(1) == "hello"

        # 列表
        arr.push([1, 2, 3])
        assert arr.at(2) == [1, 2, 3]

        # None
        arr.push(None)
        assert arr.at(3) is None

        # 混合類型搜尋
        assert arr.find("hello") == 1
        assert arr.find([1, 2, 3]) == 2
        assert arr.find(None) == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])