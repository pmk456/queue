class CircularQueue:
    def __init__(self, max):
        self.rear = self.front = -1
        self.max = max
        self.arr = [i for i in range(max)]

    def isFull(self):
        if self.front == 0 and self.rear == self.max - 1 or self.front == self.rear + 1:
            return True
        return False

    def isEmpty(self):
        if self.front == -1:
            return True
        return False

    def insert(self, data):
        if self.isFull():
            print("Queue Overflow!")
            return
        if self.front == -1:
            self.front = 0
        if self.rear == self.max - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.arr[self.rear] = data

    def delete(self):
        if self.isEmpty():
            print("Queue Underflow!")
            return
        data = self.arr[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.max - 1:
            self.front = 0
        else:
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
        i = self.front
        if self.front <= self.rear:
            while i <= self.rear:
                print(self.arr[i], end=" ")
                i += 1
        else:
            while i <= self.max - 1:
                print(self.arr[i], end=" ")
                i += 1
            i = 0
            while i <= self.rear:
                print(self.arr[i], end=" ")
                i += 1
        print()


def main():
    max = int(input("Enter Max: "))
    q = CircularQueue(max)
    print("1.Insert\n2.Delete\n3.Print First Element\n4.Display All\n5.Exit")
    while 1:
        i = int(input("Select Option: "))
        match i:
            case 1:
                data = int(input("Enter Data: "))
                q.insert(data)
            case 2:
                print(f"{q.delete()} is Deleted")
            case 3:
                print(f"Element At front is {q.peek()}")
            case 4:
                q.display()
            case 5:
                exit(0)


if __name__ == '__main__':
    main()
