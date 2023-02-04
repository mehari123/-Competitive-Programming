class Solution:
    def compress(self, chars: List[str]) -> int:
        
        pointer1=0
        pointer2=1
        pointer3=0
        
        count1=1
        
        while pointer2<len(chars):
            
            if chars[pointer2-1]==chars[pointer2]:
                count1+=1
                pointer2+=1
                
                if pointer2==len(chars):
                    
                    if count1==1:
                        chars[pointer1]=chars[pointer2-1]
                        break
                        
                    elif count1<10:
                        chars[pointer1]=chars[pointer2-1]
                        pointer1+=1
                        chars[pointer1]=str(count1)
                        break
                    else:
                        chars[pointer1]=chars[pointer2-1]
                        str2=""
                        while count1>0:
                            num=count1%10
                            count1=count1//10
                            str2+=str(num)     
                            str2=str2[::-1]
                        for c in str2:
                            pointer1+=1
                            chars[pointer1]=c
                        # pointer1+=1
                        pointer2+=1
                        count1=1
                       
            elif chars[pointer2-1]!=chars[pointer2]:
                
                if count1==1:
                    chars[pointer1]=chars[pointer2-1]
                    pointer2+=1
                    pointer1+=1
                    if pointer2==len(chars):
                    
                        if count1==1:
                            chars[pointer1]=chars[pointer2-1]
                            break
                            
                elif count1<10:
                    chars[pointer1]=chars[pointer2-1]
                    pointer1+=1
                    chars[pointer1]=str(count1)
                    pointer2+=1
                    pointer1+=1
                    count1=1
                    if pointer2==len(chars):
                    
                        if count1==1:
                            chars[pointer1]=chars[pointer2-1]
                            break
                elif count1>=10:
                    print(chars)
                    chars[pointer1]=chars[pointer2-1]
                    pointer1+=1
                    str2=""
                    while count1>0:
                        num=count1%10
                        count1=count1//10
                        str2+=str(num)
                         
                    str2=str2[::-1]
                    for c in str2:
                        chars[pointer1]=c
                        pointer1+=1
               
                    pointer2+=1
                    count1=1
                    if pointer2==len(chars):
                    
                        if count1==1:
                            chars[pointer1]=chars[pointer2-1]
                            break
                        
        return pointer1+1
                    
                
                
            
            
        
        