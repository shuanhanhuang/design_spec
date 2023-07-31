struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode *list3;
    list3=(struct ListNode *)malloc(sizeof(struct ListNode));
    list3->val=0;
    list3->next=NULL;
    struct ListNode *prev;
    prev=(struct ListNode *)malloc(sizeof(struct ListNode));
    prev=list3;
    while(list1!=NULL && list2!=NULL)
    {
        if(list1->val<=list2->val)
        {
            prev->next=list1;
            list1=list1->next;
        }
        else
        {
            prev->next=list2;
            list2=list2->next;
        }
        prev=prev->next;
    }
    if(list1!=NULL)
    {
        prev->next=list1;
    }
    if(list2!=NULL)
    {
        prev->next=list2;
    }
    

    //list3=list1->next;
    
    return list3->next;
}
