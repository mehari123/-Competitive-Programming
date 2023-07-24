from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        validIp = []
        
        def backtrack(ip, start, numdot):
            if start == len(s) and numdot == 4:
                validIp.append(ip)
                return
            
            if numdot > 3:
                return
            
            for i in range(1, 4):
                if start + i > len(s):
                    break
                
                segment = s[start:start + i]
                if (i == 1 or segment[0] != '0') and 0 <= int(segment) <= 255:
                    if numdot < 3:
                        backtrack(ip + segment + '.', start + i, numdot + 1)
                    else:
                        backtrack(ip + segment, start + i, numdot + 1)
                        
        backtrack('', 0, 0)
        return validIp