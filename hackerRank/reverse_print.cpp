//SOLVED REVERSE PRINT using recursion

#include<iostream>
using namespace std;

struct node{
    int data;
    node* next;
};

void reversePrint(node*);

int main(){

    node *root,*tptr,*nptr;
    root=NULL;

    for(int i=0;i<5;i++){
        nptr=new node;
        nptr->data=(i+1);
        nptr->next=NULL;
        if(root==NULL){
            root=nptr;
            tptr=nptr;
        }else{
            tptr->next=nptr;
            tptr=nptr;
        }
    }
    reversePrint(root);
}

void reversePrint(node* head){
    if(head==NULL){
        return;
    }
    else{
        reversePrint(head->next);
        cout<<head->data<<endl;
    }
}
