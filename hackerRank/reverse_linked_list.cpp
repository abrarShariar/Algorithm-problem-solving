#include<iostream>
using namespace std;

struct node{
    int data;
    node* next;
};

void reversePrint(node*);
node* reverseRoot(node*);

int main(){

    node *root,*tptr,*nptr;
    root=NULL;
    for(int i=0;i<5;i++){
        nptr=new node;
        nptr->data=i;
        nptr->next=NULL;
        if(root==NULL){
            root=nptr;
            tptr=nptr;
        }else{
            tptr->next=nptr;
            tptr=nptr;
        }
    }

    tptr=reverseRoot(root);

    //reversePrint(tptr);
    //test print
    while(tptr!=NULL){
        cout<<tptr->data<<endl;
        tptr=tptr->next;
    }
}

//change next pointer
node* reverseRoot(node* root){
    node* tptr;
    if(root->next->next==NULL){
        tptr=root->next;
        return root;
    }

    reverseRoot(root);
    tptr->next=root;
    root->next=NULL;
}

//print singly linked list reverse way
void reversePrint(node* root){
    if(root==NULL){
        return;
    }
    reversePrint(root->next);
    cout<<root->data<<" ";
}
