from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # biar pencarian cepat
        dp = [False] * (len(s) + 1)
        dp[0] = True  # base case

        for i in range(1, len(s) + 1):
            for word in word_set:
                if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break  # nggak perlu cek kata lain kalau udah True

        return dp[len(s)]
