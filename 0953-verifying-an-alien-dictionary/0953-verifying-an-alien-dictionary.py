class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_order={}
        for i in range(26):
            alien_order[order[i]]=i
        
        word_to_num=[]
        for k,word in enumerate(words):
            word_to_num.append([])
            for i,char in enumerate(word):
                word_to_num[k].append(alien_order[char])

        left_index=0
        right_index=1
        while right_index <len(word_to_num):
            for i in range(len(word_to_num[left_index])):
                if len(word_to_num[right_index])-1<i:
                    right_word=-1
                else:
                    right_word=word_to_num[right_index][i]
                if word_to_num[left_index][i]>right_word:
                    return False
                
                elif word_to_num[left_index][i]<right_word:
                    left_index+=1
                    right_index+=1
                    break
                elif (word_to_num[left_index][i]==right_word) and (len(word_to_num[left_index]))-1==i:
                    if right_index==len(word_to_num)-1:
                        return True
                    else:
                        left_index+=1
                        right_index+=1
                        break
                    
        return True
                
        
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 