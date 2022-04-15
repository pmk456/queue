#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
} *rear = NULL, *front = NULL;

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
    struct node *temp = (struct node *) malloc(sizeof(struct node));
    if(temp == NULL) return 1;
    return 0;
}
int isEmpty(){
    if(front == NULL) return 1;
    return 0;
}
void insert(int data){  
    struct node *temp = (struct node *) malloc(sizeof(struct node));
    if(isFull()){
        printf("Queue Overflow!\n");
        return;
    }
    temp->data = data;
    temp->next = NULL;
    if(front == NULL) front = temp;
    else rear->next = temp;
    rear = temp;
}
int del(){
    if(isEmpty()){
        printf("Queue Underflow!\n");
        return -1;
    }
    int data = front->data;
    front = front->next;
    return data;
}
int peek(){
   if(isEmpty()){
        printf("Queue Underflow!\n");
        return -1;
    }
    return front->data;
}
void display(){
    for(struct node *temp=front; temp!=NULL; temp=temp->next) printf("%d\t", temp->data);
    printf("\n");
}

