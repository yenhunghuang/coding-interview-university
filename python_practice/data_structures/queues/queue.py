#!/usr/bin/env python3
"""
Queue 數據結構實作 - 佇列 (FIFO: First In, First Out)

佇列是一種線性數據結構，遵循先進先出（FIFO）原則。
就像排隊等候，先到的人先被服務，後到的人在後面等。

主要操作：
- enqueue(item): 將元素加入佇列尾部（入隊）
- dequeue(): 移除並返回佇列前端元素（出隊）
- front(): 查看佇列前端元素但不移除
- is_empty(): 檢查佇列是否為空
- size(): 獲取佇列中元素的數量
- is_full(): 檢查佇列是否已滿（對有容量限制的佇列）
- clear(): 清空佇列

時間複雜度：
- enqueue(): O(1)
- dequeue(): O(1)
- front(): O(1)
- is_empty(): O(1)
- size(): O(1)
- is_full(): O(1)
- clear(): O(1)

空間複雜度：O(n)，其中 n 是佇列中元素的數量
"""


class Queue:
    """
    佇列數據結構實作

    使用 Python 列表作為底層存儲結構。
    列表的末尾作為佇列的尾部（rear），列表的開頭作為佇列的前端（front）。

    實作提示：
    - 使用 self._data = [] 來存儲元素
    - 使用 self._max_size 來記錄容量限制
    - enqueue 使用列表的 append() 方法在尾部添加
    - dequeue 使用列表的 pop(0) 方法從前端移除

    注意：pop(0) 是 O(n) 操作，但為了教學簡單性，我們先使用這種方式。
    進階實作可以使用循環陣列或雙端佇列來達到真正的 O(1) dequeue。
    """

    def __init__(self, max_size=None):
        """
        初始化佇列

        Args:
            max_size (int, optional): 佇列的最大容量。None 表示無限制。
                                    必須是正整數。

        Raises:
            ValueError: 當 max_size 不是正整數時

        Examples:
            >>> queue = Queue()           # 無容量限制的佇列
            >>> queue = Queue(10)         # 最大容量為 10 的佇列

        實作提示：
        - 檢查 max_size 是否為正整數（如果不是 None）
        - 初始化內部數據結構
        """
        # TODO: 在這裡實作初始化邏輯
        raise NotImplementedError("請實作 __init__ 方法")

    def enqueue(self, item):
        """
        將元素加入佇列尾部（入隊）

        Args:
            item: 要加入的元素（可以是任何類型）

        Raises:
            OverflowError: 當佇列已滿時（僅限有容量限制的佇列）

        Examples:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue("hello")
            >>> queue.enqueue([1, 2, 3])

        實作提示：
        - 先檢查容量限制
        - 使用列表的 append() 方法在尾部添加
        - 這是 O(1) 操作
        """
        # TODO: 在這裡實作 enqueue 邏輯
        raise NotImplementedError("請實作 enqueue 方法")

    def dequeue(self):
        """
        移除並返回佇列前端元素（出隊）

        Returns:
            佇列前端的元素

        Raises:
            IndexError: 當佇列為空時

        Examples:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.dequeue()  # 返回 1（先進先出）
            1
            >>> queue.dequeue()  # 返回 2
            2

        實作提示：
        - 先檢查佇列是否為空
        - 使用列表的 pop(0) 方法從前端移除
        - 注意：pop(0) 是 O(n) 操作（簡化版實作）
        """
        # TODO: 在這裡實作 dequeue 邏輯
        raise NotImplementedError("請實作 dequeue 方法")

    def front(self):
        """
        查看佇列前端元素但不移除

        Returns:
            佇列前端的元素

        Raises:
            IndexError: 當佇列為空時

        Examples:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.front()  # 返回 1，但不移除
            1
            >>> queue.size()  # 大小仍然是 2
            2

        實作提示：
        - 先檢查佇列是否為空
        - 返回列表的第一個元素（索引 0）
        - 不要修改佇列內容
        """
        # TODO: 在這裡實作 front 邏輯
        raise NotImplementedError("請實作 front 方法")

    def is_empty(self):
        """
        檢查佇列是否為空

        Returns:
            bool: True 如果佇列為空，False 否則

        Examples:
            >>> queue = Queue()
            >>> queue.is_empty()
            True
            >>> queue.enqueue(1)
            >>> queue.is_empty()
            False

        實作提示：
        - 檢查內部列表的長度
        """
        # TODO: 在這裡實作 is_empty 邏輯
        raise NotImplementedError("請實作 is_empty 方法")

    def is_full(self):
        """
        檢查佇列是否已滿

        Returns:
            bool: True 如果佇列已滿，False 否則
                 對於無容量限制的佇列，始終返回 False

        Examples:
            >>> queue = Queue(2)
            >>> queue.is_full()
            False
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.is_full()
            True

        實作提示：
        - 如果沒有容量限制，返回 False
        - 否則比較當前大小和最大容量
        """
        # TODO: 在這裡實作 is_full 邏輯
        raise NotImplementedError("請實作 is_full 方法")

    def size(self):
        """
        獲取佇列中元素的數量

        Returns:
            int: 佇列中元素的數量

        Examples:
            >>> queue = Queue()
            >>> queue.size()
            0
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.size()
            2

        實作提示：
        - 返回內部列表的長度
        """
        # TODO: 在這裡實作 size 邏輯
        raise NotImplementedError("請實作 size 方法")

    def clear(self):
        """
        清空佇列，移除所有元素

        Examples:
            >>> queue = Queue()
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> queue.size()
            2
            >>> queue.clear()
            >>> queue.size()
            0
            >>> queue.is_empty()
            True

        實作提示：
        - 使用列表的 clear() 方法
        - 或者重新初始化為空列表
        """
        # TODO: 在這裡實作 clear 邏輯
        raise NotImplementedError("請實作 clear 方法")

    def __str__(self):
        """
        返回佇列的字串表示

        Returns:
            str: 佇列的字串表示，前端元素在左側

        Examples:
            >>> queue = Queue()
            >>> str(queue)
            'Queue: []'
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> str(queue)
            'Queue: front -> [1, 2] <- rear'

        實作提示：
        - 空佇列顯示 "Queue: []"
        - 有元素時顯示 "Queue: front -> [元素列表] <- rear"
        - 清楚標示前端和尾部
        """
        # TODO: 在這裡實作 __str__ 邏輯
        raise NotImplementedError("請實作 __str__ 方法")

    def __repr__(self):
        """
        返回佇列的詳細表示，用於調試

        Returns:
            str: 佇列的詳細表示，包括容量信息

        Examples:
            >>> queue = Queue(5)
            >>> queue.enqueue(1)
            >>> repr(queue)
            'Queue(size=1, max_size=5, data=[1])'

        實作提示：
        - 顯示大小、最大容量和數據
        - 這個方法是選擇性的，可以最後實作
        """
        # TODO: 在這裡實作 __repr__ 邏輯（選擇性）
        raise NotImplementedError("請實作 __repr__ 方法")

    @property
    def max_size(self):
        """
        獲取佇列的最大容量

        Returns:
            int or None: 最大容量，None 表示無限制

        實作提示：
        - 這是一個屬性方法，返回 self._max_size
        """
        # TODO: 在這裡實作 max_size 屬性
        raise NotImplementedError("請實作 max_size 屬性")


