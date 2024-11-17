#include <queue>
/*
知识点：优先队列中 cmp(a, b) 是对比 a b两个变量，返回true就是右比左的优先级更高，即 b 比 a 的优先级高
最小堆自动完成了在内部比较得到最小值的过程，不需要手动对比
decltype(cmp) 相当于获取匿名函数的名字给到 prioriry_queue，因为他的初始化需要 cmp 对比器
*/
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](ListNode*&a, ListNode*&b) {
            return a->val > b->val;
        };
        std::priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> q(cmp);
        ListNode* dummy = new LisNode(-1), *cur = dummy;
        for(auto node : lists) {
            if(node) q.push(node);
        }
        while(!q.empty()) {
            ListNode* t = q.top(); q.pop();
            cur->next = t;
            cur = cur->next;
            if(cur->next) q.push(cur->next);
        }
        return dummy->next;
    }
};
