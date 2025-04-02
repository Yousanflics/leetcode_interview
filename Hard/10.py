"""
表达式匹配的问题，考虑用递归或者dp，这题难就难在考虑dp的递推公式:

模式中可以包含：
普通字符：与文本中的字符一一对应
.：可以匹配任意单个字符
*：表示前面的字符可以重复出现零次或多次

解题思路：dp
设置一个二维数组dp，其中dp[i][j]表示text从位置i到结尾的子串是否能被pattern从位置j到结尾的子模式所匹配。(相当于是一个倒推，最后需要知道的是 dp[0][0] 的结果能不能满足)
边界条件：dp[len(text)][len(pattern)] = True，表示空文本与空模式是匹配的。
从后向前填充动态规划表

"""
class Solution:
    def isMatch(self, text:str, pattern:str)->bool:
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        # 设置空文本满足匹配即 dp[len(text)][len(pattern)] = True
        dp[-1][-1] = True
        # 行， -1 从最后一个开始，-1 是反向步长
        for i in range(len(text), -1, -1):
            # 列
            for j in range(len(pattern)-1, -1, -1):
                # 最核心的部分，dp 递推公式
                # 从尾部开始 i 没有越界，pattern 的 i 跟 text[i] 相同或者i位置是 '.'（通配符）
                first_match = i < len(text) and pattern[j] in {text[i], '.'}

                """
                当遇到*模式时（即pattern[j+1] == '*'）
                为什么使用j+1而不是j-1:
                虽然我们是从后向前遍历，但字符串的结构和含义不变：在正则表达式中，*总是修饰它前面的字符。
                如果模式是 "a*"，那么：
                pattern[0] 是 'a'（被修饰的字符）
                pattern[1] 是 '*'（修饰符）
                """
                # 首先没有越界其次判断 j 的下一个是 *，因为j 这个位置包有元素的
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    """
                    dp[i][j+2] 的含义:
                    当我们遇到星号模式（pattern[j+1] == '*'）时，有两种处理方式：
                    1.忽略这个星号模式：完全跳过当前字符及其星号修饰符，这相当于让星号匹配0次。
                    因为星号模式占用了两个字符位置（一个是字符，一个是*），所以要跳过这个模式，需要从j跳到j+2。
                    例如，在模式"a*b"中，如果当前在j=0（字符'a'），跳过"a*"就到了j=2（字符'b'）。
                    使用这个星号模式：如果当前字符匹配（first_match为True），那么我们可以让星号匹配1次或多次。

                    first_match and dp[i+1][j] 的含义:
                    2.这部分代码处理的是使用星号模式的情况：
                    first_match：检查当前文本字符text[i]是否与模式字符pattern[j]匹配
                    dp[i+1][j]：假设当前匹配成功，检查剩余的文本（从i+1开始）是否仍然能与当前的模式（保持在j位置）匹配

                    这里的关键是星号允许模式重复多次，所以我们保持模式索引不变（仍为j），但前进文本索引（到i+1）。(星号使用多次 =  保持 pattern 的 index 不变仍然为 j)
                    """
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    #当遇到普通字符时
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]