# 實際應用示例函數 - 這些是進階練習，可以在完成基本 Queue 後實作
def hot_potato(names, num):
    """
    使用佇列模擬燙手山芋遊戲

    這是佇列的經典應用之一。遊戲規則：
    - 一群人圍成圈傳遞「燙手山芋」
    - 傳遞 num 次後，持有者出局
    - 繼續遊戲直到只剩一人

    Args:
        names (list): 參與者名單
        num (int): 每輪傳遞次數

    Returns:
        str: 獲勝者的名字

    Examples:
        >>> hot_potato(["Alice", "Bob", "Carol", "David"], 7)
        'Carol'

    實作提示：
    - 建立一個 Queue 實例並將所有名字加入
    - 重複 num 次：dequeue 後立即 enqueue（模擬傳遞）
    - num 次後，dequeue 的人出局
    - 繼續直到佇列只剩一人
    """
    # TODO: 在這裡實作燙手山芋遊戲邏輯
    raise NotImplementedError("請實作 hot_potato 函數")


def generate_binary_numbers(n):
    """
    使用佇列生成 1 到 n 的二進位表示

    這展示了佇列在數字生成算法中的應用。

    Args:
        n (int): 要生成的數字範圍（1 到 n）

    Returns:
        list: 包含 1 到 n 的二進位字串列表

    Examples:
        >>> generate_binary_numbers(5)
        ['1', '10', '11', '100', '101']
        >>> generate_binary_numbers(10)
        ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010']

    實作提示：
    - 建立一個 Queue，先加入 "1"
    - 對於每個數字：
      1. dequeue 得到當前二進位數
      2. 將它加上 "0" 和 "1" 後分別 enqueue
    - 重複直到生成 n 個數字
    """
    # TODO: 在這裡實作二進位數字生成邏輯
    raise NotImplementedError("請實作 generate_binary_numbers 函數")


def level_order_traversal(tree_root):
    """
    使用佇列進行樹的層序遍歷（Level-Order Traversal）

    這是佇列在樹結構遍歷中的經典應用（BFS）。

    Args:
        tree_root: 樹的根節點（假設節點有 value, left, right 屬性）

    Returns:
        list: 層序遍歷的節點值列表

    Examples:
        樹結構：
              1
            /   \
           2     3
          / \   / \
         4   5 6   7

        >>> level_order_traversal(root)
        [1, 2, 3, 4, 5, 6, 7]

    實作提示：
    - 建立一個 Queue，先加入根節點
    - 當佇列不為空時：
      1. dequeue 一個節點
      2. 記錄它的值
      3. 將它的左右子節點 enqueue（如果存在）
    - 這就是廣度優先搜尋（BFS）
    """
    # TODO: 在這裡實作層序遍歷邏輯
    raise NotImplementedError("請實作 level_order_traversal 函數")


if __name__ == "__main__":
    # 這個部分會在你完成實作後可以執行
    print("=== Queue 實作練習 ===")
    print("請先完成 Queue 類別的實作，然後運行測試：")
    print("python3 test_stage1.py")
    print("\n當所有測試通過後，你可以嘗試實作下面的應用示例：")
    print("- hot_potato(): 燙手山芋遊戲模擬")
    print("- generate_binary_numbers(): 生成二進位數字")
    print("- level_order_traversal(): 樹的層序遍歷（BFS）")

    # 這些示例代碼在你實作完成後可以取消註解測試：
    """
    # 基本操作示例
    queue = Queue()
    print(f"空佇列: {queue}")

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"加入 1, 2, 3: {queue}")

    print(f"front(): {queue.front()}")
    print(f"dequeue(): {queue.dequeue()}")
    print(f"現在的佇列: {queue}")

    # 實際應用示例
    print("\n燙手山芋遊戲：")
    winner = hot_potato(["Alice", "Bob", "Carol", "David", "Eve"], 7)
    print(f"獲勝者: {winner}")

    print("\n生成二進位數字：")
    binary_numbers = generate_binary_numbers(10)
    print(f"1 到 10 的二進位: {binary_numbers}")

    # 層序遍歷需要先定義樹節點類別
    """
