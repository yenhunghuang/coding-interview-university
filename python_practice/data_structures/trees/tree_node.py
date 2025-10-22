"""
TreeNode - 樹節點類別
用於建立二元搜尋樹的節點
"""


class TreeNode:
    """
    二元樹節點類別

    屬性:
        value: 節點儲存的值
        left: 左子節點
        right: 右子節點
    """

    def __init__(self, value):
        """
        初始化樹節點

        參數:
            value: 節點要儲存的值
        """
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        """返回節點的字串表示"""
        return f"TreeNode({self.value})"

    def __str__(self):
        """返回節點的字串表示"""
        return str(self.value)
