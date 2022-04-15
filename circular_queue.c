#include<stdio.h>
#include<stdlib.h>
#define MAX 5
int arr[MAX];
int rear = -1;
int front = -1;

void insert(int data);
int del();
int peek();
int isEmpty();
int isFull();
void display();
int main(){
    int op, data;
    printf("1.Insert\n2.Delete\n3.Display Top Element");
    printf("\n4.Display All Queue Elements\n5.Exit\n");
    do{
        printf("Enter option: ");
        scanf("%d", &op);
        switch(op){
            case 1:
                printf("Enter Data: ");
                scanf("%d", &data);
                insert(data);
                break;
            case 2:
                data = del();
                if (data != -1) printf("Popped item is %d\n", data);
                break;
            case 3:
                data = peek();
                if(data != -1) printf("Top Element is %d\n", data);
                break;
            case 4:
                display();
                break;
            case 5:
                exit(0);
            default:
                printf("Enter Correct Option!\n");
        }
    }while(op != 5);
}
int isFull(){
    if((front == 0 && rear == MAX - 1) || front == rear + 1) return 1;
    return 0;
}
int isEmpty(){
    if(front == -1) return 1;
    return 0;
}
void insert(int data){
    if(isFull()){
        printf("Queue Overflow!\n");
        return;
    }
    if(front == -1)
        front = 0;
    if(rear == MAX - 1)
        rear = 0;
    else
        rear++;
    arr[rear] = data;
}
int del(){
    if(isEmpty()){
        printf("Queue Underflow!\n");
        return -1;
    }
    int data = arr[front];
    if(front == rear) front = rear = -1;
    else if (front == MAX - 1) front = 0;
    else front++;
    return data;
}
int peek(){
    if(isEmpty()){
        printf("Queue Underflow!\n");
        return -1;
    }
    return arr[front];
}
void display(){
    int i;
    if(isEmpty()){
        printf("Queue Underflow!\n");
        return;
    }
    i = front;
    if(front<=rear){
        while(i<=rear) printf("%d ", arr[i++]);
    }
    else{
        while(i<=MAX-1) printf("%d ", arr[i++]);
        i = 0;
        while(i<=rear) printf("%d ", arr[i++]);
    }
}


