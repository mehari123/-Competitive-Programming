class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.Fchild = defaultdict(list)
        self.Fchild[kingName]=list()
        self.dead = defaultdict(int)
        
    def birth(self, parentName: str, childName: str) -> None:
        
        self.Fchild[parentName].append(childName)

    def death(self, name: str) -> None:
        
        self.dead[name] = 1
        
    def getInheritanceOrder(self) -> List[str]:
        
        ans = list()
        ans.append(self.kingName)
        curOrder = set()
        curOrder.add(self.kingName)
        
        def successor(x):
            
            children = self.Fchild[x]
            king_child = True
            
            for child in children:
                
                if child not in curOrder:
                    
                    king_child = False
                    break
                
            if not children or king_child:
                
                return 
        
            for ch in children:

                if ch not in curOrder:

                    curOrder.add(ch)
                    ans.append(ch)
                    successor(ch)
                    
        successor(self.kingName)           
        return [cur for cur in ans if cur not in self.dead ]
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()