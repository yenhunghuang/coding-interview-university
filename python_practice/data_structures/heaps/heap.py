"""
Min Heap (最小堆積) 實作
======================

堆積（Heap）是一種特殊的完全二元樹（Complete Binary Tree），
其中每個父節點的值都小於或等於其子節點的值（Min Heap）。

特性：
1. 完全二元樹結構
2. 父節點 ≤ 子節點（Min Heap）
3. 使用陣列表示
4. 索引關係：
   - 父節點：(i - 1) // 2
   - 左子節點：2 * i + 1
   - 右子節點：2 * i + 2

時間複雜度：
- insert: O(log n)
- extract_min: O(log n)
- peek_min: O(1)
- 建立堆積: O(n)

應用：
- 優先權佇列（Priority Queue）
- 堆積排序（Heap Sort）
- 找出第 K 大/小元素
- 求中位數
- 圖形演算法（Dijkstra, Prim）
"""


class MinHeap:
    """
    最小堆積實作（使用陣列）

    屬性：
        _heap: 儲存堆積元素的陣列
        _capacity: 堆積的最大容量（None 表示無限制）
    """

    def __init__(self, capacity=None):
        """
        初始化最小堆積

        參數：
            capacity: 堆積的最大容量，預設為 None（無限制）

        範例：
            >>> heap = MinHeap()
            >>> heap = MinHeap(capacity=10)
        """
        # TODO: 初始化空的陣列來儲存堆積元素
        # TODO: 設定堆積的容量限制
        pass

    def size(self):
        """
        回傳堆積中的元素數量

        時間複雜度：O(1)

        回傳：
            int: 堆積中的元素數量

        範例：
            >>> heap = MinHeap()
            >>> heap.size()
            0
        """
        # TODO: 回傳陣列的長度
        pass

    def is_empty(self):
        """
        檢查堆積是否為空

        時間複雜度：O(1)

        回傳：
            bool: 若堆積為空回傳 True，否則回傳 False

        範例：
            >>> heap = MinHeap()
            >>> heap.is_empty()
            True
        """
        # TODO: 檢查陣列長度是否為 0
        pass

    def _parent(self, index):
        """
        取得父節點的索引

        公式：parent_index = (index - 1) // 2

        參數：
            index: 子節點的索引

        回傳：
            int: 父節點的索引

        範例：
            索引 1 的父節點是 0
            索引 2 的父節點是 0
            索引 3 的父節點是 1
        """
        # TODO: 使用公式計算父節點索引
        pass

    def _left_child(self, index):
        """
        取得左子節點的索引

        公式：left_index = 2 * index + 1

        參數：
            index: 父節點的索引

        回傳：
            int: 左子節點的索引

        範例：
            索引 0 的左子節點是 1
            索引 1 的左子節點是 3
            索引 2 的左子節點是 5
        """
        # TODO: 使用公式計算左子節點索引
        pass

    def _right_child(self, index):
        """
        取得右子節點的索引

        公式：right_index = 2 * index + 2

        參數：
            index: 父節點的索引

        回傳：
            int: 右子節點的索引

        範例：
            索引 0 的右子節點是 2
            索引 1 的右子節點是 4
            索引 2 的右子節點是 6
        """
        # TODO: 使用公式計算右子節點索引
        pass

    def peek_min(self):
        """
        查看堆積中的最小值（不移除）

        時間複雜度：O(1)

        回傳：
            最小值（堆積頂端的元素）

        例外：
            IndexError: 如果堆積為空

        範例：
            >>> heap = MinHeap()
            >>> heap.insert(5)
            >>> heap.peek_min()
            5
        """
        # TODO: 檢查堆積是否為空，若為空則拋出例外
        # TODO: 回傳陣列的第一個元素（索引 0）
        pass

    def insert(self, value):
        """
        插入新元素到堆積中

        步驟：
        1. 將新元素加到陣列末端
        2. 執行 heapify_up 維護堆積性質

        時間複雜度：O(log n)

        參數：
            value: 要插入的值

        例外：
            OverflowError: 如果堆積已滿

        範例：
            >>> heap = MinHeap()
            >>> heap.insert(5)
            >>> heap.insert(3)
            >>> heap.peek_min()
            3
        """
        # TODO: 檢查堆積是否已滿（如果有容量限制）
        # TODO: 將新值加到陣列末端
        # TODO: 對新加入的元素執行 heapify_up
        pass

    def _heapify_up(self, index):
        """
        向上調整堆積（用於插入後維護堆積性質）

        過程：
        1. 比較當前節點與父節點
        2. 如果當前節點小於父節點，則交換
        3. 繼續向上比較，直到滿足堆積性質或到達根節點

        時間複雜度：O(log n)

        參數：
            index: 要調整的節點索引

        範例：
            插入 2 到 [5, 10, 15] 後成為 [5, 10, 15, 2]
            執行 heapify_up(3) 調整為 [2, 5, 15, 10]
        """
        # TODO: 當索引大於 0 時（還沒到根節點）
        #   1. 計算父節點索引
        #   2. 如果當前節點小於父節點
        #      - 交換兩個節點
        #      - 更新索引為父節點索引
        #      - 繼續向上調整
        #   3. 否則停止（堆積性質已滿足）
        pass

    def extract_min(self):
        """
        移除並回傳堆積中的最小值

        步驟：
        1. 儲存根節點（最小值）
        2. 將最後一個元素移到根節點
        3. 移除最後一個元素
        4. 執行 heapify_down 維護堆積性質

        時間複雜度：O(log n)

        回傳：
            最小值（堆積頂端的元素）

        例外：
            IndexError: 如果堆積為空

        範例：
            >>> heap = MinHeap()
            >>> heap.insert(5)
            >>> heap.insert(3)
            >>> heap.extract_min()
            3
            >>> heap.extract_min()
            5
        """
        # TODO: 檢查堆積是否為空，若為空則拋出例外
        # TODO: 儲存最小值（索引 0）
        # TODO: 將最後一個元素移到根節點
        # TODO: 移除陣列的最後一個元素
        # TODO: 如果堆積不為空，對根節點執行 heapify_down
        # TODO: 回傳最小值
        pass

    def _heapify_down(self, index):
        """
        向下調整堆積（用於刪除後維護堆積性質）

        過程：
        1. 找出當前節點和兩個子節點中的最小值
        2. 如果最小值不是當前節點，則與最小子節點交換
        3. 繼續向下調整，直到滿足堆積性質或到達葉節點

        時間複雜度：O(log n)

        參數：
            index: 要調整的節點索引

        範例：
            從 [15, 5, 10, 20] 移除根節點後成為 [20, 5, 10]
            執行 heapify_down(0) 調整為 [5, 20, 10] 再調整為 [5, 10, 20]
        """
        # TODO: 設定當前最小值索引為當前索引
        # TODO: 計算左子節點和右子節點的索引
        # TODO: 如果左子節點存在且小於當前最小值，更新最小值索引
        # TODO: 如果右子節點存在且小於當前最小值，更新最小值索引
        # TODO: 如果最小值索引改變了
        #   1. 交換當前節點與最小子節點
        #   2. 遞迴對交換後的位置執行 heapify_down
        pass

    def get_heap(self):
        """
        取得堆積的內部陣列表示（用於測試和視覺化）

        回傳：
            list: 堆積的陣列表示
        """
        # TODO: 回傳堆積陣列的副本
        pass

    def __repr__(self):
        """
        回傳堆積的字串表示

        回傳：
            str: 堆積的字串表示
        """
        return f"MinHeap({self._heap})"

    def __len__(self):
        """
        支援 len() 函數

        回傳：
            int: 堆積中的元素數量
        """
        return self.size()


