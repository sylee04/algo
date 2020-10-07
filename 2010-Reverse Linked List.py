#206. Reverse Linked List
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

#class Solution(object):
#    def reverseList(self, head):
#        """
#        :type head: ListNode
#        :rtype: ListNode
#        """
#        
#        #if head == None or head.next == None:
#        #    return head
#        
#        #else:                
#        #    temp = head.next
#        #    tail = self.reverseList(head.next)
#        #    temp.next = head 
#        #    head.next = None
#        
#        #    return tail
#        
#        pre = None        
#        while head:            
#            cur = head 
#            head = cur.next
#            cur.next = pre 
#            pre = cur 
#        
#        return pre 
#        
#sol = Solution()
#print(sol.reverseList(1))
        


#class Solution(object):
#    def reverseList(self, head):
#        """
#        :type head: ListNode
#        :rtype: ListNode
#        """
#        newHead = None ;
#        while head:
#            nextNode = head.next ;
#            head.next = newHead ;
#            newHead = head ;
#            head = nextNode ;
#        return newHead ;
#
#            
#if __name__=="__main__":
#    print(Solution().reverseList([1,2,3]))


#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
#
#    def reverseList(self, head):
#        prev = None
#        curr = head
#        
#        while curr!= None:
#            tmp = curr.next
#            curr.next = prev
#            prev = curr
#            curr = tmp
#            
#        return prev
#        
#ln = ListNode()
#print(ln.reverseList([1,2,3,4,5]))

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