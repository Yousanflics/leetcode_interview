/*
简化 path，思路大概就是遇到 . 直接合并如果是 .. 就将 .. 前面的 /x 合并(也可以理解为去除掉)，同时根据/ 分割字符串

这里if(s == "..") 要用双引号，因为 ".." 是一个 const char* c++ 中重载了 == 使得其支持 const char * 跟 std::string 进行比较
最后一行的 "/" 也必须使用双引号，因为 ?: 三元运算符要求 res.empty() ? xxx : yyy 要求 xxx 和 yyy 是相同的返回类型

*/
class Solution {
public:
    string simplifyPath(string path) {
        string res;
        vector<string> dirs;
        int i = 0, n = path.size();
        while(i < n) {
            while(path[i] == '/' && i < n) ++i;
            if(i == path.size()) break;
            int start = i;
            while(path[i] != '/' && i < n) ++i;
            //找到下一个 / 之前的元素
            // 最后元素是 i - 1 因为这里是 ++i，上一个while的是就确定了下一次的元素
            int end = i - 1;
            string s = path.substr(start, end - start + 1);
            if(s == "..") {
                if(!dirs.empty()) dirs.pop_back();
            } else if (s != ".") {// 对 != 的重载要求左右都是 string or const char *
                dirs.push_back(s);
            }
        }
        for(string str : dirs) res += '/' + str;
        return res.empty() ? "/" , res;
    }
};
