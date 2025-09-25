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
    def __init__(self, initial_capacity: int = 16):
        if initial_capacity < 1:
            raise ValueError("Initial capacity must be at least 1")
        self._data = [None] * initial_capacity
        self._size = 0
        self._capacity = initial_capacity
        
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
        
    def size(self)->int: 
        """回傳陣列中的元素數量"""
        return self._size
    
    def capacity(self)->int:
        return self._capacity
    
    def is_empty(self)->bool:
        return self.size() == 0

    
    def push(self, item) -> None:
        """
        在陣列尾端新增元素

        Args:
            item: 要新增的元素
        """
        if self._size == self._capacity:
            self._resize(2 * self._capacity)  # 擴展容量至 2 倍
        self._data[self._size] =item
        self._size+=1
        
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
        if index<0 or index >= self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}")
        return self._data[index] 
        
        
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
        item = self._data[self._size-1]
        self._data[self._size-1] = None
        self._size -=1

        # 檢查是否需要縮容
        if self._size > 0 and self._size <= self._capacity//4:
            new_capacity= max(16,self._capacity//2)  # 容量減少至最小16
            self._resize(new_capacity)
        return item
    
    def find(self, item)->int:
        """
        搜尋元素的位置

        Args:
            item: 要搜尋的元素

        Returns:
            元素的索引，找不到時回傳 -1
        """
        for  i in range(0, self._size):
            if self._data[i] == item \
                and type(self._data[i]) == type(item):
                return i
        return -1
        
    def insert(self, index: int, item)-> None:
        # 📝 添加index檢查
        if index < 0 or index > self._size:
          raise IndexError(f"Index {index} out of bounds for size {self._size}")
        #   容量檢查與擴容（如同 push）
        if self._size == self._capacity:
            self._resize(2 * self._capacity)  # 擴展容量至 2 倍
        #   元素右移（從後往前移動，避免覆蓋）
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i-1]
        #   插入新元素，更新_size
        self._data[index] = item
        self._size+=1
        
    def prepend(self,item) -> None:
        if self._size == self._capacity:
            self._resize(2 * self._capacity)  # 擴展容量至 2 倍
        for i in range(self._size,0, -1):
            self._data[i] = self._data[i-1]
        #   插入新元素，更新_size
        self._data[0] = item
        self._size+=1
        
    def delete(self, index: int) -> None:
        #  索引邊界檢查
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}")
        #   元素左移
        for i in range(index, self._size-1):
            self._data[i] = self._data[i+1]
        #   清理最後堆出來的位置並更新size
        self._data[self._size-1] = None
        self._size -= 1
        
        # 檢查是否需要縮容
        if self._size > 0 and self._size <= self._capacity // 4:
            new_capacity = max(16, self._capacity // 2)
            self._resize(new_capacity)
    
    def remove(self, item):
        index = self.find(item)
        #如果找到就刪除
        if index != -1:
            self.delete(index)
                
        