#include<iostream>
using namespace std;

struct node{
    int data;
    node* next;
};

node* Reverse(node*);

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

    tptr=Reverse(root);
    cout<<tptr->data<<endl;

}

node* Reverse(node* root){

    if(root==NULL){
        return root;
    }else{
        node* tptr;
        root->next=Reverse(root->next);
        root->next=root;
    }
}
