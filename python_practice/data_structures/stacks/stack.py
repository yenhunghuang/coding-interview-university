#!/usr/bin/env python3
"""
Stack 數據結構實作 - 堆疊 (LIFO: Last In, First Out)

堆疊是一種線性數據結構，遵循後進先出（LIFO）原則。
就像一疊盤子，你只能從頂部取出盤子，也只能往頂部放盤子。

主要操作：
- push(item): 將元素推入堆疊頂部
- pop(): 移除並返回堆疊頂部元素
- peek()/top(): 查看堆疊頂部元素但不移除
- is_empty(): 檢查堆疊是否為空
- size(): 獲取堆疊中元素的數量
- is_full(): 檢查堆疊是否已滿（對有容量限制的堆疊）
- clear(): 清空堆疊

時間複雜度：
- push(): O(1)
- pop(): O(1)
- peek()/top(): O(1)
- is_empty(): O(1)
- size(): O(1)
- is_full(): O(1)
- clear(): O(1)

空間複雜度：O(n)，其中 n 是堆疊中元素的數量
"""


class Stack:
    """
    堆疊數據結構實作

    使用 Python 列表作為底層存儲結構。
    列表的末尾作為堆疊的頂部，這樣 append 和 pop 操作都是 O(1)。

    實作提示：
    - 使用 self._data = [] 來存儲元素
    - 使用 self._max_size 來記錄容量限制
    - 列表的 append() 和 pop() 方法可以實現 O(1) 的堆疊操作
    """

    def __init__(self, max_size=None):
        """
        初始化堆疊

        Args:
            max_size (int, optional): 堆疊的最大容量。None 表示無限制。
                                    必須是正整數。

        Raises:
            ValueError: 當 max_size 不是正整數時

        Examples:
            >>> stack = Stack()           # 無容量限制的堆疊
            >>> stack = Stack(10)         # 最大容量為 10 的堆疊

        實作提示：
        - 檢查 max_size 是否為正整數（如果不是 None）
        - 初始化內部數據結構
        """
        # TODO: 在這裡實作初始化邏輯
        raise NotImplementedError("請實作 __init__ 方法")

    def push(self, item):
        """
        將元素推入堆疊頂部

        Args:
            item: 要推入的元素（可以是任何類型）

        Raises:
            OverflowError: 當堆疊已滿時（僅限有容量限制的堆疊）

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push("hello")
            >>> stack.push([1, 2, 3])

        實作提示：
        - 先檢查容量限制
        - 使用列表的 append() 方法
        """
        # TODO: 在這裡實作 push 邏輯
        raise NotImplementedError("請實作 push 方法")

    def pop(self):
        """
        移除並返回堆疊頂部元素

        Returns:
            堆疊頂部的元素

        Raises:
            IndexError: 當堆疊為空時

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.pop()  # 返回 2
            2
            >>> stack.pop()  # 返回 1
            1

        實作提示：
        - 先檢查堆疊是否為空
        - 使用列表的 pop() 方法
        """
        # TODO: 在這裡實作 pop 邏輯
        raise NotImplementedError("請實作 pop 方法")

    def peek(self):
        """
        查看堆疊頂部元素但不移除

        Returns:
            堆疊頂部的元素

        Raises:
            IndexError: 當堆疊為空時

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.peek()  # 返回 2，但不移除
            2
            >>> stack.size()  # 大小仍然是 2
            2

        實作提示：
        - 先檢查堆疊是否為空
        - 返回列表的最後一個元素（索引 -1）
        """
        # TODO: 在這裡實作 peek 邏輯
        raise NotImplementedError("請實作 peek 方法")

    def top(self):
        """
        peek() 的別名方法，查看堆疊頂部元素但不移除

        Returns:
            堆疊頂部的元素

        Raises:
            IndexError: 當堆疊為空時

        Note:
            這是一個常見的別名方法，許多堆疊實作都提供這個方法

        實作提示：
        - 直接調用 peek() 方法
        """
        # TODO: 在這裡實作 top 邏輯
        raise NotImplementedError("請實作 top 方法")

    def is_empty(self):
        """
        檢查堆疊是否為空

        Returns:
            bool: True 如果堆疊為空，False 否則

        Examples:
            >>> stack = Stack()
            >>> stack.is_empty()
            True
            >>> stack.push(1)
            >>> stack.is_empty()
            False

        實作提示：
        - 檢查內部列表的長度
        """
        # TODO: 在這裡實作 is_empty 邏輯
        raise NotImplementedError("請實作 is_empty 方法")

    def is_full(self):
        """
        檢查堆疊是否已滿

        Returns:
            bool: True 如果堆疊已滿，False 否則
                 對於無容量限制的堆疊，始終返回 False

        Examples:
            >>> stack = Stack(2)
            >>> stack.is_full()
            False
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.is_full()
            True

        實作提示：
        - 如果沒有容量限制，返回 False
        - 否則比較當前大小和最大容量
        """
        # TODO: 在這裡實作 is_full 邏輯
        raise NotImplementedError("請實作 is_full 方法")

    def size(self):
        """
        獲取堆疊中元素的數量

        Returns:
            int: 堆疊中元素的數量

        Examples:
            >>> stack = Stack()
            >>> stack.size()
            0
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.size()
            2

        實作提示：
        - 返回內部列表的長度
        """
        # TODO: 在這裡實作 size 邏輯
        raise NotImplementedError("請實作 size 方法")

    def clear(self):
        """
        清空堆疊，移除所有元素

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.size()
            2
            >>> stack.clear()
            >>> stack.size()
            0
            >>> stack.is_empty()
            True

        實作提示：
        - 使用列表的 clear() 方法
        """
        # TODO: 在這裡實作 clear 邏輯
        raise NotImplementedError("請實作 clear 方法")

    def __str__(self):
        """
        返回堆疊的字串表示

        Returns:
            str: 堆疊的字串表示，頂部元素在右側

        Examples:
            >>> stack = Stack()
            >>> str(stack)
            'Stack: []'
            >>> stack.push(1)
            >>> stack.push(2)
            >>> str(stack)
            'Stack: [1, 2] <- top'

        實作提示：
        - 空堆疊顯示 "Stack: []"
        - 有元素時顯示 "Stack: [元素列表] <- top"
        """
        # TODO: 在這裡實作 __str__ 邏輯
        raise NotImplementedError("請實作 __str__ 方法")

    def __repr__(self):
        """
        返回堆疊的詳細表示，用於調試

        Returns:
            str: 堆疊的詳細表示，包括容量信息

        Examples:
            >>> stack = Stack(5)
            >>> stack.push(1)
            >>> repr(stack)
            'Stack(size=1, max_size=5, data=[1])'

        實作提示：
        - 顯示大小、最大容量和數據
        - 這個方法是選擇性的，可以最後實作
        """
        # TODO: 在這裡實作 __repr__ 邏輯（選擇性）
        raise NotImplementedError("請實作 __repr__ 方法")

    @property
    def max_size(self):
        """
        獲取堆疊的最大容量

        Returns:
            int or None: 最大容量，None 表示無限制

        實作提示：
        - 這是一個屬性方法，返回 self._max_size
        """
        # TODO: 在這裡實作 max_size 屬性
        raise NotImplementedError("請實作 max_size 屬性")


