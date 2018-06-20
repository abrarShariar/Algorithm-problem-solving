//https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
//SOLVED
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


int getNode(SinglyLinkedListNode* head, int positionFromTail) {

    int counter = 0;
    SinglyLinkedListNode *newHead;
    while(head){
       SinglyLinkedListNode *node = new SinglyLinkedListNode(head->data);
        if(counter == 0){
            node->next = nullptr;
        } else {
            node->next = newHead;
        }

        newHead = node;
        head = head->next;
        counter++;
    }
    if(positionFromTail == 0){
        return newHead->data;
    }

    for(int i=0;i<positionFromTail;i++){
        newHead = newHead->next;
    }
    return newHead->data;
}


//main starts here!
int main(){

    int tests;
    cin >> tests;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int tests_itr = 0; tests_itr < tests; tests_itr++) {
        SinglyLinkedList* llist = new SinglyLinkedList();

        int llist_count;
        cin >> llist_count;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        for (int i = 0; i < llist_count; i++) {
            int llist_item;
            cin >> llist_item;
            cin.ignore(numeric_limits<streamsize>::max(), '\n');

            llist->insert_node(llist_item);
        }

        int position;
        cin >> position;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        int result = getNode(llist->head, position);

        cout << result << "\n";
    }
}