# 額外功能（選擇性實作）

def heapify(array):
    """
    將陣列轉換為最小堆積（原地操作）

    使用自下而上的方式建立堆積
    時間複雜度：O(n)

    參數：
        array: 要轉換的陣列

    範例：
        >>> arr = [9, 5, 6, 2, 3]
        >>> heapify(arr)
        >>> arr
        [2, 3, 6, 5, 9]
    """
    # TODO: 從最後一個非葉節點開始
    # TODO: 對每個節點執行 heapify_down
    pass


def heap_sort(array):
    """
    堆積排序

    步驟：
    1. 建立最大堆積
    2. 重複將根節點與最後一個元素交換
    3. 縮小堆積範圍並調整

    時間複雜度：O(n log n)
    空間複雜度：O(1)

    參數：
        array: 要排序的陣列

    回傳：
        排序後的陣列

    範例：
        >>> heap_sort([9, 5, 6, 2, 3])
        [2, 3, 5, 6, 9]
    """
    # TODO: 實作堆積排序
    pass


def find_kth_smallest(array, k):
    """
    找出陣列中第 K 小的元素

    使用最小堆積
    時間複雜度：O(n log n)

    參數：
        array: 輸入陣列
        k: 第 K 小（1-indexed）

    回傳：
        第 K 小的元素

    範例：
        >>> find_kth_smallest([7, 10, 4, 3, 20, 15], 3)
        7
    """
    # TODO: 建立最小堆積並插入所有元素
    # TODO: 提取 K 次最小值
    pass
