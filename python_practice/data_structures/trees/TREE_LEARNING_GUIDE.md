# 二元搜尋樹 (Binary Search Tree) 學習指南

## 目錄
1. [什麼是二元搜尋樹？](#什麼是二元搜尋樹)
2. [BST 的性質](#bst-的性質)
3. [基本操作](#基本操作)
4. [樹的遍歷](#樹的遍歷)
5. [時間複雜度分析](#時間複雜度分析)
6. [平衡與不平衡樹](#平衡與不平衡樹)
7. [實際應用](#實際應用)
8. [進階主題](#進階主題)
9. [練習題目](#練習題目)
10. [學習資源](#學習資源)

---

## 什麼是二元搜尋樹？

**二元搜尋樹 (Binary Search Tree, BST)** 是一種特殊的二元樹資料結構，具有以下特性：

- 每個節點最多有兩個子節點（左子節點和右子節點）
- 左子樹的所有節點值**小於**父節點值
- 右子樹的所有節點值**大於**父節點值
- 左右子樹也都是二元搜尋樹

### 視覺化範例

```
        50
       /  \
      30   70
     / \   / \
   20  40 60  80
```

在這個 BST 中：
- 50 是根節點
- 30 < 50，所以在左邊
- 70 > 50，所以在右邊
- 20, 40 都 < 30，60, 80 都 > 70
- 所有左子樹節點 < 50 < 所有右子樹節點

---

## BST 的性質

### 1. 有序性質
BST 的**中序遍歷**會產生一個**排序好的序列**。

```python
# 對上面的樹進行中序遍歷
結果: [20, 30, 40, 50, 60, 70, 80]  # 已排序！
```

### 2. 唯一路徑
從根節點到任何節點都有唯一的路徑。

### 3. 遞迴結構
BST 的每個子樹也是一個 BST。

### 4. 搜尋效率
可以在每次比較後排除一半的子樹（類似二分搜尋）。

---

## 基本操作

### 1. 插入 (Insert)

**演算法：**
1. 從根節點開始
2. 如果值 < 當前節點，往左走
3. 如果值 > 當前節點，往右走
4. 找到空位置就插入

**範例：** 插入 45 到上面的樹

```
初始:
        50
       /  \
      30   70
     / \   / \
   20  40 60  80

步驟:
1. 45 < 50，往左
2. 45 > 30，往右
3. 45 > 40，往右（40 的右邊是空的）
4. 在這裡插入 45

結果:
        50
       /  \
      30   70
     / \   / \
   20  40 60  80
        \
        45
```

**程式碼：**
```python
def insert(self, value):
    if self.root is None:
        self.root = TreeNode(value)
    else:
        self._insert_recursive(self.root, value)

def _insert_recursive(self, node, value):
    if value < node.value:
        if node.left is None:
            node.left = TreeNode(value)
        else:
            self._insert_recursive(node.left, value)
    elif value > node.value:
        if node.right is None:
            node.right = TreeNode(value)
        else:
            self._insert_recursive(node.right, value)
```

### 2. 搜尋 (Search)

**演算法：**
1. 從根節點開始
2. 如果值 == 當前節點，找到了
3. 如果值 < 當前節點，往左搜尋
4. 如果值 > 當前節點，往右搜尋
5. 如果走到 None，表示不存在

**範例：** 搜尋 60

```
        50          1. 60 > 50，往右
       /  \
      30   70       2. 60 < 70，往左
     / \   / \
   20  40 60  80    3. 60 == 60，找到了！
```

**程式碼：**
```python
def search(self, value):
    return self._search_recursive(self.root, value)

def _search_recursive(self, node, value):
    if node is None or node.value == value:
        return node

    if value < node.value:
        return self._search_recursive(node.left, value)
    else:
        return self._search_recursive(node.right, value)
```

### 3. 刪除 (Delete)

刪除是 BST 中最複雜的操作，有三種情況：

#### 情況 1：刪除葉節點（無子節點）
直接刪除即可。

```
刪除 20:
        50                    50
       /  \                  /  \
      30   70    -->        30   70
     / \   / \               \   / \
   20  40 60  80             40 60  80
```

#### 情況 2：刪除只有一個子節點的節點
用子節點替換該節點。

```
刪除 30（假設 30 只有右子節點 40）:
        50                    50
       /  \                  /  \
      30   70    -->        40   70
       \   / \               \   / \
       40 60  80             45 60  80
        \
        45
```

#### 情況 3：刪除有兩個子節點的節點
1. 找到右子樹的最小值（或左子樹的最大值）
2. 用該值替換要刪除的節點
3. 刪除那個最小值節點

```
刪除 50:
        50                    60        (用右子樹最小值 60 替換)
       /  \                  /  \
      30   70    -->        30   70
     / \   / \             / \     \
   20  40 60  80         20  40    80
```

**程式碼：**
```python
def delete(self, value):
    self.root = self._delete_recursive(self.root, value)

def _delete_recursive(self, node, value):
    if node is None:
        return None

    if value < node.value:
        node.left = self._delete_recursive(node.left, value)
    elif value > node.value:
        node.right = self._delete_recursive(node.right, value)
    else:
        # 找到要刪除的節點

        # 情況 1 & 2: 葉節點或只有一個子節點
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        # 情況 3: 有兩個子節點
        # 找右子樹的最小值
        min_node = self._find_min_node(node.right)
        node.value = min_node.value
        node.right = self._delete_recursive(node.right, min_node.value)

    return node
```

### 4. 找最小值 / 最大值

**最小值：** 一直往左走到底
**最大值：** 一直往右走到底

```python
def get_min(self):
    if self.root is None:
        return None
    current = self.root
    while current.left is not None:
        current = current.left
    return current.value

def get_max(self):
    if self.root is None:
        return None
    current = self.root
    while current.right is not None:
        current = current.right
    return current.value
```

---

## 樹的遍歷

### 1. 中序遍歷 (Inorder: 左-根-右)

對 BST 進行中序遍歷會得到**排序好的序列**。

```
        50
       /  \
      30   70
     / \   / \
   20  40 60  80

中序: [20, 30, 40, 50, 60, 70, 80]  ← 已排序！
```

**遍歷步驟：**
1. 遍歷左子樹
2. 訪問根節點
3. 遍歷右子樹

**應用：** 排序、驗證 BST

### 2. 前序遍歷 (Preorder: 根-左-右)

```
        50
       /  \
      30   70
     / \   / \
   20  40 60  80

前序: [50, 30, 20, 40, 70, 60, 80]
```

**遍歷步驟：**
1. 訪問根節點
2. 遍歷左子樹
3. 遍歷右子樹

**應用：** 複製樹、序列化樹、前綴表達式

### 3. 後序遍歷 (Postorder: 左-右-根)

```
        50
       /  \
      30   70
     / \   / \
   20  40 60  80

後序: [20, 40, 30, 60, 80, 70, 50]
```

**遍歷步驟：**
1. 遍歷左子樹
2. 遍歷右子樹
3. 訪問根節點

**應用：** 刪除樹、後綴表達式、計算目錄大小

### 4. 層序遍歷 (Level Order: 逐層從左到右)

也稱為**廣度優先搜尋 (BFS)**。

```
        50
       /  \
      30   70
     / \   / \
   20  40 60  80

層序: [50, 30, 70, 20, 40, 60, 80]
      └層0  └─層1─┘  └───層2───┘
```

**演算法：** 使用佇列 (Queue)
1. 將根節點放入佇列
2. 當佇列不為空：
   - 取出前端節點
   - 訪問該節點
   - 將其左右子節點放入佇列

**應用：** 找最短路徑、層級相關問題

### 遍歷方式比較

| 遍歷方式 | 順序 | 應用 | 實作方式 |
|---------|------|------|---------|
| 中序 | 左-根-右 | 排序、驗證 BST | 遞迴/堆疊 |
| 前序 | 根-左-右 | 複製、序列化 | 遞迴/堆疊 |
| 後序 | 左-右-根 | 刪除、計算 | 遞迴/堆疊 |
| 層序 | 逐層訪問 | 最短路徑 | 佇列 (BFS) |

---

## 時間複雜度分析

### 平衡樹（理想情況）

當樹是平衡的（左右子樹高度差不大）：

| 操作 | 時間複雜度 | 說明 |
|------|-----------|------|
| 搜尋 | O(log n) | 每次比較排除一半節點 |
| 插入 | O(log n) | 需要先搜尋位置 |
| 刪除 | O(log n) | 需要搜尋並可能找後繼 |
| 找最小值 | O(log n) | 往左走到底 |
| 找最大值 | O(log n) | 往右走到底 |
| 遍歷 | O(n) | 需要訪問所有節點 |

**為什麼是 O(log n)？**

對於 n 個節點的平衡樹：
- 高度 h ≈ log₂(n)
- 從根到葉的路徑長度 ≈ log₂(n)
- 搜尋需要走這條路徑

範例：
- 1000 個節點 → 高度約 10
- 1,000,000 個節點 → 高度約 20

### 不平衡樹（最壞情況）

當樹退化成鏈狀（如按順序插入）：

```
1          ← 這不是好的 BST！
 \
  2        高度 = n-1
   \
    3
     \
      4
       \
        5
```

| 操作 | 時間複雜度 | 說明 |
|------|-----------|------|
| 搜尋 | O(n) | 需要遍歷整條鏈 |
| 插入 | O(n) | 需要走到最後 |
| 刪除 | O(n) | 需要遍歷整條鏈 |

### 空間複雜度

| 操作 | 空間複雜度 | 說明 |
|------|-----------|------|
| 儲存 | O(n) | 需要儲存 n 個節點 |
| 遞迴遍歷 | O(h) | 遞迴呼叫堆疊深度 = 樹高 |
| 層序遍歷 | O(w) | 佇列最大寬度 = 最寬層的節點數 |

---

## 平衡與不平衡樹

### 什麼是平衡樹？

**平衡樹**是指左右子樹的高度差不會太大的樹。

```
平衡的 BST:                不平衡的 BST:
        50                       1
       /  \                       \
      30   70                      2
     / \   / \                      \
   20  40 60  80                     3
                                      \
高度 = 2                               4
所有操作 O(log n)                       \
                                        5

                                    高度 = 4
                                    所有操作 O(n)
```

### 平衡因子 (Balance Factor)

節點的平衡因子 = 左子樹高度 - 右子樹高度

- 平衡樹：所有節點的平衡因子 ∈ {-1, 0, 1}
- 不平衡：存在節點的平衡因子 > 1 或 < -1

### 為什麼需要平衡？

| 樹類型 | 插入順序 | 高度 | 搜尋效率 |
|--------|---------|------|---------|
| 平衡樹 | 50,30,70,20,40,60,80 | log n | O(log n) |
| 不平衡樹 | 1,2,3,4,5,6,7 | n | O(n) |

**結論：** 不平衡的 BST 失去了高效搜尋的優勢！

### 自平衡樹

為了保持平衡，發展出自平衡的 BST 變體：

1. **AVL Tree** - 嚴格平衡，平衡因子 ∈ {-1, 0, 1}
2. **Red-Black Tree** - 相對平衡，保證操作 O(log n)
3. **Splay Tree** - 自調整樹，經常訪問的節點會移到根部

---

## 實際應用

### 1. 資料庫索引

資料庫使用 B-Tree（BST 的變體）來建立索引：

```sql
SELECT * FROM users WHERE id = 12345;
```

- 索引就是一個 BST
- 快速找到 id=12345 的記錄
- 時間複雜度 O(log n)

### 2. 檔案系統

檔案系統使用樹狀結構：

```
C:\
├── Users\
│   ├── Alice\
│   └── Bob\
└── Program Files\
    ├── App1\
    └── App2\
```

### 3. 排序和去重

```python
# 使用 BST 排序
def bst_sort(arr):
    bst = BinarySearchTree()
    for value in arr:
        bst.insert(value)
    return bst.inorder_traversal()

# 使用 BST 去重
def deduplicate(arr):
    bst = BinarySearchTree()
    for value in arr:
        bst.insert(value)  # BST 自動處理重複
    return bst.inorder_traversal()
```

### 4. 自動完成和拼寫檢查

```
字典樹（Trie）是特殊的樹結構：
        root
       /  |  \
      c   d   t
     /    |    \
    a     o     r
   /      |      \
  t       g       e
         /         \
        s           e
```

### 5. 優先佇列

堆（Heap）是特殊的樹，用於實作優先佇列：
- Min Heap: 父節點 < 子節點
- Max Heap: 父節點 > 子節點

### 6. 範圍查詢

找出某個範圍內的所有值：

```python
# 找出 30 到 60 之間的所有值
def range_query(bst, low, high):
    result = []
    for value in bst.inorder_traversal():
        if low <= value <= high:
            result.append(value)
    return result
```

---

## 進階主題

### 1. AVL Tree（AVL 樹）

**發明者：** Adelson-Velsky 和 Landis (1962)

**特點：**
- 嚴格平衡的 BST
- 每個節點的平衡因子 ∈ {-1, 0, 1}
- 通過旋轉操作維持平衡

**旋轉操作：**

```
左旋 (Left Rotation):
    y                x
   / \              / \
  x   C    -->     A   y
 / \                  / \
A   B                B   C

右旋 (Right Rotation):
  x                  y
 / \                / \
A   y      -->     x   C
   / \            / \
  B   C          A   B
```

**何時使用：**
- 需要頻繁插入和刪除
- 需要保證 O(log n) 的最壞情況
- 讀取和寫入次數相當

### 2. Red-Black Tree（紅黑樹）

**特點：**
- 每個節點有顏色（紅或黑）
- 根節點和葉節點（NIL）是黑色
- 紅色節點的子節點必須是黑色
- 從根到葉的所有路徑包含相同數量的黑色節點

**性質：**
- 保證從根到葉的最長路徑 ≤ 2 × 最短路徑
- 所有操作 O(log n)
- 旋轉次數少於 AVL

**何時使用：**
- 寫入頻繁（如 Linux 核心的調度器）
- C++ STL 的 map 和 set
- Java 的 TreeMap 和 TreeSet

### 3. B-Tree 和 B+ Tree

**用途：** 資料庫和檔案系統

**特點：**
- 每個節點可以有多個子節點（不只 2 個）
- 減少磁碟 I/O 次數
- 適合大量資料

```
B-Tree 範例（每個節點最多 3 個值）：
            [30, 60]
           /    |    \
    [10,20]  [40,50]  [70,80,90]
```

### 4. Trie（字典樹）

**用途：** 字串搜尋、自動完成

**特點：**
- 每個節點代表一個字元
- 從根到葉的路徑形成一個字串
- 公共前綴共享路徑

```
插入 "cat", "car", "dog":
      root
     /    \
    c      d
    |      |
    a      o
   / \     |
  t   r    g
```

### 5. 線段樹 (Segment Tree)

**用途：** 範圍查詢和更新

**特點：**
- 支援高效的範圍操作
- 查詢和更新都是 O(log n)

**應用：**
- 範圍和查詢
- 範圍最小值 / 最大值查詢

---

## 練習題目

### 基礎題

1. **驗證 BST** - 檢查一個二元樹是否是有效的 BST
   - LeetCode 98: Validate Binary Search Tree

2. **BST 中第 K 小的元素** - 找出 BST 中第 k 小的元素
   - LeetCode 230: Kth Smallest Element in a BST

3. **BST 的最近公共祖先** - 找兩個節點的最近公共祖先
   - LeetCode 235: Lowest Common Ancestor of a BST

### 中階題

4. **平衡二元樹** - 檢查樹是否平衡
   - LeetCode 110: Balanced Binary Tree

5. **將排序陣列轉換為 BST** - 將已排序陣列轉為平衡 BST
   - LeetCode 108: Convert Sorted Array to Binary Search Tree

6. **BST 迭代器** - 實作 BST 的迭代器
   - LeetCode 173: Binary Search Tree Iterator

7. **刪除 BST 中的節點** - 實作刪除操作
   - LeetCode 450: Delete Node in a BST

### 進階題

8. **恢復 BST** - 修復兩個節點被錯誤交換的 BST
   - LeetCode 99: Recover Binary Search Tree

9. **序列化和反序列化 BST** - 將 BST 轉為字串並還原
   - LeetCode 449: Serialize and Deserialize BST

10. **實作 AVL Tree** - 完整實作自平衡 AVL 樹

### 實作練習

```python
# 練習 1: 實作 BST 的高度計算
def get_height(node):
    # TODO: 實作
    pass

# 練習 2: 檢查是否為有效的 BST
def is_valid_bst(root):
    # TODO: 實作
    pass

# 練習 3: 找出 BST 中兩個節點的最近公共祖先
def lowest_common_ancestor(root, p, q):
    # TODO: 實作
    pass

# 練習 4: 將排序陣列轉為平衡 BST
def sorted_array_to_bst(nums):
    # TODO: 實作
    pass

# 練習 5: 實作 BST 的迭代器
class BSTIterator:
    def __init__(self, root):
        # TODO: 實作
        pass

    def next(self):
        # TODO: 實作
        pass

    def has_next(self):
        # TODO: 實作
        pass
```

---

## 學習資源

### 線上課程

1. **Coursera - Algorithms, Part I** (Princeton)
   - 包含 BST 和平衡樹的詳細講解

2. **MIT OpenCourseWare - Introduction to Algorithms**
   - 6.006: 完整的樹結構課程

3. **VisuAlgo** - https://visualgo.net/en/bst
   - BST 操作的視覺化演示

### 書籍

1. **《算法導論》(Introduction to Algorithms)** - CLRS
   - 第 12 章：二元搜尋樹
   - 第 13 章：紅黑樹

2. **《數據結構與算法分析》** - Mark Allen Weiss
   - 第 4 章：樹

3. **《算法》第 4 版** - Robert Sedgewick
   - 第 3.2 節：二元搜尋樹
   - 第 3.3 節：平衡查找樹

### 線上資源

1. **GeeksforGeeks**
   - https://www.geeksforgeeks.org/binary-search-tree-data-structure/
   - 大量 BST 相關文章和程式碼

2. **LeetCode**
   - 樹的專題：https://leetcode.com/tag/tree/
   - BST 的專題：https://leetcode.com/tag/binary-search-tree/

3. **HackerRank**
   - 樹的練習題

### 視覺化工具

1. **VisuAlgo** - https://visualgo.net/en/bst
   - 互動式 BST 視覺化

2. **BST Visualization** - https://www.cs.usfca.edu/~galles/visualization/BST.html
   - 簡單易用的 BST 動畫

3. **Tree Visualizer** - https://tree-visualizer.netlify.app/
   - 繪製和視覺化樹結構

---

## 學習路線圖

### 第 1 週：基礎概念
- [ ] 理解樹的基本概念
- [ ] 理解 BST 的性質
- [ ] 實作 TreeNode 類別
- [ ] 完成測試階段 1

### 第 2 週：基本操作
- [ ] 實作插入操作
- [ ] 實作搜尋操作
- [ ] 完成測試階段 2-3

### 第 3 週：遍歷方式
- [ ] 實作深度優先遍歷（前序、中序、後序）
- [ ] 實作廣度優先遍歷（層序）
- [ ] 完成測試階段 4

### 第 4 週：進階操作
- [ ] 實作最小值 / 最大值查找
- [ ] 實作高度計算
- [ ] 實作刪除操作
- [ ] 完成測試階段 5-6

### 第 5 週：複雜操作
- [ ] 完成層序遍歷
- [ ] 處理邊界情況
- [ ] 完成測試階段 7-8

### 第 6 週：整合與應用
- [ ] 完成最終測試
- [ ] 練習 LeetCode 題目
- [ ] 研究實際應用

### 第 7-8 週：進階主題
- [ ] 學習 AVL 樹
- [ ] 學習紅黑樹
- [ ] 研究 B-Tree

---

## 常見問題 (FAQ)

### Q1: BST 和普通二元樹有什麼差別？
**A:** BST 有順序性質：左子樹 < 根 < 右子樹。普通二元樹沒有這個限制。

### Q2: 什麼時候 BST 效能最差？
**A:** 當數據已排序時（升序或降序），樹會退化成鏈狀，所有操作變成 O(n)。

### Q3: 如何避免 BST 不平衡？
**A:**
1. 隨機化插入順序
2. 使用自平衡樹（AVL、紅黑樹）
3. 定期重建樹

### Q4: BST 可以儲存重複值嗎？
**A:** 可以，但需要決定策略：
- 不允許重複（本實作採用）
- 允許重複，放在左邊或右邊
- 在節點中記錄計數

### Q5: 中序遍歷為什麼能得到排序序列？
**A:** 因為中序遍歷的順序是「左-根-右」，而 BST 的性質保證左 < 根 < 右。

### Q6: BST 和 Hash Table 哪個更好？
**A:** 取決於需求：
- Hash Table：O(1) 查找，但無序
- BST：O(log n) 查找，但有序，支援範圍查詢

### Q7: 什麼時候應該使用 BST？
**A:**
- 需要維護有序數據
- 需要範圍查詢
- 需要找最小值 / 最大值
- 需要中序遍歷

### Q8: BST 的空間複雜度是多少？
**A:** O(n)，需要儲存 n 個節點。遞迴操作額外需要 O(h) 的堆疊空間，h 是樹高。

---

## 總結

### 關鍵要點

1. **BST 性質**：左 < 根 < 右，遞迴成立
2. **中序遍歷**：得到排序序列
3. **平衡很重要**：平衡樹 O(log n)，不平衡樹 O(n)
4. **三種刪除情況**：葉節點、一個子節點、兩個子節點
5. **實際應用**：資料庫、檔案系統、排序

### 下一步

1. **掌握基礎**：確保能夠實作基本的 BST
2. **練習題目**：在 LeetCode 上刷樹的題目
3. **學習進階**：研究 AVL、紅黑樹等自平衡樹
4. **實際應用**：了解資料庫索引、檔案系統的實現

---

## 附錄：複雜度速查表

| 資料結構 | 搜尋 | 插入 | 刪除 | 空間 | 備註 |
|---------|------|------|------|------|------|
| 陣列（未排序） | O(n) | O(1) | O(n) | O(n) | - |
| 陣列（已排序） | O(log n) | O(n) | O(n) | O(n) | 二分搜尋 |
| 鏈結串列 | O(n) | O(1) | O(n) | O(n) | - |
| BST（平衡） | O(log n) | O(log n) | O(log n) | O(n) | 需維持平衡 |
| BST（不平衡） | O(n) | O(n) | O(n) | O(n) | 最壞情況 |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(n) | 嚴格平衡 |
| Red-Black Tree | O(log n) | O(log n) | O(log n) | O(n) | 相對平衡 |
| Hash Table | O(1)* | O(1)* | O(1)* | O(n) | 平均情況 |

*平均情況，最壞情況 O(n)

---

**祝你學習愉快！Happy Learning!** 🌳
