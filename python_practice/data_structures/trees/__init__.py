"""
Trees Module - 樹狀資料結構模組

這個模組包含二元搜尋樹（Binary Search Tree）的完整實作和學習資源。

主要類別：
    - TreeNode: 樹節點類別
    - BinarySearchTree: 二元搜尋樹類別

使用方式：
    from trees import BinarySearchTree

    # 創建 BST
    bst = BinarySearchTree()

    # 插入值
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)

    # 搜尋
    node = bst.search(5)

    # 遍歷
    print(bst.inorder_traversal())  # [5, 10, 15]

學習資源：
    - 閱讀 TREE_LEARNING_GUIDE.md 獲取詳細的學習指南
    - 按順序執行測試檔案：test_stage1.py 到 test_stage_final.py

測試階段：
    Stage 1: 節點創建和基本結構
    Stage 2: 插入操作
    Stage 3: 搜尋操作
    Stage 4: 遍歷操作（中序、前序、後序）
    Stage 5: 最小值、最大值和高度
    Stage 6: 刪除操作
    Stage 7: 層序遍歷
    Stage 8: 複雜操作和邊界情況
    Final: 整合測試和實際應用

作者: Claude
版本: 1.0.0
"""

from tree_node import TreeNode
from binary_search_tree import BinarySearchTree

__all__ = ['TreeNode', 'BinarySearchTree']

__version__ = '1.0.0'
__author__ = 'Claude'
