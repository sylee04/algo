#206. Reverse Linked List
#from __future__ import annotations
from typing import Any, Type

# Definition for singly-linked list. → leetcode 206
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#class Solution:
#    def reverseList(self, head: ListNode) -> ListNode:


if 0:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    class Solution:
        def reverseList(self, head):
            prev = None
            curr = head
            
            while curr!= None:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            return prev
            
    sol = Solution()
    #print(sol.reverseList([1,2,3,4,5]))


    #     tmp = curr.next
    # AttributeError: 'list' object has no attribute 'next'

if 0 :    
    class Solution(object):
        def reverseList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            
            #if head == None or head.next == None:
            #    return head
            
            #else:                
            #    temp = head.next
            #    tail = self.reverseList(head.next)
            #    temp.next = head 
            #    head.next = None
            
            #    return tail
            
            pre = None        
            while head:            
                cur = head 
                head = cur.next
                cur.next = pre 
                pre = cur 
            
            return pre 
            
    sol = Solution()
    print(sol.reverseList(1))
        

if 0:
    class Solution(object):
        def reverseList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            newHead = None ;
            while head:
                nextNode = head.next ;
                head.next = newHead ;
                newHead = head ;
                head = nextNode ;
            return newHead ;
    
                
    if __name__=="__main__":
        print(Solution().reverseList([1,2,3]))

if 0:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
        def reverseList(self, head):
            prev = None
            curr = head
            
            while curr!= None:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            return prev
            
    ln = ListNode()
    print(ln.reverseList([1,2,3,4,5]))

if 0:  
    # Python program to reverse a linked list  
    # Time Complexity : O(n) 
    # Space Complexity : O(1) 
      
    # Node class  
    class Node: 
      
        # Constructor to initialize the node object 
        def __init__(self, data): 
            self.data = data 
            self.next = None
      
    class LinkedList: 
      
        # Function to initialize head 
        def __init__(self): 
            self.head = None
      
        # Function to reverse the linked list 
        def reverse(self): 
            prev = None
            current = self.head 
            while(current is not None): 
                next = current.next
                current.next = prev 
                prev = current 
                current = next
            self.head = prev 
              
        # Function to insert a new node at the beginning 
        def push(self, new_data): 
            new_node = Node(new_data) 
            new_node.next = self.head 
            self.head = new_node 
      
        # Utility function to print the linked LinkedList 
        def printList(self): 
            temp = self.head 
            while(temp): 
                print(temp.data, )
                temp = temp.next
      
        
      
    # Driver program to test above functions 
    llist = LinkedList() 
    llist.push(20) 
    llist.push(4) 
    llist.push(15) 
    llist.push(85) 
      
    print("Given Linked List")
    llist.printList() 
    llist.reverse() 
    print("\nReversed Linked List")
    llist.printList() 
      
    # Driver program to test above functions 
    llist = LinkedList() 
    for i in range(1,5):
        llist.push(i)
      
    print("Given Linked List")
    llist.printList() 
    llist.reverse() 
    print("\nReversed Linked List")
    llist.printList() 
      
    # Driver program to test above functions 
    llist = LinkedList() 
    for i in range(5,1,-1):
        llist.push(i)
      
    print("Given Linked List")
    llist.printList() 
    llist.reverse() 
    print("\nReversed Linked List")
    llist.printList() 
    
    
#from __future__ import annotations
#from typing import Any, Type

class Node:
    """연결 리스트용 노드 클래스"""
    #def __init__(self, data: Any = None, next: Node = None): #NameError: name 'Node' is not defined
    def __init__(self, data: Any = None, next = None):
        """초기화"""
        self.data = data #데이터
        self.next = next #뒤쪽 포인터
   

class LinkedList:
    """연결 리스트 클래스"""
    def __init__(self) -> None:
        """초기화"""
        self.no = 0     # 노드의 개수
        self.head = None    # 머리 노드
        self.current = None # 주목 노드
        
    def __len__(self) -> int:
        """연결리스트의 노드 개수를 반환"""
        return self.no
        
    def add_first(self, data: Any) -> None:
        """맨앞에 노드를 삽입"""
        ptr = self.head # 삽입하기 전의 머리 노드
        self.head = self.current = Node(data, ptr)
        self.no += 1
        
    def add_last(self, data: Any):
        """맨 끝에 노드를 삽입"""
        if self.head is None :  # 리스트가 비어 있으면
            self.add_first(data)
        else :
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev             

    def reverseList(self, head): # leed 206 에는 head인수 有
        prev = None
        curr = head
        while curr!= None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev        

            
    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end=' ')
            ptr = ptr.next

        
            
            
llist = LinkedList() 
if 10:
    for i in range(1,6):
        llist.add_last(i) # 알고리즘 교재대로
        
    print('='*20)
    print("count of node : ", len(llist))  
    print()
    
    print("added Linked List")
    llist.print() 
    print('\n')
    
    print("Reversed Linked List")
    llist.reverse() 
    llist.print() 
    print('\n', end='='*20)
else :
    print(llist.reverseList(head)) # AttributeError: headed object has no attribute 'next'
    #leed 206 def reverseList(self, head: ListNode) ==> head 인수에 들어갈 자료 예시? 어떤식으로 input? local Com에서 어떻게 실행?
    
    
    

















        

    
    