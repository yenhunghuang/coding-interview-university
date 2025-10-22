# Queue (佇列) 學習指南

## 📚 什麼是 Queue？

Queue（佇列）是一種線性數據結構，遵循 **FIFO (First In, First Out)** 原則，即「先進先出」。

### 生活中的比喻
想像在銀行或超市排隊：
- 先到的人先被服務
- 新來的人排在隊伍後面
- 最先進入隊伍的人，會是第一個離開的

這就是 Queue 的運作方式！

## 🎯 核心概念

### FIFO 原則
```
Enqueue 操作：        Dequeue 操作：
   (入隊)               (出隊)
     ↓                    ↑
     |                    |
[1, 2, 3, 4, 5]    [1, 2, 3, 4, 5]
 ↑           ↑      ↑           ↑
front      rear    front      rear
(前端)     (尾部)  (移除)     (尾部)
```

### 主要操作

| 操作 | 描述 | 時間複雜度 |
|------|------|------------|
| `enqueue(item)` | 將元素加入佇列尾部 | O(1) |
| `dequeue()` | 移除並返回前端元素 | O(1)* |
| `front()` | 查看前端元素但不移除 | O(1) |
| `is_empty()` | 檢查是否為空 | O(1) |
| `size()` | 獲取元素數量 | O(1) |
| `is_full()` | 檢查是否已滿 | O(1) |
| `clear()` | 清空佇列 | O(1) |

*註：使用列表實作時 `pop(0)` 是 O(n)，但使用循環陣列或鏈表可達到真正的 O(1)

## 🛠️ 實作方式

### 1. 使用陣列/列表實作（簡化版）
```python
class Queue:
    def __init__(self, max_size=None):
        self._data = []
        self._max_size = max_size

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")
        self._data.append(item)  # O(1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data.pop(0)  # O(n) - 簡化版
```

**優點：**
- 實作簡單直觀
- 容易理解 FIFO 概念

**缺點：**
- `pop(0)` 是 O(n) 操作（需移動所有元素）
- 不適合頻繁的 dequeue 操作

### 2. 使用循環陣列實作（優化版）
```python
class CircularQueue:
    def __init__(self, max_size):
        self._data = [None] * max_size
        self._front = 0
        self._rear = 0
        self._size = 0
        self._max_size = max_size

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")
        self._data[self._rear] = item
        self._rear = (self._rear + 1) % self._max_size  # 循環
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self._data[self._front]
        self._front = (self._front + 1) % self._max_size  # 循環
        self._size -= 1
        return item
```

**優點：**
- 所有操作都是真正的 O(1)
- 空間利用效率高
- 適合固定大小的佇列

**缺點：**
- 需要預先分配空間
- 實作較複雜

### 3. 使用鏈表實作
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self._rear is None:
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return item
```

**優點：**
- 動態大小，不需預分配
- 所有操作都是 O(1)
- 記憶體使用靈活

**缺點：**
- 每個元素需要額外的指標空間
- 快取局部性較差
- 實作較複雜

## 🌟 實際應用

### 1. 任務調度系統
```python
class TaskScheduler:
    def __init__(self):
        self.task_queue = Queue()

    def add_task(self, task):
        """添加新任務到佇列"""
        self.task_queue.enqueue(task)
        print(f"任務已加入: {task}")

    def process_next_task(self):
        """處理下一個任務（FIFO）"""
        if not self.task_queue.is_empty():
            task = self.task_queue.dequeue()
            print(f"正在處理: {task}")
            return task
        else:
            print("沒有待處理任務")
            return None

# 使用範例
scheduler = TaskScheduler()
scheduler.add_task("發送郵件")
scheduler.add_task("生成報告")
scheduler.add_task("備份數據")

while not scheduler.task_queue.is_empty():
    scheduler.process_next_task()
```

### 2. 廣度優先搜尋（BFS）
```python
def bfs(graph, start):
    """
    使用佇列實作廣度優先搜尋

    這是佇列最經典的應用之一
    """
    visited = set()
    queue = Queue()

    queue.enqueue(start)
    visited.add(start)

    while not queue.is_empty():
        vertex = queue.dequeue()
        print(f"訪問: {vertex}")

        # 將所有未訪問的鄰居加入佇列
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

