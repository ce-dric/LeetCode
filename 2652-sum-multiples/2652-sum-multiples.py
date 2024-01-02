class Solution:
    def sumOfMultiples(self, n: int) -> int:
        _list = []
        for ele in range(1, n+1):
            if ele % 3 == 0 :
                _list.append(ele)
            elif ele % 5 == 0 :
                _list.append(ele)
            elif ele % 7 == 0 :
                _list.append(ele)
        return sum(_list)