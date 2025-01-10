/*
题目分析：
这道题是经典的动态规划问题，计算两个字符串之间的**编辑**距离，编辑距离也就是说
将一个字符串转换为另一个字符串所需的最少的操作数，其中雨荨的操作包括：
1. 插入一个字符
2. 删除一个字符
3. 替换一个字符

代码实现思路：
- 状态定义：
    - 用动态规划数组 prev 和 curr 表示前一行和当前行的计算结果
    - prev[j] 表示从 word[0..i-1]转换到 word2[0..j-1] 的最小编辑距离
    - curr[j] 表示从 word1[0..i] 转换到 word2[0..i] 的最小编辑距离

- 初始条件：
    - 当第一个字符串为空时，编辑距离等于第二个字符串的长度，因此pre[j]=j表示需要插入 j 个字符
    - 当第二个字符串为空时，编辑距离等于第一个字符串的长度，因curr[0] = i表示需要删除 i 个字符

- 状态转移：对于每个字符对 word1[i - 1] 和 word2[j - 1]
    - 如果字符相同(word1[i - 1] == word2[j - 1]), 则不需要额外操作，继承迁移状态: curr[j] = prec[j - 1]
    
    - 如果字符不同，考虑从下面三种操作中获取最小值：
        - 插入：从 curr[j - 1] 转换过来，操作数 +1
        - 删除：从 prev[j] 转换过来，操作数 +1
        - 替换：从 prev[j - 1] 转换过来，操作数 +1
        - 转换方程为： curr[j] =  1 + min(prev[j], curr[j - 1], prev[j - 1])
    
    - 为什么插入是 curr[j - 1] +1
        - 例如：
            假设我们已经将 word1[0..i] 转换为 word2[0..j-1]，现在只需要额外插入一个字符，使其等于 word2[j-1]，这样就可以匹配到 word2[0..j]。
            word1 = "abc", word2 = "abcd".
            当前 curr[j-1] 记录了 word1 转换到 word2[0..j-1] ("abc") 的编辑距离。
            插入 word2[j-1] ('d')，操作数 +1。
            因此，curr[j] = curr[j-1] + 1。

            - 为什么下标是 j - 1
                因为这个时候是插入说明 word1[0..i-1]都是符合的了，只需要考虑已经弯针搞得 curr[j - 1] 也就是 curr[j] 的前一个状态的大小

    - 为什么删除是 prev[j] + 1
        - 例如：
            假设我们已经将 word1[0..i-1] 转换为 word2[0..j]，现在只需要删除 word1[i]，就可以匹配到 word2[0..j]。
            word1 = "abcd", word2 = "abc".
            当前 prev[j] 记录了 word1[0..i-1] ("abcd") 转换到 word2[0..j] ("abc") 的编辑距离。
            删除 word1[i-1] ('d')，操作数 +1。
            因此，curr[j] = prev[j] + 1。
            
            - 为什么是 j 作为下标
                - 因为是 word1[0..i-1] 到 word2[j]
                - 这个值已经存储到了上一行的 prev[j] 中，因为它代表的是从 word1[0..i-1]转换为 word2[0..j]的编辑距离
                - 并且删除操作的代价是 +1(其实这三个操作都需要 +1 因为这个时候都进行了操作，在之前的基础上)


        - 滚动数组优化：
    - 原始动态规划需要二维数组 dp[i][j] 表示转台，耗费 O[n1 * n2] 的空间
   
    - 使用滚动数组优化，只需存储前一行和当前行的状态，空间复杂度降低为 O(n2)
- 结果
    - 编辑距离存储在 prev[n2] 中，表示从 word1 转换到 word2 的最小操作数
*/

class Solution {
public:
    int minEditDistance(string word1, string word2) {
        int n1 = word1.size();
        int n2 = word2.size();
        vector<int> prev(n2+1, 0), curr(n2+1, 0);
        for(int j = 0; j <= n2; ++j) {
            prev[j] = j;
        }
        for(int i = 1; i < n1; i++) {
            curr[0] = i;
            for(int j = 1; j <= n2; ++j) {
                if(word1[i - 1] == word2[j - 1]) {
                    curr[j] = prev[j - 1];
                } else {
                    int a = prev[j];
                    int b = curr[j - 1];
                    int c = prev[j - 1];
                    curr[j] = 1 + min(a, min(b, c));
                }
            }
            prev = curr;
        }
        return prev[n2];
    }
};

