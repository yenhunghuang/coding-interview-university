# Stack (堆疊) 學習指南

## 📚 什麼是 Stack？

Stack（堆疊）是一種線性數據結構，遵循 **LIFO (Last In, First Out)** 原則，即「後進先出」。

### 生活中的比喻
想像一疊盤子：
- 你只能從頂部取盤子
- 你只能往頂部放盤子
- 最後放上去的盤子，會是第一個被取走的

這就是 Stack 的運作方式！

## 🎯 核心概念

### LIFO 原則
```
Push 操作：    Pop 操作：
   ↓             ↑
[  3  ] ← top   [  3  ] ← 被移除
[  2  ]         [  2  ] ← 新的 top
[  1  ]         [  1  ]
```

### 主要操作

| 操作 | 描述 | 時間複雜度 |
|------|------|------------|
| `push(item)` | 將元素推入堆疊頂部 | O(1) |
| `pop()` | 移除並返回頂部元素 | O(1) |
| `peek()/top()` | 查看頂部元素但不移除 | O(1) |
| `is_empty()` | 檢查是否為空 | O(1) |
| `size()` | 獲取元素數量 | O(1) |

## 🛠️ 實作方式

### 1. 使用陣列/列表實作
```python
class Stack:
    def __init__(self):
        self._data = []  # 列表末尾作為堆疊頂部

    def push(self, item):
        self._data.append(item)  # O(1)

    def pop(self):
        return self._data.pop()  # O(1)
```

**優點：**
- 實作簡單
- 記憶體效率高
- 所有操作都是 O(1)

**缺點：**
- 需要預分配空間（或動態調整）
- 可能有容量限制

### 2. 使用鏈表實作
```python
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    def __init__(self):
        self._head = None  # 鏈表頭作為堆疊頂部

    def push(self, item):
        self._head = Node(item, self._head)  # O(1)

    def pop(self):
        data = self._head.data
        self._head = self._head.next  # O(1)
        return data
```

**優點：**
- 動態大小
- 不需要預分配空間

**缺點：**
- 每個元素需要額外的指標空間
- 快取局部性較差

## 🌟 實際應用

### 1. 函數調用堆疊 (Call Stack)
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 調用 factorial(3) 時的堆疊狀態：
# factorial(3) ← 當前執行
# factorial(2)
# factorial(1)
```

### 2. 括號匹配檢查
```python
def check_brackets(expression):
    stack = Stack()
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in pairs:  # 開括號
            stack.push(char)
        elif char in pairs.values():  # 閉括號
            if stack.is_empty() or pairs[stack.pop()] != char:
                return False

    return stack.is_empty()

# 例子：
check_brackets("([{}])")  # True
check_brackets("([)]")    # False
```

### 3. 表達式求值
```python
# 中綴轉後綴 (Infix to Postfix)
# 中綴: 3 + 4 * 2
# 後綴: 3 4 2 * +

def evaluate_postfix(expression):
    stack = Stack()

    for token in expression.split():
        if token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            result = apply_operator(a, b, token)
            stack.push(result)
        else:
            stack.push(float(token))

    return stack.pop()
```

### 4. 瀏覽器歷史記錄
```python
class BrowserHistory:
    def __init__(self):
        self.back_stack = Stack()    # 後退歷史
        self.forward_stack = Stack() # 前進歷史
        self.current_page = None

    def visit(self, url):
        if self.current_page:
            self.back_stack.push(self.current_page)
        self.current_page = url
        self.forward_stack.clear()  # 清除前進歷史

    def back(self):
        if not self.back_stack.is_empty():
            self.forward_stack.push(self.current_page)
            self.current_page = self.back_stack.pop()

    def forward(self):
        if not self.forward_stack.is_empty():
            self.back_stack.push(self.current_page)
            self.current_page = self.forward_stack.pop()
```

### 5. 撤銷/重做功能
```python
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def type(self, content):
        self.undo_stack.push(self.text)  # 保存當前狀態
        self.text += content
        self.redo_stack.clear()  # 清除重做歷史

    def undo(self):
        if not self.undo_stack.is_empty():
            self.redo_stack.push(self.text)
            self.text = self.undo_stack.pop()

    def redo(self):
        if not self.redo_stack.is_empty():
            self.undo_stack.push(self.text)
            self.text = self.redo_stack.pop()
