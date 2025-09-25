"""
Dynamic Array 實作

這是一個從零開始實作的動態陣列，模擬低階記憶體管理。
目的是理解 Python list 的內部工作原理。

時間複雜度：
- 存取 at(index): O(1)
- 尾端新增 push(): O(1) amortized, O(n) worst case
- 尾端移除 pop(): O(1) amortized, O(n) worst case
- 插入 insert(): O(n)
- 刪除 delete(): O(n)
- 搜尋 find(): O(n)

空間複雜度：O(n)
"""


class DynamicArray:
    """
    動態陣列實作

    特性：
    - 自動調整容量
    - 當容量滿時，擴展至 2 倍大小
    - 當使用量小於 1/4 容量時，縮減至 1/2 大小
    """

    def __init__(self, initial_capacity: int = 16):
        """
        初始化動態陣列

        Args:
            initial_capacity: 初始容量，預設為 16
        """
        if initial_capacity < 1:
            raise ValueError("Initial capacity must be at least 1")

        # 使用 None 填充的 list 模擬原始記憶體陣列
        self._data = [None] * initial_capacity
        self._size = 0  # 實際元素數量
        self._capacity = initial_capacity  # 總容量

    def size(self) -> int:
        """回傳陣列中的元素數量"""
        return self._size

    def capacity(self) -> int:
        """回傳陣列目前的容量"""
        return self._capacity

    def is_empty(self) -> bool:
        """檢查陣列是否為空"""
        return self._size == 0

    def at(self, index: int):
        """
        根據索引取得元素

        Args:
            index: 元素索引

        Returns:
            指定位置的元素

        Raises:
            IndexError: 索引超出範圍
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}")

        return self._data[index]

    def push(self, item) -> None:
        """
        在陣列尾端新增元素

        Args:
            item: 要新增的元素
        """
        # 檢查是否需要擴容
        if self._size >= self._capacity:
            self._resize(self._capacity * 2)

        self._data[self._size] = item
        self._size += 1

    def insert(self, index: int, item) -> None:
        """
        在指定位置插入元素

        Args:
            index: 插入位置
            item: 要插入的元素

        Raises:
            IndexError: 索引超出範圍
        """
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of bounds for insert operation")

        # 檢查是否需要擴容
        if self._size >= self._capacity:
            self._resize(self._capacity * 2)

        # 將索引後的元素往右移
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = item
        self._size += 1

    def prepend(self, item) -> None:
        """
        在陣列開頭插入元素

        Args:
            item: 要插入的元素
        """
        self.insert(0, item)

    def pop(self):
        """
        移除並回傳尾端元素

        Returns:
            被移除的元素

        Raises:
            IndexError: 陣列為空
        """
        if self.is_empty():
            raise IndexError("Pop from empty array")

        item = self._data[self._size - 1]
        self._data[self._size - 1] = None  # 清除參考
        self._size -= 1

        # 檢查是否需要縮容
        if self._size > 0 and self._size <= self._capacity // 4:
            new_capacity = max(16, self._capacity // 2)  # 最小容量為 16
            self._resize(new_capacity)

        return item

    def delete(self, index: int) -> None:
        """
        刪除指定位置的元素

        Args:
            index: 要刪除的位置

        Raises:
            IndexError: 索引超出範圍
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}")

        # 將索引後的元素往左移
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._data[self._size - 1] = None  # 清除參考
        self._size -= 1

        # 檢查是否需要縮容
        if self._size > 0 and self._size <= self._capacity // 4:
            new_capacity = max(16, self._capacity // 2)
            self._resize(new_capacity)

    def remove(self, item) -> None:
        """
        移除第一個匹配的元素

        Args:
            item: 要移除的元素

        Raises:
            ValueError: 元素不存在
        """
        index = self.find(item)
        if index == -1:
            raise ValueError(f"Item {item} not found in array")

        self.delete(index)

    def find(self, item) -> int:
        """
        搜尋元素的位置

        Args:
            item: 要搜尋的元素

        Returns:
            元素的索引，找不到時回傳 -1
        """
        for i in range(self._size):
            if self._data[i] == item:
                return i
        return -1

    def _resize(self, new_capacity: int) -> None:
        """
        調整陣列容量（私有方法）

        Args:
            new_capacity: 新的容量
        """
        if new_capacity < self._size:
            raise ValueError("New capacity cannot be smaller than current size")

        # 建立新的陣列
        new_data = [None] * new_capacity

        # 複製現有元素
        for i in range(self._size):
            new_data[i] = self._data[i]

        self._data = new_data
        self._capacity = new_capacity

    def __str__(self) -> str:
        """回傳陣列的字串表示"""
        if self.is_empty():
            return "[]"

        items = [str(self._data[i]) for i in range(self._size)]
        return "[" + ", ".join(items) + "]"

    def __repr__(self) -> str:
        """回傳陣列的詳細表示"""
        return f"DynamicArray(size={self._size}, capacity={self._capacity}, data={str(self)})"

    def __len__(self) -> int:
        """支援 len() 函數"""
        return self._size

    def __getitem__(self, index: int):
        """支援索引存取 arr[index]"""
        return self.at(index)

    def __setitem__(self, index: int, value) -> None:
        """支援索引設定 arr[index] = value"""
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}")
        self._data[index] = value