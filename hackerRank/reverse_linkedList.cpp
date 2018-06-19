//SOLVED
//https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
#include<iostream>
#include<limits>
using namespace std;

class SinglyLinkedListNode {
    public:
        int data;
        SinglyLinkedListNode *next;

        SinglyLinkedListNode(int node_data) {
            this->data = node_data;
            this->next = nullptr;
        }
};

class SinglyLinkedList {
    public:
        SinglyLinkedListNode *head;
        SinglyLinkedListNode *tail;

        SinglyLinkedList() {
            this->head = nullptr;
            this->tail = nullptr;
        }

        void insert_node(int node_data) {
            SinglyLinkedListNode* node = new SinglyLinkedListNode(node_data);

            if (!this->head) {
                this->head = node;
            } else {
                this->tail->next = node;
            }

            this->tail = node;
        }
};

void print(SinglyLinkedListNode *head){
    while(head){
        cout<<head->data<<" ";
        head = head->next;
    }
}


//reverse method starts here
SinglyLinkedListNode* reverse(SinglyLinkedListNode* head) {
    int counter = 0;

    SinglyLinkedListNode *tail;
    while(head){
       SinglyLinkedListNode *node = new SinglyLinkedListNode(head->data);
        if(counter == 0){
            node->next = nullptr;
        } else {
            node->next = tail;
        }

        tail = node;
        head = head->next;
        counter++;
    }

    return tail;
}


//main starts here!
int main(){

    SinglyLinkedList* llist = new SinglyLinkedList();

    int llist_count;
    cin>>llist_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for(int i=0;i < llist_count;i++){
        int llist_item;
        cin>>llist_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        llist->insert_node(llist_item);
    }

    //reverse method

    SinglyLinkedListNode* llist1 = reverse(llist->head);
    print(llist1);

}
