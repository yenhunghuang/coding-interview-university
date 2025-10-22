# 堆積（Heap）完整學習指南

## 目錄

1. [什麼是堆積？](#什麼是堆積)
2. [堆積的特性](#堆積的特性)
3. [堆積的陣列表示](#堆積的陣列表示)
4. [堆積操作](#堆積操作)
5. [時間複雜度分析](#時間複雜度分析)
6. [堆積 vs 二元搜尋樹](#堆積-vs-二元搜尋樹)
7. [堆積的應用](#堆積的應用)
8. [實作細節](#實作細節)
9. [常見問題與解答](#常見問題與解答)
10. [練習題目](#練習題目)
11. [學習路徑](#學習路徑)

---

## 什麼是堆積？

**堆積（Heap）** 是一種特殊的完全二元樹（Complete Binary Tree）資料結構，滿足以下性質：

### 最小堆積（Min Heap）
每個父節點的值都**小於或等於**其子節點的值，因此根節點是整個堆積中的最小值。

```
        1
       / \
      3   2
     / \ / \
    7  5 4  6
```

### 最大堆積（Max Heap）
每個父節點的值都**大於或等於**其子節點的值，因此根節點是整個堆積中的最大值。

```
        9
       / \
      7   8
     / \ / \
    3  5 4  6
```

### 完全二元樹
- 除了最後一層，其他層都必須是滿的
- 最後一層的節點必須從左到右填充
- 這種特性使得堆積可以用陣列有效地表示

---

## 堆積的特性

### 1. 結構性質
- **完全二元樹**：所有層級都是滿的，除了可能的最後一層
- **左對齊**：最後一層的節點從左到右填充

### 2. 堆積性質（以最小堆積為例）
```
對於任意節點 i：
- heap[i] <= heap[left_child(i)]
- heap[i] <= heap[right_child(i)]
```

### 3. 重要觀察
- 根節點（索引 0）始終是最小值（最小堆積）或最大值（最大堆積）
- 從任意節點到根的路徑是遞增的（最小堆積）或遞減的（最大堆積）
- 堆積不保證兄弟節點之間的順序關係

---

## 堆積的陣列表示

堆積最有效的表示方式是使用**陣列**，利用完全二元樹的特性：

### 索引關係公式

對於陣列索引從 0 開始的實作：

```python
# 父節點索引
def parent(i):
    return (i - 1) // 2

# 左子節點索引
def left_child(i):
    return 2 * i + 1

# 右子節點索引
def right_child(i):
    return 2 * i + 2
```

### 視覺化範例

```
陣列: [1, 3, 2, 7, 5, 4, 6]
索引:  0  1  2  3  4  5  6

樹狀表示:
        1 (索引 0)
       / \
      3   2 (索引 1, 2)
     / \ / \
    7  5 4  6 (索引 3, 4, 5, 6)

關係驗證:
- 索引 0 的左子 = 2*0+1 = 1, 右子 = 2*0+2 = 2 ✓
- 索引 1 的左子 = 2*1+1 = 3, 右子 = 2*1+2 = 4 ✓
- 索引 2 的左子 = 2*2+1 = 5, 右子 = 2*2+2 = 6 ✓
- 索引 3 的父節點 = (3-1)//2 = 1 ✓
```

### 優點
1. **空間效率**：不需要額外的指標儲存
2. **快取友善**：陣列元素在記憶體中連續存放
3. **簡單實作**：索引計算非常直觀

---

## 堆積操作

### 1. 插入（Insert）

**步驟：**
1. 將新元素加到陣列末端（維持完全二元樹性質）
2. 執行 **heapify-up**（向上調整）來維護堆積性質

**Heapify-Up 過程：**
```python
def heapify_up(index):
    while index > 0:
        parent_idx = (index - 1) // 2

        # 如果當前節點小於父節點（最小堆積）
        if heap[index] < heap[parent_idx]:
            # 交換
            heap[index], heap[parent_idx] = heap[parent_idx], heap[index]
            index = parent_idx
        else:
            break
```

**視覺化範例：插入 2**
```
初始堆積: [1, 3, 5, 7, 4]
        1
       / \
      3   5
     / \
    7   4

步驟 1: 加到末端
[1, 3, 5, 7, 4, 2]
        1
       / \
      3   5
     / \ /
    7  4 2

步驟 2: Heapify-up
比較 2 和父節點 5: 2 < 5, 交換
[1, 3, 2, 7, 4, 5]
        1
       / \
      3   2
     / \ / \
    7  4 5

完成！（2 < 1 不成立，停止）
```

**時間複雜度：O(log n)** - 最多需要遍歷樹的高度

---

### 2. 提取最小值（Extract Min）

**步驟：**
1. 儲存根節點的值（最小值）
2. 將最後一個元素移到根節點位置
3. 移除最後一個元素
4. 執行 **heapify-down**（向下調整）來維護堆積性質
5. 回傳儲存的最小值

**Heapify-Down 過程：**
```python
def heapify_down(index):
    while True:
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # 找出父節點和兩個子節點中的最小值
        if left < heap_size and heap[left] < heap[smallest]:
            smallest = left

        if right < heap_size and heap[right] < heap[smallest]:
            smallest = right

        # 如果最小值不是父節點，交換並繼續
        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            index = smallest
        else:
            break
```

**視覺化範例：提取最小值**
```
初始堆積: [1, 3, 2, 7, 4, 5]
        1
       / \
      3   2
     / \ /
    7  4 5

步驟 1: 儲存 1，將 5 移到根
[5, 3, 2, 7, 4]
        5
       / \
      3   2
     / \
    7   4

步驟 2: Heapify-down
比較 5 與子節點 3, 2: 最小是 2, 交換
[2, 3, 5, 7, 4]
        2
       / \
      3   5
     / \
    7   4

完成！回傳 1
```

**時間複雜度：O(log n)** - 最多需要遍歷樹的高度

---

### 3. 查看最小值（Peek Min）

**操作：**
直接回傳陣列的第一個元素（索引 0）

```python
def peek_min():
    if heap_size == 0:
        raise IndexError("Heap is empty")
    return heap[0]
```

**時間複雜度：O(1)** - 常數時間

---

### 4. 從陣列建立堆積（Heapify）

有兩種方法：

#### 方法 1：逐個插入
```python
def build_heap_insert(array):
    heap = MinHeap()
    for element in array:
        heap.insert(element)
```
**時間複雜度：O(n log n)**

#### 方法 2：自下而上 Heapify（更有效）
```python
def build_heap_efficient(array):
    # 從最後一個非葉節點開始
    for i in range(len(array) // 2 - 1, -1, -1):
        heapify_down(i)
```
**時間複雜度：O(n)** - 更優！

**為什麼 O(n) 更快？**
- 大部分節點在樹的底部
- 底部節點只需要少量調整
- 只有少數節點需要完整的 O(log n) 調整

---

## 時間複雜度分析

| 操作 | 時間複雜度 | 說明 |
|------|-----------|------|
| peek_min() | O(1) | 直接存取陣列第一個元素 |
| insert(value) | O(log n) | 需要 heapify-up，最多樹的高度 |
| extract_min() | O(log n) | 需要 heapify-down，最多樹的高度 |
| build_heap() | O(n) | 使用自下而上方法 |
| heap_sort() | O(n log n) | n 次 extract 操作 |
| size() | O(1) | 簡單的計數器 |
| is_empty() | O(1) | 檢查大小是否為 0 |

### 空間複雜度
- **O(n)** - 儲存 n 個元素
- 陣列實作不需要額外的指標空間

---

## 堆積 vs 二元搜尋樹

| 特性 | 堆積（Heap） | 二元搜尋樹（BST） |
|------|-------------|------------------|
| **結構** | 完全二元樹 | 可能不平衡 |
| **順序** | 部分排序（只保證父子關係） | 完全排序（中序遍歷有序） |
| **插入** | O(log n) | O(log n) 平均，O(n) 最壞 |
| **刪除最小** | O(log n) | O(log n) 平均，O(n) 最壞 |
| **查找任意元素** | O(n) | O(log n) 平均，O(n) 最壞 |
| **查找最小** | O(1) | O(log n) |
| **實作** | 陣列 | 節點+指標 |
| **記憶體** | 緊湊 | 需要指標額外空間 |
| **快取效能** | 優秀 | 較差 |

### 何時使用堆積？
- 需要快速存取最小/最大值
- 實作優先權佇列
- 不需要查找或刪除任意元素
- 需要最佳的空間效率

### 何時使用 BST？
- 需要維護完全排序
- 需要快速查找任意元素
- 需要範圍查詢
- 需要有序遍歷

---

## 堆積的應用

### 1. 優先權佇列（Priority Queue）

**概念：**
元素根據優先權而非插入順序被處理。

**實作：**
```python
class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def enqueue(self, priority, item):
        self.heap.insert((priority, item))

    def dequeue(self):
        if self.heap.is_empty():
            raise IndexError("Queue is empty")
        priority, item = self.heap.extract_min()
        return item
```

**應用場景：**
- 作業系統任務排程
- 網路封包排程
- 事件驅動模擬
- Dijkstra 最短路徑演算法

---

### 2. 堆積排序（Heap Sort）

**演算法步驟：**
1. 從陣列建立最大堆積
2. 將根（最大值）與最後一個元素交換
3. 縮小堆積範圍（排除已排序的元素）
4. 對新根執行 heapify-down
5. 重複步驟 2-4

**實作：**
```python
def heap_sort(array):
    # 建立最大堆積
    build_max_heap(array)

    # 逐個提取最大值
    for i in range(len(array) - 1, 0, -1):
        # 交換根和最後一個元素
        array[0], array[i] = array[i], array[0]

        # 對剩餘元素執行 heapify
        heapify_down(array, 0, i)

    return array
```

**特性：**
- **時間複雜度：** O(n log n) - 所有情況
- **空間複雜度：** O(1) - 原地排序
- **穩定性：** 不穩定（相同元素可能改變相對順序）

**優點：**
- 保證 O(n log n) 時間
- 原地排序，不需額外空間
- 比快速排序更可預測

**缺點：**
- 實務上比快速排序慢（快取效能較差）
- 不穩定
- 不如合併排序適合連結串列

---

### 3. 找出第 K 大/小元素

**方法 1：使用最小堆積找第 K 小**
```python
def find_kth_smallest(array, k):
    heap = MinHeap()
    for num in array:
        heap.insert(num)

    # 提取 K 次
    for _ in range(k - 1):
        heap.extract_min()

    return heap.peek_min()
```
**時間複雜度：** O(n + k log n)

**方法 2：使用固定大小的最大堆積**
```python
def find_kth_smallest_efficient(array, k):
    # 維護大小為 K 的最大堆積
    # 堆積中保存最小的 K 個元素
    # 堆積頂端就是第 K 小
    max_heap = MaxHeap(capacity=k)

    for num in array:
        if max_heap.size() < k:
            max_heap.insert(num)
        elif num < max_heap.peek_max():
            max_heap.extract_max()
            max_heap.insert(num)

    return max_heap.peek_max()
```
**時間複雜度：** O(n log k) - 更優！

---

### 4. 合併 K 個已排序陣列

**問題：**
給定 K 個已排序的陣列，將它們合併成一個已排序的陣列。

**解法：**
```python
def merge_k_sorted_arrays(arrays):
    min_heap = MinHeap()
    result = []

    # 將每個陣列的第一個元素加入堆積
    # 格式：(值, 陣列索引, 元素索引)
    for i, array in enumerate(arrays):
        if array:
            min_heap.insert((array[0], i, 0))

    # 持續提取最小值
    while not min_heap.is_empty():
        value, array_idx, elem_idx = min_heap.extract_min()
        result.append(value)

        # 如果該陣列還有元素，加入下一個
        if elem_idx + 1 < len(arrays[array_idx]):
            next_value = arrays[array_idx][elem_idx + 1]
            min_heap.insert((next_value, array_idx, elem_idx + 1))

    return result
```

**時間複雜度：** O(N log K)
- N = 所有元素總數
- K = 陣列數量

**應用：**
- 外部排序（External Sort）
- 分散式系統的資料合併
- 資料庫查詢優化

---

### 5. 尋找資料串流的中位數

**問題：**
設計一個資料結構，可以高效地：
1. 加入新數字
2. 找出當前所有數字的中位數

**解法：使用兩個堆積**
```python
class MedianFinder:
    def __init__(self):
        self.max_heap = MaxHeap()  # 儲存較小的一半
        self.min_heap = MinHeap()  # 儲存較大的一半

    def add_num(self, num):
        # 先加到 max_heap
        self.max_heap.insert(num)

        # 平衡：max_heap 的最大值應該 <= min_heap 的最小值
        if (not self.min_heap.is_empty() and
            self.max_heap.peek_max() > self.min_heap.peek_min()):
            val = self.max_heap.extract_max()
            self.min_heap.insert(val)

        # 平衡大小：兩個堆積大小差不超過 1
        if self.max_heap.size() > self.min_heap.size() + 1:
            val = self.max_heap.extract_max()
            self.min_heap.insert(val)
        elif self.min_heap.size() > self.max_heap.size():
            val = self.min_heap.extract_min()
            self.max_heap.insert(val)

    def find_median(self):
        if self.max_heap.size() > self.min_heap.size():
            return self.max_heap.peek_max()
        else:
            return (self.max_heap.peek_max() +
                    self.min_heap.peek_min()) / 2.0
```

**時間複雜度：**
- add_num: O(log n)
- find_median: O(1)

---

### 6. 圖形演算法

#### Dijkstra 最短路徑演算法
```python
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # 優先權佇列：(距離, 節點)
    pq = MinHeap()
    pq.insert((0, start))

    while not pq.is_empty():
        current_dist, current_node = pq.extract_min()

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                pq.insert((distance, neighbor))

    return distances
```

#### Prim 最小生成樹演算法
使用優先權佇列選擇最小權重的邊。

---

## 實作細節

### 1. 容量管理

**固定容量：**
```python
class MinHeap:
    def __init__(self, capacity=None):
        self._heap = []
        self._capacity = capacity

    def insert(self, value):
        if self._capacity and len(self._heap) >= self._capacity:
            raise OverflowError("Heap is full")
        # ... 插入邏輯
```

**動態擴展：**
```python
class MinHeap:
    def __init__(self):
        self._heap = []
        # Python list 會自動擴展
```

---

### 2. 比較函數

**使用自訂比較：**
```python
class MinHeap:
    def __init__(self, key=None):
        self._heap = []
        self._key = key or (lambda x: x)

    def _compare(self, i, j):
        return self._key(self._heap[i]) < self._key(self._heap[j])
```

**應用：**
```python
# 根據元組的第一個元素建立堆積
heap = MinHeap(key=lambda x: x[0])
heap.insert((5, 'Task A'))
heap.insert((1, 'Task B'))
```

---

### 3. 錯誤處理

```python
def peek_min(self):
    if self.is_empty():
        raise IndexError("Heap is empty")
    return self._heap[0]

def extract_min(self):
    if self.is_empty():
        raise IndexError("Cannot extract from empty heap")
    # ... 提取邏輯

def insert(self, value):
    if self._capacity and len(self._heap) >= self._capacity:
        raise OverflowError("Heap is full")
    # ... 插入邏輯
```

---

### 4. 測試策略

**單元測試範例：**
```python
def test_heap_property(heap):
    """驗證堆積性質"""
    array = heap.get_heap()

    for i in range(len(array)):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(array):
            assert array[i] <= array[left], \
                f"Heap property violated at index {i}"

        if right < len(array):
            assert array[i] <= array[right], \
                f"Heap property violated at index {i}"
```

---

## 常見問題與解答

### Q1: 堆積中可以有重複元素嗎？
**A:** 可以！堆積只關心父子關係，重複元素完全沒問題。

```python
heap = MinHeap()
heap.insert(5)
heap.insert(5)
heap.insert(5)
# [5, 5, 5] - 完全有效
```

---

### Q2: 如何在堆積中刪除任意元素？
**A:** 標準堆積不支援高效刪除任意元素（需要 O(n) 搜尋）。如果需要此功能，考慮：

1. **使用額外的雜湊表追蹤元素位置**
```python
class IndexedMinHeap:
    def __init__(self):
        self._heap = []
        self._position = {}  # 元素 -> 索引

    def delete(self, value):
        if value not in self._position:
            return False

        index = self._position[value]
        # 用最後一個元素替換
        last = self._heap[-1]
        self._heap[index] = last
        self._position[last] = index
        self._heap.pop()
        del self._position[value]

        # 調整
        self._heapify_up(index)
        self._heapify_down(index)
```

2. **惰性刪除（Lazy Deletion）**
- 標記為已刪除，但不實際移除
- 在 extract 時跳過已標記的元素

---

### Q3: 堆積是穩定的嗎？
**A:** 不穩定。相同優先權的元素可能改變相對順序。

如需穩定性，可以使用：
```python
# 在優先權中加入序號
counter = 0
heap = MinHeap()

def insert_stable(priority, item):
    global counter
    heap.insert((priority, counter, item))
    counter += 1
```

---

### Q4: 如何實作最大堆積？
**A:** 兩種方法：

**方法 1：反轉比較邏輯**
```python
class MaxHeap:
    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            # 改成大於比較
            if self._heap[index] > self._heap[parent]:
                # 交換
                pass
```

**方法 2：使用負值**
```python
# 使用最小堆積實作最大堆積
min_heap = MinHeap()
min_heap.insert(-5)  # 插入 5
min_heap.insert(-3)  # 插入 3
max_val = -min_heap.extract_min()  # 提取最大值
```

---

### Q5: 為什麼建立堆積是 O(n) 而不是 O(n log n)？
**A:** 使用自下而上的方法：

- 葉節點（約 n/2 個）：0 次比較
- 倒數第二層（約 n/4 個）：最多 1 次交換
- 倒數第三層（約 n/8 個）：最多 2 次交換
- ...

**總計算：**
```
T(n) = n/2 * 0 + n/4 * 1 + n/8 * 2 + n/16 * 3 + ...
     = n * (1/4 + 2/8 + 3/16 + ...)
     = n * Σ(k/2^(k+1))  (k=1 to ∞)
     = n * 1/2  (級數收斂)
     = O(n)
```

---

### Q6: 堆積排序 vs 快速排序 vs 合併排序？

| 特性 | 堆積排序 | 快速排序 | 合併排序 |
|------|---------|---------|---------|
| 最壞時間 | O(n log n) | O(n²) | O(n log n) |
| 平均時間 | O(n log n) | O(n log n) | O(n log n) |
| 空間 | O(1) | O(log n) | O(n) |
| 穩定性 | 否 | 否 | 是 |
| 快取效能 | 差 | 優 | 中 |
| 原地排序 | 是 | 是 | 否 |

**建議：**
- **快速排序**：一般用途，平均最快
- **堆積排序**：需要保證 O(n log n) 且空間有限
- **合併排序**：需要穩定性或處理連結串列

---

## 練習題目

### 初級題目

1. **實作最大堆積**
   - 將最小堆積改寫為最大堆積
   - 時間：30 分鐘

2. **堆積驗證**
   - 給定陣列，判斷是否為有效的最小堆積
   - LeetCode: #1337

3. **最後一顆石頭的重量**
   - LeetCode: #1046
   - 難度：簡單

4. **數據流中的第 K 大元素**
   - LeetCode: #703
   - 難度：簡單

---

### 中級題目

5. **前 K 個高頻元素**
   - LeetCode: #347
   - 難度：中等
   - 概念：堆積 + 雜湊表

6. **合併 K 個排序鏈表**
   - LeetCode: #23
   - 難度：困難
   - 概念：最小堆積合併

7. **醜數 II**
   - LeetCode: #264
   - 難度：中等
   - 概念：動態規劃 + 堆積

8. **滑動窗口中位數**
   - LeetCode: #480
   - 難度：困難
   - 概念：雙堆積

---

### 進階題目

9. **會議室 II**
   - LeetCode: #253
   - 難度：中等
   - 概念：掃描線 + 堆積

10. **天際線問題**
    - LeetCode: #218
    - 難度：困難
    - 概念：掃描線 + 多集合/堆積

11. **找出數據流的中位數**
    - LeetCode: #295
    - 難度：困難
    - 概念：雙堆積平衡

12. **IPO**
    - LeetCode: #502
    - 難度：困難
    - 概念：雙堆積 + 貪心

---

### 系統設計題目

13. **設計推特**
    - LeetCode: #355
    - 使用堆積合併多個用戶的推文

14. **設計任務排程器**
    - 實作帶有優先權的任務佇列
    - 支援動態優先權調整

15. **實作 LRU/LFU 快取**
    - 結合堆積和雜湊表
    - 優化快取淘汰策略

---

## 學習路徑

### 第 1 週：基礎理解

**目標：理解堆積的概念和基本操作**

#### 第 1-2 天：理論學習
- [ ] 閱讀本指南的「什麼是堆積」和「堆積特性」章節
- [ ] 手繪堆積的插入和刪除過程
- [ ] 理解陣列表示和索引關係

**練習：**
- 在紙上畫出插入 [5, 3, 7, 1, 9] 的過程
- 手動計算各節點的父子索引

#### 第 3-4 天：實作基礎方法
- [ ] 完成 `__init__`, `size()`, `is_empty()`
- [ ] 完成索引計算方法
- [ ] 通過 test_stage1.py

**目標：** 理解堆積的結構表示

#### 第 5-6 天：實作插入
- [ ] 實作 `insert()` 方法
- [ ] 實作 `_heapify_up()` 方法
- [ ] 實作 `peek_min()` 方法
- [ ] 通過 test_stage2.py

**目標：** 掌握向上調整的邏輯

#### 第 7 天：複習和除錯
- [ ] 重新執行所有測試
- [ ] 理解每個測試案例
- [ ] 在紙上追蹤演算法執行

---

### 第 2 週：進階操作

**目標：完成所有堆積操作**

#### 第 8-9 天：實作提取
- [ ] 實作 `extract_min()` 方法
- [ ] 實作 `_heapify_down()` 方法
- [ ] 通過 test_stage3.py

**目標：** 掌握向下調整的邏輯

#### 第 10-11 天：整合測試
- [ ] 通過 test_stage4.py
- [ ] 理解堆積性質的維護
- [ ] 處理複雜操作序列

**目標：** 確保堆積在所有操作下正確

#### 第 12-13 天：邊界條件
- [ ] 通過 test_stage5.py
- [ ] 處理所有異常情況
- [ ] 測試極端值

**目標：** 提高程式碼健壯性

#### 第 14 天：週複習
- [ ] 重構程式碼
- [ ] 加入註解
- [ ] 效能優化

---

### 第 3 週：應用和進階

**目標：掌握堆積的實際應用**

#### 第 15-16 天：堆積排序
- [ ] 實作 `heapify()` 函數
- [ ] 實作 `heap_sort()` 函數
- [ ] 理解 O(n) 建堆的原理

**目標：** 理解堆積的另一種建立方式

#### 第 17-18 天：進階應用
- [ ] 實作 `find_kth_smallest()`
- [ ] 通過 test_stage6.py
- [ ] 研究實際應用案例

**目標：** 將堆積應用於問題解決

#### 第 19 天：最終測試
- [ ] 通過 test_stage_final.py
- [ ] 所有測試通過
- [ ] 程式碼審查

**目標：** 驗證完整實作

#### 第 20-21 天：LeetCode 練習
- [ ] 完成 3 道簡單題
- [ ] 完成 2 道中等題
- [ ] 記錄解題思路

**推薦題目：**
- #703, #1046, #347, #23, #295

---

### 第 4 週：精通和擴展

**目標：成為堆積專家**

#### 第 22-23 天：實作最大堆積
- [ ] 建立 MaxHeap 類別
- [ ] 實作所有方法
- [ ] 完整測試

#### 第 24-25 天：進階變體
- [ ] 研究 d-ary heap（d 叉堆積）
- [ ] 研究 Fibonacci heap（費氏堆積）
- [ ] 理解理論優勢

#### 第 26-27 天：系統設計
- [ ] 實作優先權佇列系統
- [ ] 實作任務排程器
- [ ] 完整文件撰寫

#### 第 28 天：總複習
- [ ] 複習所有概念
- [ ] 解決困難 LeetCode 題目
- [ ] 準備面試問題

---

## 面試準備

### 必會問題

1. **基礎概念**
   - 什麼是堆積？與 BST 的區別？
   - 堆積性質是什麼？
   - 為什麼使用陣列表示？

2. **時間複雜度**
   - 各操作的時間複雜度及原因
   - 為什麼建堆是 O(n)？
   - 堆積排序的複雜度分析

3. **實際應用**
   - 說明優先權佇列的實作
   - 如何找第 K 大元素？
   - 如何合併 K 個已排序陣列？

4. **程式設計**
   - 現場實作 insert 和 extract_min
   - 實作堆積排序
   - 解決實際問題

---

### 面試技巧

1. **說明思路**
   - 先說明堆積的選擇理由
   - 畫圖解釋過程
   - 分析時間空間複雜度

2. **程式碼規範**
   - 清晰的變數命名
   - 適當的註解
   - 錯誤處理

3. **測試案例**
   - 空堆積
   - 單元素
   - 大量元素
   - 重複元素

4. **優化討論**
   - 空間優化
   - 快取友善性
   - 實作選擇（最大堆積 vs 最小堆積）

---

## 延伸閱讀

### 書籍推薦
1. **《算法導論》（CLRS）**
   - 第 6 章：Heapsort
   - 理論證明完整

2. **《演算法》（Sedgewick）**
   - 第 2.4 節：Priority Queues
   - 實務導向

3. **《演算法設計手冊》（Skiena）**
   - 優先權佇列應用

### 線上資源
- [VisuAlgo - Heap](https://visualgo.net/en/heap)：視覺化工具
- [YouTube - Abdul Bari](https://www.youtube.com/watch?v=HqPJF2L5h9U)：詳細講解
- [GeeksforGeeks - Heap](https://www.geeksforgeeks.org/heap-data-structure/)：豐富範例

### 進階主題
- **二項堆積（Binomial Heap）**
- **費氏堆積（Fibonacci Heap）**
- **配對堆積（Pairing Heap）**
- **左偏樹（Leftist Heap）**
- **斜堆積（Skew Heap）**

---

## 總結

### 關鍵要點

1. **堆積是完全二元樹，維護父子順序關係**
2. **使用陣列表示，索引計算簡單高效**
3. **插入和刪除都是 O(log n)**
4. **查看最小值是 O(1)**
5. **建堆可以在 O(n) 時間完成**

### 何時使用堆積？

✅ **適合：**
- 需要快速存取最小/最大值
- 實作優先權佇列
- 堆積排序
- 動態維護前 K 大/小元素
- 合併多個已排序序列

❌ **不適合：**
- 需要查找任意元素
- 需要維護完全排序
- 需要範圍查詢
- 需要頻繁更新任意元素的優先權

### 下一步

完成此學習包後，你應該能夠：
- ✓ 完整實作最小堆積和最大堆積
- ✓ 理解所有操作的時間複雜度
- ✓ 應用堆積解決實際問題
- ✓ 在面試中自信地討論堆積
- ✓ 解決 LeetCode 上的堆積相關題目

**繼續學習：**
1. 實作其他堆積變體
2. 解決更多 LeetCode 題目
3. 研究系統設計中的應用
4. 探索進階資料結構（如費氏堆積）

---

**祝學習順利！如有問題，請參考測試案例和註解。**

**記住：理解比記憶更重要。不要只是寫程式碼，要理解每一行的意義！**