# 使用範例
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')  # 輸出：A B C D E F
```

### 3. 樹的層序遍歷
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    """
    使用佇列進行層序遍歷

    樹結構：
          1
        /   \
       2     3
      / \   / \
     4   5 6   7

    輸出：[1, 2, 3, 4, 5, 6, 7]
    """
    if not root:
        return []

    result = []
    queue = Queue()
    queue.enqueue(root)

    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.value)

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    return result

# 建立樹
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(level_order_traversal(root))  # [1, 2, 3, 4, 5, 6, 7]
```

### 4. 客服系統排隊
```python
class CustomerService:
    def __init__(self, max_wait=10):
        self.queue = Queue(max_size=max_wait)
        self.ticket_number = 0

    def take_ticket(self, customer_name):
        """客戶取號排隊"""
        if self.queue.is_full():
            print(f"抱歉 {customer_name}，目前人數已滿，請稍後再來")
            return None

        self.ticket_number += 1
        ticket = {"number": self.ticket_number, "name": customer_name}
        self.queue.enqueue(ticket)
        print(f"{customer_name} 取得號碼: {self.ticket_number}")
        print(f"前方還有 {self.queue.size() - 1} 位等候")
        return self.ticket_number

    def serve_next(self):
        """服務下一位客戶"""
        if self.queue.is_empty():
            print("目前沒有等候的客戶")
            return None

        ticket = self.queue.dequeue()
        print(f"請 {ticket['number']} 號 {ticket['name']} 到櫃台")
        print(f"剩餘等候: {self.queue.size()} 位")
        return ticket

# 使用範例
service = CustomerService(max_wait=5)
service.take_ticket("Alice")
service.take_ticket("Bob")
service.take_ticket("Carol")

service.serve_next()  # 服務 Alice
service.serve_next()  # 服務 Bob
```

### 5. 打印機佇列
```python
class PrintQueue:
    def __init__(self):
        self.queue = Queue()

    def add_job(self, document, pages):
        """添加打印任務"""
        job = {
            "document": document,
            "pages": pages,
            "timestamp": time.time()
        }
        self.queue.enqueue(job)
        print(f"已加入打印佇列: {document} ({pages} 頁)")

    def print_next(self):
        """打印下一份文件"""
        if self.queue.is_empty():
            print("打印佇列為空")
            return None

        job = self.queue.dequeue()
        print(f"正在打印: {job['document']}")
        print(f"  頁數: {job['pages']}")
        print(f"  剩餘任務: {self.queue.size()}")
        return job

    def show_queue(self):
        """顯示當前佇列狀態"""
        print(f"待打印文件數: {self.queue.size()}")

# 使用範例
printer = PrintQueue()
printer.add_job("報告.pdf", 10)
printer.add_job("照片.jpg", 1)
printer.add_job("簡報.pptx", 25)

printer.show_queue()
printer.print_next()
printer.print_next()
```

### 6. 緩衝區管理
```python
class Buffer:
    """
    數據緩衝區，用於處理數據流
    生產者-消費者模式
    """
    def __init__(self, size=100):
        self.buffer = Queue(max_size=size)

    def produce(self, data):
        """生產者添加數據"""
        try:
            self.buffer.enqueue(data)
            print(f"已添加數據: {data}")
            return True
        except OverflowError:
            print("緩衝區已滿，無法添加")
            return False

    def consume(self):
        """消費者取出數據"""
        try:
            data = self.buffer.dequeue()
            print(f"已處理數據: {data}")
            return data
        except IndexError:
            print("緩衝區為空")
            return None

    def status(self):
        """顯示緩衝區狀態"""
        print(f"緩衝區: {self.buffer.size()}/{self.buffer.max_size}")

# 使用範例
buffer = Buffer(size=5)

# 生產數據
for i in range(3):
    buffer.produce(f"data_{i}")

buffer.status()

# 消費數據
buffer.consume()
buffer.consume()

buffer.status()
```

## 🧪 TDD 學習過程

我們的實作採用測試驅動開發（TDD）方法，分為 6 個階段：

### 階段 1: 基礎結構 (test_stage1.py)
- 測試初始化和基本查詢方法
- 實作 `__init__()`, `size()`, `is_empty()`
- 驗證容量限制的初始化
- 錯誤處理（無效容量）

