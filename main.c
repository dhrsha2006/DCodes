#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct node{
    char data[100];
    int status;//0 implies not done while 1 implies done
    struct node* next;
};
struct node* addTask(struct node* head,char data[100]) {
    struct node* newTask=(struct node*)malloc(sizeof(struct node));
    if (newTask==NULL) {
        printf("Failed to allocate space!\n");
        return NULL;
    }
    strcpy(newTask->data,data);
    newTask->status=0;
    newTask->next=head;
    head=newTask;
    printf("Data added successfully!\n");
    return head;
}
void displayTask(struct node* head) {
    struct node* temp=head;
    while(temp!=NULL){
        printf("Task:%s Status:%d\n",temp->data,temp->status);
        temp=temp->next;
    }
    printf("Note: 1 implies done while 0 implies not done.\n");
}
struct node* deleteTask(struct node* head,char target[100]) {
    struct node* temp=head;
    struct node* prev=NULL;
    if (head==NULL) {
        printf("No task to delete!\n");
        return NULL;
    }
    while (temp!=NULL&&strcmp(temp->data,target)!=0) {
        prev=temp;
        temp=temp->next;
    }
    if (temp==NULL) {
        printf("Task not found!\n");
        return head;
    }
    if (prev==NULL) {
        head=temp->next;
    }
    else {
        prev->next=temp->next;
    }
    free(temp);
    printf("Data deleted successfully!\n");
    return head;
}
struct node* markDone(struct node* head,char target[100]) {
    struct node* temp=head;
    struct node* prev=NULL;
    while (temp!=NULL&&strcmp(temp->data,target)!=0) {
        temp=temp->next;
    }
    if (temp==NULL) {
        printf("Task not found!\n");
        return NULL;
    }
    temp->status=1;
    printf("%s is marked as done!\n",temp->data);
    printf("Do you want to delete the task?\n");
    char str[4];
    scanf("%s",str);
    if (strcmp(str,"Yes")==0||strcmp(str,"yes")==0) {
        head=deleteTask(head,target);
    }
    return head;
}
int main() {
    struct node* head=NULL;
    int choice;
    char data[100],target[100];
    do {
        printf("Please enter\n1.Adding Task\n2.Display Task\n3.Mark Task Done\n4.Delete Task\n5.Exit\n");
        scanf("%d",&choice);
        switch (choice) {
            case 1:printf("Please enter the task:");
                scanf("%s",data);
                head=addTask(head,data);
                break;
            case 2:displayTask(head);
                break;
            case 3:printf("Please enter the task you would like to mark as done:");
                scanf("%s",target);
                head=markDone(head,target);
                break;
            case 4:printf("Please enter the task you would like to delete:");
                scanf("%s",target);
                head=deleteTask(head,target);
                break;
            case 5:printf("Exiting...\n");
                break;
            default:printf("Invalid input!\n");
        }
    }while (choice>0&&choice<5);
}
