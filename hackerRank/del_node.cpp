//SOLVED
//DELETE NODE

#include<iostream>
using namespace std;

struct node{
    int data;
    node* next;
};

node* deleteNode(node*,int);

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


    root=deleteNode(root,4);
    //test print
    tptr=root;
    while(tptr!=NULL){
        cout<<tptr->data<<endl;
        tptr=tptr->next;
    }

}

node* deleteNode(node *head,int position){
    node* tptr;
    tptr=head;
    if(position==0){
        head=head->next;
        delete tptr;
        return head;
    }

    int index=1;
    while(index<position){
        tptr=tptr->next;
        index++;
    }

    //cout<<tptr->data<<endl;
    node* del;
    del=tptr->next;

    tptr->next=tptr->next->next;
    delete del;
    return head;
}