**學習重點：**
- 理解佇列的基本結構
- 掌握初始化參數
- 學習錯誤處理

### 階段 2: 入隊操作 (test_stage2.py)
- 測試 `enqueue()` 和 `is_full()` 方法
- 驗證容量限制
- 測試不同數據類型

**學習重點：**
- 實作入隊邏輯
- 處理容量溢出
- 理解佇列的尾部操作

### 階段 3: 出隊操作 (test_stage3.py)
- 測試 `dequeue()` 和 `front()` 方法
- 驗證 FIFO 行為
- 空佇列錯誤處理
- 混合操作測試

**學習重點：**
- 實作出隊邏輯
- 驗證 FIFO 原則
- 理解佇列的前端操作

### 階段 4: 完整 FIFO 驗證 (test_stage4.py)
- 大規模操作測試
- 複雜場景驗證
- 邊界條件測試
- 交替操作測試

**學習重點：**
- 確保 FIFO 正確性
- 處理複雜場景
- 測試性能表現

### 階段 5: 輔助功能 (test_stage5.py)
- 測試 `clear()` 方法
- 測試 `__str__()` 和 `__repr__()`
- 測試 `max_size` 屬性
- 邊界情況處理

**學習重點：**
- 完善輔助功能
- 改善用戶體驗
- 提供清晰的調試信息

### 階段 6: 最終驗證 (test_stage_final.py)
- 綜合測試所有功能
- 實際應用場景驗證
- 效能測試
- 進階應用函數測試

**學習重點：**
- 整體功能驗證
- 實際應用能力
- 性能評估

## 📊 複雜度分析

### 時間複雜度

#### 簡化列表實作
- **Enqueue**: O(1) - 使用 `append()`
- **Dequeue**: O(n) - 使用 `pop(0)` 需移動元素
- **Front**: O(1) - 直接訪問索引 0
- **Is_empty**: O(1) - 檢查長度
- **Size**: O(1) - 返回長度
- **Clear**: O(1) - 清空列表

#### 循環陣列實作
- **所有操作**: O(1) - 使用索引和取模運算

#### 鏈表實作
- **所有操作**: O(1) - 直接操作頭尾指標

### 空間複雜度
- **整體**: O(n) - n 是佇列中元素的數量
- **循環陣列**: O(max_size) - 需預分配空間
- **鏈表**: O(n) - 每個節點額外空間
- **每個操作**: O(1) - 不需要額外空間

### 性能比較

| 實作方式 | Enqueue | Dequeue | 空間效率 | 適用場景 |
|---------|---------|---------|---------|---------|
| 簡化列表 | O(1) | O(n) | 高 | 學習、小規模 |
| 循環陣列 | O(1) | O(1) | 中 | 固定大小、高性能 |
| 鏈表 | O(1) | O(1) | 低 | 動態大小、頻繁操作 |

## 🚫 常見錯誤

### 1. 空佇列操作
```python
queue = Queue()
# 錯誤：嘗試從空佇列 dequeue
try:
    queue.dequeue()  # 會拋出 IndexError
except IndexError:
    print("佇列為空！")

# 正確做法：先檢查
if not queue.is_empty():
    item = queue.dequeue()
```

### 2. 混淆 front 和 dequeue
```python
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)

# front 不會移除元素
front_item = queue.front()  # front_item = 1, 佇列仍是 [1, 2]
print(queue.size())  # 2

# dequeue 會移除元素
item = queue.dequeue()  # item = 1, 佇列現在是 [2]
print(queue.size())  # 1
```

### 3. 容量溢出
```python
queue = Queue(max_size=2)
queue.enqueue(1)
queue.enqueue(2)

# 錯誤：超過容量限制
try:
    queue.enqueue(3)  # 會拋出 OverflowError
except OverflowError:
    print("佇列已滿！")

# 正確做法：先檢查
if not queue.is_full():
    queue.enqueue(3)
```

### 4. 混淆 Stack 和 Queue
```python
# Stack (LIFO) - 後進先出
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 3 (最後進入的先出來)

# Queue (FIFO) - 先進先出
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 1 (最先進入的先出來)
```

