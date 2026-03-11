class Solution:
    def smallestNumber(self, num: int) -> int:
        digits = sorted(str(abs(num)))
        if num >= 0:
            for i, d in enumerate(digits):
                if d != '0':
                    digits[0], digits[i] = digits[i], digits[0]
                    break
            return int(''.join(digits))
        else:
            return -int(''.join(sorted(digits, reverse=True)))