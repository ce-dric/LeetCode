class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        _idx = 0
        _max = 0
        while _idx < len(s) and _max < len(g):
            if s[_idx] >= g[_max]:
                _max += 1
            _idx += 1

        return _max