### 5. 循環陣列索引計算錯誤
```python
# 錯誤：沒有使用取模運算
def enqueue_wrong(self, item):
    self._data[self._rear] = item
    self._rear += 1  # 錯誤：會超出邊界

# 正確：使用取模實現循環
def enqueue_correct(self, item):
    self._data[self._rear] = item
    self._rear = (self._rear + 1) % self._max_size  # 正確
```

## 🎓 練習題

### 初級

1. **實作基本 Queue**
   - 使用列表實作所有基本操作
   - 確保 FIFO 行為正確

2. **燙手山芋遊戲**
   ```python
   def hot_potato(names, num):
       """
       模擬燙手山芋遊戲
       names: 參與者列表
       num: 每輪傳遞次數
       返回：獲勜者
       """
       pass
   ```

3. **生成二進位數字**
   ```python
   def generate_binary_numbers(n):
       """
       生成 1 到 n 的二進位表示
       使用佇列實作
       """
       pass
   ```

### 中級

1. **用兩個 Stack 實作 Queue**
   ```python
   class QueueUsingStacks:
       """
       使用兩個堆疊實作佇列
       思考如何保證 FIFO
       """
       def __init__(self):
           self.stack1 = []  # 入隊用
           self.stack2 = []  # 出隊用
   ```

2. **實作循環佇列**
   ```python
   class CircularQueue:
       """
       實作固定大小的循環佇列
       所有操作都是 O(1)
       """
       pass
   ```

3. **設計滑動窗口最大值**
   - LeetCode 239: Sliding Window Maximum
   - 使用雙端佇列（Deque）優化

### 高級

1. **實作 LRU Cache**
   ```python
   class LRUCache:
       """
       使用 Queue + HashMap 實作 LRU Cache
       """
       pass
   ```

2. **實作優先佇列**
   ```python
   class PriorityQueue:
       """
       元素按優先級排序的佇列
       可以使用堆（Heap）優化
       """
       pass
   ```

3. **實作雙端佇列（Deque）**
   ```python
   class Deque:
       """
       兩端都可以插入和刪除的佇列
       """
       pass
   ```

4. **解決複雜問題**
   - LeetCode 102: Binary Tree Level Order Traversal
   - LeetCode 207: Course Schedule (拓撲排序)
   - LeetCode 994: Rotting Oranges (BFS)

## 🔗 相關概念

### 與其他數據結構的比較

| 數據結構 | 訪問順序 | 插入位置 | 刪除位置 | 主要應用 |
|----------|----------|----------|----------|----------|
| **Queue** | FIFO | 尾部 | 頭部 | 任務調度、BFS、緩衝區 |
| **Stack** | LIFO | 頂部 | 頂部 | 函數調用、表達式求值、DFS |
| **Deque** | 兩端 | 兩端 | 兩端 | 滑動窗口、回文檢查 |
| **Priority Queue** | 按優先級 | 任意 | 最高優先級 | Dijkstra、任務調度 |
| **Array** | 隨機 | 任意 | 任意 | 隨機訪問、靜態數據 |

### Queue 的變體

#### 1. 雙端佇列（Deque）
```python
from collections import deque

# Python 內建的高效雙端佇列
d = deque()
d.append(1)      # 右端添加
d.appendleft(2)  # 左端添加
d.pop()          # 右端移除
d.popleft()      # 左端移除
```

#### 2. 優先佇列（Priority Queue）
```python
import heapq

# 使用堆實作優先佇列
pq = []
heapq.heappush(pq, (1, 'task1'))  # (優先級, 任務)
heapq.heappush(pq, (3, 'task3'))
heapq.heappush(pq, (2, 'task2'))

# 總是彈出優先級最小的
priority, task = heapq.heappop(pq)  # (1, 'task1')
```

#### 3. 阻塞佇列（Blocking Queue）
```python
import queue

# 線程安全的佇列，用於多線程
q = queue.Queue(maxsize=10)

# 生產者線程
def producer():
    q.put(item)  # 如果滿了會阻塞

# 消費者線程
def consumer():
    item = q.get()  # 如果空了會阻塞
    q.task_done()
```

## 📈 學習路徑建議

### 第一階段：基礎理解（1-2 天）
1. ✅ 理解 FIFO 原則
2. ✅ 掌握基本操作概念
3. ✅ 了解應用場景
4. ✅ 學習時間複雜度

