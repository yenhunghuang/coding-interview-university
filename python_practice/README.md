# Python Practice for Coding Interview University

這是用於 Coding Interview University 的 Python 實作練習目錄。

## 環境設置

### 啟動虛擬環境
```bash
source coding-interview-env/bin/activate  # Linux/Mac
# 或
coding-interview-env\Scripts\activate     # Windows
```

### 安裝依賴套件
```bash
pip install -r requirements.txt
```

### 停用虛擬環境
```bash
deactivate
```

## 目錄結構

```
python-practice/
├── data-structures/        # 數據結構實作
│   ├── arrays/            # 陣列
│   ├── linked-lists/      # 鏈表
│   ├── stacks/            # 堆疊
│   ├── queues/            # 佇列
│   ├── hash-tables/       # 雜湊表
│   ├── trees/             # 樹
│   ├── graphs/            # 圖
│   └── heaps/             # 堆積
├── algorithms/             # 演算法實作
│   ├── sorting/           # 排序演算法
│   ├── searching/         # 搜尋演算法
│   ├── dynamic-programming/ # 動態規劃
│   ├── recursion/         # 遞迴
│   └── graph-algorithms/  # 圖演算法
├── tests/                 # 測試檔案
├── utils/                 # 輔助工具
└── coding-interview-env/  # 虛擬環境 (已忽略)
```

## 運行測試

### 運行所有測試
```bash
pytest
```

### 運行特定測試檔案
```bash
pytest tests/test_arrays.py
```

### 運行測試並顯示覆蓋率
```bash
pytest --cov=data-structures --cov=algorithms
```

## 程式碼風格

### 格式化程式碼
```bash
black .
```

### 程式碼檢查
```bash
flake8
```

### 型別檢查
```bash
mypy data-structures/ algorithms/
```

## 學習順序建議

1. **基礎數據結構**
   - Arrays (陣列)
   - Linked Lists (鏈表)
   - Stacks (堆疊)
   - Queues (佇列)

2. **進階數據結構**
   - Hash Tables (雜湊表)
   - Trees (樹)
   - Heaps (堆積)
   - Graphs (圖)

3. **基礎演算法**
   - Sorting (排序)
   - Searching (搜尋)
   - Recursion (遞迴)

4. **進階演算法**
   - Dynamic Programming (動態規劃)
   - Graph Algorithms (圖演算法)

## 實作指導原則

1. **從零開始實作**：不使用內建的數據結構，自己實作基本功能
2. **寫測試**：每個實作都要有對應的測試案例
3. **時間複雜度分析**：在註解中說明時間和空間複雜度
4. **多種實作方式**：如果有多種實作方法，都要嘗試

## 參考資源

- [Python Cheat Sheet](../extras/cheat%20sheets/python-cheat-sheet-v1.pdf)
- [Coding Interview Python Language Essentials](../extras/cheat%20sheets/Coding%20Interview%20Python%20Language%20Essentials.pdf)
- [作者的 Python 練習 Repository](https://github.com/jwasham/practice-python)

## 進度追蹤

在主要的 README.md 中標記完成的項目，使用 `[x]` 來表示已完成。