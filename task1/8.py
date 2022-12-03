class  Node:
    def _init_(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def _init_(self):
        self.head=None
        self.size=0

    def add_first(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.size+=1

    def append(self,data):
        new_node=Node(data)

        if self.head==None:
            self.head=new_node
            self.size+=1
        else:
            node=self.head
            while node.next is not None:
                node=node.next
            node.next=new_node
            self.size+=1

    def insert(self,prev_node,data):
        new_data=Node(data)
        if prev_node ==None:
            print("you can't insert")
        else:
            new_data.next=prev_node.next
            prev_node.next=new_data
            self.size+=1

    def show(self):
        node=self.head
        while node is not None:
            print(node.data,end=" ")
            node=node.next
        print()
    def length(self):
        print(f'size={self.size}')

    def remove(self,element):
        this_node=self.head
        prev_node=None
        while this_node != None:
            if this_node.data == element:
                if prev_node== None:
                    self.head=this_node.next
                    self.size-=1
                    return f'{element}'
                else:
                    prev_node.next=this_node.next
                    self.size -= 1
            else:
                prev_node=this_node
                this_node=this_node.next
        return "not found"


l=LinkedList()
l.add_first(5)
l.add_first(15)
l.add_first(10)
l.append(6)
l.insert(l.head.next,11)
l.length()
l.show()
l.remove(10)
l.show()

