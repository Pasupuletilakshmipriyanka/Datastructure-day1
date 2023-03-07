class Node:
  def __init__(self,data):
    self.data=data
    self.next=None



class SLL:
  def __init__(self):
    self.head=None
  def display(self):
      if self.head is None:
        print("LL is empty")
      else:
          temp=self.head
          while(temp):
            print(temp.data,"==>",end=" ")
            temp=temp.next



obj=SLL()
n1=Node(100)
obj.head=n1
n2=Node(200)
n1.next=n2
n3=Node(300)
n2.next=n3
obj.display()
