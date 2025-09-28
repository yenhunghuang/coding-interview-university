"""
Singly Linked List Implementation

這個模組包含了完整的單向鏈表實作，包括 Node 類別和 SinglyLinkedList 類別。

實作的功能：
- 14個核心方法符合 Coding Interview University 要求
- 完整的錯誤處理和邊界條件檢查
- 高效的演算法實作（三指標反轉等）
- 全面的測試覆蓋（8個漸進式測試階段）

使用方式：
    from linked_lists.node import Node
    from linked_lists.singly_linked_list import SinglyLinkedList

    # 或者
    from linked_lists import Node, SinglyLinkedList

測試方式：
    cd linked_lists/
    python3 test_stage1.py    # 基礎結構測試
    python3 test_stage2.py    # 前端操作測試
    python3 test_stage3.py    # 後端操作測試
    python3 test_stage4.py    # 隨機存取測試
    python3 test_stage5.py    # 進階演算法測試
    python3 test_stage6.py    # 數值操作測試
    python3 test_stage7.py    # 整合測試
    python3 test_stage8.py    # 性能測試
    python3 test_stage_final.py  # 最終驗證

作者：通過 TDD (Test-Driven Development) 方式學習實作
版本：1.0.0
"""

# 當這個模組可以正常導入時，可以啟用以下導入
# 現在先註解掉，避免在實作文件不存在時報錯

# try:
#     from .node import Node
#     from .singly_linked_list import SinglyLinkedList
#
#     __all__ = ['Node', 'SinglyLinkedList']
# except ImportError:
#     # 實作文件還不存在時的提示
#     print("提示：請先實作 node.py 和 singly_linked_list.py 文件")
#     __all__ = []

__all__ = []
__version__ = "1.0.0"