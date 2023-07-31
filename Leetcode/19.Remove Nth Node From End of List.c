/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    int count = 1;
    int index = 1;
    struct ListNode* p = head;
    struct ListNode* temp = head;
    while(p->next != NULL){
        count = count + 1;
        p = p ->next;
    }
    printf("%d\n",count);
    if(n == 1){
        if(count == 1){
            temp = NULL;
        }
        else{
            for(int i=0; i<count-2;i++){
                    head = head->next;
            }
            head->next = NULL;
        }
        
    }
    else if(n == count){
        temp = head->next; 
    }
    else{
        while(head != NULL){
            if(index == count-n){
                head->next = head->next->next;
            }
            head = head->next; 
            index = index+1;
            
        }
    }

    return temp;
}
