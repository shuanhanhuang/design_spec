struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    typedef struct ListNode Node;
    Node *l3, *last, *head = 0;
    int count = 0;
    int num = 0;
    while(l1 !=NULL || l2 != NULL || count!= 0){ //count ¶i¦ì

        if(l1 !=NULL && l2 != NULL){
            num = l1->val + l2->val + count;
            l1 = l1->next;
            l2 = l2->next;
        }
        else if(l1 == NULL && l2 != NULL){
            num = l2->val + count;
            l2 = l2->next;
        }
        else if(l1 !=NULL && l2 == NULL){
            num = l1->val + count;
            l1 = l1->next;
        }
        else{
            num = count;
        }
        
        if(num>9){
            count = 1;
        }
        else{
            count = 0;
        }
        l3 = (Node *) malloc(sizeof(Node));
        l3-> val = num%10;
        l3-> next = NULL;
        if(head == NULL){
            head = l3;
        }
        else{
            last->next = l3;
        }
        last = l3;
    }

    l3 = head;

    return l3;
}
