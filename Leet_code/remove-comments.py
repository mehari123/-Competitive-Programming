class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        uncommented=[]
        commented=False
        str1=""
        index1=0
        uncommented.append([])
        for index,src in enumerate(source):


                if "/*" not in src and "//" not in src and  "*/" not in src and commented==False:
                        uncommented[index1].append(src)
                        uncommented.append([])
                        index1+=1

                else:
                  
                    sliced_s=src.split(" ")
                    size_s=len(sliced_s)

                    for index2,sliced in enumerate(sliced_s):
                        
                        if commented==False:

                            if "//" in sliced:

                                src1=sliced.split("//")
                                uncommented[index1].append(src1[0])
                                uncommented.append([])
                                index1+=1
                                break
                
                            elif "/*" in sliced:
                       
                                src1=sliced.split("/*")
                                uncommented[index1].append(src1[0])
                                commented=True

                            else:
                                if size_s-1==index2:
                                    uncommented[index1].append(sliced)
                                    uncommented.append([])
                                    index1+=1
                                else:

                                    if sliced=="":
                                        uncommented[index1].append(" ")
                                    uncommented[index1].append(sliced)

                        elif "*/" in sliced:
                            src2=sliced.split("*/")
                            # return src2[1]
                            uncommented[index1].append(src2[1])
                            uncommented.append([])
                            index1+=1
                            commented=False


        source_code=[]
        for line_code in uncommented:
            line=""
            for token in line_code:
                if token!="":
                    line+= token
            if line!="":
                source_code.append(line)
            
        return  source_code
                
                        


        
