/*
模拟栈：
如果当前的没有爆炸加入 stack 中每次拿到 stack 的 top（这里是back）查看是否跟当前的 asteroid 会导致爆炸，没有加入其中，有的话：如果相同 popup（pop_back)，如果绝对值栈顶的更小则 continue跟下一个比，处理没有爆炸的：没爆炸的加入到结果 stack 中
*/
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stack;
        for(int asteroid : asteroids) {
            bool exploded = false;
            while(!stack.empty() && asteroid < 0 && stack.back() > 0){
                if(stack.back() < - asteroid) {
                    stack.pop_back();
                    continue;
                }else if(stack.back() = -asteroid) {
                    stack.pop_back();
                }
                exploded = true;
                break;
            }
            if(!exploded) {
                stack.push_back(asteroid);
            }
        }
        return stack;
    }
};
