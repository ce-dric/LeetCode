class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        if str == None:
            return 0
        else:
            result = 0
            for idx, ch in enumerate(s):
                before_ch = s[idx-1] if idx -1 >=0 else None

                if before_ch is not None:
                    diff = list(romans.keys()).index(ch) - list(romans.keys()).index(before_ch)
                    if diff <= 2 and diff > 0:
                        result -= 2 * romans[before_ch]

                result += romans[ch]
            return result