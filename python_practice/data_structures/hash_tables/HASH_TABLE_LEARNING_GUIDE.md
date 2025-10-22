# 雜湊表 (Hash Table) 完整學習指南

## 目錄
1. [什麼是雜湊表](#什麼是雜湊表)
2. [核心概念](#核心概念)
3. [雜湊函數設計](#雜湊函數設計)
4. [碰撞解決方法](#碰撞解決方法)
5. [負載因子與動態調整](#負載因子與動態調整)
6. [時間複雜度分析](#時間複雜度分析)
7. [實作細節](#實作細節)
8. [實際應用](#實際應用)
9. [常見面試問題](#常見面試問題)
10. [練習題目](#練習題目)

---

## 什麼是雜湊表

雜湊表（Hash Table，也稱為哈希表或散列表）是一種實作**關聯陣列**（associative array）的資料結構，它能夠將鍵（key）映射到值（value）。

### 主要特點
- **快速查找**：平均時間複雜度為 O(1)
- **動態大小**：可以根據需要自動擴容
- **鍵值對儲存**：每個鍵對應一個值
- **無序性**：元素沒有特定的順序

### 為什麼需要雜湊表？

假設我們需要儲存學生的成績：

```python
# 使用陣列 - 需要遍歷查找，O(n)
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

# 使用雜湊表 - 直接查找，O(1)
grades = HashTable()
grades.put("Alice", 85)
grades.put("Bob", 92)
grades.put("Charlie", 78)

# 快速查找
alice_grade = grades.get("Alice")  # O(1) 時間
```

---

## 核心概念

### 1. 雜湊函數 (Hash Function)

雜湊函數將任意大小的鍵轉換為固定範圍的整數（陣列索引）。

```
鍵 → 雜湊函數 → 索引
"Alice" → hash("Alice") % capacity → 3
```

**好的雜湊函數特性：**
- **確定性**：相同的鍵總是產生相同的雜湊值
- **均勻分布**：鍵應該均勻分布在所有可能的索引上
- **快速計算**：雜湊計算應該很快
- **雪崩效應**：輸入的微小變化應該導致輸出的巨大變化

### 2. 碰撞 (Collision)

當兩個不同的鍵映射到相同的索引時，就發生了碰撞。

```
hash("Alice") % 10 = 3
hash("Bob") % 10 = 3  ← 碰撞！
```

### 3. 負載因子 (Load Factor)

```
負載因子 = 元素數量 / 容量
```

- 衡量雜湊表的「擁擠程度」
- 影響性能和記憶體使用
- 通常設定在 0.75 左右

---

## 雜湊函數設計

### 基本雜湊函數

```python
def simple_hash(key, capacity):
    """簡單的雜湊函數"""
    return hash(key) % capacity
```

### Python 內建的 hash()

Python 為常見類型提供了內建的雜湊函數：

```python
hash("hello")      # 字串
hash(42)           # 整數
hash((1, 2, 3))    # 元組（不可變）
# hash([1, 2, 3])  # 列表不可雜湊！
```

### 常見雜湊函數技術

#### 1. 除法雜湊 (Division Method)
```python
def division_hash(key, capacity):
    return hash(key) % capacity
```

**優點**：簡單快速
**缺點**：容量選擇很重要（最好是質數）

#### 2. 乘法雜湊 (Multiplication Method)
```python
def multiplication_hash(key, capacity):
    A = 0.6180339887  # 黃金比例
    return int(capacity * ((hash(key) * A) % 1))
```

**優點**：容量選擇不太重要
**缺點**：計算較慢

#### 3. 字串的多項式雜湊
```python
def polynomial_hash(s, capacity):
    """字串的多項式雜湊"""
    hash_value = 0
    p = 31  # 質數
    for char in s:
        hash_value = (hash_value * p + ord(char)) % capacity
    return hash_value
```

---

## 碰撞解決方法

### 方法 1: 分離鏈結法 (Separate Chaining)

**原理**：每個桶存放一個鏈結串列，所有雜湊到該桶的元素都存在鏈結串列中。

```
索引 0: → [key1, value1] → [key2, value2] → None
索引 1: → [key3, value3] → None
索引 2: → None
索引 3: → [key4, value4] → [key5, value5] → [key6, value6] → None
```

**優點**：
- 實作簡單
- 不會因為容量滿了而失敗
- 刪除操作容易

**缺點**：
- 需要額外的指標空間
- 快取性能較差（鏈結串列不連續）

**實作重點**：
```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# 插入時
index = self._hash(key)
new_node = Node(key, value)
new_node.next = self._buckets[index]
self._buckets[index] = new_node  # 頭插法
```

### 方法 2: 開放定址法 (Open Addressing)

**原理**：所有元素都存在陣列中，發生碰撞時尋找下一個空位。

#### 線性探測 (Linear Probing)
```python
index = hash(key) % capacity
while table[index] is not None:
    if table[index].key == key:
        # 找到了
        break
    index = (index + 1) % capacity  # 線性探測
```

#### 二次探測 (Quadratic Probing)
```python
i = 0
while table[index] is not None:
    index = (hash(key) + i * i) % capacity
    i += 1
```

#### 雙重雜湊 (Double Hashing)
```python
index = hash1(key) % capacity
step = hash2(key)
while table[index] is not None:
    index = (index + step) % capacity
```

### 比較

| 特性 | 分離鏈結法 | 開放定址法 |
|------|-----------|-----------|
| 實作難度 | 較簡單 | 較複雜 |
| 記憶體使用 | 額外指標 | 無額外空間 |
| 快取性能 | 較差 | 較好 |
| 刪除操作 | 容易 | 需要標記 |
| 負載因子 | 可以 > 1 | 必須 < 1 |

---

## 負載因子與動態調整

### 為什麼需要動態調整？

當負載因子過高時：
- 碰撞增加
- 鏈結串列變長
- 性能降低到 O(n)

### 擴容策略

```python
def _resize(self):
    """擴容並重新雜湊"""
    # 1. 儲存舊資料
    old_buckets = self._buckets

    # 2. 容量加倍
    self._capacity *= 2

    # 3. 建立新陣列
    self._buckets = [None] * self._capacity
    self._size = 0

    # 4. 重新雜湊所有元素
    for bucket in old_buckets:
        current = bucket
        while current:
            self.put(current.key, current.value)
            current = current.next
```

### 何時觸發擴容？

```python
if self._size / self._capacity > self._load_factor:
    self._resize()
```

### 負載因子的選擇

| 負載因子 | 優點 | 缺點 | 適用場景 |
|---------|------|------|---------|
| 0.5 | 碰撞少，快速 | 浪費空間 | 性能優先 |
| 0.75 | 平衡 | - | **推薦（Python dict 使用）** |
| 0.9 | 節省空間 | 碰撞多 | 記憶體受限 |

### 縮容（可選）

當負載因子過低時，可以縮小容量：

```python
if self._size < self._capacity / 4:
    self._capacity //= 2
    self._resize()
```

---

## 時間複雜度分析

### 理想情況（無碰撞）

| 操作 | 時間複雜度 |
|------|-----------|
| 插入 | O(1) |
| 查找 | O(1) |
| 刪除 | O(1) |
| 空間 | O(n) |

### 最壞情況（所有鍵碰撞）

| 操作 | 時間複雜度 | 說明 |
|------|-----------|------|
| 插入 | O(n) | 需要遍歷整個鏈結串列 |
| 查找 | O(n) | 需要遍歷整個鏈結串列 |
| 刪除 | O(n) | 需要遍歷整個鏈結串列 |

### 平均情況

假設雜湊函數均勻分布：

```
平均鏈長 = n / m （n = 元素數，m = 容量）

查找成功：O(1 + α/2)，其中 α = 負載因子
查找失敗：O(1 + α)
```

**當 α ≤ 0.75 時，平均時間仍然是 O(1)**

### 擴容的攤銷分析

```
插入 n 個元素：
- 大多數插入：O(1)
- 偶爾擴容：O(n)

總時間 = n * O(1) + log(n) * O(n) = O(n)
攤銷時間 = O(n) / n = O(1)
```

---

## 實作細節

### 完整的操作流程

#### 1. 插入 (put)

```python
def put(self, key, value):
    # 步驟 1: 計算索引
    index = self._hash(key)

    # 步驟 2: 檢查鍵是否已存在（更新）
    current = self._buckets[index]
    while current:
        if current.key == key:
            current.value = value  # 更新
            return
        current = current.next

    # 步驟 3: 插入新節點（頭插法）
    new_node = Node(key, value)
    new_node.next = self._buckets[index]
    self._buckets[index] = new_node
    self._size += 1

    # 步驟 4: 檢查是否需要擴容
    if self._size / self._capacity > self._load_factor:
        self._resize()
```

#### 2. 查找 (get)

```python
def get(self, key):
    # 步驟 1: 計算索引
    index = self._hash(key)

    # 步驟 2: 遍歷鏈結串列
    current = self._buckets[index]
    while current:
        if current.key == key:
            return current.value
        current = current.next

    # 步驟 3: 未找到
    raise KeyError(f"Key '{key}' not found")
```

#### 3. 刪除 (remove)

```python
def remove(self, key):
    # 步驟 1: 計算索引
    index = self._hash(key)

    # 步驟 2: 遍歷鏈結串列
    current = self._buckets[index]
    prev = None

    while current:
        if current.key == key:
            # 找到了
            if prev is None:
                # 刪除頭節點
                self._buckets[index] = current.next
            else:
                # 刪除非頭節點
                prev.next = current.next
            self._size -= 1
            return
        prev = current
        current = current.next

    # 步驟 3: 未找到
    raise KeyError(f"Key '{key}' not found")
```

### 常見陷阱

#### 1. 忘記更新大小
```python
# 錯誤
def put(self, key, value):
    # ... 插入邏輯
    # self._size += 1  ← 忘記更新！

# 正確
def put(self, key, value):
    if not self.contains(key):  # 只有新插入才增加
        self._size += 1
```

#### 2. 更新時也增加大小
```python
# 錯誤
def put(self, key, value):
    # ... 插入或更新
    self._size += 1  # 不管是插入還是更新都增加

# 正確
def put(self, key, value):
    # 先檢查是更新還是插入
    is_update = self.contains(key)
    # ... 插入或更新邏輯
    if not is_update:
        self._size += 1  # 只有插入才增加
```

#### 3. 刪除鏈結串列頭節點的特殊處理
```python
# 需要特別處理頭節點
if prev is None:
    self._buckets[index] = current.next  # 頭節點
else:
    prev.next = current.next  # 非頭節點
```

#### 4. 擴容時忘記重置大小
```python
# 錯誤
def _resize(self):
    old_buckets = self._buckets
    self._capacity *= 2
    self._buckets = [None] * self._capacity
    # 沒有重置 self._size
    for bucket in old_buckets:
        # ... 重新插入（會累加大小）

# 正確
def _resize(self):
    old_buckets = self._buckets
    self._capacity *= 2
    self._buckets = [None] * self._capacity
    self._size = 0  # 重置大小
    for bucket in old_buckets:
        # ... 重新插入
```

---

## 實際應用

### 1. 資料庫索引

```python
# 學生資料庫索引
student_index = HashTable()

# 建立索引（學號 → 記錄位置）
student_index.put("S12345", {"name": "Alice", "major": "CS"})
student_index.put("S12346", {"name": "Bob", "major": "Math"})

# O(1) 查詢
alice = student_index.get("S12345")
```

### 2. 快取系統

```python
class Cache:
    def __init__(self, capacity=100):
        self.cache = HashTable()
        self.capacity = capacity

    def get(self, key):
        """獲取快取數據"""
        try:
            return self.cache.get(key)
        except KeyError:
            return None

    def put(self, key, value):
        """存入快取"""
        if self.cache.size() >= self.capacity:
            # 簡單策略：清空
            self.cache.clear()
        self.cache.put(key, value)
```

### 3. 計數器和頻率統計

```python
def word_frequency(text):
    """統計單詞頻率"""
    freq = HashTable()
    words = text.split()

    for word in words:
        if freq.contains(word):
            count = freq.get(word)
            freq.put(word, count + 1)
        else:
            freq.put(word, 1)

    return freq

# 使用
text = "hello world hello python"
freq = word_frequency(text)
print(freq.get("hello"))  # 2
```

### 4. 去重

```python
def remove_duplicates(items):
    """使用雜湊表去重"""
    seen = HashTable()
    result = []

    for item in items:
        if not seen.contains(item):
            seen.put(item, True)
            result.append(item)

    return result

# 使用
items = [1, 2, 3, 2, 4, 1, 5]
unique = remove_duplicates(items)  # [1, 2, 3, 4, 5]
```

### 5. 符號表（編譯器）

```python
class SymbolTable:
    """編譯器符號表"""
    def __init__(self):
        self.table = HashTable()

    def declare(self, var_name, var_type):
        """變數聲明"""
        if self.table.contains(var_name):
            raise Exception(f"Variable {var_name} already declared")
        self.table.put(var_name, {"type": var_type})

    def lookup(self, var_name):
        """查找變數"""
        return self.table.get(var_name)
```

### 6. 兩數之和（LeetCode #1）

```python
def two_sum(nums, target):
    """
    找出陣列中兩個數字相加等於目標值
    時間複雜度：O(n)
    """
    seen = HashTable()

    for i, num in enumerate(nums):
        complement = target - num
        if seen.contains(complement):
            return [seen.get(complement), i]
        seen.put(num, i)

    return []
```

---

## 常見面試問題

### 理論問題

#### Q1: 雜湊表和陣列的區別是什麼？

**答：**
- **陣列**：透過整數索引訪問，O(1) 隨機訪問，但查找值需要 O(n)
- **雜湊表**：透過任意類型的鍵訪問，O(1) 查找、插入、刪除

#### Q2: 什麼是好的雜湊函數？

**答：**
好的雜湊函數應該：
1. **確定性**：相同輸入總是產生相同輸出
2. **均勻分布**：減少碰撞
3. **快速計算**：不影響性能
4. **雪崩效應**：輸入的小變化導致輸出的大變化

#### Q3: 為什麼 Python 的 list 不能作為字典的鍵？

**答：**
因為 list 是可變的（mutable）。如果 list 可以作為鍵：
```python
d = {}
key = [1, 2, 3]
d[key] = "value"
key.append(4)  # 修改了鍵
# 現在 d 內部的雜湊值與新的 key 不匹配！
```

只有不可變類型（str, int, tuple）可以作為鍵。

#### Q4: 分離鏈結法和開放定址法的選擇？

**答：**

**選擇分離鏈結法，如果：**
- 不確定元素數量
- 需要經常刪除
- 實作簡單優先

**選擇開放定址法，如果：**
- 記憶體受限
- 需要更好的快取性能
- 負載因子可控

#### Q5: 負載因子為什麼通常選擇 0.75？

**答：**
0.75 是時間和空間的權衡：
- **< 0.75**：更少碰撞，但浪費空間
- **> 0.75**：節省空間，但更多碰撞
- **0.75**：統計上的最佳平衡點

### 程式碼問題

#### Q6: 實作一個 LRU 快取

```python
class LRUCache:
    def __init__(self, capacity):
        self.cache = HashTable()
        self.capacity = capacity
        self.order = []  # 追蹤使用順序

    def get(self, key):
        if not self.cache.contains(key):
            return -1

        # 更新使用順序
        self.order.remove(key)
        self.order.append(key)

        return self.cache.get(key)

    def put(self, key, value):
        if self.cache.contains(key):
            self.order.remove(key)
        elif self.cache.size() >= self.capacity:
            # 移除最久未使用的
            lru_key = self.order.pop(0)
            self.cache.remove(lru_key)

        self.cache.put(key, value)
        self.order.append(key)
```

#### Q7: 檢查兩個字串是否為變位詞 (Anagram)

```python
def is_anagram(s1, s2):
    """
    時間複雜度：O(n)
    空間複雜度：O(n)
    """
    if len(s1) != len(s2):
        return False

    char_count = HashTable()

    # 統計第一個字串的字元頻率
    for char in s1:
        if char_count.contains(char):
            count = char_count.get(char)
            char_count.put(char, count + 1)
        else:
            char_count.put(char, 1)

    # 檢查第二個字串
    for char in s2:
        if not char_count.contains(char):
            return False
        count = char_count.get(char)
        if count == 1:
            char_count.remove(char)
        else:
            char_count.put(char, count - 1)

    return char_count.is_empty()
```

#### Q8: 找出陣列中第一個不重複的字元

```python
def first_unique_char(s):
    """
    時間複雜度：O(n)
    空間複雜度：O(n)
    """
    char_count = HashTable()

    # 第一次遍歷：統計頻率
    for char in s:
        if char_count.contains(char):
            count = char_count.get(char)
            char_count.put(char, count + 1)
        else:
            char_count.put(char, 1)

    # 第二次遍歷：找第一個頻率為 1 的
    for char in s:
        if char_count.get(char) == 1:
            return char

    return None
```

---

## 練習題目

### 基礎題（掌握基本操作）

1. **實作基本雜湊表**
   - 實作 put, get, remove, contains 方法
   - 使用分離鏈結法處理碰撞

2. **計算負載因子**
   - 實作一個函數計算當前負載因子
   - 當負載因子 > 0.75 時觸發擴容

3. **統計字元頻率**
   - 給定一個字串，統計每個字元出現的次數
   - 回傳頻率最高的字元

### 中階題（組合運用）

4. **兩數之和（LeetCode #1）**
   ```
   給定：nums = [2, 7, 11, 15], target = 9
   輸出：[0, 1]（因為 nums[0] + nums[1] = 9）
   ```

5. **字母異位詞分組（LeetCode #49）**
   ```
   給定：["eat", "tea", "tan", "ate", "nat", "bat"]
   輸出：[["eat","tea","ate"], ["tan","nat"], ["bat"]]
   ```

6. **最長連續序列（LeetCode #128）**
   ```
   給定：[100, 4, 200, 1, 3, 2]
   輸出：4（最長連續序列是 [1, 2, 3, 4]）
   ```

7. **設計實作快取系統**
   - 實作 LRU（Least Recently Used）快取
   - 支援 get 和 put 操作，都要 O(1) 時間

### 進階題（深入理解）

8. **實作開放定址法**
   - 使用線性探測處理碰撞
   - 實作刪除操作（需要標記）

9. **設計 HashMap with Time**
   - 每個鍵值對有時間戳
   - 支援查詢某個時間點的值

10. **一致性雜湊（Consistent Hashing）**
    - 實作一致性雜湊演算法
    - 應用於分散式系統的負載均衡

11. **完美雜湊函數**
    - 為給定的靜態鍵集合設計無碰撞的雜湊函數

12. **雜湊表性能分析**
    - 實作不同的雜湊函數並比較性能
    - 分析碰撞率和查詢時間

### LeetCode 推薦題目

**簡單：**
- #1 Two Sum
- #242 Valid Anagram
- #387 First Unique Character in a String
- #383 Ransom Note
- #205 Isomorphic Strings

**中等：**
- #49 Group Anagrams
- #36 Valid Sudoku
- #347 Top K Frequent Elements
- #128 Longest Consecutive Sequence
- #560 Subarray Sum Equals K

**困難：**
- #146 LRU Cache
- #76 Minimum Window Substring
- #30 Substring with Concatenation of All Words

---

## 學習路徑建議

### 第 1 週：基礎概念
- [ ] 理解雜湊表的基本概念
- [ ] 學習雜湊函數的作用
- [ ] 完成 test_stage1.py 的所有測試

### 第 2 週：基本操作
- [ ] 實作 put 和 get 方法
- [ ] 理解鍵值對的儲存
- [ ] 完成 test_stage2.py 的所有測試

### 第 3 週：碰撞處理
- [ ] 深入理解碰撞的概念
- [ ] 實作分離鏈結法
- [ ] 完成 test_stage3.py 的所有測試

### 第 4 週：刪除操作
- [ ] 實作 remove 方法
- [ ] 處理鏈結串列的刪除
- [ ] 完成 test_stage4.py 的所有測試

### 第 5 週：動態調整
- [ ] 理解負載因子
- [ ] 實作自動擴容
- [ ] 完成 test_stage5.py 的所有測試

### 第 6 週：進階功能
- [ ] 實作 keys, values, clear 方法
- [ ] 完成 test_stage6.py 的所有測試

### 第 7 週：整合與應用
- [ ] 完成 test_stage_final.py 的所有測試
- [ ] 解決 3-5 道 LeetCode 題目
- [ ] 嘗試實作開放定址法

---

## 進階主題

### 1. Python dict 的實作

Python 的 dict 使用開放定址法：
- 使用隨機探測（random probing）
- 負載因子閾值為 2/3
- 刪除操作使用標記位

### 2. 布隆過濾器（Bloom Filter）

空間效率的機率資料結構：
- 用於快速檢查元素是否「可能存在」
- 允許假陽性（false positive），但無假陰性
- 應用：網頁去重、垃圾郵件過濾

### 3. 一致性雜湊（Consistent Hashing）

分散式系統中的雜湊技術：
- 當節點增加/減少時，只需重新映射少量鍵
- 應用：負載均衡、分散式快取

### 4. 完美雜湊（Perfect Hashing）

對靜態鍵集合的無碰撞雜湊：
- 兩級雜湊
- O(1) 最壞情況查詢時間

---

## 參考資源

### 書籍
- 《演算法導論》（CLRS）第 11 章
- 《資料結構與演算法分析》（Mark Allen Weiss）
- 《Python 演算法教程》

### 線上資源
- [VisuAlgo - Hash Table](https://visualgo.net/en/hashtable)
- [CS50 - Hash Tables](https://cs50.harvard.edu/x/)
- [Python dict 實作](https://github.com/python/cpython/blob/main/Objects/dictobject.c)

### 影片
- MIT 6.006 Introduction to Algorithms - Hashing
- UC Berkeley CS61B - Hash Tables

---

## 總結

雜湊表是最重要的資料結構之一：

**核心優勢：**
✅ O(1) 平均查找時間
✅ 動態大小
✅ 應用廣泛

**學習重點：**
1. 理解雜湊函數的作用
2. 掌握碰撞處理方法
3. 理解負載因子和動態調整
4. 熟悉實際應用場景

**下一步：**
- 完成所有測試階段
- 解決 LeetCode 題目
- 研究 Python dict 的原始碼
- 學習進階主題（布隆過濾器、一致性雜湊）

記住：**理解原理比記住程式碼更重要！**

---

祝你學習順利！如有問題，請參考程式碼中的註解或重新閱讀本指南的相關章節。