### 第二階段：基本實作（2-3 天）
1. ✅ 完成簡化列表實作
2. ✅ 通過所有測試階段
3. ✅ 實作應用函數
4. ✅ 理解常見錯誤

### 第三階段：優化實作（3-5 天）
1. 📝 實作循環陣列版本
2. 📝 實作鏈表版本
3. 📝 比較不同實作的性能
4. 📝 學習 Python collections.deque

### 第四階段：進階應用（1-2 週）
1. 📝 使用 Queue 實作 BFS
2. 📝 解決樹的層序遍歷問題
3. 📝 實作生產者-消費者模式
4. 📝 學習優先佇列

### 第五階段：實戰練習（持續）
1. 📝 LeetCode Queue 相關題目
2. 📝 系統設計中的佇列應用
3. 📝 實作消息佇列系統
4. 📝 學習分布式佇列（如 RabbitMQ）

## 🎯 檢查點

完成學習後，你應該能夠：

### 基礎知識
- ✅ 解釋 FIFO 原則和 Queue 的基本概念
- ✅ 說明 Queue 與 Stack 的區別
- ✅ 識別適合使用 Queue 的場景

### 實作能力
- ✅ 實作完整的 Queue 數據結構
- ✅ 使用不同方式實作（列表、循環陣列、鏈表）
- ✅ 處理邊界情況和錯誤

### 分析能力
- ✅ 分析 Queue 操作的時間和空間複雜度
- ✅ 比較不同實作方式的優劣
- ✅ 選擇適合的實作方式

### 應用能力
- ✅ 使用 Queue 解決實際問題
- ✅ 實作 BFS 算法
- ✅ 實作任務調度系統
- ✅ 理解生產者-消費者模式

## 🌟 Queue 在面試中的重要性

### 常見面試題型

1. **基礎實作題**
   - 實作 Queue 的各種操作
   - 用 Stack 實作 Queue
   - 用 Queue 實作 Stack

2. **BFS 相關題**
   - 樹的層序遍歷
   - 圖的最短路徑
   - 連通分量

3. **滑動窗口題**
   - 滑動窗口最大值
   - 滑動窗口平均值

4. **系統設計題**
   - 設計任務調度器
   - 設計打印機佇列
   - 設計消息佇列

### 面試準備建議

1. **熟練基本操作**
   - 能快速實作 Queue
   - 理解各種實作方式
   - 掌握時間複雜度

2. **掌握 BFS**
   - Queue 是 BFS 的核心
   - 練習各種 BFS 變體
   - 理解何時使用 BFS

3. **了解實際應用**
   - 任務調度
   - 消息傳遞
   - 緩衝區管理

4. **練習相關題目**
   - LeetCode Queue tag 題目
   - 系統設計中的佇列應用

## 📚 延伸閱讀

### 推薦資源
- 《算法導論》- Queue 章節
- 《數據結構與算法分析》
- Python collections.deque 文檔
- LeetCode Queue 專題

### 相關主題
- **Deque（雙端佇列）** - 兩端都可操作
- **Priority Queue（優先佇列）** - 按優先級處理
- **Circular Queue（循環佇列）** - 空間優化
- **Blocking Queue（阻塞佇列）** - 多線程同步

### 實戰項目建議
1. 實作簡單的任務調度器
2. 實作網頁瀏覽器歷史管理
3. 實作 BFS 可視化工具
4. 實作消息佇列系統

---

## 🎊 總結

Queue 是一種簡單但強大的數據結構：

- **核心原則**: FIFO (First In, First Out)
- **主要操作**: enqueue, dequeue, front
- **時間複雜度**: 理想情況下都是 O(1)
- **典型應用**: BFS、任務調度、緩衝區管理

掌握 Queue 是學習更複雜算法和數據結構的基礎。通過系統的學習和練習，你將能夠：
1. 靈活運用 Queue 解決問題
2. 在面試中自信地處理相關題目
3. 在實際項目中正確使用 Queue
4. 理解更高級的數據結構變體

**繼續加油！** Queue 是通往更複雜算法的重要基石。完成這個學習包後，你已經具備了堅實的 Queue 知識基礎，可以挑戰更多進階主題了！
