class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        // dummy node 虚拟头结点，方便划分的时候跟进遍历
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* prev = dummy, *cur = head;
        while(prev->next && prev->next->val < x) prev = prev->next;
        cur = pre;
        while(cur->next) {
            if(cur->next->val < x) {
                ListNode *tmp = cur->next;
                cur->next = tmp->next;
                prev->next = tmp;
                prev = prev->next;
            } else {
                cur = cur->next;
            }
        }
        return dummy->next;
    }
};
