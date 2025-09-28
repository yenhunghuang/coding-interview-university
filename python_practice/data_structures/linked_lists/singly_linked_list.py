from node import Node

class SinglyLinkedList:
    def __init__ (self):
        self._head = None
        self._size = 0
        
        
    def size(self) ->int:
        return self._size
    
    def empty(self) ->bool:
        return self._head is None
    
    def push_front(self, data)-> None:
        new_node = Node(data, self._head)
        self._head = new_node
        self._size +=1
        
    def pop_front(self):
        # 檢查空列表
        if self.empty():
            raise IndexError("pop from empty list")
        data = self._head.data
        self._head = self._head.next
        self._size -=1
        return data
    
    def front(self):
        # 檢查空列表
        if self.empty():
            raise IndexError("front from empty list")
        data = self._head.data
        return data
    
    # push_back(), pop_back(), back()
    def push_back(self, data)-> None:
        new_node = Node(data)

        if self._head is None:
            # 空列表：新節點成為 head
            self._head = new_node
        else:
            #遍歷鏈
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node
        #size更新
        self._size+=1
        
    def back(self):
        if self.empty():
            raise IndexError("back from empty list")
        # 遍歷到最後一個節點
        current = self._head
        while current.next is not None:
            current = current.next
        return current.data    
        
    def pop_back(self):
        # 檢查空列表
        if self.empty():
            raise IndexError("pop_back from empty list")
        if self._head.next is None:
          # 只有一個元素
          data = self._head.data
          self._head = None
          self._size -= 1
          return data
        else:
            #遍歷鏈
            current = self._head
            while current.next.next is not None:
                current = current.next
            #保存data方便彈出並刪除最後一項
            data = current.next.data
            current.next=None
        self._size -=1
        return data

    def value_at(self,index):
        #檢查邊界
        if index<0 or index >= self.size():
            raise IndexError("value_at index out of range")
        current = self._head
        for _ in range(index):
            current = current.next
        return current.data  
        
    def insert(self, index, data):
        #   - 需要找到插入位置的前一個節點
        #   - 創建新節點，調整指針連接
        #檢查邊界
        if index<0 or index > self.size():
            raise IndexError("insert index out of range")
        if index == 0:
            return self.push_front(data)
        
        current = self._head
        for _ in range(index-1):
            current = current.next
            
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        self._size+=1
        
    def erase(self, index):
        #   - 找到要刪除節點的前一個節點
        #   - 調整指針跳過目標節點
        #檢查邊界
        if index<0 or index >= self.size():
            raise IndexError("erase index out of range")
        if index == 0:
            return self.pop_front()
        if index == self._size - 1:
            return self.pop_back()
            
        current = self._head
        for _ in range(index-1):
            current = current.next
        data = current.next.data
        current.next = current.next.next
            
        self._size-=1
        return data
    
    def reverse(self)-> None:
        
        #初始化三個節點
        #逐步反轉節點
        #移動到下一個節點
        #更新head
        prev = None
        current = self._head
        if current is None:
            return  # 空列表直接返回
        
        while current is not None:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        self._head = prev
        
    def value_n_from_end(self, n):
        # 1. 邊界檢查
        if n <= 0 or n > self._size:
            raise IndexError("n out of range")
        fast = self._head
        slow = self._head
        
        for i in range(n):
            if fast is None:
              raise IndexError("n too large")
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow.data
    
    def remove_value(self, data):
        for i in range(self._size):
            if self.value_at(i) == data:
                self.erase(i)
                return
        
         
            
        
    
        


       