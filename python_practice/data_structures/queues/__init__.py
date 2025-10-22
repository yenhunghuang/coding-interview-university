"""
Queue (佇列) 數據結構實作

這個模組提供 Queue 數據結構的完整實作，包括：
- Queue 類別：遵循 FIFO (First In, First Out) 原則的佇列實作
- 實際應用函數：燙手山芋遊戲、二進位數字生成、樹的層序遍歷

主要特性：
- 完整的 FIFO 操作支援
- 容量限制和溢出處理
- 清晰的錯誤訊息
- 豐富的實際應用範例

使用方式：
    from queues import Queue

    # 創建無限制容量的佇列
    queue = Queue()

    # 創建有容量限制的佇列
    limited_queue = Queue(max_size=10)

    # 基本操作
    queue.enqueue(1)
    queue.enqueue(2)
    item = queue.dequeue()  # 返回 1 (FIFO)
    front = queue.front()   # 查看前端但不移除

學習資源：
- QUEUE_LEARNING_GUIDE.md - 完整學習指南（繁體中文）
- queue.py - Queue 類別實作
- test_stage*.py - 階段性測試文件

測試驅動開發（TDD）階段：
1. test_stage1.py - 基礎結構測試
2. test_stage2.py - 入隊操作測試
3. test_stage3.py - 出隊操作測試
4. test_stage4.py - 完整 FIFO 行為驗證
5. test_stage5.py - 輔助功能和邊界情況測試
6. test_stage_final.py - 最終綜合測試

開始學習：
    python3 test_stage1.py
"""

from .queue import Queue, hot_potato, generate_binary_numbers, level_order_traversal

__all__ = [
    'Queue',
    'hot_potato',
    'generate_binary_numbers',
    'level_order_traversal',
]

__version__ = '1.0.0'
__author__ = 'Coding Interview University'
__description__ = 'Queue (佇列) 數據結構實作 - FIFO 原則學習包'
