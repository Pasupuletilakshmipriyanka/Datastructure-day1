class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class SLL:
  def __init__(self):
    self.head=None
  def insert_end(self,data):
    ne=Node(data)
    temp=self.head
    while temp.next:
      temp=temp.next
    temp.next=ne
  def display(self):
    if self.head is None:
      print("LL is empty")
    else:
      temp=self.head
      while(temp):
        print(temp.data,"==>",end=" ")
        temp=temp.next
obj=SLL()
n1=Node(200)
obj.head=n1
n2=Node(300)
n1.next=n2
n3=Node(400)
n2.next=n3
n4=Node(500)
n3.next=n4
print("before inserting 100")
obj.display()
print(" ")
print("after inserting 100")
obj.insert_end(100)
obj.display()

    
