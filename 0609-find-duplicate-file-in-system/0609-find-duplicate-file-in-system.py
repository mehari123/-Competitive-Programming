class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hash_path={}
        for path in paths:
            p_info=path.split(" ")

            p_size=len(p_info)
            for index in range(1,p_size):
                file_info=p_info[index].split("(")
                
                path=p_info[0] + "/" + file_info[0]
                if file_info[1] in hash_path:
                    hash_path[file_info[1]].append(path)
                else:
                    hash_path[file_info[1]]=[]
                    hash_path[file_info[1]].append(path)

        duplicate_file=[]
        for value in hash_path.values():
            if len(value)>1:
                duplicate_file.append(value)

        return duplicate_file

                    
                    



        