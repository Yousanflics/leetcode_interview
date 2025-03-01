/*
这题说是 rotate list (右移 k 个元素)其实跟 rotate 数组那个很像 nodelist 跟 array 的操作更复杂一点因为不能通过下标的移动来交换
最佳方案：1. 遍历链表得到链表长度 2. 可以考虑将链表成环，计算找到新的头 3. 返回 newhead
*/
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head) return nullptr;
        int n = 1;
        ListNode* cur= head;
        while(cur->next) {
            ++n;
            cur = cur->next;
        }
        cur->next = head;
        int m = n - k % n;
        for(int i = 0; i < m; i++) {
            cur = cur->next;
        }
        ListNode* newhead = cur->next;
        // 清理多余内存
        cur->next = nullptr;
        return newhead;
    }
};
