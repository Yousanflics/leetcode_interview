/*
- 题目分析
    实现一个简单的 LRU 算法，LRU = Least Recently Used，为了实现 LRU 需要有两个操作
    - put
    - get


- 总结
    - 需要强化对容器的了解和掌握，尤其是熟练运用迭代器
    - 熟练掌握 LRU 的实现思路，需要做到拿起代码就知道如何实现
*/
class LRUCache{
public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        auto it = m.find(key);
        if (it == m.end()) return -1;
        l.splice(l.begin(), l, it->second);
        return it->second->second;
    }
    
    void put(int key, int value) {
        auto it = m.find(key);
        if (it != m.end()) l.erase(it->second);
        l.push_front(make_pair(key, value));
        m[key] = l.begin();
        if (m.size() > cap) {
            int k = l.rbegin()->first;
            l.pop_back();
            m.erase(k);
        }
    }
    
private:
    int cap;
    list<pair<int, int>> l;
    unordered_map<int, list<pair<int, int>>::iterator> m;
};
