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

                        if commented==False:
                            if "/*/" in src:
                                src3=src.split("/*/")
                                src=src3[0]+src[1]
                            if "/**/" in src:
                                src3=src.split("/**/")
                                src=src3[0]+src3[1]

                            if "//" in src:

                                src1=src.split("//")
                                uncommented[index1].append(src1[0])
                                uncommented.append([])
                                index1+=1
    
                            elif "/*" in src:
                       
                                src1=src.split("/*")
                                uncommented[index1].append(src1[0])
                                commented=True
                                if "*/" in src1[1]:
                                    src2=src1[1].split("*/")
                                    uncommented[index1].append(src2[1])
                                    uncommented.append([])
                                    index1+=1
                                    commented=False
                            else:
                                    uncommented[index1].append(src)
                                    uncommented.append([])
                                    index1+=1

                        elif "*/" in src:
                            src2=src.split("*/")
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
                
                        


        
                
                        


        