# 實際應用示例函數 - 這些是進階練習，可以在完成基本 Stack 後實作
def check_balanced_parentheses(expression):
    """
    使用堆疊檢查括號是否平衡

    這是堆疊的經典應用之一。

    Args:
        expression (str): 要檢查的表達式

    Returns:
        bool: True 如果括號平衡，False 否則

    Examples:
        >>> check_balanced_parentheses("()")
        True
        >>> check_balanced_parentheses("([{}])")
        True
        >>> check_balanced_parentheses("([)]")
        False

    實作提示：
    - 建立一個 Stack 實例
    - 建立開閉括號的對應字典 {'(': ')', '[': ']', '{': '}'}
    - 遇到開括號時 push 到堆疊
    - 遇到閉括號時檢查是否匹配堆疊頂部的開括號
    - 最後檢查堆疊是否為空
    """
    # TODO: 在這裡實作括號檢查邏輯
    raise NotImplementedError("請實作 check_balanced_parentheses 函數")


def evaluate_postfix(expression):
    """
    使用堆疊計算後綴表達式

    這是堆疊在計算器實作中的經典應用。

    Args:
        expression (str): 後綴表達式，用空格分隔

    Returns:
        float: 計算結果

    Examples:
        >>> evaluate_postfix("3 4 +")
        7.0
        >>> evaluate_postfix("15 7 1 1 + - / 3 * 2 1 1 + + -")
        5.0

    實作提示：
    - 建立一個 Stack 實例
    - 分割表達式為 token 列表
    - 遇到數字時 push 到堆疊
    - 遇到運算符時 pop 兩個數字進行運算，然後 push 結果
    - 注意：先 pop 的是右操作數
    """
    # TODO: 在這裡實作後綴表達式計算邏輯
    raise NotImplementedError("請實作 evaluate_postfix 函數")


def reverse_string(s):
    """
    使用堆疊反轉字串

    演示堆疊如何自然地反轉順序。

    Args:
        s (str): 要反轉的字串

    Returns:
        str: 反轉後的字串

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Stack")
        'kcatS'

    實作提示：
    - 建立一個 Stack 實例
    - 將字串的每個字符 push 到堆疊
    - 從堆疊中 pop 所有字符並組合成新字串
    """
    # TODO: 在這裡實作字串反轉邏輯
    raise NotImplementedError("請實作 reverse_string 函數")


if __name__ == "__main__":
    # 這個部分會在你完成實作後可以執行
    print("=== Stack 實作練習 ===")
    print("請先完成 Stack 類別的實作，然後運行測試：")
    print("python3 test_stage1.py")
    print("\n當所有測試通過後，你可以嘗試實作下面的應用示例：")
    print("- check_balanced_parentheses(): 括號匹配檢查")
    print("- evaluate_postfix(): 後綴表達式計算")
    print("- reverse_string(): 字串反轉")

    # 這些示例代碼在你實作完成後可以取消註解測試：
    """
    # 基本操作示例
    stack = Stack()
    print(f"空堆疊: {stack}")

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"推入 1, 2, 3: {stack}")

    print(f"peek(): {stack.peek()}")
    print(f"pop(): {stack.pop()}")
    print(f"現在的堆疊: {stack}")

    # 實際應用示例
    expressions = ["()", "([{}])", "([)]", "((()))", "())"]
    for expr in expressions:
        result = check_balanced_parentheses(expr)
        print(f"'{expr}' 括號平衡: {result}")

    postfix_expr = "3 4 + 2 *"  # (3 + 4) * 2 = 14
    result = evaluate_postfix(postfix_expr)
    print(f"後綴表達式 '{postfix_expr}' = {result}")

    original = "Hello, Stack!"
    reversed_str = reverse_string(original)
    print(f"'{original}' 反轉為 '{reversed_str}'")
    """