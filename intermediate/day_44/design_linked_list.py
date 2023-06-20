# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        temp = self
        while temp.next is not None:
            print(temp.val, end = " --> ")
            temp = temp.next
        print(str(temp.val),"--> None")

class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list
    def insertFirst(self, root, x):
        if root is None:
            return ListNode(x)
        new = ListNode(x)
        new.next = root
        return new

    def insertLast(self, root, x):
        if root is None:
            return ListNode(x)
        new = ListNode(x)
        temp = root
        while temp.next is not None:
            temp = temp.next
        temp.next = new
        return root

    def insertIndex(self, root, x, index):
        if root is None:
            return ListNode(x)
        temp = root
        count = 0
        if index == 0:
            return self.insertFirst(root, x)
        isAtIndex = False
        while not isAtIndex and temp is not None:
            count = count + 1
            if count == index:
                isAtIndex = True
                continue
            temp = temp.next
        if isAtIndex:
            temp1 = temp
            new = ListNode(x)
            new.next = temp1.next
            temp1.next = new
        return root

    def deleteIndex(self, root, index):
        temp = root
        if temp is None:
            return root
        if index == 0:
            return root.next
        count = 0
        isAtIndex = False
        while not isAtIndex and temp.next is not None:
            if count == index - 1:
                isAtIndex = True
                continue
            count = count + 1
            temp = temp.next
        if isAtIndex:
            temp.next = temp.next.next
        return root

    def solve(self, A):
        n = len(A)
        root = None
        for i in range(n):
            op = A[i][0]
            first = A[i][1]
            second = A[i][2]
            if op == 0:
                root = self.insertFirst(root, first)
            elif op == 1:
                root = self.insertLast(root, first)
            elif op == 2:
                root = self.insertIndex(root, first, second)
            elif op == 3:
                root = self.deleteIndex(root, first)
            print(op,first, second, end=" ==> ")
            if root is None:
                print(" None ")
            else:
                root.printList()
            print(" ")

        return root




if __name__ == "__main__":
    solu = Solution()
    array = [
        # [
        #     [
        #         [0, 1, -1],
        #         [1, 2, -1],
        #         [2, 3, 1],
        #     ]
        # ] ,
        # [
        #     [
        #         [0, 1, -1],
        #         [1, 2, -1],
        #         [2, 3, 1],
        #         [0, 4, -1],
        #         [3, 1, -1],
        #         [3, 2, -1],
        #     ]
        # ],
        [
            [
                # 12 -> 12 -> 17 -> 11 -> 19 
                [3,1,-1],
                [3,1,-1],
                [1,18,-1],
                [2,12,1],
                [1,17,-1],
                [2,11,3],
                [1,19,-1],
                [3,0,-1],
                [0,12,-1]
            ]
        ],
        # [
        #     [
        #         [1,13,-1],
        #         [3,0,-1],
        #         [3,1,-1],
        #         [2,15,0],
        #         [3,0,-1],
        #         [1,12,-1],
        #         [3,0,-1],
        #         [1,19,-1],
        #         [1,13,-1],
        #         [3,0,-1],
        #         [0,12,-1],
        #         [1,13,-1],
        #         [3,2,-1]
        #     ]
        # ],
        # [
        #     [
        #         [2,18,0],
        #         [2,5,1],
        #         [2,8,0],
        #         [1,7,-1],
        #         [1,5,-1]
        #     ]
        # ]
    ]
    for A in array:
        ans = solu.solve(A[0])
        ans.printList()
        print("output for ",A," is ",ans)