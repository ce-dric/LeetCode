class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        d = purchaseAmount // 10
        r1, r2 = d * 10, (d + 1) * 10
        p = min(r1, r2, key=lambda r: (abs(r - purchaseAmount), -r))
        
        return 100 - p