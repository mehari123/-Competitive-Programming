class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dictPlayer={}
        loser=1
        winner=0
        for match in matches:
            if match[winner] not in dictPlayer:
                dictPlayer[match[winner]]=0
            if match[loser] in dictPlayer:
                dictPlayer[match[loser]]+=1
            elif match[loser] not in dictPlayer:
                dictPlayer[match[loser]]=1
                
        ans=[[],[]]
        for player,losing in dictPlayer.items():
            if losing==0:
                ans[0].append(player)
            if losing==1:
                ans[1].append(player)
                
        ans1=sorted(ans[0])
        ans2=sorted(ans[1])
        ans=[ans1,ans2]
        
        return ans
                
            
        
            