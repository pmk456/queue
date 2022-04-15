class Queue:
    def __init__(self, max__):
        self.rear = -1
        self.front = -1
        self.arr = [i for i in range(max__)]
        self.max_ = max__

    def isEmpty(self):
        if self.front == -1 or self.front == self.rear + 1:
            return True
        return False

    def isFull(self):
        if self.rear == self.max_ - 1:
            return True
        return False

    def insert(self, data):
        if self.isFull():
            print("Queue Overflow!")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.arr[self.rear] = data

    def delete(self):
        if self.isEmpty():
            print("Queue Underflow!")
            return
        data = self.arr[self.front]
        self.front += 1
        return data

    def peek(self):
        if self.isEmpty():
            print("Queue Underflow!")
            return
        return self.arr[self.front]

    def display(self):
        if self.isEmpty():
            print("Queue Underflow!")
            return
        for i in range(self.front, self.rear + 1):
            print(self.arr[i])
        print()


def main():
    max_ = int(input("Enter Max Elements: "))
    q = Queue(max_)
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
