# VBS - Volatility Breakthrough Strategy. 변동성 돌파 전략 구현하기

import datetime

class Volatility_BS(object):
    def __init__(
        self,
        ask,
        open_now,
        high_past,
        low_past,
        
        k = 0.5
    ):
        super().__init__()
        self.ask = int(ask)
        self.open_now = int(open_now)
        self.high_past = int(high_past)
        self.low_past = int(low_past)
        
        self.right_side = self.open_now + (self.high_past - self.low_past)*k
        
    def VBS_calc(self):
        if self.ask > self.right_side:
            return True
        else: return False
        
a = Volatility_BS(5, 3, 7, 2).VBS_calc()
print(a)
