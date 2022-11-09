class Solution():
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx-sx) % sy == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty-sy) % sx == 0
        
        return sx == tx and sy == ty