```

## 🧪 TDD 學習過程

我們的實作採用測試驅動開發（TDD）方法：

### 階段 1: 基礎結構
- 測試初始化和基本查詢方法
- 文件：`test_stage1.py`

### 階段 2: 基本操作
- 測試 push 和 peek/top 操作
- 文件：`test_stage2.py`

### 階段 3: 移除操作
- 測試 pop 操作和完整 LIFO 行為
- 文件：`test_stage3.py`

### 階段 4: 容量管理
- 測試有限容量和溢出處理
- 文件：`test_stage4.py`

### 階段 5: 輔助功能
- 測試 clear 和字串表示
- 文件：`test_stage5.py`

### 最終階段: 完整驗證
- 綜合測試和實際應用驗證
- 文件：`test_stage_final.py`

## 📊 複雜度分析

### 時間複雜度
- **Push**: O(1) - 直接在頂部添加
- **Pop**: O(1) - 直接從頂部移除
- **Peek**: O(1) - 直接訪問頂部
- **Is_empty**: O(1) - 檢查大小
- **Size**: O(1) - 維護計數器

### 空間複雜度
- **整體**: O(n) - n 是堆疊中元素的數量
- **每個操作**: O(1) - 不需要額外空間

## 🚫 常見錯誤

### 1. 空堆疊操作
```python
stack = Stack()
# 錯誤：嘗試從空堆疊 pop
try:
    stack.pop()  # 會拋出 IndexError
except IndexError:
    print("堆疊為空！")
```

### 2. 混淆 peek 和 pop
```python
stack = Stack()
stack.push(1)
stack.push(2)

# peek 不會移除元素
top = stack.peek()  # top = 2, 堆疊仍有 [1, 2]

# pop 會移除元素
top = stack.pop()   # top = 2, 堆疊現在是 [1]
```

### 3. 容量溢出
```python
stack = Stack(max_size=2)
stack.push(1)
stack.push(2)

# 錯誤：超過容量限制
try:
    stack.push(3)  # 會拋出 OverflowError
except OverflowError:
    print("堆疊已滿！")
```

## 🎓 練習題

### 初級
1. 使用堆疊反轉字串
2. 檢查括號是否平衡
3. 實作最小堆疊（能 O(1) 時間取得最小值）

### 中級
1. 計算後綴表達式
2. 中綴表達式轉後綴表達式
3. 實作瀏覽器歷史功能

### 高級
1. 實作具有 getMin() 功能的堆疊
2. 用兩個堆疊實作隊列
3. 設計能進行 push、pop、top 和 getMin 的堆疊，所有操作都要 O(1)

## 🔗 相關概念

### 與其他數據結構的比較

| 數據結構 | 訪問順序 | 插入位置 | 刪除位置 | 應用場景 |
|----------|----------|----------|----------|----------|
| Stack | LIFO | 頂部 | 頂部 | 函數調用、表達式求值 |
| Queue | FIFO | 尾部 | 頭部 | 任務調度、廣度優先搜尋 |
| Array | 隨機存取 | 任意 | 任意 | 隨機訪問、數學運算 |
| Linked List | 順序存取 | 任意 | 任意 | 動態插入刪除 |

### 變體
- **動態堆疊**: 大小可以動態調整
- **靜態堆疊**: 固定大小
- **最小堆疊**: 支援 O(1) 取得最小值
- **雙端堆疊**: 兩端都可以操作

## 📈 學習路徑建議

1. **理解概念** - 掌握 LIFO 原則
2. **基本實作** - 完成基本的 Stack 類別
3. **測試驗證** - 通過所有階段測試
4. **實際應用** - 解決括號匹配等問題
5. **進階練習** - 挑戰複雜的 Stack 相關算法
6. **效能優化** - 分析和優化實作

## 🎯 檢查點

完成學習後，你應該能夠：

- ✅ 解釋 LIFO 原則和 Stack 的基本概念
- ✅ 實作完整的 Stack 數據結構
- ✅ 分析 Stack 操作的時間和空間複雜度
- ✅ 使用 Stack 解決實際問題
- ✅ 識別適合使用 Stack 的場景
- ✅ 處理 Stack 相關的錯誤情況

繼續加油！Stack 是很多高級算法和數據結構的基礎。掌握了 Stack，你就為學習更複雜的概念打下了堅實的基礎。