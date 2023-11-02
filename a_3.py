class Solution(object):
    def isMatch(self, s, p):
        i, j = len(s) - 1, len(p) - 1
        return self.backtrack({}, s, p, i, j)

    def backtrack(self, cache, s, p, i, j):
        key = (i, j)
        if key in cache:
            return cache[key]

        if i == -1 and j == -1:
            cache[key] = True
            return True

        if i != -1 and j == -1:
            cache[key] = False
            return cache[key]

        if i == -1 and p[j] == '*':
            k = j
            while k != -1 and p[k] == '*':
                k -= 2

            if k == -1:
                cache[key] = True
                return cache[key]

            cache[key] = False
            return cache[key]

        if i == -1 and p[j] != '*':
            cache[key] = False
            return cache[key]

        if p[j] == '*':
            if self.backtrack(cache, s, p, i, j - 2):
                cache[key] = True
                return cache[key]

            if p[j - 1] == s[i] or p[j - 1] == '.':
                if self.backtrack(cache, s, p, i - 1, j):
                    cache[key] = True
                    return cache[key]

        if p[j] == '.' or s[i] == p[j]:
            if self.backtrack(cache, s, p, i - 1, j - 1):
                cache[key] = True
                return cache[key]

        cache[key] = False
        return cache[key]


class Solution:
    def averageOfSubtree(self, root):
        def helper(node):
            if not node:
                return 0, 0
            left_sum, left_count = helper(node.left)
            right_sum, right_count = helper(node.right)
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count
            return total_sum, total_count

        def dfs(node):
            if not node:
                return 0
            subtree_sum, subtree_count = helper(node)
            if subtree_count == 1 or node.val == subtree_sum // subtree_count:
                return 1 + dfs(node.left) + dfs(node.right)
            else:
                return dfs(node.left) + dfs(node.right)

        return dfs(root)


class Solution(object):
    def intToRoman(self, num):
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ""

        for i in range(len(values)):
            quotient = num // values[i]

            if quotient > 0:
                roman += symbols[i] * quotient
                num -= values[i] * quotient

            if num == 0:
                break

        return roman

class Solution(object):
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total + roman[s[-1]]


class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]