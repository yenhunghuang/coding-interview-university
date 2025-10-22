"""
雜湊表 (Hash Table) 實作
使用分離鏈結法 (Separate Chaining) 處理碰撞

雜湊表是一種能夠以 O(1) 平均時間複雜度進行查找、插入和刪除操作的資料結構。
它透過雜湊函數將鍵值映射到陣列索引，並使用鏈結串列處理碰撞。
"""


class Node:
    """
    鏈結串列節點，用於儲存鍵值對

    Attributes:
        key: 鍵
        value: 值
        next: 指向下一個節點的指標
    """

    def __init__(self, key, value):
        """
        初始化節點

        Args:
            key: 鍵
            value: 值
        """
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    雜湊表實作 - 使用分離鏈結法處理碰撞

    這個實作使用陣列加上鏈結串列的方式來處理碰撞。
    當負載因子超過閾值時，會自動擴展容量。

    Attributes:
        _capacity: 雜湊表的容量（陣列大小）
        _load_factor: 負載因子閾值
        _size: 當前儲存的鍵值對數量
        _buckets: 儲存鏈結串列的陣列
    """

    def __init__(self, capacity=16, load_factor=0.75):
        """
        初始化雜湊表

        Args:
            capacity: 初始容量，預設為 16
            load_factor: 負載因子閾值，預設為 0.75

        時間複雜度: O(n)，其中 n 是容量
        空間複雜度: O(n)
        """
        # TODO: 初始化容量（必須是正整數）
        self._capacity = capacity if capacity > 0 else 16

        # TODO: 初始化負載因子（必須在 0 到 1 之間）
        self._load_factor = load_factor if 0 < load_factor <= 1 else 0.75

        # TODO: 初始化大小為 0
        self._size = 0

        # TODO: 建立一個大小為 capacity 的陣列，初始值都是 None
        # 這個陣列的每個位置稱為「桶」(bucket)，用來存放鏈結串列的頭節點
        self._buckets = [None] * self._capacity

    def _hash(self, key):
        """
        雜湊函數：將鍵轉換為陣列索引

        使用 Python 內建的 hash() 函數，然後對容量取模
        確保結果在有效的索引範圍內

        Args:
            key: 要雜湊的鍵

        Returns:
            int: 對應的陣列索引 (0 到 capacity-1)

        時間複雜度: O(1)

        注意：好的雜湊函數應該：
        1. 確定性：相同的鍵總是產生相同的雜湊值
        2. 均勻分布：不同的鍵應該均勻分布在陣列中
        3. 快速計算：雜湊計算應該很快
        """
        # TODO: 實作雜湊函數
        # 提示：使用 hash(key) 取得雜湊值，然後用 % self._capacity 確保在範圍內
        return hash(key) % self._capacity

    def put(self, key, value):
        """
        插入或更新鍵值對

        如果鍵已存在，更新其值；否則插入新的鍵值對。
        插入後如果負載因子超過閾值，會觸發擴容。

        Args:
            key: 鍵
            value: 值

        時間複雜度:
            - 平均: O(1)
            - 最壞: O(n) 當需要擴容時

        碰撞處理：使用分離鏈結法
        """
        # TODO: 步驟 1 - 計算雜湊索引
        index = self._hash(key)

        # TODO: 步驟 2 - 取得該索引位置的鏈結串列頭節點
        current = self._buckets[index]

        # TODO: 步驟 3 - 走訪鏈結串列，檢查鍵是否已存在
        while current is not None:
            if current.key == key:
                # 鍵已存在，更新值
                current.value = value
                return
            current = current.next

        # TODO: 步驟 4 - 鍵不存在，建立新節點並插入到鏈結串列頭部
        new_node = Node(key, value)
        new_node.next = self._buckets[index]
        self._buckets[index] = new_node

        # TODO: 步驟 5 - 增加大小計數
        self._size += 1

        # TODO: 步驟 6 - 檢查是否需要擴容
        # 如果 (size / capacity) > load_factor，則需要擴容
        if self._size / self._capacity > self._load_factor:
            self._resize()

    def get(self, key):
        """
        根據鍵取得值

        Args:
            key: 要查找的鍵

        Returns:
            value: 對應的值

        Raises:
            KeyError: 如果鍵不存在

        時間複雜度:
            - 平均: O(1)
            - 最壞: O(n) 當所有鍵都碰撞到同一個桶時
        """
        # TODO: 步驟 1 - 計算雜湊索引
        index = self._hash(key)

        # TODO: 步驟 2 - 取得該索引位置的鏈結串列頭節點
        current = self._buckets[index]

        # TODO: 步驟 3 - 走訪鏈結串列尋找鍵
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        # TODO: 步驟 4 - 鍵不存在，拋出例外
        raise KeyError(f"Key '{key}' not found in hash table")

    def remove(self, key):
        """
        刪除鍵值對

        Args:
            key: 要刪除的鍵

        Raises:
            KeyError: 如果鍵不存在

        時間複雜度:
            - 平均: O(1)
            - 最壞: O(n)
        """
        # TODO: 步驟 1 - 計算雜湊索引
        index = self._hash(key)

        # TODO: 步驟 2 - 取得該索引位置的鏈結串列頭節點
        current = self._buckets[index]
        prev = None

        # TODO: 步驟 3 - 走訪鏈結串列尋找要刪除的節點
        while current is not None:
            if current.key == key:
                # 找到要刪除的節點
                if prev is None:
                    # 要刪除的是頭節點
                    self._buckets[index] = current.next
                else:
                    # 要刪除的不是頭節點
                    prev.next = current.next

                # TODO: 步驟 4 - 減少大小計數
                self._size -= 1
                return

            prev = current
            current = current.next

        # TODO: 步驟 5 - 鍵不存在，拋出例外
        raise KeyError(f"Key '{key}' not found in hash table")

    def contains(self, key):
        """
        檢查鍵是否存在

        Args:
            key: 要檢查的鍵

        Returns:
            bool: 如果鍵存在回傳 True，否則回傳 False

        時間複雜度: O(1) 平均
        """
        # TODO: 實作 contains 方法
        # 提示：可以使用 get 方法，並捕捉 KeyError 例外
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def size(self):
        """
        回傳雜湊表中鍵值對的數量

        Returns:
            int: 鍵值對數量

        時間複雜度: O(1)
        """
        # TODO: 回傳 _size
        return self._size

    def is_empty(self):
        """
        檢查雜湊表是否為空

        Returns:
            bool: 如果為空回傳 True，否則回傳 False

        時間複雜度: O(1)
        """
        # TODO: 檢查 _size 是否為 0
        return self._size == 0

    def keys(self):
        """
        回傳所有鍵的列表

        Returns:
            list: 包含所有鍵的列表

        時間複雜度: O(n)，其中 n 是鍵值對數量
        """
        # TODO: 走訪所有桶和鏈結串列，收集所有鍵
        result = []
        for bucket in self._buckets:
            current = bucket
            while current is not None:
                result.append(current.key)
                current = current.next
        return result

    def values(self):
        """
        回傳所有值的列表

        Returns:
            list: 包含所有值的列表

        時間複雜度: O(n)
        """
        # TODO: 走訪所有桶和鏈結串列，收集所有值
        result = []
        for bucket in self._buckets:
            current = bucket
            while current is not None:
                result.append(current.value)
                current = current.next
        return result

    def clear(self):
        """
        清空雜湊表

        時間複雜度: O(n)，其中 n 是容量
        """
        # TODO: 重置所有桶為 None
        self._buckets = [None] * self._capacity

        # TODO: 重置大小為 0
        self._size = 0

    def _resize(self):
        """
        擴容雜湊表

        當負載因子超過閾值時調用。
        將容量加倍，並重新雜湊所有現有的鍵值對。

        時間複雜度: O(n)，其中 n 是鍵值對數量

        為什麼需要擴容？
        - 當桶中的鏈結串列過長時，查找效率會下降
        - 擴容可以減少碰撞，維持 O(1) 的平均查找時間
        """
        # TODO: 步驟 1 - 儲存舊的桶陣列
        old_buckets = self._buckets

        # TODO: 步驟 2 - 將容量加倍
        self._capacity *= 2

        # TODO: 步驟 3 - 建立新的桶陣列
        self._buckets = [None] * self._capacity

        # TODO: 步驟 4 - 重置大小（重新插入時會增加）
        self._size = 0

        # TODO: 步驟 5 - 重新雜湊所有鍵值對
        # 走訪舊陣列的每個桶
        for bucket in old_buckets:
            current = bucket
            # 走訪該桶的鏈結串列
            while current is not None:
                # 使用 put 方法重新插入（會使用新的容量計算索引）
                self.put(current.key, current.value)
                current = current.next

    def get_load_factor(self):
        """
        回傳當前的負載因子

        Returns:
            float: 當前負載因子 (size / capacity)
        """
        if self._capacity == 0:
            return 0
        return self._size / self._capacity

    def get_capacity(self):
        """
        回傳當前容量

        Returns:
            int: 當前容量
        """
        return self._capacity

    def __str__(self):
        """
        回傳雜湊表的字串表示

        Returns:
            str: 雜湊表的字串表示
        """
        if self.is_empty():
            return "{}"

        items = []
        for key in self.keys():
            value = self.get(key)
            items.append(f"'{key}': {value}")

        return "{" + ", ".join(items) + "}"

    def __repr__(self):
        """
        回傳雜湊表的官方字串表示

        Returns:
            str: 雜湊表的官方字串表示
        """
        return f"HashTable(size={self._size}, capacity={self._capacity}, load_factor={self.get_load_factor():.2f})"
