class Solution:
    def interpret(self, command: str) -> str:
        size=len(command)
        output=''
        i=0
        while i<size:
            if command[i]=="G":
                output +="G"
                i+=1
            elif command[i]=="(" and command[i+1]==")":
                output +="o"
                i+=2
            else:
                output += "al"  
                i+=4
                  
        return output
