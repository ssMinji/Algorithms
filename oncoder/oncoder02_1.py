goldValues = [2, 1, 4, 1, 2, 1, 8, 1]
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head:
            curn = self.head
            while curn.next != self.head:
                curn = curn.next 
            curn.next = node
            node.next = self.head
        else:
            self.head = node
            node.next = self.head

    def show(self):
        curn = self.head
        string = ''
        maxGold = 0
        while curn:
            string += str(curn.val)
            maxGold = max(maxGold, curn.val)
            if curn.next:
                string += '->'
            if curn.next == self.head:
                # string = '->' +string
                break
            curn = curn.next
        print(string, maxGold)

    def takeGold(self, val):
        curn = self.head
        if curn.val == val:
            curn.val = 0
        
        curn = curn.next
        while curn != self.head:
            if curn.val == val:
                curn.val = 0
            curn = curn.next 

if __name__ == "__main__":
    circular = CircularLinkedList()

    for gold in goldValues:
        circular.append(Node(gold))    

    circular.show()
    circular.takeGold(8)
    circular.show()
    circular.takeGold(4)
    circular.show()

