class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        i = 0
        f = True

        strs = sorted(strs, key=lambda x: len(x))
        print(strs)

        if "" in strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        while f:
            if i >= len(strs[0]):
                break
            pref = strs[0][i]
            # print(pref)

            for word in strs:
                if word[i] != pref:
                    f = False
                    break
            if f:
                ans += pref
                i += 1

        return ans