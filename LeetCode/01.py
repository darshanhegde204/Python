# Smallest Number With All Set Bits
class Solution:
    def smallestNumber(self, n: int) -> int:
        power = 1
        while (power<=n) :
            power = power*2
        return power-1
