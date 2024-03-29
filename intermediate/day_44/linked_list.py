class Node:
    data = None
    next = None
    def __init__(self,data):
        self.data = data
        self.next = None
       
class LinkedList:
    head = None
    length = 0
    def __init__(self):
        self.head = None
        self.length = 0

ll = LinkedList()

def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    if position > ll.length + 1:
        return
    newNode = Node(value)
    c = 0
    temp = ll.head
    if position == 1:
        newNode.next = ll.head
        ll.head = newNode
        ll.length += 1
    else:
        c = 1
        while c < position -1:
            temp = temp.next
            c += 1
        newNode.next = temp.next
        temp.next = newNode
        ll.length += 1

def delete_node(position):
    # @param position, integer
    # @return an integer
    if position > ll.length:
        return
    temp = ll.head
    if position == 1:
        newhead = temp.next
        ll.head = newhead
        ll.length -=1
    else:
        c = 1
        while c < position-1:
            temp = temp.next
            c += 1
        newval = temp.next.next
        temp.next = newval
        ll.length -=1



def print_ll():
    # Output each element followed by a space
    temp = ll.head
    while temp.next:
        print(temp.data,end= " ")
        temp = temp.next
    if(temp):
        print(temp.data,end= "")
    print()

t = 100
inputStr = '''i 1 226
i 2 875
i 3 604
i 4 550
i 5 498
i 6 875
i 7 847
i 8 633
i 9 793
i 10 872
i 11 313
i 12 440
i 13 331
i 14 582
i 15 188
i 16 476
i 17 722
i 18 402
i 19 890
i 20 713
i 21 421
i 22 930
i 23 579
i 24 459
i 25 278
i 26 818
i 27 320
i 28 549
i 29 240
i 30 528
i 31 367
i 32 835
i 33 20
i 34 170
i 35 903
i 36 242
i 37 943
i 38 802
i 39 145
i 40 291
i 41 224
i 42 400
i 43 43
i 44 355
i 45 83
i 46 26
i 47 816
i 48 477
i 49 425
i 50 543
i 51 211
i 52 799
i 53 185
i 54 5
i 55 184
i 56 150
i 57 572
i 58 626
i 59 109
i 60 807
d 25
p
d 53
p
d 12
d 54
p
p
p
p
p
d 39
d 42
p
d 47
d 45
d 35
p
d 13
p
d 18
d 59
d 47
d 43
d 38
p
p
p
p
p
p
d 8
p
d 8
p
d 39
d 60
d 16
p
p'''
for i in range(int(t)):
    a = inputStr.split("\n")[i].split(" ")
    # a = input().strip().split(" ")
    print(i,a)
    if a[0] == 'i':
        position = int(a[1])
        value = int(a[2])
        insert_node(position,value)
    elif a[0] == 'd':
        position = int(a[1])
        delete_node(position)
        print_ll()
        break
    elif a[0] == 'p':
        print_ll()