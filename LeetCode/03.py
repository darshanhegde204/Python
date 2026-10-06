class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        arr = []
        for i in range (0,len(s),k):
            group=s[i:i+k]
            while (len(group)<k):
                group+=fill
            arr.append(group)
        return arr    