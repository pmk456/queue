class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        pass


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front is None:
            return True
        return False

    def insert(self, data):
        temp = Node(data, None)
        if self.front is None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp

    def delete(self):
        if self.isEmpty():
            print("Queue Underflow!")
            return
        data = self.front.data
        self.front = self.front.next
        return data

    def peek(self):
        if self.isEmpty():
            print("Queue Underflow!")
            return
        return self.front.data

    def display(self):
        head = self.front
        while head:
            print(head.data, end="\t")
            head = head.next
        print()


def main():
    q = Queue()
    print("1.Insert\n2.Delete\n3.Print First Element\n4.Display All\n5.Exit")
    while 1:
        i = int(input("Select Option: "))
        match i:
            case 1:
                data = int(input("Enter Data: "))
                q.insert(data)
            case 2:
                print(f"{q.delete()} is Deleted\n")
            case 3:
                print(f"Element At front is {q.peek()}")
            case 4:
                q.display()
            case 5:
                exit(0)


if __name__ == '__main__':
    main()
