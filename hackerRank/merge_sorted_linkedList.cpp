//SOLVED
//https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
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

//merge linked list method
SinglyLinkedListNode* mergeLists(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {

    SinglyLinkedList *newList = new SinglyLinkedList();
    while(head1 && head2){
        int minElement;
        if(head1->data <= head2->data){
            minElement = head1->data;
            head1 = head1->next;
        } else {
            minElement = head2->data;
            head2 = head2->next;
        }
        newList->insert_node(minElement);
    }

    while(head1){
        newList->insert_node(head1->data);
        head1 = head1->next;
    }

    while(head2){
        newList->insert_node(head2->data);
        head2 = head2->next;
    }

    return newList->head;
}


//main starts here!
int main(){

    SinglyLinkedList* llist1 = new SinglyLinkedList();

    int llist1_count;
    cin>>llist1_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for(int i=0;i < llist1_count;i++){
        int llist_item;
        cin>>llist_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        llist1->insert_node(llist_item);
    }

    //reverse method

    SinglyLinkedList* llist2 = new SinglyLinkedList();
    int llist2_count;
    cin >> llist2_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int i = 0; i < llist2_count; i++) {
        int llist2_item;
        cin >> llist2_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        llist2->insert_node(llist2_item);
    }

    SinglyLinkedListNode* llist3 = mergeLists(llist1->head, llist2->head);

    print(llist3);
}

