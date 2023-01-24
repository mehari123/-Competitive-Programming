class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill1=sorted(skill)
        
        left=0
        right=len(skill)-1
        team_skill=skill1[left]+skill1[right]
        chemistry=0
        while left<right:
            if skill1[left]+skill1[right]!=team_skill:
                return -1
                
            chemistry+=skill1[left]*skill1[right]
            left+=1
            right-=1
        
        return chemistry
            
       
        